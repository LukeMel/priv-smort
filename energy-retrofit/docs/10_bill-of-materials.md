# Bill of Materials (Specification Classes)

Brand‑agnostic list with size ranges. Final selections should follow detailed calcs and installer standards.

## Heat Generation and Storage

- Reversible AWHP (R290), 6–10 kW class, monobloc or split; low noise kit; night mode.
- Optional Plate Heat Exchanger (AWHP↔House), sized for full capacity with low approach ΔT; glycol on AWHP side.
- Heating/Cooling Buffer: 800–1000 L, stratified, 100–150 mm insulation, 3× thermowells.
- DHW Heating Buffer: 200–300 L, high insulation, 3× thermowells.
- FriWa Module: 25–35 kW plate HX, variable‑speed primary pump, flow sensor, electronic outlet control, service valves, potable filter/strainer.
- Wood Stove w/Back‑Boiler (optional): rated output matched to buffer; return‑lift valve (≥60°C), thermal discharge valve, emergency cooling path components; chimney parts as required.

## Hydronic Periphery

- Circulation Pumps: ECM pumps for AWHP loop(s), buffer charging, UFH circuits, FriWa primary.
- Valves: 3‑way mixing valve (UFH), motorized zone valves for seasonal decoupling, check valves, balancing valves, drain/fill valves.
- Separators: air and dirt separators at key locations; magnetic dirt separator if needed.
- Expansion Vessels: sized for total water volume; service valves and gauges.
- Safety: PRVs (typically 3 bar), manometers, automatic air vents; condensate traps for cold lines.

## Distribution

- UFH Manifolds and Loops: oxygen‑barrier PEX/MLCP, manifold cabinets, flow meters, actuators if zoned.
- Pipe Insulation: hot lines to code; cold lines diffusion‑tight; manifold/valve box insulation where possible.

## Ventilation (Decentralized HRV)

- 6–8 single‑room HRV units (dual‑fan continuous or push‑pull pairs), wall sleeves, exterior hoods, acoustic liners, filters.
- Control accessories: boost switches, humidity/CO₂ sensors (where supported), integration gateway (optional).

## Controls, Sensors, Electrical

- Hydronic Controller: mixing valve + pump control with dew‑point input and lockout.
- Sensors: buffer temps (top/mid/bottom), UFH VL/RL, ambient T/RH per floor, optional manifold surface probe.
- Energy Meters: heat meter(s) on AWHP and FriWa primary (optional), sub‑meter for HP electrical.
- Electrical: critical‑loads subpanel, ATS/transfer switch for backup, SPDs, labeling, wiring accessories.
- Home Assistant Host: small, reliable compute (e.g., SBC or mini‑PC), network connectivity, UPS (optional).

## Water Treatment and Service

- VDI 2035 treatment unit/chemistry, test kit (conductivity/hardness), fill/drain assemblies.
- Filters/Strainers: potable filter for FriWa; strainers where needed on primary; spare filter sets.
- Serviceability: isolation valves, drain points, thermowells/test points, access panels.
