# Projektüberblick

- Gebäude: Reihenmittelhaus (~113 m²), Baujahr ~1972, EG + DG + Keller.
- Belegung: 3 Personen.
- Energie (2023):
  - Raumwärme: ~9.824 kWh/a (~87 kWh/m²·a), Fernwärme.
  - TWW‑Volumen: ~16,86 m³ (≈881 kWh/a thermisch, ΔT≈45 K).
  - Strom: ~2.671 kWh/a.
- Ziele:
  - Effizienzhaus 85 + Erneuerbare‑Energien‑Klasse (≥65 % erneuerbare Wärme/Kälte) erreichen.
  - Hohen PV‑Eigenverbrauch, Resilienz durch Batteriespeicher und Unterverteilung für wichtige Stromkreise.
  - Einfache, effiziente Bedienung, sichere Regelung, saubere Inbetriebnahme.
  - Sanftes hydronisches Kühlen ohne Klimageräte (UFH + Taupunkt‑Schutz).

## Schlüsselentscheidungen

- Doppelpuffer‑System:
  - TWW‑Heizspeicher (200–300 L) ganzjährig heiß (55–60 °C), speist FriWa (kein Trinkwasserspeicher).
  - Heiz-/Kühlspeicher (800–1.000 L) im Winter warm, im Sommer kalt (Ziel 16–18 °C für Nachtladung).
- Wärmeerzeuger: Reversible Luft‑Wasser‑Wärmepumpe (R290), monovalent nach Heizlast; wasserführender Holzofen als Komfort/Backup.
- Verteilung: Wassergeführte Fußbodenheizung (UFH) in Hauptzonen; keine Gebläsekonvektoren, keine AC.
- Lüftung: Dezentrale Einzelraumgeräte (6–8 Stück) gemäß DIN 1946‑6.
- Steuerung: Harte Sicherheits‑/Regeltechnik + Taupunktlogik; Home Assistant (HA) zur PV‑Orchestrierung/Monitoring.

## Zielwerte

- Hülle (typisch EH85):
  - Kellerdecke U ≤ 0,25 W/(m²·K)
  - Dach/Oberste Decke U ≤ 0,14 W/(m²·K)
  - Fenster Uw ≤ 0,90 W/(m²·K)
  - Luftdichtheit n50 ≤ 1,5 h⁻¹ (Blower‑Door vorher/nachher)
- Hydronik:
  - Heizen: Auslegung VL ≤ 35 °C; lange Verdichterlaufzeiten.
  - Kühlen: VL ≥ Taupunkt + 2 K, typ. 19–21 °C.
  - UFH‑Kühlleistung: ~10–25 W/m² (≈1,1–2,8 kW gesamt).

## Erwartete Wirkungen (grobe Ordnung)

- Hülle + Wärmebrücken: ~25–40 % weniger Heizenergie ggü. Ist‑Zustand.
- PV ~5,8–8 kWp: ~5,5–8,5 MWh/a; mit ~10 kWh Speicher 50–70 % Eigenverbrauch realistisch.
- Hydronisches Kühlen: angenehme Grundkühlung; Feuchte über Lüftung/Taupunktlogik geführt (bei Extremwetter ggf. mobiler Entfeuchter).

## Randbedingungen

- Offenes Kellertreppenhaus: Luftdichte, transparente Abtrennung + Kellerdeckendämmung.
- Loggia/Eingangsbereich: ausgeprägte Wärmebrücken; Optionen siehe 05_envelope-airtightness.md.
- Keine zentrale Lüftung möglich: Einzelraumgeräte mit akustischer und strömungstechnischer Planung.
