# Design Architecture — Dual Buffers

This document defines the hydraulic concept, operating modes, key setpoints, and component sizing for the dual‑buffer plan: a dedicated always‑hot DHW heating buffer feeding a FriWa, plus a separate heating/cooling buffer that is hot in winter and cold in summer. No air conditioners or fan‑coils are used; cooling is via UFH with dew‑point protection.

## One‑Line Hydraulic Schematic (ASCII)

```
           [PV + Battery + Critical Loads Subpanel]
                          |
                   [Electrical Supply]
                          |
                       [AWHP R290]
                          |
                   (optional Plate HX)
                          |
                 +--------+---------+
                 |                  |
       [Heating/Cooling Buffer]   [DHW Heating Buffer]
          800–1000 L, strat.         200–300 L, 55–60°C
                 |                  |
                 |                  +--> [FriWa] --> Potable DHW
                 |                           ^
                 |                           |
           +-----+----+                 Cold mains in
           |          |
        3‑way       Return
        mixing        from
        valve        UFH
           |          ^
           v          |
         [UFH Supply] +---> [UFH Loops] ---> [UFH Return]

 [Wood Stove w/Back‑Boiler] --(return lift, safety)--> Buffer Top
```

Notes:
- The DHW heating buffer contains closed system water (not potable). The FriWa heats potable water on demand via a plate heat exchanger.
- The heating/cooling buffer acts as hydraulic separator and energy store. In summer it is chilled at night; in winter it is kept warm.
- An optional plate heat exchanger (PHE) between the AWHP and indoor circuit allows glycol on the AWHP side and protects indoor water quality.

## Operating Modes

- Winter
  - AWHP runs weather‑compensated to charge the heating/cooling buffer (mid‑zone) for space heating; VL design ≤ 35°C.
  - Midday PV window: AWHP prioritizes DHW heating buffer to 55–60°C for FriWa draws; thereafter returns to space heating.
  - Wood stove charges the buffer top via return‑lift valve (≥60°C) and has thermal discharge safety and gravity emergency cooling per EN 303‑5.
  - Home Assistant (HA) orchestrates priorities and notifications; safety/limits are hard‑wired in dedicated controllers.

- Summer
  - Night: AWHP chills the heating/cooling buffer to ~16–18°C.
  - Day: UFH supply is limited to ≥(dew point + 2 K), typically 19–21°C, to avoid condensation.
  - DHW heating buffer remains hot year‑round; AWHP charges it around midday using PV.

- Shoulder Seasons
  - Minimal buffer setpoints; DHW midday priority; occasional night‑chill during heatwaves.

## Setpoints, Limits, and Sensors

- DHW heating buffer: 55–60°C setpoint; anti‑scald mixing valves at fixtures if needed.
- Heating/Cooling buffer (winter): weather‑compensated targets to achieve VL ≤ 35°C at design.
- Heating/Cooling buffer (summer): night target 16–18°C.
- UFH supply in cooling: ≥(dew point + 2 K). Example: 26°C and 60% RH → dew point ≈ 17.8°C → UFH supply ≥ 20°C.
- Sensors (minimum):
  - Buffers: top/mid/bottom temperatures on both tanks.
  - UFH: supply and return temperatures; optional surface sensor at manifold.
  - Ambient: at least one temperature/RH sensor per floor for dew‑point calculation.
  - Heat/cold metering: heat meters on AWHP to buffer and FriWa primary if feasible.

## Component Sizing (Guidance)

- AWHP (reversible, R290): select by EN 12831 heat loss; typical post‑retrofit terrace house 4–6 kW at −10°C; choose 6–10 kW class with good turndown and quiet operation.
- Heating/Cooling buffer: 800–1000 L, stratified, 100–150 mm insulation, low Δp connections, 3 thermowells (top/mid/bottom).
- DHW heating buffer: 200–300 L, 3 thermowells, maintained at 55–60°C year‑round.
- FriWa: 25–35 kW plate HX module with variable‑speed primary pump, flow sensor, electronic outlet control; potable‑side filtration/anti‑scale as required by local water hardness.
- Valves/Pumps: ECM circulation pumps; 3‑way mixing valve for UFH with hard dew‑point input; motorized isolation valves for summer/winter decoupling; check valves and balancing valves.
- Optional PHE: sized for full thermal capacity with low approach ΔT; glycol on AWHP side; include air/dirt separators on both circuits.
- Expansion vessels: sized for total volume (buffers + pipework + emitters); verify per manufacturer; often 50–80 L combined.

## Safety and Water Quality

- Stove loop: return‑lift (e.g., 60°C cartridge), thermal discharge safety valve to drain, gravity‑safe emergency cooling path, adequate expansion vessel (EN 303‑5 compliance).
- System protection: pressure relief valves (typically 3 bar), air/dirt separators, VDI 2035 water treatment (conductivity/hardness), full insulation of hot lines and diffusion‑tight insulation on all cold lines with managed condensate.
- Electrical: critical‑loads subpanel to maintain HP enable, pumps, controls, network, fridge, and selected lighting/outlets during outages via battery.

## Control Allocation

- Safety/primary control: heat pump native controller; dedicated hydronic controller for mixing valves, pumps, temperature limits, dew‑point cutout; hard interlocks, not dependent on HA.
- Orchestration (HA): PV‑aware scheduling (e.g., DHW midday), seasonal mode toggles, notifications (wood stove use, filter service, abnormal RH/temps), data logging (buffer temps, RH, energy meters, COP proxy).
