# Review Report: 07_richter.json (Richter / Judges)

## Übersicht & Metriken
- **Geprüfte Fragen:** 140
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 45 (Vokabular- und Rechtschreibangleichung an Luther 1912, Großschreibung von NICHT/KEIN, Option-Balancierung)
- **Geänderte Fragen (EN):** 82 (Neuausrichtung und KJV-1769-Neuübersetzung verschobener Frageblöcke 18–50, 59–79, 109–132 sowie Angleichung an DE 1:1)
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 1 (Kultische Sach- und Begriffsklärung in `ri_055`: Priesterliches Ephod zur Gottesbefragung vs. Gideons Abgötterei)
- **Entfernte / bereinigte Erklärungen:** 139 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle 560 Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 140 Fragen vollständig in `en/07_richter.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten, KJV-Verszählung und balancierter Optionen

## Bemerkenswerte Vokabel- und Inhaltsänderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `ri_001` | DE: `hinaufziehen` statt `in den Kampf ziehen` | Luther 1912 Richter 1:1 (`wer soll unter uns zuerst hinaufziehen?`). |
| `ri_002` | DE: `Daumenscheiben` / `Daumen an Händen und Füßen` statt moderner Umschreibungen | Luther 1912 Richter 1:6 (`Daumen an seinen Händen und Füßen abgehauen`). |
| `ri_004` | DE: `Wollte Gott, dass du mir einen Segen gäbest` statt `Gib mir doch eine Segensgabe!` | Luther 1912 Richter 1:15 Wortlaut. |
| `ri_005` | DE: `eiserne Wagen` statt `Sichelwagen`; Negation `NICHT` | Luther 1912 Richter 1:19 (`denn sie hatten eiserne Wagen`). |
| `ri_006` | DE: `zinsbar` statt `frondienstpflichtig` | Luther 1912 Richter 1:28 (`dass sie zinsbar wurden`). |
| `ri_017` | DE: `Ochsenstecken` statt `Ochsentreiberstab`; KJV: `ox goad` | Luther 1912 Richter 3:31 (`mit einem Ochsenstecken`); KJV (`with an ox goad`). |
| `ri_018`–`ri_050` | EN: Vollständig neu übersetzt und an DE ausgerichtet | Die englischen Fragen 18–50 waren inhaltlich gegen andere Verse formuliert und stimmten nicht mit den deutschen Fragen überein. |
| `ri_051` | DE: `Sebah und Zalmuna` statt `Sebach und Salmunna`; `Pnuel` statt `Penuel` | Luther 1912 Schreibweise (Richter 8:5-8). |
| `ri_055` | DE & EN: Historische Begriffserklärung zum Ephod beibehalten | Priesterlicher Gegenstand zur Befragung des HERRN; Gideons Fallstrick. |
| `ri_058` | DE: `Jotham, der jüngste Sohn Jerubbaals`; Optionen balanciert | Luther 1912 Richter 9:5; Balance der Distraktoren. |
| `ri_059`–`ri_079` | EN: Vollständig neu übersetzt und an DE ausgerichtet | Verschiebung behoben; 1:1-Übereinstimmung mit DE hergestellt. |
| `ri_068` | DE: `Jephta` statt `Jephtha`; `Tob` | Luther 1912 Richter 11:1-3. |
| `ri_080`–`ri_105` | DE: `Simson` statt `Samson` | Durchgehende Harmonisierung auf die authentische Luther-1912-Namensform. |
| `ri_082` | DE: `ein Geweihter Gottes` statt `ein Nasiräer` | Luther 1912 Richter 13:5 (`ein Geweihter Gottes wird der Knabe sein`). |
| `ri_093` | DE: `dreihundert Füchse` | Luther 1912 Richter 15:4 (`fing dreihundert Füchse`, KJV: `three hundred foxes`). |
| `ri_097` | DE: `Eselkinnbacken` | Luther 1912 Richter 15:15-16 (`frischen Eselkinnbacken`, KJV: `jawbone of an ass`). |
| `ri_099`, `ri_100` | EN: Optionen-Reihenfolge korrigiert | In EN waren die Distraktoren vertauscht, sodass der Lösungsindex auf die falsche Option zeigte. |
| `ri_106` | DE: `tausendundhundert Silberlinge` statt modern `1100 Silberstücke` | Luther 1912 Richter 17:2. |
| `ri_109`–`ri_132` | EN: Vollständig neu übersetzt und an DE ausgerichtet | Behebung der inhaltlichen Verschiebung in den Erzählungen um Micha und Gibea. |
| `ri_113` | DE: `Kebsweib` statt `Nebenfrau`; KJV: `concubine` | Luther 1912 Richter 19:1; KJV (`concubine`). |
| `ri_116` | DE: `böse Buben` statt `Söhne Belials`; KJV: `sons of Belial` | Luther 1912 Richter 19:22 (`Männer der Stadt, böse Buben`); KJV (`sons of Belial`). |
| `ri_138` | DE & EN: Distraktor balanciert | Überlanger Distraktor auf einheitliche Länge verkürzt. |
| `ri_139` | DE: Multi-Ref auf `Richter 4:4-22` zusammengefasst; Distraktoren balanciert | Validierungskonforme Referenz und balancierte Optionen. |
| `ri_140` | DE & EN: Referenz auf `Richter 3:9` verengt | Startvers für Reihenfolgefrage. |

## Zur menschlichen Entscheidung

1. **Neuausrichtung der englischen Frageblöcke (18–50, 59–79, 109–132):**
   In der englischen Ursprungsfassung waren mehrere größere Abschnitte gegenüber der deutschen Datei versetzt (andere Fragestellungen zu anderen Versen innerhalb desselben Buchs). Sämtliche 140 englischen Fragen stimmen nun semantisch, thematisch und in den Lösungsindizes exakt 1:1 mit der deutschen Vorlage überein und nutzen die KJV 1769.

2. **Korrektur vertauschter Optionen in `ri_099` und `ri_100`:**
   In der englischen Version waren bei `ri_099` und `ri_100` die Distraktoren in abweichender Reihenfolge eingetragen, wodurch `correctAnswers: [0]` auf eine falsche Antwort zeigte. Die englischen Optionen wurden an die Reihenfolge der deutschen Vorlage angepasst.

3. **Namens- und Begriffsharmonisierung auf Luther 1912:**
   - „Simson“ statt „Samson“ (Fragen 80–105).
   - „Jephta“ statt „Jephtha“.
   - „Sebah und Zalmuna“ / „Pnuel“ statt „Sebach und Salmunna“ / „Penuel“.
   - „Kebsweib“ statt „Nebenfrau“.
   - „ein Geweihter Gottes“ statt „ein Nasiräer“ (Richter 13:5).
