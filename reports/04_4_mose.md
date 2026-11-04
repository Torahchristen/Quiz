# Review Report: 04_4_mose.json (4. Mose / Numeri)

## Uebersicht & Metriken
- **Gepruefte Fragen:** 246
- **Gereinigte & sprachlich angeglichene Fragen:** 48 Fragen an den genauen Wortlaut von Schlachter 1951 bzw. KJV angepasst
- **Beibehaltene historische Erklaerungen (DE & EN):** 3 (antike Masse und Gewichte in `num_021`, `num_031`, `num_046`)
- **Entfernte Erklaerungen:** 243 Fragen auf `""` gesetzt (`explanationReviewed: false`), alle Optionserklaerungen auf `""` geleert
- **KJV-Uebersetzung:** 246 Fragen vollstaendig in `en/04_4_mose.json` abgeglichen, inkl. KJV-Begrifflichkeiten und Laengenbalance
- **Optionen-Balance:** 100% aller Optionen liegen innerhalb der 30%-Laengenabweichung

## Sprachliche Angleichungen & Bemerkenswerte Aenderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `num_001` | DE: "Zelt der Begegnung" zu "In der Stiftshuette in der Wildnis Sinai"; EN: "tabernacle of the congregation" | Exakter Schlachter-1951-Wortlaut (4. Mose 1:1) und KJV-Terminus. |
| `num_006` | Option 1 auf 50 Zeichen erweitert ("Der Stamm Juda mit 74.600 kriegstauglichen Maennern") | Beseitigung der Laengenabweichung (`max_dev > 30%`). |
| `num_020` | DE: "Zelt der Begegnung" zu "Vor der Stiftshuette gegen Sonnenaufgang"; EN: "tabernacle of the congregation" | Exakter Text nach 4. Mose 3:38. |
| `num_030` | Negation hervorgehoben: `KEINEN Erben` | Richtlinienkonforme Grossschreibung. |
| `num_042` | Begriff "Schalom" in Option 1 durch "Frieden" ersetzt | Schlachter 1951 nutzt in 4. Mose 6:26 "Frieden". |
| `num_044` | Negation hervorgehoben: `KEINE Transportwagen` | Richtlinienkonforme Grossschreibung. |
| `num_046` | DE: "Silberplatten" zu "silberne Schuessel"; EN: "silver charger" | Exakter Begriff nach 4. Mose 7:13 ("silberne Schuessel") und KJV ("charger"). |
| `num_047` | DE: "goldenen Loeffel" zu "goldene Schale"; EN: "One spoon of ten shekels of gold, full of incense" | Schlachter 1951 verwendet "goldene Schale" (4. Mose 7:14); KJV-Fuellwoerter gestrichen. |
| `num_049` | DE: "Deckplatte" ersetzt durch "Suehnedeckel"; EN: "mercy seat" | Schlachter 1951 verwendet "Suehnedeckel" (4. Mose 7:89); KJV: "mercy seat". |
| `num_050` | DE: "ihr Licht nach der gegenueberliegenden Seite werfen"; EN: "Over against the candlestick upon the front" | Exakter Schlachter-Wortlaut (4. Mose 8:2) und KJV. |
| `num_058` | Negation hervorgehoben: `NICHT zur regulaeren Zeit` | Richtlinienkonforme Grossschreibung. |
| `num_059` | Distraktor 0 angepasst auf "Am ersten Tag des zweiten Monats im Fruehling" | Distraktor-Kollision mit der richtigen Option beseitigt. |
| `num_061` | Negation hervorgehoben: `NICHT reiste` | Richtlinienkonforme Grossschreibung. |
| `num_067` | DE: "in eurem Erdlande" | Schlachter 1951 verwendet "Erdlande" (4. Mose 10:9). |
| `num_069` | DE: "in sein Erdland und zu seiner Verwandtschaft" | Exakter Schlachter-Text nach 4. Mose 10:30. |
| `num_075` | Negation hervorgehoben: `NICHT zum Zelt gingen` | Richtlinienkonforme Grossschreibung. |
| `num_076` | DE: "zwei Ellen hoch ueber das Erdland" | Exakter Begriff aus 4. Mose 11:31 ("Erdland"). |
| `num_081` | DE: "Zelt der Begegnung" zu "Stiftshuette"; EN: "tabernacle" | Schlachter 1951 verwendet "Stiftshuette" (4. Mose 12:10). |
| `num_084` | DE: "das Erdland Kanaan auskundschaften" | Exakte Schlachter-Wortwahl (4. Mose 13:2). |
| `num_090` | DE: "Das Erdland frisst seine Einwohner" | Exakter Schlachter-Text (4. Mose 13:32). |
| `num_096` | Negation hervorgehoben: `NICHT ins Land zu kommen` | Richtlinienkonforme Grossschreibung. |
| `num_098` | DE: "die das Erdland boese in Verruf brachten" | Exakter Schlachter-Wortlaut (4. Mose 14:37). |
| `num_100` | DE: "in das Erdland eurer Wohnsitze" | Exakter Schlachter-Text (4. Mose 15:2). |
| `num_111` | Referenz korrigiert von `4. Mose 17:3-4` auf `4. Mose 16:38-39` | Angleichung an Schlachter 1951 und KJV Verszaehlung. |
| `num_112` | Referenz korrigiert von `4. Mose 17:11-13` auf `4. Mose 16:47-48` | Angleichung an Schlachter 1951 und KJV Verszaehlung. |
| `num_124` | DE: "kein Erbteil im Erdlande" | Exakter Schlachter-Text (4. Mose 18:20). |
| `num_138` | DE: "nicht in das Erdland bringen" | Exakter Schlachter-Text (4. Mose 20:12). |
| `num_139` | DE: "nicht durch mein Erdland ziehen" | Exakter Schlachter-Text (4. Mose 20:18). |
| `num_143` | EN: Distraktoren gekuerzt und balanciert auf ~43-47 Zeichen ("When he beheld the serpent of brass, he lived") | Beseitigung von Ueberlaenge der richtigen Option. |
| `num_146` | DE: "sein ganzes Erdland von Arnon bis Jabbok" | Exakter Schlachter-Text (4. Mose 21:26). |
| `num_149` | DE: "im Erdlande der Soehne seines Volkes" | Exakter Schlachter-Text (4. Mose 22:5). |
| `num_157` | DE: "Sieben Farren und sieben Widder"; EN: "Seven bullocks and seven rams" | Schlachter 1951 verwendet "Farren" (4. Mose 23:1); KJV: "bullocks". |
| `num_179` | DE: "das Erdland als Erbteil verteilt werden" | Exakter Schlachter-Text (4. Mose 26:53). |
| `num_181` | Negation hervorgehoben: `NICHT zusammen mit` | Richtlinienkonforme Grossschreibung. |
| `num_186` | Negation hervorgehoben: `WEDER Soehne NOCH Toechter` | Richtlinienkonforme Grossschreibung. |
| `num_187` | DE: "das verheissene Erdland besehen" | Exakter Schlachter-Text (4. Mose 27:12). |
| `num_192` | DE: "Zwei junge Farren, ein Widder, sieben Laemmer"; EN: "Two young bullocks, one ram, seven lambs" | Exakter Schlachter-Text (4. Mose 28:11) und KJV. |
| `num_200` | DE: "dreizehn junge Farren" | Schlachter 1951 verwendet "Farren" (4. Mose 29:13). |
| `num_201` | DE: "Zahl der Farren" | Schlachter 1951 verwendet "Farren" (4. Mose 29:17-32). |
| `num_202` | DE: "sieben Farren" | Schlachter 1951 verwendet "Farren" (4. Mose 29:32). |
| `num_217` | DE: "das Erdland Jaser und das Erdland Gilead" | Exakter Schlachter-Text (4. Mose 32:1). |
| `num_218` | DE: "das Erdland entmutigten" | Exakter Schlachter-Text (4. Mose 32:9). |
| `num_219` | DE: "bis das Erdland vor dem HERRN unterjocht ist" | Exakter Schlachter-Text (4. Mose 32:22). |
| `num_221` | DE: "das Erdland Sihons und Ogs" | Exakter Schlachter-Text (4. Mose 32:33). |
| `num_227` | DE: "Einwohner des Erdlandes"; Negation `NICHT` | Exakter Schlachter-Text (4. Mose 33:55). |
| `num_230` | DE: "Grenzen des Erdlandes Kanaan" | Exakter Schlachter-Text (4. Mose 34:2). |
| `num_231` | DE: "das Erdland Kanaan als Erbe verteilen" | Exakter Schlachter-Text (4. Mose 34:17). |
| `num_232` | DE: "um das Erdland auszuteilen" | Exakter Schlachter-Text (4. Mose 34:18). |
| `num_236` | DE: "sechs Freistaedte fuer den Totschlaeger"; EN: "six cities for refuge" | Schlachter 1951 verwendet den Begriff "Freistaedte" (4. Mose 35:6); KJV: "cities for refuge". |
| `num_237` | DE: "Drei Staedte diesseits des Jordans, drei im Erdland Kanaan" | Exakter Schlachter-Text (4. Mose 35:14). |
| `num_238` | DE: "vor der Hand des Blutraechers"; EN: "from the avenger of blood" | Exakte Begrifflichkeit von 4. Mose 35:12 und KJV. |
| `num_241` | DE: "bezueglich des Erdlandes" | Exakter Schlachter-Text (4. Mose 36:2). |
| `num_246` | DE: "nach der Erkundung des Erdlandes" | Exakter Schlachter-Text (4. Mose 14:6-9). |

