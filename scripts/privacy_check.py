#!/usr/bin/env python3
"""Scan chats/*.md for things that shouldn't be public.

Exits with status 1 if anything is found, which makes the GitHub Action fail;
GitHub then emails whoever pushed the commit, and summary.json is NOT updated.

Findings are printed WITHOUT the sensitive value itself (only file, line, type
and a masked hint), because Action logs of a public repo are public too.

False positive? Add the exact text to scripts/privacy_allowlist.txt (one per line).
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOW_FILE = ROOT / "scripts" / "privacy_allowlist.txt"

CHECKS = [
    ("email address", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")),
    ("Chinese mobile number", re.compile(r"(?<![\d.])(?:\+?86[ -]?)?1[3-9]\d[ -]?\d{4}[ -]?\d{4}(?!\d)")),
    ("international phone number", re.compile(r"(?<![\w+])\+(?!86)\d{1,3}[ -]?\(?\d{2,4}\)?(?:[ -]?\d{3,4}){2,3}(?!\d)")),
    ("Chinese ID number", re.compile(r"(?<!\d)[1-9]\d{5}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx](?!\d)")),
    ("API key (OpenAI/DeepSeek/Anthropic style)", re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr|github_pat)_[A-Za-z0-9_]{20,}")),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{20,}", re.I)),
    ("password / secret assignment", re.compile(r"(?i)\b(?:password|passwd|pwd|secret|api[_-]?key|access[_-]?token|密码|口令)\b\s*[:=：]\s*['\"]?[^\s'\"`]{6,}")),
    ("URL with credentials or token", re.compile(r"https?://[^\s/:@]+:[^\s/@]+@|[?&](?:token|key|apikey|access_token|sig|signature)=[A-Za-z0-9._-]{12,}", re.I)),
    ("private IP address", re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b")),
]


def mask(value):
    value = value.strip()
    if len(value) <= 6:
        return "*" * len(value)
    return value[:2] + "*" * (len(value) - 4) + value[-2:]


def main():
    allow = set()
    if ALLOW_FILE.exists():
        allow = {l.strip() for l in ALLOW_FILE.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")}
    findings = []
    for path in sorted((ROOT / "chats").glob("*.md")):
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for label, rx in CHECKS:
                for m in rx.finditer(line):
                    if any(a in m.group(0) or m.group(0) in a for a in allow):
                        continue
                    findings.append((path.relative_to(ROOT), n, label, mask(m.group(0))))
    if not findings:
        print("Privacy check passed: nothing sensitive found in chats/.")
        return 0
    print(f"::error::Privacy check found {len(findings)} possible issue(s). summary.json was NOT updated.")
    for file, n, label, hint in findings:
        # GitHub annotation: shows up on the commit / run page without revealing the value
        print(f"::error file={file},line={n}::{label} ({hint})")
        print(f"  {file}:{n}  {label}  [{hint}]")
    print("\nFix: remove or replace these lines and push again.")
    print("If one is a false positive, add the exact text to scripts/privacy_allowlist.txt.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
