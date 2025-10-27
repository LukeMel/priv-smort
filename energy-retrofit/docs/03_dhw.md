# Domestic Hot Water (DHW) — FriWa + DHW Heating Buffer

This design uses a dedicated DHW heating buffer (closed system water) held at ~55–60°C, feeding a Frischwasserstation (FriWa). There is no potable water storage; potable water is heated on demand through a plate heat exchanger.

## Rationale

- Hygiene: No stored potable hot water → minimized legionella risk; simple anti‑scald control at outlets.
- Summer compatibility: The DHW buffer remains hot while the separate heating/cooling buffer can stay cold for UFH cooling.
- PV synergy: Midday charging of the DHW buffer with PV improves self‑consumption and reduces evening load.

## Hydraulics

- DHW heating buffer (200–300 L): maintained at 55–60°C year‑round; fitted with top/mid/bottom sensors and good insulation.
- FriWa module (25–35 kW): includes plate HX, primary variable‑speed pump, flow sensor, electronic temperature control; potable‑side filter/strainer and service valves.
- AWHP priority logic: DHW charging has time‑of‑day priority (midday) and temperature priority (if buffer top < setpoint); otherwise AWHP serves space heating/cooling buffer.

## Control and Setpoints

- DHW buffer setpoint: 55–60°C (tune to water hardness and comfort). Use anti‑scald mixing valves at fixtures.
- PV‑aware charging: If battery SoC is high and PV surplus available, run DHW charge to target; otherwise defer to off‑peak schedule.
- Standby losses: Keep buffer well insulated; consider night setback only if draw patterns allow and comfort unaffected.

## Sizing and Performance

- Buffer volume: 200–300 L is typically sufficient for 3 persons with showers and occasional bath; choose larger end if simultaneous draws are common.
- FriWa capacity: 25–35 kW HX module typically gives 10–16 L/min at 40–45°C with sufficient primary temperature; confirm with manufacturer curves.
- Approach temperature: Ensure primary (DHW buffer) temperature margin to meet outlet setpoint during peak draws; tune FriWa PID.

## Water Quality and Maintenance

- Potable side: inline filter/strainer; periodic inspection/descaling based on local hardness.
- Primary side (system water): VDI 2035 treatment to protect plate HX, pumps, valves; monitor conductivity/hardness.
- Serviceability: install isolation valves, drains, and test taps for FriWa and DHW buffer.

## Commissioning Checks

- Verify FriWa outlet stability from 2–16 L/min; ensure no overshoot/undershoot.
- Confirm anti‑scald protection at outlets (thermostatic mixers where applicable).
- Log DHW charging periods and temperatures; validate PV alignment.
