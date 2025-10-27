# Project Overview

- Building: Mid‑terrace house (Reihenmittelhaus), ~113 m², built ~1972, EG + DG + cellar.
- Occupancy: 3 persons.
- Current energy (2023):
  - Space heat: ~9,824 kWh/yr (~87 kWh/m²·yr), district heating.
  - DHW: ~16.86 m³ water (~≈881 kWh/yr thermal, ΔT≈45 K).
  - Electricity: ~2,671 kWh/yr.
- Goals:
  - Achieve Effizienzhaus 85 + Erneuerbare‑Energien‑Klasse (≥65% renewable share for heat/cold).
  - Strong PV self‑consumption; resilience with battery and critical‑loads subpanel.
  - Efficient, simple‑to‑operate system with safe controls and clean commissioning.
  - Gentle hydronic cooling without AC (UFH cooling with dew‑point protection).

## Key Design Decisions

- Dual‑buffer system:
  - DHW heating buffer (200–300 L) always hot (55–60°C), supplies FriWa (no potable storage).
  - Heating/Cooling buffer (800–1,000 L) hot in winter, cold in summer (16–18°C target for night charging).
- Heat source: Reversible air‑to‑water heat pump (AWHP, R290), monovalent for design heat load; wood stove with back‑boiler as comfort/backup.
- Distribution: Water‑based underfloor heating (UFH) in main zones; no fan‑coils, no AC.
- Ventilation: Decentralized single‑room HRV units (6–8 total), DIN 1946‑6 compliant.
- Controls: Hard‑wired safety + dew‑point logic; Home Assistant for PV‑aware orchestration and monitoring.

## Performance Targets

- Envelope targets (typical for EH 85):
  - Basement ceiling U ≤ 0.25 W/(m²·K)
  - Roof/attic U ≤ 0.14 W/(m²·K)
  - Windows Uw ≤ 0.90 W/(m²·K)
  - Airtightness n50 ≤ 1.5 h⁻¹ (pre/post blower‑door tests)
- Hydronic targets:
  - Heating design VL ≤ 35°C; long compressor runs.
  - Cooling VL ≥ dew point + 2 K, typically 19–21°C.
  - UFH cooling capacity expectation: ~10–25 W/m² (≈1.1–2.8 kW total).

## Expected Impacts (order‑of‑magnitude)

- Envelope + thermal bridge fixes: ~25–40% reduction in space‑heating energy vs. current baseline.
- PV ~5.8–8 kWp: ~5.5–8.5 MWh/yr generation; with battery 10 kWh, self‑consumption 50–70% typically achievable.
- Hydronic cooling: pleasant background cooling; humidity managed by ventilation and dew‑point limit (add dehumidifier only during unusual heat/humidity spells).

## Constraints and Notes

- Open basement staircase: add airtight glazed partition and insulate basement ceiling.
- Loggia (interior balcony) and open entry are thermal bridges; see 05_envelope‑airtightness.md for options (winter garden / vestibule prioritized).
- No central ventilation feasible; plan single‑room HRV units with proper placement and acoustics.
