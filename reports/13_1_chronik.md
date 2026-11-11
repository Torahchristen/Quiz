# Review Report: 13_1_chronik.json (1. Chronik / 1 Chronicles)

## Übersicht & Metriken
- **Geprüfte Fragen:** 85
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 32 (Angleichung an Luther 1912: Lot Gold, Zentner Gold und Silber, Nathan, Jaebez, Bath-Sua, Serubabel, Phul, Thilgath-Pilneser, Beer-Seba, Sebuel, Tilgung des verdächtigen Begriffs „Exil“ in `1chr_007` und `1chr_041`, Großschreibung von NICHT in `1chr_025` und `1chr_086`, Balancierung extremer Längenunterschiede in `1chr_002`, `1chr_020`, `1chr_034`, `1chr_038`, `1chr_039`, `1chr_041`, `1chr_042`, `1chr_050`, `1chr_053`, `1chr_067`, `1chr_074`, `1chr_077`, `1chr_082`, `1chr_084`)
- **Geänderte Fragen (EN):** 85 (Vollständige KJV-1769-Neuübertragung mit authentischem KJV-Vokabular: shekels of gold by weight, talents of gold and silver, Jabez, Bath-shua, Pul, Tilgath-pilneser, Beer-sheba, Shebuel, porters, cunning musicians, balanced options)
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 3
  - `1chr_020`: Krone von Rabba (1 Zentner Gold / 1 talent of gold = ca. 30–34 kg Feingold)
  - `1chr_023`: Dreschtenne Ornans (600 Lot Gold / 600 shekels of gold by weight = ca. 6,8–7 kg Gold)
  - `1chr_032`: Davids Stiftung (3.000 Zentner Gold / 3,000 talents of gold = ca. 100 Tonnen Feingold)
