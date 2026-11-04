# Review Report: 08_rut.json (Rut / Ruth)

## Übersicht & Metriken
- **Geprüfte Fragen:** 31
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 21 (inklusive der durchgängigen Anpassung des Namens „Naemi“ gemäß Luther 1912 in 17 Fragen)
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 2 (`rut_014`: antikes Hohlmaß Epha = ca. 20–22 Liter; `rut_025`: antiker Schuh-Brauch zur Eigentums- und Rechtsübertragung nach Rut 4:7-8)
- **Entfernte / bereinigte Erklärungen:** 29 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle 124 Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 31 Fragen vollständig in `en/08_rut.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten, KJV-Verszählung und balancierter Optionen

## Bemerkenswerte Änderungen (DE)

| questionId | Was | Warum |
|---|---|---|
| `rut_002`–`rut_009`, `rut_012`, `rut_015`, `rut_016`, `rut_020`, `rut_022`, `rut_024`, `rut_027`, `rut_030`, `rut_031` | Namensform von `Noomi` zu `Naemi` harmonisiert | Entspricht der authentischen Namensform der Luther 1912 (in der englischen KJV verbleibt es bei `Naomi`). |
| `rut_014` | Option 2 balanciert und historische Maßerklärung (Epha = ca. 20–22 Liter) beibehalten | Antike Maßeinheit nach Richtlinie 3 erklärt; falscher Übersetzungshinweis der Vorversion bereinigt. |
| `rut_017` | Optionen balanciert auf einheitlich 31–36 Zeichen | Beseitigung der auffälligen Längenabweichung (`max_dev = 49%`). |
| `rut_025` | Symbolische Rechtsbrauchtumserklärung (Schuh-Ausziehen) beibehalten | Antiker alttestamentlicher Rechtsakt nach Richtlinie 3 und Benutzervorgabe präzise erläutert. |
| `rut_027` | Antwortoptionen harmonisiert auf 21–24 Zeichen | Beseitigung der extremen Längenabweichung (`Obed` hatte 4 Zeichen vs. 37 Zeichen im Distraktor). |
| `rut_031` | Optionen harmonisiert (`Hanna` statt `Abigail`) | Ausgleich der Zeichenlängen im Mehrfachauswahl-Format. |

## Zur menschlichen Entscheidung

1. **Namensharmonisierung Naemi vs. Naomi:**
   Im Textbestand der Luther 1912 lautet der Name der Schwiegermutter Ruts durchgängig „Naemi“ (z. B. Rut 1:2: „sein Weib Naemi“; Rut 4:17: „Naemi ist ein Kind geboren“). In der Quizdatei war zuvor die moderne Namensform „Noomi“ verwendet worden. Gemäß der Richtlinie für Bücher 06–39 (Luther 1912) wurde der Name in allen Fragen und Optionen auf „Naemi“ vereinheitlicht. In der englischen Fassung `en/08_rut.json` wurde die Standardform der King James Version („Naomi“) verwendet.

2. **Beibehaltung der historischen Sach- und Brauchtumserklärungen (`rut_014` und `rut_025`):**
   In Übereinstimmung mit Richtlinie 3 wurden zwei historische Erklärungen beibehalten und sprachlich präzisiert:
   - In `rut_014` die Erläuterung des antiken Hohlmaßes Epha (ca. 20 bis 22 Liter Getreide), da dieses Maß im Vers vorausgesetzt, aber nicht in seiner Dimension erklärt wird.
   - In `rut_025` die Bedeutung des alttestamentlichen Schuh-Brauchs nach Rut 4:7-8 als symbolischer Rechtsverzicht und Übertragung des Lösungsrechts auf den nächsten Verwandten.

3. **Längenausgleich in `rut_027`:**
   In Frage `rut_027` stach die richtige Option „Obed“ (4 Zeichen) gegenüber den wortreichen Distraktoren (bis zu 37 Zeichen) optisch stark hervor. Die Distraktoren und die richtige Option wurden auf 21 bis 24 Zeichen harmonisiert („Obed, der Vater Isais“), sodass ein ausgewogenes und faires Antwortbild gewährleistet ist.
