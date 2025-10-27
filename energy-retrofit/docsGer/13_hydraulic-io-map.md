# Hydraulikschema — Kennzeichnung und I/O‑Plan

Ergänzende Kennzeichen (Tags) für Komponenten, Sensoren und Regel‑I/O zur Verdrahtung, Beschriftung und Inbetriebnahme.

## Tag‑Konvention

- Speicher: T1 = Heiz-/Kühlspeicher, T2 = TWW‑Heizspeicher
- Wärmepumpe: HP1
- Plattenwärmetauscher (optional): HX1 (WP↔Haus)
- Frischwasserstation: FW1
- Ofenkreis: WS1
- Pumpen: P‑xx, Ventile: V‑xx, Sensoren: S‑xx, Regler/Relais: C‑xx/R‑xx

## Komponenten/Tags

- HP1: Reversible L/W‑WP (R290)
- HX1: Optionaler PHE, Glykol WP‑seitig
- T1: Heiz-/Kühlspeicher (800–1000 L)
  - S‑T1‑TOP/MID/BOT (Temperaturen)
- T2: TWW‑Heizspeicher (200–300 L)
  - S‑T2‑TOP/MID/BOT (Temperaturen)
- FW1: FriWa (Platten‑WT, Primärpumpe, Auslauftemp‑Regelung)
  - S‑FW‑FLOW (Durchfluss), S‑FW‑OUT (TWW‑Auslauf)
- WS1: Wasserführender Ofen inkl. Sicherheit
  - V‑WS‑RL (Rücklaufanhebung ≥60 °C), V‑WS‑TD (thermische Ablaufsicherung)
- UFH: Verteiler/Schleifen
  - V‑MX‑UFH (3‑Wege‑Mischer), P‑UFH, S‑UFH‑VL/RL, S‑UFH‑SURF (optional)
- Saisonarmaturen
  - V‑SEAS‑T1/T2 für Service/Modus

## Raum‑Sensorik

- S‑AMB‑GF: EG T/r.F. (Taupunkt)
- S‑AMB‑DG: DG T/r.F. (Taupunkt)

## Elektro/Zähler

- R‑HP‑EN: WP‑Freigabe‑Relais
- M‑HP‑EL: Stromzähler WP
- M‑HP‑HT: WMZ WP→T1
- M‑FW‑HT: WMZ T2→FW1 (optional)

## I/O‑Plan (Beispiel)

- Regler C‑HYD (Hydraulik):
  - Eingänge: S‑T1‑TOP/MID/BOT, S‑T2‑TOP/MID/BOT, S‑UFH‑VL/RL, S‑AMB‑GF/DG, S‑UFH‑SURF (opt.)
  - Ausgänge: V‑MX‑UFH (0–10 V), P‑UFH (Ein/Aus oder PWM), P‑FW‑PRI (via FW1), R‑HP‑EN, V‑SEAS‑T1/T2, Alarm
  - Logik: Taupunktlimit; TWW‑Priorität; Saison; Antitakt; sicherer Stopp
- Regler C‑HP (in HP1):
  - Heizkurve; Vor-/Rücklaufgrenzen; Abtauung; Schnittstelle R‑HP‑EN
- FW1 intern:
  - Auslauftemperatur‑Soll; moduliert Primärpumpe nach Durchfluss/ΔT

## Beschriftung/Doku

- Jeder Tag erscheint in Schema, Verdrahtung, Geräteschild, Protokollen.
- Tag‑Legende ausdrucken und nahe T1/T2 anbringen.
