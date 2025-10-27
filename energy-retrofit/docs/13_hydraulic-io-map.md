# Hydraulic Diagram — Tags and I/O Map

This augments the architecture with reference tags for components, sensors, and control I/O. Use it to drive wiring, labels, and commissioning.

## Tagging Convention

- Tanks: T1 = Heating/Cooling Buffer, T2 = DHW Heating Buffer
- Heat Pump: HP1
- Plate Heat Exchanger (optional): HX1 (AWHP↔House)
- FriWa: FW1
- Wood Stove Loop: WS1
- Pumps: P‑xx, Valves: V‑xx, Sensors: S‑xx, Controllers/Relays: C‑xx/R‑xx

## Components and Tags

- HP1: Reversible AWHP (R290)
- HX1: Optional PHE with glycol on HP1 side
- T1: Heating/Cooling Buffer (800–1000 L)
  - S‑T1‑TOP, S‑T1‑MID, S‑T1‑BOT (temperatures)
- T2: DHW Heating Buffer (200–300 L)
  - S‑T2‑TOP, S‑T2‑MID, S‑T2‑BOT (temperatures)
- FW1: FriWa module (plate HX, primary pump, outlet control)
  - S‑FW‑FLOW (flow sensor), S‑FW‑OUT (DHW outlet temp)
- WS1: Wood stove with back‑boiler and safety kit
  - V‑WS‑RL (return‑lift valve ≥60°C), V‑WS‑TD (thermal discharge safety)
- UFH: Manifold(s) and loops
  - V‑MX‑UFH (3‑way mixing valve), P‑UFH (circulator), S‑UFH‑VL/S‑UFH‑RL (temps), S‑UFH‑SURF (optional surface)
- Seasonal Decoupling Valves
  - V‑SEAS‑T1 (isolate T1), V‑SEAS‑T2 (isolate T2) as needed for service/mode control

## Ambient Sensors

- S‑AMB‑GF: Ground floor T/RH (dew‑point input)
- S‑AMB‑DG: Top floor T/RH (dew‑point input)

## Electrical and Meters

- R‑HP‑EN: Heat pump enable relay (from hydronic controller/safety chain)
- M‑HP‑EL: Electric sub‑meter for HP
- M‑HP‑HT: Heat meter HP→T1
- M‑FW‑HT: Heat meter T2→FW1 primary (optional)

## Control I/O Map (Example)

- Controller C‑HYD (hydronic):
  - Inputs: S‑T1‑TOP/MID/BOT, S‑T2‑TOP/MID/BOT, S‑UFH‑VL/RL, S‑AMB‑GF/DG, S‑UFH‑SURF (opt.)
  - Outputs: V‑MX‑UFH (0–10 V), P‑UFH (on/off or PWM), P‑FW‑PRI (via FW1), R‑HP‑EN, V‑SEAS‑T1/T2, alarm relay
  - Logic: dew‑point limit; DHW priority window; seasonal mode; anti‑short‑cycle; safe shutdown
- Controller C‑HP (in HP1):
  - Weather curve; supply/return temp limits; defrost; interface with R‑HP‑EN.
- FW1 internal controller:
  - Outlet temperature setpoint; modulates P‑FW‑PRI by flow/ΔT.

## Labeling and Documentation

- Each tag must appear on: hydraulic schematic, wiring diagram, device labels, and commissioning forms.
- Provide a printed tag legend and laminate a small copy near T1/T2 manifolds.
