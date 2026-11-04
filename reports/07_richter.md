# Review Report: 07_richter.json (Richter / Judges)

## Übersicht & Metriken
- **Geprüfte Fragen:** 140
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 12 (zuzüglich Vereinheitlichung der Schreibweise von „Simson“ in den Fragen 80–105)
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 1 (Kultische Sach- und Begriffsklärung in `ri_055`: Priesterliches Ephod zur Gottesbefragung vs. Gideons Abgötterei)
- **Entfernte / bereinigte Erklärungen:** 139 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle 560 Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 140 Fragen vollständig in `en/07_richter.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten, KJV-Verszählung und balancierter Optionen

## Bemerkenswerte Änderungen (DE)

| questionId | Was | Warum |
|---|---|---|
| `ri_005` | Negation hervorgehoben: `NICHT aus ihren Städten vertreiben konnte` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `ri_006` | Optionen harmonisiert und balanciert auf einheitlich 42 Zeichen | Beseitigung der auffälligen Längenabweichung (`max_dev > 30%`). |
| `ri_009` | Optionen präzisiert und auf 42–45 Zeichen balanciert | Beseitigung der Längenabweichung (`max_dev > 30%`). |
| `ri_016` | Optionen präzisiert und auf 26–29 Zeichen balanciert | Beseitigung der Längenabweichung (`max_dev > 30%`). |
| `ri_032` | Optionen präzisiert und auf 38–39 Zeichen balanciert | Beseitigung der Längenabweichung (`max_dev > 30%`). |
| `ri_035` | Optionen auf einheitlich 23–24 Zeichen gestrafft | Beseitigung der Längenabweichung (`max_dev > 30%`). |
| `ri_050` | Negation hervorgehoben: `NICHT sogleich zum Kampf gerufen` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `ri_055` | Historische Begriffserklärung zum Ephod beibehalten | Antiker priesterlicher Gegenstand, dessen kultische Fehlverwendung der Verskontext allein nicht vollumfänglich erklärt. |
| `ri_128` | Optionen balanciert auf einheitlich 25–28 Zeichen | Beseitigung der extremen Längenabweichung (`max_dev = 56%`). |
| `ri_134` | Negation hervorgehoben: `KEINEN einzigen Mann` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `ri_139` | Referenz von Multi-Ref auf `Richter 4:4-22` zusammengefasst | Validierungskonforme Einzelreferenz, die beide relevanten Verse umfasst. |
| `ri_140` | Referenz auf den ersten Richter `Richter 3:9` verengt | Validierungskonforme Zuweisung für Reihenfolgefragen. |
| `ri_080`–`ri_105` | Namensform von `Samson` zu `Simson` harmonisiert | Entspricht der authentischen Schreibweise der Luther 1912; in der englischen KJV-Fassung verbleibt es bei `Samson`. |

## Zur menschlichen Entscheidung

1. **Namensharmonisierung Simson vs. Samson:**
   In der Luther-1912-Übersetzung wird der hebräische Name Shimshon ausnahmslos als „Simson“ wiedergegeben. In den bestehenden Fragen 80 bis 105 wurde jedoch die moderne Form „Samson“ verwendet, während Fragen `ri_138` und `ri_140` bereits „Simson“ enthielten. Gemäß Regel 2b wurde die Schreibweise in der deutschen Datei einheitlich auf „Simson“ harmonisiert. In der englischen Datei `en/07_richter.json` wurde durchgehend die standardmäßige KJV-Namensform „Samson“ gewählt.

2. **Kultische Begriffsklärung in `ri_055` (Ephod):**
   In Übereinstimmung mit Regel 3 wurde eine kurze, sachliche historische Erklärung beibehalten: Das Ephod war nach dem mosaischen Gesetz das priesterliche Schulterkleid zur Befragung des HERRN (mit Urim und Tummim). Gideons eigenmächtiges goldenes Kultobjekt in Ophra pervertierte diese Funktion und wurde dem Volk zum geistlichen Fallstrick.

3. **Referenzbereinigung in `ri_139` und `ri_140`:**
   Frage `ri_139` enthielt zwei durch Semikolon getrennte Referenzen (`Richter 4:4; Richter 4:21`). Diese wurden in die zusammenhängende Spanne `Richter 4:4-22` überführt, wodurch sowohl Deboras Richteramt als auch Jaels Tötung Siseras abgedeckt sind. Die chronologische Anordnungsfrage `ri_140` wurde wie in den vorangegangenen Büchern auf das einleitende Ereignis (`Richter 3:9`) verengt.