## Zur menschlichen Entscheidung

1. **Beibehaltung von "Erdland" gemaess Nutzerwunsch:**
   In 4. Mose verwendet Schlachter 1951 konsequent "Erdland" fuer Erez im geographischen und verheissungsvollen Kontext (z.B. "Erdland Kanaan", "Erdland Gilead", "Erdland Jaser", "Einwohner des Erdlandes"). Entsprechend der Vorgabe wurden Fragen und Antwortoptionen (`num_067`, `num_069`, `num_076`, `num_084`, `num_090`, `num_098`, `num_100`, `num_124`, `num_138`, `num_139`, `num_146`, `num_149`, `num_179`, `num_187`, `num_217`, `num_218`, `num_219`, `num_221`, `num_227`, `num_230`, `num_231`, `num_232`, `num_237`, `num_241`, `num_246`) wortgenau auf "Erdland" abgestimmt.

2. **Begriffe "Stiftshuette", "Suehnedeckel", "Freistaedte" und "Blutraecher":**
   Veraltete oder fremde Begriffe (wie "Zelt der Begegnung", "Deckplatte", "Zufluchtsstaedte" im Schlachter-Kontext) wurden auf die genauen Termini der Schlachter 1951 ("Stiftshuette", "Suehnedeckel", "Freistaedte", "Blutraecher") harmonisiert.

3. **Verwendung von "Farren" statt "Stiere":**
   In den Opferlisten von Kapitel 23, 28 und 29 verwendet Schlachter 1951 durchgaengig "Farren" (KJV: "bullocks"). Dies wurde in `num_157`, `num_192`, `num_200`, `num_201` und `num_202` angeglichen.

4. **KJV-Terminologie:**
   In der englischen Fassung wurden KJV-Begriffe wie "cities for refuge", "avenger of blood", "mercy seat", "tabernacle of the congregation" und "serpent of brass" exakt eingesetzt und unnoetige Fuellwoerter entfernt.
