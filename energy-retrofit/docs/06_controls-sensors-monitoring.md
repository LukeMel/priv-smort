# Controls, Sensors, Monitoring

Safety controls must be hard‑wired; Home Assistant (HA) is used for orchestration and monitoring only. Dew‑point protection is mandatory for UFH cooling.

## Safety/Primary Controls (Hard‑wired)

- Heat pump controller: compressor protections, defrost logic, supply/return limits.
- Hydronic controller: 3‑way mixing valve control for UFH, pump control, buffer temperature limits, DHW priority.
- Dew‑point cutout: direct input limiting UFH supply temperature to ≥(dew point + 2 K); independent of HA.
- Stove safety: return‑lift valve (≥60°C), thermal discharge safety valve, gravity emergency cooling path; pressure relief; expansion vessel sizing.

## Sensors and Instrumentation

- Buffers: top/mid/bottom temperatures on DHW and heating/cooling buffers.
- UFH: supply and return temperatures; optional manifold surface temperature.
- Ambient: at least one temperature/RH sensor per floor for dew point.
- Energy metering: heat meters for AWHP→buffer and FriWa primary (optional), electric sub‑meter for HP.
- Flow/pressure: as required by FriWa and UFH balancing; include purge points and drains.

## Orchestration (Home Assistant or similar)

- PV‑aware schedules: DHW buffer charge at midday; optional winter buffer preheat during PV surplus.
- Seasonal modes: winter (heating), summer (cooling + DHW only), shoulder (adaptive minimal setpoints).
- Notifications: wood stove opportunity prompts; filter service (HRV/FriWa); abnormal RH/temperature alerts; fault relays from HP.
- Data logging: buffer temps, UFH VL/RL, indoor RH/T, HP power, heat meter data; derive COP proxy where meters available.

## Example Dew‑Point Logic

- Inputs: indoor T, indoor RH → dew point; measured UFH supply temperature.
- Limit: UFH supply target = max(heating curve demand, dew point + 2 K) with absolute min typically 19–21°C.
- Fault/lockout: if supply < (dew point + 2 K) or manifold surface moisture detected, close mixing valve/stop pump until conditions safe.

## Electrical and Resilience

- Critical‑loads subpanel: HP enable, circulators, hydronic controller, HA host, network gear, fridge, selected lights/outlets.
- Surge protection: SPD coordination for PV, battery, HP, control electronics.
- Night mode: reduce acoustic output of outdoor unit and HRV where possible.
