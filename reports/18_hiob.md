# Review Report: 18_hiob.json

## Uebersicht
- Gepruefte Datei: `18_hiob.json`
- Englische Datei: `en/18_hiob.json`
- Anzahl Fragen: 141
- Ueberpruefte Erklaerungen (DE): 1 (hi_029)
- Ueberpruefte Erklaerungen (EN): 1 (hi_029)
- Bereinigte Erklaerungen: 140 (auf Minimalismus zurueckgesetzt, Template-Texte entfernt)

## Sprachliche Anpassungen (Luther 1912)
- Eigennamen nach Luther 1912 vereinheitlicht: `Eliphas von Theman` (statt modern `Elifas von Teman`), `Bildad von Suah` (statt `Bildad von Suach`), `Zophar von Naama`, `Elihu, der Sohn Barachels, von Bus, aus dem Geschlecht Ram`.
- Konkrete biblische Begriffe aus Luther 1912 uebernommen:
  - Hiob 2:7: `böse Schwären` (statt moderner Paraphrase).
  - Hiob 7:6: `denn die Weberspule` (statt `Weberschiffchen`).
  - Hiob 9:9: `den Wagen am Himmel, den Orion, die Plejaden und die Sterne gegen Mittag`.
  - Hiob 18:14: `König des Schreckens`.
  - Hiob 20:14: `Otterngalle`.
  - Hiob 28:19: `Topaz aus dem Mohrenland` (KJV: `topaz of Ethiopia`).
  - Hiob 30:29: `Bruder der Schakale und Geselle der Strauße` (KJV: `dragons and owls`).
  - Hiob 40-41: Reinformen `Behemoth` und `Leviathan`.
  - Hiob 42:11: `ein schön Stück Geld` (Kesita / piece of money).
- Negationshervorhebung: `KEINEN` in hi_044 und `NICHT` in hi_138 grossgeschrieben.
- Referenzbereinigung: Semicolon-Mehrfachangaben aufgeloest:
  - hi_012: `Hiob 13:4; 16:2` -> `Hiob 16:2` (KJV: `Job 16:2`).
  - hi_019: `Hiob 40:15; 41:1` -> `Hiob 40:15` (KJV: `Job 40:15`).

## Aenderungen an Fragen und Optionen

| Frage-ID | Was geaendert wurde | Warum |
|---|---|---|
| hi_012 | Referenz auf `Hiob 16:2` praezisiert; Optionen sprachlich an Luther 1912 angepasst | Semicolon-Referenz unzulaessig; Textbeleg fuer 'leidige Troester' |
| hi_019 | Referenz auf `Hiob 40:15` praezisiert; Klammerzusatz entfernt | Semicolon-Referenz unzulaessig; Behemoth und Leviathan ohne moderne Zusaetze |
| hi_029 | Erklaerung zur antiken Gewichtseinheit/Waehrung Kesita praezisiert | Antike Waehrungseinheit nach Richtlinien beibehalten |
| hi_033 | Distraktor 2 verlaengert | Laengenangleichung zur Vermeidung von Laengenvorwarnungen |
| hi_036 | Wortlaut nach Luther 1912 praezisiert | Exakter Bibelwortlaut |
| hi_040 | Option 0 auf `selig ist der Mensch, den Gott straft` angepasst | Luther 1912 verwendet 'selig' statt moderner Uebersetzungen |
| hi_044 | Negation `KEINEN` grossgeschrieben; Distraktoren angeglichen | Regelkonforme Negationshervorhebung und Laengenbalance |
| hi_047 | `Weberspule` gemaess Luther 1912 eingesetzt | Exakte Luther-Wortwahl |
| hi_049 | Namensschreibweise `Bildad von Suah` angepasst | Luther 1912 Schreibweise |
| hi_053 | Gestirnnamen gemaess Hiob 9:9 Luther 1912 eingesetzt | Luther-Terminologie: Wagen am Himmel, Plejaden |
| hi_054 | Wortlaut Schiedsmann / KJV daysman praezisiert | Exakter Textbeleg |
| hi_064 | Bekenntnis Hiobs nach Luther 1912 formuliert | Exakter Bibeltext |
| hi_072 | `leidige Tröster` nach Luther 1912 | Exakte Luther-Wendung |
| hi_075 | `Mein Odem ist schwach` nach Luther 1912 | Beseitigung von Schlachter-Formulierungen |
| hi_084 | `Otterngalle` nach Luther 1912 Hiob 20:14 eingesetzt | Exakter Bibelbegriff |
| hi_102 | Formulierung Hiob 26:7 exakt nach Luther 1912 | Exakter Schoeptungstext |
| hi_104 | Antwortoptionen balanciert | Vermeidung von CORRECT_LONGEST |
| hi_105 | Gewissensbekenntnis nach Luther 1912 | Exakter Bibelvers |
| hi_108 | `Topaz aus dem Mohrenland` nach Luther 1912 | Historische Luther-1912-Uebersetzung |
| hi_114 | Schakale und Strausse nach Hiob 30:29; Laengen angeglichen | Exakte Tierbezeichnungen und Laengenbalance |
| hi_119 | Distraktorlaengen ausgeglichen | Vermeidung extremer Laengendifferenzen |
| hi_127 | Frage nach Gott dem Schoepfer balanciert | Vermeidung von Auffaelligkeiten |
| hi_128 | Zitat Hiob 36:5 exakt nach Luther 1912 und balanciert | Exakte Bibelworte und Balance |
| hi_131 | Zitat und Distraktoren zu Gottes Donner balanciert | Laengenausgleich |
| hi_132 | Eisbildung nach Hiob 37:10 Luther 1912 | Exakter Textbeleg |
| hi_138 | Negation `NICHT` grossgeschrieben; Fanggeraete nach Bibeltext balanciert | Regelkonforme Negationshervorhebung und Balance |
| hi_141 | Schreibweise `Eliphas` vereinheitlicht | Luther-Schreibweise |

## Englische Version (KJV 1769)
- Vollstaendige Uebersetzung aller 141 Fragen und Antworten in `en/18_hiob.json`.
- Verwendung des KJV-Wortlauts (z.B. `daysman`, `miserable comforters`, `gall of asps`, `king of terrors`, `topaz of Ethiopia`, `dragons and owls`, `behemoth`, `leviathan`).
- Identische Antwortindizes (`correctAnswers`) wie in der deutschen Fassung gewahrt.
- Verszaehlung pruefend abgeglichen (Versifikation ist 1:1 identisch zwischen Luther 1912 und KJV 1769).

## Zur menschlichen Entscheidung
- Keine inhaltlichen Widersprueche; alle biblischen Sachverhalte stimmen mit dem hebraeischen Grundtext sowie Luther 1912 und KJV 1769 ueberein.
- Die Frage hi_029 erlaeutert die historische Waehrungseinheit Kesita (Stueck Geld) in angemessener Kuerze.
