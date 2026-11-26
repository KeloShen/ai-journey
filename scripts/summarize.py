#!/usr/bin/env python3
"""Build summary.json from chats/*.md.

Stats (tools, topics, recent chats) are computed locally. If an LLM API key is
set, the script also asks the model for a headline and a short "what I learned"
list in English, Chinese and German; without a key those fields stay empty and
the website simply shows the stats.

Env (set as GitHub Actions secrets / variables):
  LLM_API_KEY    secret, required for the AI summary
  LLM_PROVIDER   "openai" (any OpenAI-compatible API: DeepSeek, Qwen, ...) or "anthropic"; default openai
  LLM_MODEL      e.g. "deepseek-chat" or "claude-haiku-5-5"
  LLM_BASE_URL   for openai-compatible providers, e.g. "https://api.deepseek.com/v1"
"""
import json, os, re, sys, datetime, urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHATS = ROOT / "chats"
OUT = ROOT / "summary.json"
LANGS = ("en", "zh", "de")


def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^\s*([\w-]+)\s*:\s*(.*?)\s*$", line)
        if not kv or line.strip().startswith("#"):
            continue
        key, val = kv.group(1), kv.group(2)
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
        else:
            val = val.strip("'\"")
        meta[key] = val
    return meta, text[m.end():]


def load_chats():
    chats = []
    for path in sorted(CHATS.glob("*.md")):
        if path.name.startswith("_"):
            continue  # templates
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        if str(meta.get("draft", "")).lower() in ("true", "yes", "1"):
            continue
        topics = meta.get("topics") or []
        if isinstance(topics, str):
            topics = [topics]
        chats.append({
            "path": f"chats/{path.name}",
            "date": str(meta.get("date", "")),
            "tool": meta.get("tool", "Other"),
            "topics": topics,
            "title": {lang: meta.get("title" if lang == "en" else f"title_{lang}") or meta.get("title", path.stem) for lang in LANGS},
            "body": body.strip(),
        })
    chats.sort(key=lambda c: c["date"], reverse=True)
    return chats


def call_llm(prompt):
    key = os.environ.get("LLM_API_KEY")
    if not key:
        return None
    provider = os.environ.get("LLM_PROVIDER", "openai").lower()
    model = os.environ.get("LLM_MODEL") or ("claude-haiku-5-5" if provider == "anthropic" else "deepseek-chat")
    if provider == "anthropic":
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps({"model": model, "max_tokens": 2000, "messages": [{"role": "user", "content": prompt}]}).encode(),
            headers={"content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"},
        )
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.load(r)
        return "".join(b.get("text", "") for b in data.get("content", []))
    base = (os.environ.get("LLM_BASE_URL") or "https://api.deepseek.com/v1").rstrip("/")
    req = urllib.request.Request(
        f"{base}/chat/completions",
        data=json.dumps({"model": model, "max_tokens": 2000, "temperature": 0.4,
                         "messages": [{"role": "user", "content": prompt}]}).encode(),
        headers={"content-type": "application/json", "authorization": f"Bearer {key}"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    return data["choices"][0]["message"]["content"]


def ai_summary(chats, topics):
    if not chats:
        return None
    digest = "\n\n".join(
        f"### {c['title']['en']} ({c['date']}, {c['tool']}, topics: {', '.join(c['topics'])})\n{c['body'][:3500]}"
        for c in chats[:30]
    )
    prompt = f"""You are summarising a person's curated AI conversation logs for their portfolio website.
Write in first person, as the person. Be specific and honest; never invent facts that are not in the logs.

Return ONLY a JSON object, no prose, with this shape:
{{
  "headline": {{"en": "...", "zh": "...", "de": "..."}},
  "learned": [{{"en": "...", "zh": "...", "de": "..."}}],
  "topics": {{"<topic as given>": {{"zh": "...", "de": "..."}}}}
}}
- headline: 1–2 sentences on how I use AI and what it has helped me do.
- learned: 3–6 concrete things I learned (skills, insights, habits), one sentence each.
- topics: translations of these topic names: {json.dumps(sorted(topics))}

LOGS:
{digest}
"""
    try:
        text = call_llm(prompt)
    except Exception as e:  # network/API problems shouldn't break the build
        print(f"LLM call failed: {e}", file=sys.stderr)
        return None
    if not text:
        return None
    m = re.search(r"\{.*\}", text, re.S)
    try:
        return json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        print("LLM returned invalid JSON; skipping AI summary", file=sys.stderr)
        return None


def main():
    chats = load_chats()
    tools = Counter(c["tool"] for c in chats)
    topic_counts = Counter(t for c in chats for t in c["topics"])
    previous = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    ai = ai_summary(chats, topic_counts.keys()) or {}
    tr = ai.get("topics", {})
    summary = {
        "updated": datetime.date.today().isoformat(),
        "totalChats": len(chats),
        # keep the last good AI text if this run had no key / the call failed
        "headline": ai.get("headline") or previous.get("headline") or "",
        "learned": ai.get("learned") or previous.get("learned") or [],
        "tools": dict(tools.most_common()),
        "topics": [{"name": {"en": t, **tr.get(t, {})}, "count": n} for t, n in topic_counts.most_common(8)],
        "recent": [{"date": c["date"], "tool": c["tool"], "title": c["title"], "path": c["path"]} for c in chats[:10]],
    }
    OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"summary.json: {len(chats)} chats, AI summary: {'yes' if ai else 'no'}")


if __name__ == "__main__":
    main()
