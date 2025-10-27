# Trinkwarmwasser (TWW) — FriWa + TWW‑Heizspeicher

Separater TWW‑Heizspeicher (Heizungswasser) mit ~55–60 °C versorgt eine Frischwasserstation (FriWa). Es gibt keinen Trinkwasserspeicher; TWW wird im Durchlauf erwärmt.

## Begründung

- Hygiene: Kein stehendes Trinkwarmwasser → minimiertes Legionellenrisiko; Verbrühschutz an Zapfstellen.
- Sommerkompatibilität: TWW‑Speicher bleibt heiß, Heiz-/Kühlspeicher kann kalt bleiben (UFH‑Kühlung).
- PV‑Synergie: TWW‑Ladung mittags nutzt PV‑Überschuss, reduziert Abendlast.

## Hydraulik

- TWW‑Heizspeicher (200–300 L): 55–60 °C ganzjährig; oben/Mitte/unten Sensoren; gute Dämmung.
- FriWa (25–35 kW): Platten‑WT, variable Primärpumpe, Durchflusssensor, elektronische Auslauftemperatur; Trinkwasserseite mit Filter/Absperrungen.
- WP‑Priorität: Zeitbasiert (mittags) und temperaturgeführt (wenn Speichertemperatur < Soll) zuerst TWW, sonst Heiz-/Kühlspeicher.

## Regelung/Sollwerte

- TWW‑Soll: 55–60 °C (Wasserhärte/Komfort beachten). Verbrühschutzmischer einsetzen.
- PV‑Fenster: Bei hohem SoC und PV‑Überschuss TWW laden; sonst zeitversetzt/off‑peak.
- Stillstandsverluste: Speicher gut dämmen; ggf. Nachtabschaltung, wenn Bedarfsmuster es zulässt.

## Dimensionierung/Leistung

- Speicher: 200–300 L für 3 Personen (Duschen, gelegentlich Baden); eher 300 L bei parallelen Zapfungen.
- FriWa: 25–35 kW liefern typ. 10–16 L/min bei 40–45 °C (abhängig von Primärtemperatur/Kennlinien).
- Annäherung ΔT: Primärtemperatur mit Reserve zur Auslauftemperatur; FriWa‑Regelung fein abstimmen.

## Wasserqualität/Wartung

- Trinkwasserseite: Filter/Sieb; Inspektion/Entkalkung gemäß Wasserhärte.
- Primärseite: VDI 2035 (Leitfähigkeit/Härte) zum Schutz von WT, Pumpen, Ventilen.
- Service: Absperrungen, Entleerungen, Messstellen vorsehen.

## Inbetriebnahme‑Checks

- Stabiler TWW‑Auslauf 2–16 L/min ohne Überschwingen.
- Verbrühschutz prüfen.
- TWW‑Ladezeiten/Temperaturverläufe loggen und PV‑Timing verifizieren.
