# Review Report: 08_rut.json (Rut / Ruth)

## Übersicht & Metriken
- **Geprüfte Fragen:** 31
- **Geänderte Fragen (DE):** 31 (strikte Vokabularangleichung an Luther 1912: Teuerung, Mahlon und Chiljon, Naemi, Erbe/beerben, Balancierung aller Optionen)
- **Geänderte Fragen (EN):** 31 (vollständige Neuausrichtung und Behebung kritischer Antwortschlüssel-Fehler, 1:1-Harmonisierung mit DE unter Verwendung der KJV 1769)
- **Beibehaltene / präzisierte historische Erklärungen (DE & EN):** 2 (`rut_015`: antikes Hohlmaß Epha = ca. 20–22 Liter; `rut_025`: antiker Schuh-Brauch zur Eigentums- und Rechtsübertragung nach Rut 4:7-8)
- **Entfernte / bereinigte Erklärungen:** 29 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle 124 Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 31 Fragen vollständig validiert und balanciert in `en/08_rut.json`

## Bemerkenswerte Vokabel- und Inhaltsänderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `rut_001` | DE: `Teuerung im Lande`, `da die Richter regierten` statt `Hungersnot` / `herrschten` | Luther 1912 Rut 1:1 Wortlaut. |
| `rut_002` | DE: `Bethlehem-Juda`, `sein Weib Naemi` | Luther 1912 Rut 1:1-2 Wortlaut. |
| `rut_003` | DE: `Mahlon und Chiljon` statt `Machlon und Kiljon` | Luther 1912 Schreibweise Rut 1:2-5. |
| `rut_004` | DE: `moabitische Weiber`, `Ruth`; EN: Optionen an DE angepasst | In EN war Option 0 die Lösung, während `correctAnswers: [3]` auf Hanna und Peninna zeigte. |
| `rut_005` | EN: Frage und Optionen komplett neu übersetzt | In EN bezog sich die Vorversion auf Rut 1:6, während DE nach dem Rat Naemis in Rut 1:8-12 fragte. |
| `rut_007` | EN: Distraktoren korrigiert | In EN stand die richtige Antwort auf Index 0, während der Antwortschlüssel `[2]` auf einen Distraktor zeigte. |
| `rut_008` | DE: `Heißt mich Mara, denn der Allmächtige betrübte mich` | Luther 1912 Rut 1:20-21; EN Distraktoren an DE ausgerichtet. |
| `rut_009` | DE: `Im Anfang der Gerstenernte`; Optionen balanciert (35–38 Zeichen) | Luther 1912 Rut 1:22. |
| `rut_010` | DE: `Mann von großem Vermögen`, `Boas`; EN Distraktoren angeglichen | Luther 1912 Rut 2:1 (`von großem Vermögen`, KJV: `mighty man of wealth`). |
| `rut_011` | DE: `Knaben`, `zwischen den Garben auflesen`, `nicht schelten` | Luther 1912 Rut 2:15-16. |
| `rut_014` | Erklärung nach `rut_015` verschoben | In der Vorversion war die Erklärung zum Epha fälschlich bei `rut_014` (Brot und Essig) hinterlegt. |
| `rut_015` | DE: `bei einem Epha gemessene Gerste`; historische Erklärung beibehalten | Luther 1912 Rut 2:17; Erklärung zur biblischen Maßeinheit (ca. 20–22 Liter). |
| `rut_016` | DE: `Dirnen des Boas`, `Gerstenernte und Weizenernte aus war` | Luther 1912 Rut 2:23. |
| `rut_018` | DE: `denn du bist der Erbe`, `Flügel über deine Magd breiten` | Luther 1912 Rut 3:9 (KJV: `spread skirt over handmaid`, `near kinsman`). |
| `rut_019` | DE: `tugendsam Weib`, `das ganze Tor meines Volks` | Luther 1912 Rut 3:11 (KJV: `virtuous woman`, `all the city of my people`). |
| `rut_020` | DE: `es ist einer noch näher als ich` (Erbe) | Luther 1912 Rut 3:12; EN Distraktoren synchronisiert. |
| `rut_021` | DE: `sechs Maß Gerste`; Optionen balanciert (32–34 Zeichen) | Luther 1912 Rut 3:15 (KJV: `six measures of barley`). |
| `rut_022` | DE: `Tor der Stadt Bethlehem-Juda` | Luther 1912 Rut 4:1-2; EN Distraktoren synchronisiert. |
| `rut_023` | DE: `zehn Männer von den Ältesten` | Luther 1912 Rut 4:2; EN Distraktoren synchronisiert. |
| `rut_024` | DE: `daß ich nicht vielleicht mein Erbteil verderbe` | Luther 1912 Rut 4:6 (KJV: `lest I mar mine own inheritance`). |
| `rut_025` | DE: `Zog seinen Schuh aus und gab ihn dem andern`; Rechtsbrauchtumserklärung | Luther 1912 Rut 4:7-8; Beibehaltung der Rechtsakt-Erklärung. |
| `rut_026` | DE: `wie Rahel und Lea im Hause Israel` | Luther 1912 Rut 4:11-12; EN Distraktor-Reihenfolge korrigiert. |
| `rut_027` | DE & EN: Optionen balanciert (33–38 Zeichen) | Beseitigung der extremen Längenabweichung (`Obed` 4 Zeichen vs. Distraktoren 37 Zeichen). |
| `rut_028` | DE: `König David, der Sohn Isais`; EN Antwortschlüssel korrigiert | In EN zeigte `correctAnswers: [3]` fälschlich auf Hiskia statt auf David. |
| `rut_029` | DE: `Geschlecht des Perez` | Luther 1912 Rut 4:18-22; EN Distraktoren synchronisiert. |
| `rut_030` | DE: `Ruth` | Luther 1912 Rut 1:16. |
| `rut_031` | DE & EN: `Ruth` und `Orpa` | Luther 1912 Rut 1:4. |

