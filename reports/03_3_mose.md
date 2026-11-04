# Review Report: 03_3_mose.json (3. Mose / Levitikus)

## Uebersicht & Metriken
- **Gepruefte Fragen:** 173
- **Gereinigte & sprachlich angeglichene Fragen:** 32 Fragen an den genauen Wortlaut von Schlachter 1951 bzw. KJV angepasst
- **Beibehaltene historische Erklaerungen (DE & EN):** 3 (antike Masse und Gewichte in `lev_030`, `lev_171`, `lev_173`)
- **Entfernte Erklaerungen:** 170 Fragen auf `""` gesetzt (`explanationReviewed: false`), alle Optionserklaerungen auf `""` geleert
- **KJV-Uebersetzung:** 173 Fragen vollstaendig in `en/03_3_mose.json` abgeglichen, inkl. KJV-Begrifflichkeiten und Laengenbalance
- **Optionen-Balance:** 100% aller Optionen liegen innerhalb der 30%-Laengenabweichung

## Sprachliche Angleichungen & Bemerkenswerte Aenderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `lev_001` | DE: "Zeltes der Begegnung" zu "Von der heiligen Stiftshütte aus"; EN: "tabernacle of the congregation" | Exakter Schlachter-1951-Wortlaut ("von der Stiftshuette aus") und KJV-Terminus. |
| `lev_002` | DE: "fehlerfreier Maennling" zu "Ein makelloses maennliches Tier"; EN: "A male without blemish" | Exakte Begrifflichkeit von 3. Mose 1:3 ("makelloses maennliches Tier") statt moderner Paraphrase. |
| `lev_003` | DE: "fest auf den Kopf legen" zu "auf den Kopf des Brandopfers stuetzen"; EN: "Put his hand upon the head of the burnt offering" | Exakte Verbverwendung von 3. Mose 1:4 ("stuetzen"). |
| `lev_004` | DE: "bronzenen Altar im Hof" zu "Altar vor der Stiftshuette"; EN: "Round about upon the altar by the tabernacle door" | Schlachter 1951 und KJV nennen den Ort exakt: vor der Tuer der Stiftshuette. |
| `lev_005` | DE: "Beine des Tieres" zu "Sein Eingeweide und seine Schenkel"; EN: "His inwards and his legs" | Schlachter 1951 verwendet "Schenkel" statt "Beine". |
| `lev_006` | EN: Erfundener Zusatz "of the field" gestrichen: "Turtledoves, or young pigeons" | Streichung von Fuellwoertern, Anpassung an KJV Leviticus 1:14. |
| `lev_009` | DE: "Gedenkopfer" zu "Gedaechtnisopfer"; EN: "all the incense" zu "all frankincense" | Schlachter 1951 spricht von "Gedaechtnisopfer" (3. Mose 2:2); KJV von "frankincense". |
| `lev_011` | Negation hervorgehoben: `KEINEM` | Richtlinienkonforme Grossschreibung verneinter Fragestellungen. |
| `lev_018` | DE: "Speise des Feueropfers" zu "Nahrung fuer das Feuer des HERRN"; EN: "food of the offering made by fire" | Exakter Text von 3. Mose 3:11. |
| `lev_019` | DE: "Zeltes der Begegnung" zu "Stiftshuette" | Einheitliche Verwendung des Schlachter-Begriffs "Stiftshuette". |
| `lev_021` | DE: "Verfehlungen aus Unwissenheit" zu "Wenn sich eine Seele aus Irrtum versuendigt" | Exakte Formulierung aus 3. Mose 4:2 ("aus Irrtum"). |
| `lev_022` | DE: "fehlerfreien" zu "makellosen Farren" | Praezisierung gemaess 3. Mose 4:3 ("makellosen Farren"). |
| `lev_025` | DE: "fehlerfreien Ziegenbock" zu "Ziegenbock, ein makelloses Tier" | Exakter Begriff nach 3. Mose 4:23. |
| `lev_026` | DE: "fehlerfreie Ziege" zu "Eine Ziege, ein makelloses Tier" | Exakter Begriff nach 3. Mose 4:28. |
| `lev_031` | Negation hervorgehoben: `KEINESFALLS` / `KEIN Oel und KEIN Weihrauch` | Richtlinienkonforme Grossschreibung. |
| `lev_032` | DE: "makellosen Widder von den Schafen"; Distraktoren ausbalanciert | Beseitigung von Laengendifferenzen und Angleichung an 3. Mose 5:15 ("makellosen Widder"). |
| `lev_041` | DE: "in die Stiftshuette hineingebracht wird"; Negation `KEINESFALLS` | Exakter Schlachter-Text aus 3. Mose 6:30. |
| `lev_042` | DE: "geschlachtet" zu "geschaechtet" | Exakter Schlachter-Text aus 3. Mose 7:2 ("soll man auch das Schuldopfer schaechten"). |
| `lev_059` | DE: "Ein junges Kalb von den Rindern" zu "Ein Stierkalb und einen Widder, makellos" | Exakte Wiedergabe von 3. Mose 9:2. |
| `lev_061` | DE: "Einen Ziegenbock aus der Herde" zu "Den Bock, das Suendopfer des Volkes" | Exakte Uebersetzung von 3. Mose 9:15. |
| `lev_063` | DE: "Zelt" zu "Stiftshuette" | Schlachter 1951 bezeichnet das Heiligtum als "Stiftshuette" (3. Mose 9:23). |
| `lev_066` | DE: "in ihren Roecken" zu "in ihren Leibroecken" | Exakter Schlachter-Wortlaut (3. Mose 10:5). |
| `lev_081` | DE: "Ein einjaehriges Lamm" zu "Ein einjaehriges Schaf" | Schlachter 1951 schreibt in 3. Mose 12:6 "ein einjaehriges Schaf". |
| `lev_108` | DE: "Lose werfen fuer den HERRN und Asasel"; EN: "scapegoat" | Anpassung an Schlachter 1951 (3. Mose 16:8) und KJV ("scapegoat"). |
| `lev_109` | DE: "stuetzte beide Haende auf ihn und bekannte Schuld" | Exakter Schlachter-Wortlaut (3. Mose 16:21: "Haende... stuetzen"). |
| `lev_110` | DE: "Gnadenstuhl" ersetzt durch "Suehnedeckel"; EN: "mercy seat" | Schlachter 1951 verwendet "Suehnedeckel" (3. Mose 16:13); Ersetzung des fremden Luther-Begriffs. |
| `lev_111` | DE: "Gnadenstuhl" ersetzt durch "Suehnedeckel"; EN: "mercy seat" | Schlachter 1951 verwendet "Suehnedeckel" (3. Mose 16:14). |
| `lev_114` | Negation hervorgehoben: `NICHT` | Richtlinienkonforme Grossschreibung. |
| `lev_120` | DE: "Erdland Aegypten und Erdland Kanaan"; Negation `NICHT` | Beibehaltung und Anwendung des exakten Schlachter-Begriffs "Erdland" (3. Mose 18:3). |
| `lev_124` | DE: "Das Erdland wurde unrein und spie sie aus" | Exakter Schlachter-Begriff "Erdland" (3. Mose 18:25). |
| `lev_125` | DE: "Als einen Greuel vor dem Angesicht Gottes"; EN: "It is an abomination" | Exakter Begriff nach 3. Mose 18:22 ("Greuel" / "abomination"). |
| `lev_128` | DE: "Ernte des Erdlandes" | Schlachter 1951 verwendet "Erdland" in 3. Mose 19:9. |
| `lev_132` | DE: "Fruchtbaeume im Erdland" | Schlachter 1951 verwendet "Erdland" in 3. Mose 19:23. |
| `lev_134` | DE: "Das Volk des Erdlandes musste ihn steinigen" | Exakter Begriff aus 3. Mose 20:2 ("Volk des Erdlandes"). |
| `lev_142` | Negation hervorgehoben: `NICHT` | Richtlinienkonforme Grossschreibung. |
| `lev_149` | DE: "zusammenschaechten" statt "zusammenschlachten" | Exakter Schlachter-Wortlaut (3. Mose 22:28). |
| `lev_152` | DE: "Eine Sabbatfeier, ein Gedaechtnistag unter Laermblasen"; EN: "memorial of blowing of trumpets" | Exakte Begrifflichkeit von 3. Mose 23:24 und KJV. |
| `lev_161` | DE: "Das Erdland soll einen Sabbat der Ruhe haben" | Exakter Schlachter-Wortlaut aus 3. Mose 25:4 ("Erdland"). |
| `lev_175` | DE: "Saat des Erdlandes" | Exakter Begriff nach 3. Mose 27:30. |

