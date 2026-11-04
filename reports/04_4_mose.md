# Review Report: 04_4_mose.json (4. Mose / Numeri)

## Übersicht & Metriken
- **Geprüfte Fragen:** 246
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 12
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 3 (antike Maßeinheiten und Gewichte in `num_021`, `num_031`, `num_046`)
- **Entfernte / bereinigte Erklärungen:** 243 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 246 Fragen vollständig in `en/04_4_mose.json` übertragen, inkl. KJV-Begrifflichkeiten und Längenbalance

## Bemerkenswerte Änderungen (DE)

| questionId | Was | Warum |
|---|---|---|
| `num_006` | Option 1 auf 50 Zeichen erweitert ("Der Stamm Juda mit 74.600 kriegstauglichen Männern") | Beseitigung der einzigen auffälligen Längenabweichung (`max_dev > 30%`) im deutschen Originalbestand. |
| `num_030` | Negation hervorgehoben: `KEINEN Erben` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `num_042` | Begriff "Schalom" in Option 1 durch "Frieden" ersetzt ("Den Namen des HERRN, damit Er sie segne und Frieden gebe") | Schlachter 1951 nutzt in 4. Mose 6:26 "Frieden" statt der hebräischen Roh-Transliteration "Schalom". |
| `num_044` | Negation hervorgehoben: `KEINE Transportwagen` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `num_058` | Negation hervorgehoben: `NICHT zur regulären Zeit` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `num_059` | Distraktor 0 angepasst auf "Am ersten Tag des zweiten Monats im Frühling" | Distraktor 0 nannte zuvor denselben Kalendertag ("Am vierzehnten Tag des zweiten Monats") wie die richtige Option 2. |
| `num_061` | Negation hervorgehoben: `NICHT reiste` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `num_075` | Negation hervorgehoben: `NICHT zum Zelt gingen` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `num_096` | Negation hervorgehoben: `NICHT ins Land zu kommen` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `num_111` | Referenz korrigiert von `4. Mose 17:3-4` auf `4. Mose 16:38-39` | Angleichung an die Verszählung der Schlachter 1951 und KJV (Eleasars Verwertung der Räucherpfannen zu Altarblechen steht in Kapitel 16). |
| `num_112` | Referenz korrigiert von `4. Mose 17:11-13` auf `4. Mose 16:47-48` | Angleichung an die Verszählung der Schlachter 1951 und KJV (Aarons Eintreten mit der Räucherpfanne steht in Kapitel 16). |
| `num_181` | Negation hervorgehoben: `NICHT zusammen mit` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `num_186` | Negation hervorgehoben: `WEDER Söhne NOCH Töchter` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `num_227` | Negation hervorgehoben: `NICHT vertrieben würden` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |

## Zur menschlichen Entscheidung

1. **Verszählungs-Korrekturen in Kapitel 16 und 17 (`num_111`, `num_112`):**
   In der hebräischen Masora und der Lutherbibel umfasst Kapitel 17 die Verse 1 bis 15 als Bericht über Eleasars Altarbleche und Aarons Sühnung der Plage. In der Schlachter 1951 sowie in der englischen King James Version stehen diese Ereignisse jedoch am Ende von Kapitel 16 (16:36-50), während Kapitel 17 mit dem Knospen des Stabes Aarons beginnt. Die beiden deutschen Quizfragen `num_111` und `num_112` trugen noch die Luther-/MT-Referenzen `4. Mose 17:3-4` bzw. `4. Mose 17:11-13`, wodurch der Versinhalt in der Schlachter-Datenbank nicht mit der Frage übereinstimmte. Die Referenzen wurden auf `4. Mose 16:38-39` bzw. `4. Mose 16:47-48` (in KJV: `Numbers 16:38-39` bzw. `Numbers 16:46-48`) korrigiert.

2. **Beseitigung inhaltlicher Distraktor-Kollision (`num_059`):**
   In Frage `num_059` (Ersatz-Passah im zweiten Monat nach 4. Mose 9:11) lautete die richtige Option 2 "Am 14. Tag des 2. Monats zwischen den Abenden". Option 0 lautete jedoch "Am vierzehnten Tag des zweiten Monats". Da beide Optionen denselben Tag bezeichneten, war der Distraktor sachlich ebenfalls zutreffend. Option 0 wurde daher durch ein plausibles, aber falsches Frühlingsdatum ersetzt ("Am ersten Tag des zweiten Monats im Frühling").

3. **Terminologische Bereinigung (`num_042`):**
   In Option 1 von `num_042` wurde die hebräische Roh-Transliteration "Schalom" durch die authentische Schlachter-1951-Übersetzung "Frieden" ersetzt ("Den Namen des HERRN, damit Er sie segne und Frieden gebe").

4. **Minimalistische Erklärungsstrategie:**
   In 243 von 246 Fragen wurde die Erklärung auf `""` gesetzt (`explanationReviewed: false`), da der Bibelvers selbst in der App vollständig angezeigt wird. Nur bei drei antiken Maßeinheiten und Gewichten (`num_021`: Schekel und Gera; `num_031`: Zehntel-Epha; `num_046`: Schekelgewicht der silbernen Schalen) wurde eine kurze, neutrale historische Erklärung beibehalten.
