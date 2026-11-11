# Review Report: 15_esra.json (Esra / Ezra)

## Übersicht & Metriken
- **Geprüfte Fragen:** 30
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 22 (Angleichung an Luther 1912: Kores statt Kyrus in `esr_001`, `esr_002`, `esr_003`, `esr_008`, `esr_012`, `esr_016`, `esr_019`; Arthahsastha statt Artaxerxes in `esr_001`, `esr_011`, `esr_019`, `esr_021`, `esr_023`, `esr_028`; Jesua statt Jeschua in `esr_004`, `esr_007`, `esr_010`; Serubabel statt Serubbabel in `esr_004`, `esr_007`, `esr_010`, `esr_015`, `esr_018`; Schoß, Zoll und Zinse sowie Renten des Königs statt Steuern in `esr_011`, `esr_017`; Gefangenschaft statt Exil in `esr_004`; Thathnai statt Tattenai in `esr_014`, `esr_015`, `esr_017`; Großschreibung von NICHT in `esr_015`; Balancierung der Optionen in `esr_001`, `esr_005`, `esr_006`, `esr_009`, `esr_013`, `esr_018`, `esr_022`)
- **Geänderte Fragen (EN):** 30 (Vollständige KJV-1769-Neuübertragung mit authentischem KJV-Vokabular: Cyrus, Artaxerxes, Jeshua, Zerubbabel, toll, tribute, and custom, province beyond the river, captivity, balanced options)
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 0
- **Entfernte / bereinigte Erklärungen:** 30 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 30 Fragen vollständig in `en/15_esra.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten und balancierter Optionen

## Bemerkenswerte Vokabel- und Inhaltsänderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `esr_001` | DE: `König Kores in Persien`, `Arthahsastha`; EN: `King Cyrus of Persia`, `Artaxerxes`; Optionen balanciert auf 51–56 Zeichen | Luther 1912 Esra 1:1 Schreibweise (`Kores`); KJV 1769 (`Cyrus`). Beseitigung der extremen Längenabweichung (`max_dev = 48%`). |
| `esr_002` | DE: `König Kores`, `Gefäße des Hauses des HERRN`; EN: `Cyrus the king`, `vessels of the house of the LORD` | Luther 1912 Esra 1:7-8 Wortlaut; KJV 1769. |
| `esr_003` | DE: `Kores` statt `Kyrus` im Distraktor; EN: `Cyrus` | Luther 1912 Namensform. |
| `esr_004` | DE: `Gefangenschaft` statt Fremdwort `Exil`, `Serubabel`, `Jesua`; EN: `captivity`, `Zerubbabel`, `Jeshua` | Luther 1912 Esra 2:1-2 („aus der Gefangenschaft“); Tilgung der Prüf-Warnung `WORD:Exil` und `WORD:Jeschua`. |
| `esr_005` | DE & EN: Optionen balanciert auf 43–52 Zeichen | Harmonische Längenverteilung der Zahlenangaben. |
| `esr_006` | DE: `Geschlechtsregister fehlte und sie unrein geachtet wurden`; EN: `genealogy was not found` | Luther 1912 Esra 2:62 genauer Wortlaut; KJV 1769. |
| `esr_007` | DE: `Jesua und Serubabel`; EN: `Jeshua and Zerubbabel` | Luther 1912 Esra 3:2; Tilgung der Prüf-Warnung `WORD:Jeschua`. |
| `esr_008` | DE: `Kores` im Distraktor; EN: `Cyrus` | Luther 1912 Namensform. |
| `esr_009` | DE: `Alte, die das erste Haus gesehen hatten, laut weinten`; EN: `ancient men, that had seen the first house, wept aloud` | Luther 1912 Esra 3:12; KJV 1769. |
| `esr_010` | DE: `Serubabel`; EN: `Zerubbabel` | Luther 1912 Esra 4:3 Schreibweise. |
| `esr_011` | DE: Verdächtiges Fremdwort `Steuern` ersetzt durch biblisches `Schoß, Zoll und Zinse`; EN: `toll, tribute, and custom` | Luther 1912 Esra 4:13 Wortlaut („Schoß, Zoll und jährliche Zinse nicht geben“); Tilgung der Prüf-Warnung `WORD:Steuern`. |
| `esr_012` | DE: `Kores` im Distraktor, `Darius`; EN: `Cyrus`, `Darius` | Luther 1912 Esra 4:24. |
| `esr_013` | DE: `Haggai der Prophet und Sacharja, der Sohn Iddos`; EN: `Haggai the prophet, and Zechariah the son of Iddo` | Luther 1912 Esra 5:1; KJV 1769. |
| `esr_014` | DE: `Thathnai, der Landpfleger jenseits des Wassers, und Sethar-Bosnai`; EN: `Tatnai, governor on this side the river, and Shethar-boznai` | Luther 1912 Esra 5:3 Schreibweise; KJV 1769. |
| `esr_015` | Negation hervorgehoben: `Tempelbau NICHT sofort gewaltsam einstellen` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `esr_016` | DE: `Kores`, `Schlosse zu Achmetha`; EN: `Cyrus`, `palace at Achmetha` | Luther 1912 Esra 6:2; KJV 1769. |
| `esr_017` | DE: Verdächtiges Fremdwort `Steuern` ersetzt durch biblisches `Kosten von den Renten des Königs`; EN: `king's goods, even of the tribute beyond the river` | Luther 1912 Esra 6:8 („von den Renten jenseits des Wassers“); Tilgung der Prüf-Warnung `WORD:Steuern`. |
| `esr_018` | DE & EN: Optionen balanciert auf 60–75 Zeichen | Beseitigung von Längenunterschieden; Text treu an Esra 6:15-16. |
| `esr_019` | DE: `Kores`, `Arthahsastha`; EN: `Cyrus`, `Artaxerxes` | Luther 1912 Esra 7:1; KJV 1769. |
| `esr_020` | DE: `das Gesetz des HERRN zu suchen, zu tun und zu lehren`; EN: `to seek the law of the LORD, and to do it, and to teach` | Luther 1912 Esra 7:10 Wortlaut; KJV 1769. |
| `esr_021` | DE: `Arthahsastha`; EN: `Artaxerxes` | Luther 1912 Esra 7:25-26. |
| `esr_022` | DE: `Kinder Levi`; EN: `sons of Levi` | Luther 1912 Esra 8:15 Wortlaut. |
| `esr_023` | DE: `Arthahsastha`; EN: `Artaxerxes` | Luther 1912 Namensform. |
| `esr_024` | DE & EN: Optionen balanciert auf 64–73 Zeichen | Beseitigung von Längenunterschieden. |
| `esr_025` | DE: `nicht abgesondert von den Heiden`; EN: `not separated themselves from the people of the lands` | Luther 1912 Esra 9:1. |
| `esr_026` | DE: `zerriss sein Kleid und Mantel, raufte Haupthaar und saß erstarrt da`; EN: `rent garment and mantle, plucked off hair, sat astonied` | Luther 1912 Esra 9:3. |
| `esr_027` | DE: `Missetaten über ihr Haupt gewachsen sind bis an den Himmel`; EN: `iniquities are increased over our head unto the heavens` | Luther 1912 Esra 9:6. |
| `esr_028` | DE: `Arthahsastha`, `fremden Weiber hinauszutun`; EN: `strange wives` | Luther 1912 Esra 10:2-3. |
| `esr_029` | DE: `saßen auf der Straße vor dem Hause Gottes, zitternd im Regen`; EN: `sat in the street of the house of God, trembling for great rain` | Luther 1912 Esra 10:9. |
| `esr_030` | DE: `die Sache zu erforschen, bis zum ersten Monat`; EN: `examine the matter, and made an end by the first month` | Luther 1912 Esra 10:14-17. |