## Zur menschlichen Entscheidung

1. **Behebung des systematischen Antwortschlüssel-Fehlers in `en/08_rut.json`:**
   In der vorherigen englischen Übersetzung wurden die Distraktoren fast durchgängig so angelegt, dass die richtige englische Antwort an Position 0 stand, während im Array `correctAnswers` die deutschen Indizes (häufig 1, 2 oder 3) verblieben waren. Dadurch wurden im englischen Quiz absurde Falschantworten als „richtig“ gewertet (z. B. Hiskia statt David in `rut_028`, Peninna und Hanna statt Rut und Orpa in `rut_004`, 70 Älteste statt 10 in `rut_023`). Sämtliche 31 englischen Fragen und Optionen wurden 1:1 semantisch und indexgetreu an die deutschen Fragen angepasst.

2. **Vokabularharmonisierung gemäß Luther 1912:**
   - „Teuerung“ statt moderner Umschreibung „Hungersnot“ (`rut_001`).
   - „Mahlon und Chiljon“ statt Schlachter „Machlon und Kiljon“ (`rut_003`).
   - „Erbe“ / „beerben“ statt moderner Terminologie „Löser“ / „Erblöser“ in Rut 3 und 4 (`rut_018`, `rut_020`, `rut_024`).
   - „Dirnen“ und „Knaben“ für Mägde und Knechte (`rut_011`, `rut_016`).
   - „sechs Maß Gerste“ (`rut_021`).

3. **Präzisierung historischer Erklärungen (`rut_015` und `rut_025`):**
   - Die Erklärung des Hohlmaßes Epha wurde von der unpassenden Frage `rut_014` (Brot und Essig) zur eigentlichen Maßfrage `rut_015` verschoben und auf 110 Zeichen gestrafft.
   - Die rechtshistorische Erläuterung des Schuh-Brauchs in `rut_025` wurde prägnant zusammengefasst.