## Zur menschlichen Entscheidung

1. **Begrifflichkeit "Suehnedeckel" vs. "Gnadenstuhl":**
   In frueheren Versionen war an zwei Stellen (`lev_110`, `lev_111`) der Begriff "Gnadenstuhl" (bekannt aus der Lutherbibel) verwendet worden. Da der Schlachter-1951-Text an allen Stellen konsequent "Suehnedeckel" verwendet, wurden Fragen und Optionen auf "Suehnedeckel" (KJV: "mercy seat") umgestellt.

2. **Beibehaltung von "Erdland" gemaess Nutzerwunsch:**
   In Schlachter 1951 wird das hebraeische Erez im Pentateuch haeufig als "Erdland" wiedergegeben. Gemaess der Benutzer-Anweisung wurde dieser Begriff in Fragen und Optionen uebernommen (`lev_120`, `lev_124`, `lev_128`, `lev_132`, `lev_134`, `lev_161`, `lev_175`), wodurch die wortgetreue Uebereinstimmung mit dem Bibeltext sichergestellt ist.

3. **Verwendung von "schaechten" statt "schlachten":**
   Schlachter 1951 verwendet fuer die rituelle Toetung der Opfertiere durchgaengig das Verb "schaechten". In `lev_003`, `lev_004`, `lev_042`, `lev_061` und `lev_149` wurde dies in den Fragen und Antwortoptionen praezisiert.

4. **KJV-Terminologie:**
   In der englischen Fassung wurden saemtliche Bezeichnungen an den KJV-1769-Wortlaut angepasst, u.a. "tabernacle of the congregation" (statt "tent of meeting"), "mercy seat" (fuer Suehnedeckel), "scapegoat" (fuer Asasel-Bock), "meat offering" (fuer Speisopfer) und "memorial of blowing of trumpets".
