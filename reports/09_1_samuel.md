# Review Report: 09_1_samuel.json (1. Samuel / 1 Samuel)

## Übersicht & Metriken
- **Geprüfte Fragen:** 111
- **Geänderte Fragen (DE Text, Referenz, Optionen oder beibehaltene Erklärung):** 15
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 1 (`1sam_070`: antikes Längenmaß zu Goliaths Körpergröße, 6 Ellen und eine Handbreit = ca. 2,90–3,00 m)
- **Entfernte / bereinigte Erklärungen:** 110 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 111 Fragen vollständig in `en/09_1_samuel.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten, KJV-Verszählung und balancierter Optionen

## Bemerkenswerte Änderungen (DE)

| questionId | Was | Warum |
|---|---|---|
| `1sam_047` | Negation hervorgehoben: `Samuel NICHT zur Zeit erschien` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1sam_056` | Optionen präzisiert und auf 38–44 Zeichen balanciert | Beseitigung der auffälligen Längenabweichung (`max_dev > 30%`). |
| `1sam_063` | Negation hervorgehoben: `Seine Beschlüsse NICHT bereut` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1sam_070` | Historische Maßerklärung beibehalten (6 Ellen und eine Handbreit = ca. 2,90–3,00 m) | Antikes Längenmaß nach Richtlinie 3 präzise und sachlich erläutert. |
| `1sam_073` | Optionen balanciert auf 39–44 Zeichen | Beseitigung der Längenabweichung (`max_dev > 30%`). |
| `1sam_076` | Namensform von `Mikal` zu `Michal` angepasst | Entspricht der authentischen Namensform der Luther 1912 (in der englischen KJV verbleibt es bei `Michal`). |
| `1sam_077` | Namensform von `Mikal` zu `Michal` angepasst | Entspricht der authentischen Namensform der Luther 1912. |
| `1sam_080` | Optionen balanciert auf 41–48 Zeichen | Beseitigung der auffälligen Längenabweichung (`max_dev > 30%`). |
| `1sam_092` | Ein-Wort-Optionen balanciert („Die Stadt ...“, 14–19 Zeichen) | Angleichung der Längen und Beseitigung auffälliger Abweichungen. |
| `1sam_093` | Negation hervorgehoben: `Gott ihm NICHT mehr durch Träume antwortete` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1sam_095` | Negation hervorgehoben: `Warum durfte David NICHT mit den Truppen` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1sam_116` | Optionen balanciert auf 15–17 Zeichen („Der junge Samuel“ etc.) | Beseitigung extremer Ein-Wort-Längenabweichungen. |
| `1sam_117` | Optionen balanciert auf 17–23 Zeichen („Der Krieger Abisai“ etc.) | Beseitigung extremer Ein-Wort-Längenabweichungen. |
| `1sam_118` | Optionen balanciert auf 30–35 Zeichen | Beseitigung der Längenabweichung (`max_dev > 30%`). |
| `1sam_119` | Multi-Referenz verengt auf `1. Samuel 16:13`; Optionen balanciert | Validierungskonforme Einzelreferenz für chronologische Reihenfolgefragen; Längenausgleich. |

## Zur menschlichen Entscheidung

1. **Namensharmonisierung Michal vs. Mikal (`1sam_076`, `1sam_077`):**
   In der Luther-1912-Übersetzung wird die jüngere Tochter Sauls durchgängig als „Michal“ geschrieben (z. B. 1. Samuel 14:49; 18:20; 19:11). In der ursprünglichen Quizdatei war die modernisierte Namensform „Mikal“ verwendet worden. Gemäß Richtlinie 2b für Luther-1912-Bücher wurde dies an den Bibeltext angepasst. Im Englischen lautet die Form in der KJV ebenfalls „Michal“.

2. **Antike Maßerklärung zu Goliaths Körpergröße (`1sam_070`):**
   In 1. Samuel 17:4 wird Goliaths Größe mit „sechs Ellen und eine Handbreit“ beziffert. Gemäß Richtlinie 3 wurde hier eine kurze, neutrale historische Erklärung beibehalten: Bei einer Elle von ca. 45–48 cm und einer Handbreit von ca. 7,5–8 cm ergibt sich eine imposante Körpergröße von etwa 2,90 bis 3,00 Metern.

3. **Referenzbereinigung und Längenausgleich bei Sortieraufgabe `1sam_119`:**
   Frage `1sam_119` enthielt eine lange Kette von fünf durch Semikolon getrennten Bibelstellen, die teilweise sogar bis in das zweite Buch Samuel reichten (`1. Samuel 16:13; 1. Samuel 17:49; 1. Samuel 19:10; 1. Samuel 31:6; 2. Samuel 2:4`). Dies widerspricht der Quiz-Validierungsregel für Einzelreferenzen. Die Referenz wurde auf das erste Ereignis der chronologischen Abfolge verengt (`1. Samuel 16:13`). Zudem wurden die Optionen so formuliert, dass sie ausgewogen zwischen 38 und 42 Zeichen lang sind.
