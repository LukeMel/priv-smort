# Ventilation — Decentralized Single‑Room HRV (DIN 1946‑6)

No central ventilation is feasible; this plan uses 6–8 decentralized HRV units to provide base air exchange with heat recovery, local boosts, and summer bypass.

## Design Principles

- Balance and coverage: Provide continuous background ventilation in living/bedrooms; stronger extraction or boost in wet rooms.
- Acoustic comfort: Low noise at base flow, night mode for bedrooms, acoustic liners/baffles.
- Simplicity: Short core drill per unit (160–200 mm), slight outward slope for condensate, easy filter access.

## Unit Types

- Dual‑fan continuous units (preferred): simultaneous supply and exhaust through a small counter‑flow core; more stable balance.
- Alternating push‑pull units (paired): ceramic core stores heat; install in pairs to approximate balance.

## Placement and Air Paths

- Wet rooms (bath, WC, kitchen): units with boost 40–60 m³/h; grease filters where needed.
- Living/bedrooms: base 15–30 m³/h per room; night mode in bedrooms.
- Door undercuts/transfer grilles to enable crossflow; avoid short‑circuiting supply to immediate exhaust.
- Exterior intakes with weather hoods and insect screens; consider façade acoustics.

## Controls

- Local control: manual boost switches (bath fans), humidity/CO₂‑based automatic boosts, night modes.
- Central overview (optional): dry contacts or Modbus/IP bridge to integrate with Home Assistant for visibility and logging (not safety‑critical).
- Summer bypass: enable to prevent unwanted heat recovery during cooling season; querventilation possible.

## Installation and Commissioning

- Core drills with slight outward slope for condensate; ensure airtight sleeve sealing.
- Configure design flow rates per DIN 1946‑6 ventilation concept; measure and record flows.
- Filters: set maintenance intervals; keep spare sets; include filter‑service notifications.

## Interaction with Hydronic Cooling

- HRV aids humidity control but does not dehumidify aggressively; monitor RH per floor.
- If RH > 60% persists during heat events, consider temporary standalone dehumidifier while maintaining “no AC” constraint.
