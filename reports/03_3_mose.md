# Review Report: 03_3_mose.json (3. Mose / Levitikus)

## Übersicht & Metriken
- **Geprüfte Fragen:** 173
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 7
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 3 (antike Maßeinheiten und Gewichte in `lev_030`, `lev_171`, `lev_173`)
- **Entfernte / bereinigte Erklärungen:** 170 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 173 Fragen vollständig in `en/03_3_mose.json` übertragen, inkl. KJV-Begrifflichkeiten und Längenbalance

## Bemerkenswerte Änderungen (DE)

| questionId | Was | Warum |
|---|---|---|
| `lev_011` | Negation hervorgehoben: `KEINEM` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `lev_031` | Negation hervorgehoben: `KEIN Öl und KEIN Weihrauch` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `lev_032` | Optionen ausbalanciert auf ~37–43 Zeichen ("Einen jungen fehlerfreien Stier vom Vieh", "Einen fehlerfreien Ziegenbock vom Kleinvieh", "Einen fehlerfreien Widder von den Schafen", "Eine fehlerfreie Ziege aus der Herde") | Beseitigung der einzigen auffälligen Längenabweichung (`CORRECT_LONGEST`) im gesamten deutschen Fragenbestand. |
| `lev_041` | Negation hervorgehoben: `KEINESFALLS` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `lev_114` | Negation hervorgehoben: `NICHT` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `lev_120` | Negation hervorgehoben: `NICHT` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `lev_142` | Negation hervorgehoben: `NICHT` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |

## Zur menschlichen Entscheidung

1. **Namens- und Verskonvention (Schlachter 1951 vs. KJV):**
   In 3. Mose stimmen die Kapitel- und Verseinteilungen der Schlachter 1951 und der King James Version (1769) zu 100 % überein. Es gab keinerlei Verszählungsverschiebungen oder unauflösbare Referenzen. Der deutsche Originalbestand war sprachlich bereits sehr rein gehalten; hebräische Roh-Transliterationen (wie *JHWH* oder *Älohim* in den Fragen/Optionen) waren im Gegensatz zu 1. und 2. Mose nicht vorhanden.

2. **Hervorhebung von Negationen:**
   Gemäß den Richtlinien wurden in sechs verneinten Fragen die Negationswörter (`NICHT`, `KEIN`, `KEINEM`, `KEINESFALLS`) in Großbuchstaben gesetzt, um Missverständnisse beim schnellen Lesen im Quizbetrieb zu vermeiden.

3. **Längenbalance-Harmonisierung (`lev_032`):**
   In Frage `lev_032` stach die richtige Option 2 ("Einen fehlerfreien Widder von den Schafen", 41 Zeichen) gegenüber den kürzeren Distraktoren (29–34 Zeichen) hervor. Durch Ergänzung passender Herkunftsbezeichnungen ("vom Vieh", "vom Kleinvieh", "aus der Herde") wurden alle vier Optionen auf einheitliche 37 bis 43 Zeichen harmonisiert.

4. **Minimalistische Erklärungsstrategie:**
   In 170 von 173 Fragen wurde die Erklärung auf `""` gesetzt (`explanationReviewed: false`), da der Bibelvers selbst in der App vollständig angezeigt wird. Lediglich bei drei antiken Maßeinheiten und Gewichten (`lev_030`: Zehntel-Epha als Tagesration Mehl; `lev_171`: Heiliger Schekel mit 20 Gera; `lev_173`: Homer Gerstensaat und Silbergewicht) wurde eine kurze, neutrale historische Erklärung beibehalten.
