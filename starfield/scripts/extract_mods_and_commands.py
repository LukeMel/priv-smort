#!/usr/bin/env python3
import json
import re
from pathlib import Path

CHAT = Path('starfielChat01')
IDS = Path('starfieldAllIds')
OUT_DIR = Path('data')
OUT_DIR.mkdir(parents=True, exist_ok=True)

def read_lines(p: Path):
    return p.read_text(encoding='utf-8', errors='ignore').splitlines()

chat = read_lines(CHAT)
ids = read_lines(IDS)

# Extract console commands: look for common patterns
cmd_patterns = [
    re.compile(r'\bplayer\.[a-z]+', re.I),
    re.compile(r'\bshowlooksmenu\b', re.I),
    re.compile(r'\bamod\b', re.I),
]

def extract_commands(lines):
    cmds = set()
    samples = {}
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if any(p.search(s) for p in cmd_patterns):
            # Normalize: collapse multiple spaces
            norm = re.sub(r'\s+', ' ', s)
            # Keep only command fragment (up to 120 chars)
            frag = norm[:120]
            cmds.add(frag)
            samples.setdefault(frag, 0)
            samples[frag] += 1
    return [{'command': c, 'count': samples[c]} for c in sorted(cmds)]

commands = extract_commands(chat) + extract_commands(ids)

# Deduplicate commands by string
seen = {}
merged = []
for c in commands:
    if c['command'] in seen:
        seen[c['command']]['count'] += c['count']
    else:
        seen[c['command']] = c
for v in seen.values():
    merged.append(v)
merged.sort(key=lambda x: x['command'])

(OUT_DIR / 'console_commands.json').write_text(json.dumps(merged, indent=2), encoding='utf-8')

# Extract mod names: heuristic around lines preceding Nexus/Creations mentions
def extract_mods(lines):
    mods = []
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s:
            continue
        if ('Nexus Mods' in s) or ('creations.bethesda.net' in s.lower()):
            # Backtrack to find a likely name line (skip empty and generic text)
            j = i - 1
            while j >= 0 and (not lines[j].strip() or lines[j].strip().lower() in {'+1', '+2', '+3', '+4'}):
                j -= 1
            if j >= 0:
                name_line = lines[j].strip()
                # Trim trailing commentary in parentheses
                name = re.split(r'\s*\(', name_line, 1)[0].strip(' -:\u2013\u2014')
                if name and len(name.split()) <= 20:  # avoid paragraph text
                    mods.append(name)
    # Deduplicate while preserving order
    seen = set()
    ordered = []
    for m in mods:
        if m not in seen:
            seen.add(m)
            ordered.append(m)
    return ordered

mods_list = extract_mods(chat)

# Categorize by simple keywords
def categorize(name: str):
    n = name.lower()
    cats = []
    if 'outpost' in n or 'hab' in n or 'crew' in n:
        cats.append('Outposts')
    if 'storage' in n or 'cargo' in n or 'container' in n:
        cats.append('Storage/Logistics')
    if 'turret' in n or 'weapon' in n or 'gun' in n or 'phaser' in n or 'plasma' in n or 'missile' in n or 'em ' in f"{n} ":
        cats.append('Weapons/Turrets')
    if 'workshop' in n:
        cats.append('Wicked Workshop Suite')
    if 'companion' in n or 'crew' in n:
        cats.append('Companions/Followers')
    if 'sfse' in n or 'plugins' in n or 'vortex' in n:
        cats.append('SFSE/Vortex')
    if 'restricted zones' in n or 'poi' in n:
        cats.append('Build/Placement')
    if not cats:
        cats.append('Misc')
    return cats

mods_json = [{'name': m, 'categories': categorize(m)} for m in mods_list]

(OUT_DIR / 'mods.json').write_text(json.dumps(mods_json, indent=2), encoding='utf-8')

print('Wrote', OUT_DIR / 'console_commands.json')
print('Wrote', OUT_DIR / 'mods.json')

