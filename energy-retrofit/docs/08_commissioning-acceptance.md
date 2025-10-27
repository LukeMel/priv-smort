# Commissioning and Acceptance

This checklist defines the procedures and evidence required to safely commission and accept the system. It is structured to match funding documentation needs.

## Pre‑Commissioning

- Mechanical:
  - Pipework flushed, pressure tested; leak‑free.
  - Expansion vessels sized and pre‑charged for total volume (buffers + circuits).
  - Air/dirt separators installed at strategic points; vents accessible.
  - Insulation complete: hot lines insulated; cold lines diffusion‑tight with condensate routes.
- Electrical:
  - Critical‑loads subpanel wired; circuits labeled; RCD/MCB verified.
  - Surge protection devices (SPDs) installed and coordinated with PV/battery.
  - Control wiring (sensors, valves, pumps) labeled; emergency stops documented.
- Water quality:
  - System water prepared per VDI 2035; conductivity/hardness logged.
- Safety (stove):
  - Return‑lift valve operation verified; thermal discharge safety connected to drain; gravity emergency cooling path tested; chimney approvals.

## Controls and Sensors Validation

- Buffers: confirm top/mid/bottom sensor readings; directions of flow validated.
- UFH: verify supply/return sensors; 3‑way valve orientation; pump rotation.
- Dew‑point logic: inject high RH in test zone or simulate via controller; confirm UFH supply limit and lockout behavior.
- HP controller: weather curve loaded; limits set (min/max VL, anti‑short‑cycle).
- FriWa: outlet temperature control tuned; stable performance over 2–16 L/min draws; anti‑scald verified.

## Functional Tests

- Heating mode (winter simulation):
  - Long steady compressor operation; buffer stratification observed; target VL achieved at test outdoor setpoint.
  - DHW midday priority: buffer top reaches 55–60°C; resume space heating post‑charge.
- Cooling mode (summer simulation):
  - Night buffer chill to ~16–18°C; daytime UFH VL maintained at dew point + 2 K; no condensation on manifolds/lines.
- Stove integration:
  - Charge buffer top; verify AWHP priority reduction on high top‑of‑buffer temperature.

## Hydraulic Balancing

- UFH circuits: measure and record volume flows per loop; adjust to design; document setpoints.
- Heat meters: verify installation direction and pulse outputs if logging.

## Ventilation (Decentralized HRV)

- Design flows set per room; boost functions verified; summer bypass configured.
- Filters installed; maintenance calendar established; acoustic checks.

## Acceptance Documentation

- Blower‑door test results (pre + post) with achieved n50 ≤ 1.5 h⁻¹ (target).
- Hydronic balancing protocol (flows per loop), HP and FriWa commissioning reports.
- VDI 2035 water quality report; pressure test certificates; electrical test reports (RCD/insulation/SPD).
- Schematics: final hydraulic diagram, control I/O map, sensor list.
- Safety attestations: stove compliance (EN 303‑5), chimney sweep approvals, emergency procedures.
- Monitoring plan: which data is logged and retention period (first season minimum).
