# Review Report: 09_1_samuel.json (1. Samuel / 1 Samuel)

## Übersicht & Metriken
- **Geprüfte Fragen:** 111
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 24 (Vokabular- und Rechtschreibangleichung an Luther 1912, Großschreibung von NICHT/KEIN, Option-Balancierung)
- **Geänderte Fragen (EN):** 22 (KJV-1769-Vokabularabgleich: emerods, familiar spirit at Endor, churlish, valley of Elah)
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 1 (`1sam_070`: antikes Längenmaß zu Goliaths Körpergröße, 6 Ellen und eine Handbreit = ca. 2,90–3,00 m)
- **Entfernte / bereinigte Erklärungen:** 110 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 111 Fragen vollständig in `en/09_1_samuel.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten, KJV-Verszählung und balancierter Optionen

## Bemerkenswerte Vokabel- und Inhaltsänderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `1sam_002` | DE: `Ihn dem HERRN zu geben all sein Leben lang` | Luther 1912 1. Samuel 1:11 Wortlaut. |
| `1sam_003` | DE: `Eli meinte, sie wäre vom Weine trunken` | Luther 1912 1. Samuel 1:13 Wortlaut. |
| `1sam_010` | DE: `Von Dan an bis gen Beer-Seba im Lande` | Luther 1912 1. Samuel 3:20 Formulierung. |
| `1sam_011` | DE: `Die Lade des Bundes des HERRN von Silo` | Luther 1912 1. Samuel 4:3-4 Wortlaut. |
| `1sam_019` | DE: `Mit schmerzhaften Beulen an heimlichen Orten`; EN: `emerods in their secret parts` | Luther 1912 1. Samuel 5:6 (`mit Beulen an heimlichen Orten`, nicht moderne „Geschwüre“); KJV (`emerods`). |
| `1sam_021` | DE: `Fünf goldene Beulen und fünf goldene Mäuse`; EN: `emerods` | Luther 1912 1. Samuel 6:4 (`Fünf goldene Beulen und fünf goldene Mäuse`, nicht Schlachter „Geschwüre“); KJV (`emerods`). |
| `1sam_047` | Negation hervorgehoben: `Samuel NICHT zur Zeit erschien` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1sam_056` | Optionen präzisiert und auf 38–44 Zeichen balanciert | Beseitigung der auffälligen Längenabweichung (`max_dev > 30%`). |
| `1sam_063` | Negation hervorgehoben: `Seine Beschlüsse NICHT bereut` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1sam_070` | Historische Maßerklärung beibehalten (6 Ellen und eine Handbreit = ca. 2,90–3,00 m) | Antikes Längenmaß nach Richtlinie 3 präzise und sachlich erläutert. |
| `1sam_073` | Optionen balanciert auf 39–44 Zeichen | Beseitigung der Längenabweichung (`max_dev > 30%`). |
| `1sam_076` | Namensform von `Mikal` zu `Michal` angepasst; `Hundert Vorhäute der Philister` | Entspricht der authentischen Namensform der Luther 1912 (1. Samuel 18:25). |
| `1sam_077` | Namensform von `Mikal` zu `Michal` angepasst | Entspricht der authentischen Namensform der Luther 1912. |
| `1sam_080` | Optionen balanciert auf 41–48 Zeichen | Beseitigung der auffälligen Längenabweichung (`max_dev > 30%`). |
| `1sam_088` | DE: `Er war hart und boshaft in seinen Händeln`; EN: `churlish and evil in his doings` | Luther 1912 1. Samuel 25:3 Wortlaut; KJV 1769 Wortlaut. |
| `1sam_092` | Ein-Wort-Optionen balanciert („Die Stadt ...“, 14–19 Zeichen) | Angleichung der Längen und Beseitigung auffälliger Abweichungen. |
| `1sam_093` | DE: `Er suchte ein Weib zu Endor mit Wahrsagergeist`; EN: `familiar spirit at Endor` | Luther 1912 1. Samuel 28:7 Wortlaut; KJV 1769 (`familiar spirit at Endor`). |
| `1sam_095` | Negation hervorgehoben: `Warum durfte David NICHT mit den Truppen` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1sam_111` | DE: `Achis` statt `Achisch` | Luther 1912 Schreibweise (1. Samuel 27:2). |
| `1sam_115` | DE: `Achis` statt `Achisch` | Luther 1912 Schreibweise (1. Samuel 29:6). |
| `1sam_116` | Optionen balanciert auf 15–17 Zeichen („Der junge Samuel“ etc.) | Beseitigung extremer Ein-Wort-Längenabweichungen. |
| `1sam_117` | Optionen balanciert auf 17–23 Zeichen („Der Krieger Abisai“ etc.) | Beseitigung extremer Ein-Wort-Längenabweichungen. |
| `1sam_118` | DE: `Die Schleuder in seiner Hand`; EN: `His sling in his hand` | Luther 1912 1. Samuel 17:40 Wortlaut; KJV 1769. |
| `1sam_119` | DE: `im Eichgrunde` statt Schlachter `im Tal Terebinthe`; EN: `valley of Elah` | Luther 1912 1. Samuel 17:2, 17:19 (`im Eichgrunde`); KJV (`valley of Elah`). |

## Zur menschlichen Entscheidung

1. **Vokabularharmonisierung gemäß Luther 1912 und KJV 1769:**
   - „Beulen“ statt Schlachter „Geschwüre“ in 1. Samuel 5:6 und 6:4 (`1sam_019`, `1sam_021`), KJV „emerods“.
   - „hart und boshaft in seinen Händeln“ statt moderner Umschreibung in 1. Samuel 25:3 (`1sam_088`), KJV „churlish and evil in his doings“.
   - „ein Weib zu Endor mit Wahrsagergeist“ statt moderner Umschreibung („Totenbeschwörerin“) in 1. Samuel 28:7 (`1sam_093`), KJV „a woman that had a familiar spirit at Endor“.
   - „im Eichgrunde“ statt „im Tal Terebinthe“ in `1sam_119` (analog zu `1sam_071` und `1sam_074` sowie Luther 1912 1. Samuel 17:2).
   - Namensform „Michal“ statt „Mikal“ (`1sam_076`, `1sam_077`).
   - Namensform „Achis“ statt „Achisch“ (`1sam_111`, `1sam_115`).

2. **Antike Maßerklärung zu Goliaths Körpergröße (`1sam_070`):**
   In 1. Samuel 17:4 wird Goliaths Größe mit „sechs Ellen und eine Handbreit“ beziffert. Gemäß Richtlinie 3 wurde hier eine kurze historische Erklärung beibehalten (ca. 2,90 bis 3,00 Meter).

3. **Referenzbereinigung und Längenausgleich bei Sortieraufgabe `1sam_119`:**
   Frage `1sam_119` enthielt eine lange Kette von fünf durch Semikolon getrennten Bibelstellen (`1. Samuel 16:13; 1. Samuel 17:49; 1. Samuel 19:10; 1. Samuel 31:6; 2. Samuel 2:4`). Diese wurde auf das einleitende Ereignis (`1. Samuel 16:13`) verengt, und die Stationen wurden auf einheitliche Zeichenlänge balanciert.
