---
title: Building my "digital life" portfolio site with Claude
title_zh: 和 Claude 一起搭建我的"数字生命"个人主页
title_de: Mein „Digital Life“-Portfolio mit Claude bauen
date: 2026-11-26
tool: Claude
topics: [Web development, Three.js & shaders, Creative direction, Information architecture]
draft: true
---

## Context
I wanted a personal homepage that lets recruiters get to know me quickly and memorably: an intro animation, then a Zork-style text adventure where typing commands reveals my background, education, hobbies and how I use AI. I worked through it in one long session with Claude, from idea to a live site at keloshen.github.io.

## Highlights

**Me:** I want my own digital life on GitHub Pages: an animation that spins twice, then a Zork-like scene with commands for my intro, education, hobbies and AI usage log. Is this feasible?

**AI:** Yes, all static. Suggested rooms as sections, clickable command hints for non-gamers, a plain "quick view", and an `ask` command backed by an LLM through a Cloudflare Worker so the API key stays secret.

The intro went through five versions, each driven by a reference image I found:
1. A rotating particle bust → I found it too "AI-looking".
2. ASCII dunes with two stick figures → too crude, cyan felt generic.
3. A 3D raymarched scene in a WebGL shader → technically impressive, still ugly to me.
4. Hand-drawn vector hands à la Michelangelo with a HUD → closer, but not smooth.
5. I showed Claude a post where someone turned a still image into ~160k particles with Three.js + an ASCII layer. We did the same: the image became ~140k particles, sand floats on a curl-noise flow field, a storm whites out the screen, and characters decode into the real terminal text.

**Me:** Not smooth like the Pinterest reference. Can't you do it in the frontend, or do I need a video?

**AI:** It can be done in the frontend; the reference looks smooth because its motion comes from real footage, while mine was CPU-rendered and snapped to a character grid. Moving the rendering to the GPU fixes both.

Later I asked for maintainability: one clear place to edit content, for me and for future AI edits. We moved everything into `content/profile.<lang>.md` (Markdown: `#` = room, `##` = item) and an ASCII `map.txt`. Adding a project or a whole room is now a text edit; the `ask` digital self reads the same file.

## Where the AI was wrong or I pushed back
- The first four intros didn't match my taste. Instead of describing what I wanted in the abstract, sending concrete reference images got far better results.
- I rejected the cyan colour scheme as "too AI"; the final UI is black-and-white with a tiny RGB accent.
- Claude initially rendered thousands of characters on the CPU every frame. When I pointed at a smoother reference, it diagnosed the cause itself and moved the work to shaders.

## What I learned
<!-- DRAFT: rewrite this section in your own words before setting draft: false -->
Reference images beat adjectives when directing AI on visual work. Asking "is this feasible, and how would a professional do it?" early saves iterations. And designing for change (one content file, a parser, a map) matters more than the first version looking perfect.
