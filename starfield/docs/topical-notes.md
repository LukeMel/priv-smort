Starfield Notes (Topical)

Outposts
- Prefab bases: Outpost NPC Prefab – Fortified Encampment; Outpost NPC Prefab – Deserted Relay Station. Place from build menu; watch terrain/navmesh quirks; pair with “build anywhere” helper on slopes.
- Wicked Workshop suite (premade camps/compounds):
  - Wicked Workshop – Outpost Projeckt 2 (base pack): 37+ prebuilt habs, garages, custom storage, cargo‑link pads, two Crew‑Station structures with benches and mission/bounty boards.
  - Wicked Workshop – Fortified: Science/Industrial/Military camps, walled forts, stackable generators/reactors, shipbuilders, cargo‑link variants.
  - Wicked Workshop – Fielded: vendors/guards/robots, crewstations, mission/navigation/bounty terminals, cargo‑link desks, large field generators.
  - Quick recipe: Large Landing Pad HQ or a Camp/Walled Fort → add Cargo‑Link pad/desk and a Field Generator → drop a Crewstation and a Vendor → add extractors/links as needed.
  - Menu locations: Structures tab (near bottom), plus Crewstations, Field Tech, Cargo Links, Workbenches.
- Other fast‑build options: Tower Hab 2 (navmeshed towers), Betamax’s Outpost Framework (prefurnished habs), Modular Outposts: Argos Extractors, OUT – Outpost Ultimate Tweaks, Outpost Anywhere (relax placement), Build Outposts in Restricted Zones (claim existing POIs as your build area).
- Logistics/QoL pairing: Outpost Resource Collector (ORC), High‑Capacity Cargo Links, TN’s Outpost Storage.

Storage
- TN’s Outpost Storage (multiplier): x3–x50 capacity for all vanilla containers; also boosts cargo‑link and transfer container; ESL‑flagged.
- Expanded Outpost Containers (Arthmoor): simple 10× capacity for all outpost containers (Creations).
- Infinite Storage Boxes: 16 buildable “decoration” containers with infinite capacity (doesn’t integrate with crafting/outpost networks).
- Universal Stash / Stash Transfer (SKK): Universal Stash container at each outpost/Decorator for building resources; automatic on‑site transfer to/from Lodge stash; manual options to switch/reset; Production Collector with 999,999 capacity for central collection; automatic behavior avoids piping into unlimited storage; guidance on safe removal and inventory return.

SFSE / Vortex
- SFSE path sanity: Place SFSE files in the same folder as the real Starfield.exe. Typical set: `sfse_loader.exe`, `sfse_steam_loader.dll`, runtime DLLs, `Data/SFSE/sfse.ini`, and optional `Data/SFSE/Plugins/`.
- Vortex alignment:
  - Manage the correct game folder (e.g., `D:\SteamLibrary\steamapps\common\Starfield`).
  - Set Mod Staging to a folder on the same drive (e.g., `D:\Vortex Mods\Starfield`).
  - Add SFSE to Vortex Dashboard pointing to `...\sfse_loader.exe` and set as primary tool.
  - Purge → Deploy, then launch from Vortex to ensure `sfse.log` shows the correct drive/path.
- Steam Play button: ensure `sfse_steam_loader.dll` is in the game root; otherwise launch via Vortex.
- Versioning: SFSE build must match your Starfield runtime version.

Console
- Achievement caveat: using the console disables achievements unless you use an enabler.
- Common commands: `player.additem <FormID> <Count>`, `player.placeatme <BaseID> <Count>`, `(RefID).amod <OMOD_ID>`, `player.addperk <PerkID> <Rank>`, `player.removeperk <PerkID>`, `showlooksmenu player 1`.
- Reference IDs: drop a weapon on the ground, open console and click it to see `WEAP (RefID)`.
- See `data/console_commands.json` for a deduplicated set extracted from both files.

Weapons
- Ship turret mods: EM Turrets; Missile Turret 19‑A‑61 (Inquisitor); Plasma Turret (Inquisitor); Starkiller Machine Gun & Turret (Inquisitor); Phaser Beams & Cannon; Better Full Auto Turret (buffs vanilla turrets).
- Outpost turrets: Inquisitor pack with lightning/missile/plasma/cryo/flame turrets.
- Grouping tip: keep ship groups simple — 1: Lasers (shields), 2: Ballistics/Particle (hull), 3: Missiles/EM. Place turrets first when nearing the weapon‑group cap.

Companions
- Framework: Companion Dialogue Framework (CK framework for true custom companions; reaction interjections; example plugin).
- “DIY companion” (no CK): Recruit Anyone as Ship Crew (Ring of Recruitment); The Gang’s All Here – Multiple Companions and Crew; Command NPCs (adds native Command + trading with unnamed crew); Enhance! Companions (appearance editing at Enhance!).
- Examples: SHAME (custom, voiced companion); Lyria – A Starfield Companion; Estelle Vincent Companion.
- Basic CK workflow (high‑level): create companion Actor/AI packages; companion quest with Start Game Enabled; reference aliases; recruitment dialogue; tools/keywords on weapons/armor; test via a clean save.

—
Sources: `starfieldAllIds` and `starfielChat01` (curated and distilled).
