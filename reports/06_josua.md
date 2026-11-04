# Review Report: 06_josua.json (Josua / Joshua)

## Übersicht & Metriken
- **Geprüfte Fragen:** 146
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 11
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 1 (antike Maßeinheit in `jos_016`: 2000 Ellen Mindestabstand zur Bundeslade als ca. 900–1000 Meter)
- **Entfernte / bereinigte Erklärungen:** 145 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle 584 Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 146 Fragen vollständig in `en/06_josua.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten, KJV-Verszählung und balancierter Optionen

## Bemerkenswerte Änderungen (DE)

| questionId | Was | Warum |
|---|---|---|
| `jos_013` | Negation hervorgehoben: `NICHT mehr gelten` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `jos_016` | Maßerklärung beibehalten (2000 Ellen = ca. 900–1000 m) | Relevante historische Längeneinheit nach Richtlinie 3 beibehalten. |
| `jos_046` | Optionen an Luther 1912 angepasst (`Silberlinge`, `goldene Stange`) | Vorherige Version nutzte Elberfelder/Schlachter-Vokabular (`Schekel`, `Zunge`); Angleichung an den exakten Wortlaut der Luther 1912. |
| `jos_060` | Negation hervorgehoben: `NICHT töten` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `jos_086` | Negation hervorgehoben (`KEIN eigenes Erbteil`) und Optionen balanciert (28–31 Zeichen) | Richtlinienkonforme Großschreibung und Beseitigung von Längenabweichungen (`max_dev > 30%`). |
| `jos_104` | Negation hervorgehoben: `NICHT aus der Stadt Jerusalem vertrieben` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `jos_105` | Distraktor korrigiert: `in Kirjath-Arba umbenannt` statt `umgetauft` | Beseitigung des anachronistischen Begriffs `umgetauft` im alttestamentlichen Kontext. |
| `jos_107` | Negation hervorgehoben: `KEINE Söhne` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `jos_112` | Negation hervorgehoben: `noch KEIN Erbteil` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `jos_133` | Erste Option präzisiert und auf 49 Zeichen balanciert | Ausgleich der Optionenlängen (`max_dev > 30%`), sodass alle Optionen zwischen 49 und 57 Zeichen liegen. |
| `jos_146` | Referenz von Multi-Ref auf `Josua 3:17` vereinheitlicht und Option 2 balanciert | Standardisierung der Referenz für die Validierungs-Skripte und Längenausgleich der Optionen. |

## Zur menschlichen Entscheidung

1. **Biblische Begrifflichkeiten nach Luther 1912 in `jos_046`:**
   In der Vorversion enthielt Frage `jos_046` eine Anmerkung zur Textabweichung, da die Antwortoptionen mit Begriffen wie „Schekel Silber“ und „goldene Zunge“ formuliert waren. Gemäß den Richtlinien für Luther-1912-Dateien (Bücher 06–39) wurden die Optionen nun wortgetreu an den Text der Luther 1912 angepasst („zweihundert Silberlinge und eine goldene Stange“). In der englischen Fassung `en/06_josua.json` wurden die entsprechenden KJV-Begriffe verwendet („two hundred shekels of silver, and a wedge of gold“).

2. **Anachronismus in `jos_105`:**
   Der Distraktor „Sie wurde in Kirjath-Arba umgetauft“ enthielt das im Alten Testament unpassende Verb „umgetauft“. Dies wurde durch die sachgemäße Formulierung „Sie wurde in Kirjath-Arba umbenannt“ ersetzt.

3. **Referenzbereinigung in der Reihenfolge-Frage `jos_146`:**
   Die ursprüngliche Referenz enthielt eine Aneinanderreihung mehrerer Bibelstellen mit Semikolon (`Josua 3:17; Josua 6:20; Josua 7:4; Josua 9:3`), die von `parse_ref` nicht geparst werden konnte. In Übereinstimmung mit früheren Dateien (z. B. 2. Mose) wurde die Referenz auf das erste einleitende Ereignis (`Josua 3:17`) verengt.
