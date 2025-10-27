# Entwurfsarchitektur — Doppelpuffer

Hydraulisches Konzept mit zwei Speichern: ein separater, ganzjährig heißer TWW‑Heizspeicher (speist eine Frischwasserstation, FriWa) sowie ein Heiz‑/Kühlspeicher, der im Winter warm und im Sommer kalt betrieben wird. Keine Klimageräte oder Fan‑Coils; Kühlung über UFH mit Taupunkt‑Schutz.

## Einlinienschema (ASCII)

```
           [PV + Batterie + Unterverteilung Wichtige Stromkreise]
                              |
                        [Netzversorgung]
                              |
                         [L/W‑WP R290]
                              |
                     (optional Platten‑WT)
                              |
                     +--------+---------+
                     |                  |
          [Heiz-/Kühlspeicher]       [TWW‑Heizspeicher]
            800–1000 L, schichtend      200–300 L, 55–60 °C
                     |                  |
                     |                  +--> [FriWa] --> TWW zu Zapfstellen
                     |                           ^
                     |                           |
               +-----+----+                 Kaltwasser
               |          |
            3‑Wege      Rücklauf
            Mischer       UFH
               |          ^
               v          |
            [UFH VL]  --> Loops --> [UFH RL]

 [Wasserführender Ofen] --(Rücklaufanhebung, Sicherheit)--> Puffer oben
```

Hinweise:
- Der TWW‑Heizspeicher enthält Heizungswasser (kein Trinkwasser). Die FriWa erwärmt Trinkwasser im Durchlauf über einen Plattenwärmetauscher.
- Der Heiz-/Kühlspeicher dient als hydraulische Weiche und Energiespeicher. Im Sommer nachts kühlen, tagsüber nutzen.
- Optionaler Plattenwärmetauscher (PHE) zwischen WP und Hauskreis ermöglicht Glykol auf WP‑Seite und schützt die Wasserqualität.

## Betriebsarten

- Winter
  - Wettergeführter Betrieb; WP belädt den Heiz-/Kühlspeicher (Mitte) für den Heizbetrieb; Auslegung VL ≤ 35 °C.
  - Mittags (PV‑Fenster) hat TWW Priorität: TWW‑Speicher auf 55–60 °C laden, danach Rückkehr zum Heizen.
  - Ofen lädt Puffer oben (Rücklaufanhebung ≥ 60 °C); thermische Ablaufsicherung und Notkühlung gemäß EN 303‑5.
  - HA orchestriert Prioritäten/Meldungen; Sicherheits- und Grenzwerte sind hart verdrahtet.

- Sommer
  - Nacht: WP kühlt den Heiz-/Kühlspeicher auf ~16–18 °C.
  - Tag: UFH‑Vorlauf wird auf ≥ (Taupunkt + 2 K) begrenzt, typ. 19–21 °C (Kondensationsschutz).
  - TWW‑Speicher bleibt ganzjährig heiß; mittags per PV laden.

- Übergangszeit
  - Minimale Puffersollwerte; TWW mittags; Nachtkühlung bei Hitzeperioden.

## Sollwerte, Grenzen, Sensorik

- TWW‑Heizspeicher: 55–60 °C; Verbrühschutz an Entnahmestellen.
- Heiz-/Kühlspeicher Winter: so, dass VL ≤ 35 °C erreicht wird.
- Heiz-/Kühlspeicher Sommer: Nachtziel 16–18 °C.
- UFH im Kühlbetrieb: ≥ (Taupunkt + 2 K). Beispiel: 26 °C/60 % r.F. → Taupunkt ≈ 17,8 °C → VL ≥ 20 °C.
- Sensorik (Minimum):
  - Speicher oben/Mitte/unten (beide Speicher)
  - UFH: VL/RL; optional Oberflächensensor am Verteiler
  - Raumklima: mind. ein T/r.F.-Sensor pro Etage (Taupunkt)
  - Wärmemengen: WP→Puffer, ggf. FriWa‑Primär

## Dimensionierung (Richtwerte)

- WP: nach EN 12831; typisch 4–6 kW @ −10 °C; Gerät 6–10 kW Klasse mit guter Modulation/Leisebetrieb.
- Heiz-/Kühlspeicher: 800–1000 L, 100–150 mm Dämmung, geringe Δp‑Anschlüsse, 3 Tauchhülsen.
- TWW‑Heizspeicher: 200–300 L, 3 Tauchhülsen, 55–60 °C.
- FriWa: 25–35 kW Platten‑WT‑Modul mit variabler Primärpumpe, Durchflusssensor, elektronischer Auslauftemperaturregelung; Trinkwasserseite mit Filter/Service.
- Ventile/Pumpen: Hocheffizienzpumpen; 3‑Wege‑Mischer (UFH) mit fester Taupunkt‑Begrenzung; motorische Absperrungen für Sommer/Winter; Rückflussverhinderer, Strangregulierungen.
- Optionaler PHE: auf volle Leistung mit kleinem Annäherungs‑ΔT; Glykol WP‑seitig; Luft/Schlammabscheider.
- Ausdehnungsgefäße: auf Gesamtvolumen ausgelegt (Speicher + Rohrnetz + Heizflächen).

## Sicherheit und Wasserqualität

- Ofenkreis: Rücklaufanhebung (≥ 60 °C), thermische Ablaufsicherung, schwerkrafttaugliche Notkühlung, ausreichendes MAG; EN 303‑5.
- System: Sicherheitsventile (i. d. R. 3 bar), Luft/Schlammabscheider, VDI 2035‑gerechtes Wasser; warme Leitungen dämmen, kalte diffusionsdicht inkl. Kondensatableitung.
- Elektro: Unterverteilung für wichtige Stromkreise (HP‑Freigabe, Pumpen, Regler, Netzwerk, Kühlung, ausgewählte Stromkreise).

## Regelungszuordnung

- Primär/Sicherheit: WP‑Regler; Hydraulikregler für Mischer, Pumpen, Temperaturgrenzen, TWW‑Priorität; harte Verriegelungen (nicht HA‑abhängig).
- Orchestrierung (HA): PV‑Zeitfenster (z. B. TWW mittags), Saisonumschaltung, Meldungen (Ofen, Filterservice, r.F./T‑Abweichungen), Logging (Puffer, r.F., Energie, COP‑Proxy).