- **Entfernte / bereinigte Erklärungen:** 82 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 85 Fragen vollständig in `en/13_1_chronik.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten und balancierter Optionen

## Bemerkenswerte Vokabel- und Inhaltsänderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `1chr_001` | DE: `Mit Adam am Anfang der Schöpfung`; EN: `With Adam in the beginning of all` | Luther 1912 1. Chronik 1:1; KJV 1769. Optionen balanciert. |
| `1chr_002` | DE & EN: Optionen balanciert auf 23–25 Zeichen (`Genau sieben Söhne Isais` etc.) | Beseitigung extremer Längenabweichung (`max_dev > 50%`). |
| `1chr_004` | DE: `Jaebez`; EN: `Jabez` | Luther 1912 1. Chronik 4:9-10 Schreibweise; KJV 1769. |
| `1chr_007` | DE: Verdächtiges Fremdwort `Exil` durch biblisches `nachdem Juda um seiner Missetat willen gen Babel weggeführt war` ersetzt | Entspricht Luther 1912 1. Chronik 9:1 („weggeführt“) und tilgt Prüf-Warnung `WORD:Exil`. |
| `1chr_017` | DE: `Nathan` statt `Natan` | Luther 1912 1. Chronik 17:1 Schreibweise. |
| `1chr_020` | DE: `Ein Zentner reinen Goldes`; EN: `A talent of gold from Rabbah`; Erklärung beibehalten | Luther 1912 1. Chronik 20:2 Gewichtsangabe (Zentner); KJV 1769 (talent). Historische Erklärung zu antiken Einheiten beibehalten. |
| `1chr_023` | DE: `sechshundert Lot Gold`; EN: `six hundred shekels of gold by weight`; Erklärung beibehalten | Luther 1912 1. Chronik 21:25 Gewichtsangabe (`Lot`); KJV 1769 (`shekels`). Historische Gewichtserklärung beibehalten. |
| `1chr_025` | Negation hervorgehoben: `das Haus Gottes NICHT selbst bauen` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1chr_029` | DE: `Sebuel, Sohn Gersoms, des Sohns Moses`; EN: `Shebuel the son of Gershom` | Luther 1912 1. Chronik 26:24; KJV 1769. |
| `1chr_031` | DE: `Nathan` statt `Natan` | Luther 1912 Namensform. |
| `1chr_032` | DE: `3.000 Zentner Gold von Ophir und 7.000 Zentner Silber`; EN: `3,000 talents of gold... 7,000 talents of silver`; Erklärung beibehalten | Luther 1912 1. Chronik 29:4 Gewichtsangabe (Zentner); KJV 1769 (talents). Historische Erklärung zu antiken Gewichten beibehalten. |
| `1chr_034` | DE: `Zadok, der gottesfürchtige Priester`; Optionen balanciert auf 31–36 Zeichen | Beseitigung der extremen Längenabweichung (`max_dev = 82%`, zuvor 5 Zeichen!). |
| `1chr_035` | DE: `Nathan` statt `Natan` | Luther 1912 1. Chronik 29:29 Namensform. |
| `1chr_037` | DE: `Sein Sohn Nebajoth`; EN: `His son Nebaioth` | Luther 1912 1. Chronik 1:29; KJV 1769. |
| `1chr_038` | DE & EN: Optionen balanciert auf 30–35 Zeichen (`Zwölf Söhne von Ruben bis Asser` etc.) | Beseitigung der starken Längenabweichung (`max_dev = 72%`). |
| `1chr_039` | DE: `Salma, der Sohn Nahassons`; Optionen balanciert auf 25–30 Zeichen | Beseitigung der extremen Längenabweichung (`max_dev = 79%`, zuvor 5 Zeichen!). |
| `1chr_040` | DE: `Bath-Sua`, `Simea, Sobab, Nathan und Salomo`, `Adonia` | Luther 1912 1. Chronik 3:5 Schreibweisen. |
| `1chr_041` | DE: Verdächtiges Fremdwort `nachexilische` ersetzt durch biblisches `als Sohn Pedajas in der Geschlechtslinie`; Optionen balanciert auf 31–35 Zeichen | Beseitigung der Warnung `WORD:nachexilische` und Balancierung. |
| `1chr_042` | DE & EN: Optionen balanciert auf 47–52 Zeichen | Beseitigung der Längenabweichung (`max_dev = 33%`). |
| `1chr_043` | DE: `Beer-Seba`; EN: `Beer-sheba` | Luther 1912 1. Chronik 4:28; KJV 1769. |
| `1chr_045` | DE: `Phul`, `Thilgath-Pilneser`; EN: `Pul`, `Tilgath-pilneser` | Luther 1912 1. Chronik 5:26; KJV 1769. |
| `1chr_048` | DE & EN: Optionen balanciert auf 46–51 Zeichen | Beseitigung der Längenabweichung. |
| `1chr_050` | DE: `Josua, der Sohn des Vaters Nun`; Optionen balanciert auf 30–34 Zeichen | Beseitigung der Längenabweichung (`max_dev = 38%`). |
| `1chr_053` | DE & EN: Optionen balanciert auf 14–20 Zeichen (`Sein Sohn Merib-Baal` etc.) | Beseitigung der Längenabweichung (`max_dev = 43%`). |
| `1chr_067` | DE & EN: Optionen balanciert auf 29–34 Zeichen (`In der alten Stadt Hebron im Süden` etc.) | Beseitigung der extremen Längenabweichung (`max_dev = 60%`, zuvor 9 Zeichen!). |
| `1chr_074` | DE & EN: Optionen balanciert auf 20–24 Zeichen (`Die Ammoniterstadt Rabba` etc.) | Beseitigung der extremen Längenabweichung (`max_dev = 52%`, zuvor 4–8 Zeichen!). |
| `1chr_077` | DE & EN: Optionen balanciert auf 26–29 Zeichen (`Achtunddreißigtausend Leviten` etc.) | Beseitigung der Längenabweichung (`max_dev = 40%`). |
| `1chr_082` | DE & EN: Optionen balanciert auf 25–28 Zeichen (`Zweihundertachtundachtzig` etc.) | Beseitigung der Längenabweichung (`max_dev = 47%`). |
| `1chr_084` | DE: `Ahia, der Mann unter den Leviten`; Optionen balanciert auf 29–32 Zeichen | Beseitigung der extremen Längenabweichung (`max_dev = 80%`, zuvor 4 Zeichen!). |
| `1chr_085` | DE: `Ahithophel`, `Husai, der Arachiter`; EN: `Hushai the Archite` | Luther 1912 1. Chronik 27:33; KJV 1769. |
| `1chr_086` | Negation hervorgehoben: `Männer unter zwanzig Jahren NICHT auf` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1chr_087` | DE: `Erkenne den Gott deines Vaters und diene ihm mit ganzem Herzen und Seele` | Luther 1912 1. Chronik 28:9 Wortlaut; KJV 1769. |

## Zur menschlichen Entscheidung

1. **Vokabularharmonisierung gemäß Luther 1912 und KJV 1769:**
   - Namen konsequent nach Luther 1912 vereinheitlicht: `Nathan` (1 Chr 17:1; 28:19; 29:29, statt Natan), `Bath-Sua` (1 Chr 3:5), `Adonia` (1 Chr 3:2), `Ornan` (1 Chr 21), `Ahithophel` und `Husai, der Arachiter` (1 Chr 27:33), `Jaebez` (1 Chr 4:9), `Beer-Seba` (1 Chr 4:28), `Phul` und `Thilgath-Pilneser` (1 Chr 5:26), `Sebuel` (1 Chr 26:24).
   - In Englisch nach KJV 1769: `Nathan`, `Bath-shua`, `Adonijah`, `Ornan the Jebusite`, `Ahithophel` and `Hushai the Archite`, `Jabez`, `Beer-sheba`, `Pul` and `Tilgath-pilneser`, `Shebuel`.
   - Vokabeln der Luther 1912 übernommen: `Lot Gold` (1 Chr 21:25), `Zentner Gold` (1 Chr 20:2; 29:4).
   - Tilgung der theologischen/modernen Fremdwörter „Exil“ in `1chr_007` und „nachexilische“ in `1chr_041` zugunsten des biblischen Textes („nachdem Juda gen Babel weggeführt war“, 1 Chr 9:1).

2. **Antike Währungs- und Maßerklärungen (`1chr_020`, `1chr_023`, `1chr_032`):**
   - In 1. Chronik 20:2 wog die Krone des Königs von Rabba „einen Zentner Goldes“ (KJV: „a talent of gold“ = ca. 30–34 kg). Dies wurde in einer kurzen historischen Erklärung erläutert.
   - In 1. Chronik 21:25 zahlte David dem Jebusiter Ornan für die Tenne „Gold, am Gewicht sechshundert Lot“ (KJV: „six hundred shekels of gold by weight“ = ca. 6,8–7 kg Gold). Dies wurde kurz historisch eingeordnet.
   - In 1. Chronik 29:4 spendete David aus eigenem Gut „dreitausend Zentner Gold von Ophir und siebentausend Zentner lauteres Silber“ (KJV: „three thousand talents of gold... seven thousand talents of refined silver“ = ca. 100 Tonnen Gold). Dies wurde sachlich dokumentiert.
