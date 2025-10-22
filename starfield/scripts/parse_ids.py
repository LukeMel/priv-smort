#!/usr/bin/env python3
import json
import re
from pathlib import Path

SRC = Path('starfieldAllIds')
OUT_DIR = Path('data/ids')

OUT_DIR.mkdir(parents=True, exist_ok=True)

text = SRC.read_text(encoding='utf-8', errors='ignore').splitlines()

def norm_hex(raw: str):
    cleaned = re.sub(r'[^0-9A-Fa-f]', '', raw).upper()
    if not cleaned:
        return None
    if len(cleaned) < 8:
        cleaned = cleaned.rjust(8, '0')
    elif len(cleaned) > 8:
        cleaned = cleaned[-8:]
    return cleaned

def is_id_line(line: str):
    m = re.match(r'^\s*([0-9A-Fa-f/]{5,})\s+(.+?)\s*$', line)
    if not m:
        return None
    raw_id, name = m.group(1), m.group(2)
    if name.lower().startswith(('player.', 'player ', 'jump to', 'view', 'none')):
        return None
    return raw_id, name

sections = {}
current = None
legendary_mode = False
legendary = []
legendary_current = None
modifiers_mode = False
mod_slot = None
modifiers = []

def start_section(title):
    global current, legendary_mode, modifiers_mode, mod_slot
    current = {'title': title, 'items': []}
    sections[title] = current
    legendary_mode = False
    modifiers_mode = False
    mod_slot = None

for line in text:
    s = line.strip()
    # Headings (special cases first)
    if s == 'All Legendary and Unique Weapon IDs in Starfield':
        legendary_mode = True
        legendary_current = None
        continue
    if s == 'All Weapon Modifier IDs in Starfield':
        modifiers_mode = True
        mod_slot = None
        continue
    if s == 'All Weapon IDs in Starfield':
        start_section(s)
        continue
    if re.match(r'^All .* IDs in Starfield$', s):
        start_section(s)
        continue

    # Parse legendary/unique block
    if legendary_mode:
        m = re.match(r'^([0-9A-Fa-f]{6,8})\s+(.+?)\s*$', s)
        if m:
            if legendary_current:
                legendary.append(legendary_current)
            raw_id, name = m.group(1), m.group(2)
            legendary_current = {
                'raw_id': raw_id,
                'id': norm_hex(raw_id),
                'name': name,
                'modifiers': [],
                'attachments': []
            }
            continue
        if ' - ' in s and legendary_current is not None:
            left, right = s.split(' - ', 1)
            legendary_current['modifiers'].append({'name': left.strip(), 'description': right.strip('.')})
            continue
        if s and legendary_current is not None and not s.lower().startswith(('legendary', 'epic', 'rare', 'base')):
            legendary_current['attachments'].append(s)
        continue

    # Parse weapon modifiers block
    if modifiers_mode:
        if re.match(r'^Slot \d+ Modifiers$', s):
            mod_slot = s.split()[1]
            continue
        s2 = s.replace('\t', '    ')
        m = re.match(r'^([0-9A-Fa-f]{6,8})\s+(.+?)\s{2,}(.+)$', s2)
        if m:
            raw_id, name, desc = m.group(1), m.group(2).strip(), (m.group(3) or '').strip()
            modifiers.append({'raw_id': raw_id, 'id': norm_hex(raw_id), 'name': name, 'description': desc, 'slot': mod_slot})
            continue
        if s.startswith('All ') and s.endswith('IDs in Starfield'):
            modifiers_mode = False
        continue

    # Skip boilerplate
    if not s or s.lower().startswith((
        'to spawn', 'to attach', 'to add or remove', 'id code', 'advertisement', 'jump to table',
        'looking for', "player.placeatme (id code)", 'player.placeatme (weapon id) 1', 'need ammo',
        'want weapon mods', 'need minerals', "whether you're", 'best starfield'
    )):
        continue

    # Generic section accumulation
    if current is not None:
        id_line = is_id_line(s)
        if id_line:
            raw_id, name = id_line
            current['items'].append({'raw_id': raw_id, 'id': norm_hex(raw_id), 'name': name})

# Flush last legendary
if legendary_mode and legendary_current:
    legendary.append(legendary_current)

# Write outputs
(OUT_DIR / 'weapons.json').write_text(
    json.dumps(sorted(sections.get('All Weapon IDs in Starfield', {}).get('items', []), key=lambda x: x.get('name','').lower()), indent=2),
    encoding='utf-8'
)
(OUT_DIR / 'legendary_unique_weapons.json').write_text(json.dumps(sorted(legendary, key=lambda x: x.get('name','').lower()), indent=2), encoding='utf-8')
(OUT_DIR / 'weapon_modifiers.json').write_text(json.dumps(sorted(modifiers, key=lambda x: (x.get('slot') or '', x.get('name','').lower())), indent=2), encoding='utf-8')

def dump_section(title: str, filename: str):
    items = sections.get(title, {}).get('items', [])
    if items:
        (OUT_DIR / filename).write_text(json.dumps(sorted(items, key=lambda x: x.get('name','').lower()), indent=2), encoding='utf-8')

dump_section('All Ammo IDs in Starfield', 'ammo.json')
dump_section('All Trait IDs in Starfield', 'traits.json')
dump_section('All Background IDs in Starfield', 'backgrounds.json')

for title, key in [
    ('All Spacesuit IDs in Starfield', 'spacesuits.json'),
    ('All Helmet IDs in Starfield', 'helmets.json'),
    ('All Boost Pack IDs in Starfield', 'boost_packs.json'),
    ('All Armor Modifier IDs in Starfield', 'armor_modifiers_raw.json'),
]:
    dump_section(title, key)

# Fallback: if weapon modifiers not parsed, try scanning block directly
if not modifiers:
    start_idx = None
    for idx, line in enumerate(text):
        if line.strip() == 'All Weapon Modifier IDs in Starfield':
            start_idx = idx
            break
    if start_idx is not None:
        slot = None
        for s in (l.strip() for l in text[start_idx+1:]):
            if not s:
                continue
            if s.startswith('Jump to Table of Contents'):
                break
            if s.startswith('Slot '):
                # e.g., Slot 1 Modifiers
                parts = s.split()
                if len(parts) >= 2:
                    slot = parts[1]
                continue
            s2 = s.replace('\t', '    ')
            m = re.match(r'^([0-9A-Fa-f]{6,8})\s+(.+?)\s{2,}(.+)$', s2)
            if m:
                raw_id, name, desc = m.group(1), m.group(2).strip(), (m.group(3) or '').strip()
                modifiers.append({'raw_id': raw_id, 'id': norm_hex(raw_id), 'name': name, 'description': desc, 'slot': slot})
        # Overwrite weapon_modifiers.json with fallback results
        (OUT_DIR / 'weapon_modifiers.json').write_text(json.dumps(modifiers, indent=2), encoding='utf-8')

print('Parsed sections:', sorted(sections.keys()))
print('Outputs written to', OUT_DIR)
