# Regelung, Sensorik, Monitoring

Sicherheits‑ und Primärregelung sind hart verdrahtet; Home Assistant (HA) dient nur zur Orchestrierung/Visualisierung. Taupunkt‑Schutz ist Pflicht.

## Sicherheit/Primärregelung (hart)

- WP‑Regler: Verdichterschutz, Abtauung, Vor-/Rücklauftemperaturlimits.
- Hydraulikregler: 3‑Wege‑Mischer UFH, Pumpen, Puffertemperaturgrenzen, TWW‑Priorität.
- Taupunktabschaltung: harte Begrenzung UFH‑VL ≥ (Taupunkt + 2 K), unabhängig von HA.
- Ofen: Rücklaufanhebung (≥ 60 °C), thermische Ablaufsicherung, schwerkraftgeeignete Notkühlung, MAG/PRV.

## Sensorik/Messtechnik

- Speicher: oben/Mitte/unten an TWW- und Heiz-/Kühlspeicher.
- UFH: VL/RL; optional Oberflächensensor am Verteiler.
- Raum: mind. ein T/r.F. je Etage (Taupunktberechnung).
- Energiemessung: Wärmemengen WP→Puffer, optional FriWa‑Primär; Strom‑Unterzähler WP.
- Durchfluss/Druck: nach Bedarf (FriWa/Strangregulierung), Entlüftungen/Spülstellen.

## Orchestrierung (HA o. ä.)

- PV‑Zeitfenster: TWW‑Ladung mittags; im Winter optional Puffer‑Vorwärmung bei PV‑Überschuss.
- Saisons: Winter (Heizen), Sommer (Kühlen + TWW), Übergang (minimal).
- Meldungen: Ofen‑Hinweise, Filterservice (WRG/FriWa), r.F./T‑Alarme, Fehlerrelais WP.
- Logging: Puffer‑T, UFH VL/RL, r.F./T innen, WP‑Leistung, WMZ; COP‑Proxy möglich.

## Beispiel Taupunktlogik

- Eingang: T innen, r.F. innen → Taupunkt; gemessener UFH‑VL.
- Limit: UFH‑VL‑Soll = max(Heizkurvenbedarf, Taupunkt + 2 K), absolut min. typ. 19–21 °C.
- Sperre: Bei VL < (Taupunkt + 2 K) oder Feuchte am Verteiler: Mischer schließen/Pumpe stoppen bis sicher.

## Elektro/Resilienz

- Unterverteilung wichtige Stromkreise: WP‑Freigabe, Pumpen, Hydraulikregler, HA‑Host, Netzwerk, Kühlgerät, ausgewählte Licht/Steckdosen.
- Überspannungsschutz (SPD) für PV, Speicher, WP, MSR.
- Nachtmodus: reduzierte Schallemission WP/WRG.