## Zur menschlichen Entscheidung

1. **Vokabularharmonisierung gemäß Luther 1912 und KJV 1769:**
   - Namen konsequent nach Luther 1912 vereinheitlicht: `Kores` (Esra 1:1, statt Kyrus), `Arthahsastha` (Esra 4:7; 7:1, statt Artaxerxes), `Jesua` (Esra 2:2; 3:2, statt Jeschua), `Serubabel` (Esra 2:2, statt Serubbabel), `Thathnai` (Esra 5:3, statt Tattenai), `Achmetha` (Esra 6:2).
   - In Englisch nach KJV 1769: `Cyrus`, `Artaxerxes`, `Jeshua`, `Zerubbabel`, `Tatnai`, `Achmetha`.
   - Tilgung von Fremdwörtern und modernen Begriffen: `Exil` in `esr_004` (durch biblisches `aus der Gefangenschaft` ersetzt, Esra 2:1), modernes `Steuern` in `esr_011` und `esr_017` (durch `Schoß, Zoll und jährliche Zinse` und `Renten des Königs jenseits des Wassers`, Esra 4:13; 6:8 ersetzt).
   - Großschreibung verneinter Fragestellung (`NICHT` in `esr_015`).

2. **Erklärungen:**
   - Da im Buch Esra keine isolierten antiken Einheitenumrechnungen abgefragt werden, wurden alle Standard- und Optionserklärungen richtlinienkonform auf `""` gesetzt (`explanationReviewed: false`).
