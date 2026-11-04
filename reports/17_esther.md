# Review Report: 17_esther.json (Esther / Esther)

## Übersicht & Metriken
- **Geprüfte Fragen:** 30
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 24 (Angleichung an Luther 1912: Mardochai statt Mordechai durchgängig in `est_004`, `est_005`, `est_006`, `est_007`, `est_011`, `est_014`, `est_015`, `est_016`, `est_018`, `est_019`, `est_021`, `est_022`, `est_026`, `est_029`, `est_030`; Vasthi statt Waschti in `est_002`, `est_003`, `est_022`; Zentner Silber statt Talente in `est_008`, `est_018`, `est_021`; Zins statt Steuer in `est_028`; „der nächste nach dem König“ statt „der Zweite“ in `est_029`; „redete Frieden für sein ganzes Geschlecht“ in `est_030`; Großschreibung von NICHT in `est_025`; Balancierung extremer Längenunterschiede in `est_004`, `est_007`, `est_008`, `est_017`, `est_028`, `est_029`)
- **Geänderte Fragen (EN):** 30 (Vollständige KJV-1769-Neuübertragung mit authentischem KJV-Vokabular: Ahasuerus, Mordecai, Vashti, Shushan the palace, ten thousand talents of silver, gallows fifty cubits high, on the spoil laid they not their hand, tribute, balanced options)
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 1
  - `est_008`: Hamans Bestechungssumme (10.000 Zentner Silber / 10,000 talents of silver = ca. 340 Tonnen Silber)
- **Entfernte / bereinigte Erklärungen:** 29 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 30 Fragen vollständig in `en/17_esther.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten und balancierter Optionen

## Bemerkenswerte Vokabel- und Inhaltsänderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `est_001` | DE: `Hundertachtzig Tage lang, gefolgt von sieben Festtagen im Hofe des Gartens`; EN: `hundred and fourscore days... seven days` | Luther 1912 Esther 1:4-5 genauer Wortlaut; KJV 1769. |
| `est_002` | DE: `Königin Vasthi`; EN: `queen Vashti` | Luther 1912 Esther 1:11 Schreibweise (`Vasthi`); KJV 1769 (`Vashti`). |
| `est_003` | DE: `Vasthi solle abgetan werden`; EN: `Vashti come no more before the king` | Luther 1912 Esther 1:19 Wortlaut; KJV 1769. |
| `est_004` | DE: `Mardochai`, `Stamme Benjamin, ein Sohn Jairs, des Sohnes Simeis`; EN: `Mordecai`, `son of Jair, son of Shimei`; Optionen balanciert auf 58–62 Zeichen | Luther 1912 Esther 2:5 Namensformen. Beseitigung der extremen Längenabweichung (`max_dev = 33%`, zuvor 38 Zeichen). |
| `est_005` | DE: `ihr Volk und ihre Freundschaft vor dem Könige nicht anzeigen`; EN: `shewed her people nor her kindred` | Luther 1912 Esther 2:10 genauer Wortlaut; KJV 1769. |
| `est_006` | DE: `Mardochai`, `Bigthan und Teresch`; EN: `Mordecai`, `Bigthan and Teresh` | Luther 1912 Esther 2:21; KJV 1769. |
| `est_007` | DE: `Mardochai`, `Agagiter Haman`; EN: `Mordecai`, `Agagite` | Luther 1912 Esther 3:2-5 Schreibweisen. |
| `est_008` | DE: `Zehntausend Zentner Silber, darzuwägen in die Kammer des Königs`; EN: `Ten thousand talents of silver`; Erklärung beibehalten | Luther 1912 Esther 3:9 Gewichtsangabe (`Zentner`); KJV 1769 (`talents`). Historische Erklärung beibehalten. |
| `est_009` | DE: `dreizehnten Tag des zwölften Monats, das ist der Monat Adar`; EN: `thirteenth day of the twelfth month, which is the month Adar` | Luther 1912 Esther 3:7, 13 Wortlaut; KJV 1769. |
| `est_010` | DE: `es sei denn, der König streckte das goldene Zepter aus`; EN: `except such to whom the king shall hold out the golden sceptre` | Luther 1912 Esther 4:11; KJV 1769. |
| `est_011` | DE: `Wer weiß, ob du nicht um dieser Zeit willen zum Königtum gekommen bist?`; EN: `who knoweth whether thou art come to the kingdom for such a time` | Luther 1912 Esther 4:14 Wortlaut; KJV 1769. |
| `est_012` | DE: `Komme ich um, so komme ich um!`; EN: `and if I perish, I perish!` | Luther 1912 Esther 4:16 Wortlaut; KJV 1769. |
| `est_013` | DE: `neigte ihr das goldene Zepter in seiner Hand zu`; EN: `king held out to Esther the golden sceptre` | Luther 1912 Esther 5:2; KJV 1769. |
| `est_015` | DE: `Zeres`, `Baum fünfzig Ellen hoch`; EN: `Zeresh`, `gallows of fifty cubits high` | Luther 1912 Esther 5:14; KJV 1769. |
| `est_016` | DE: `Dem König floh der Schlaf; er ließ die Chronik der Denkwürdigkeiten vorlesen`; EN: `could not the king sleep, and commanded to bring chronicles` | Luther 1912 Esther 6:1; KJV 1769. |
| `est_017` | DE: `Wem sollte der König lieber wollen Ehre tun denn mir?`; EN: `To whom would the king delight to do honour more than to myself?` | Luther 1912 Esther 6:6 Wortlaut; KJV 1769. |
| `est_018` | DE: `Mardochai im königlichen Kleide auf dem Rosse durch die Stadt führen`; EN: `brought Mordecai through the street` | Luther 1912 Esther 6:11; KJV 1769. |
| `est_019` | DE: `verkauft seien, vertilgt, erwürgt und umgebracht zu werden`; EN: `sold, I and my people, to be destroyed, to be slain, and to perish` | Luther 1912 Esther 7:4 Wortlaut; KJV 1769. |
| `est_020` | DE: `Der Widersacher und Feind ist dieser böse Haman!`; EN: `The adversary and enemy is this wicked Haman!` | Luther 1912 Esther 7:6 Wortlaut; KJV 1769. |
| `est_021` | DE: `Hängt ihn daran! Und sie hängten Haman an den Baum`; EN: `Hang him thereon! So they hanged Haman` | Luther 1912 Esther 7:9-10; KJV 1769. |
| `est_022` | DE: `Siegelring, den er Haman abgenommen hatte, und Hamans Haus`, `Vasthi`; EN: `ring, which he had taken from Haman`, `Vashti` | Luther 1912 Esther 8:1-2; KJV 1769. |
| `est_023` | DE: `Sich zu versammeln, für ihr Leben zu stehen und ihre Feinde zu vertilgen`; EN: `gather themselves together, to stand for life, to destroy` | Luther 1912 Esther 8:11 Wortlaut; KJV 1769. |
| `est_024` | DE: `Viele aus den Völkern wurden Juden; denn die Furcht überfiel sie`; EN: `Many of the people of the land became Jews; for the fear fell` | Luther 1912 Esther 8:17. |
| `est_025` | Negation hervorgehoben: `Was taten die Juden bemerkenswerterweise NICHT`; Option: `Sie legten ihre Hände nicht an die Beute` | Luther 1912 Esther 9:10, 15-16 Wortlaut. Richtlinienkonforme Großschreibung. |
| `est_026` | DE: `vierzehnten und fünfzehnten Tag des Monats Adar alle Jahre`; EN: `fourteenth day of month Adar, and fifteenth day of same` | Luther 1912 Esther 9:21; KJV 1769. |
| `est_027` | DE: `Nach dem Namen 'Pur', weil Haman das Los geworfen hatte`; EN: `After the name of Pur, because Haman had cast lot` | Luther 1912 Esther 9:26. |
| `est_028` | DE: Verdächtiges Fremdwort `Steuer` ersetzt durch `Zins auf das Land und die Inseln im Meere`; EN: `laid a tribute upon the land, and upon the isles` | Luther 1912 Esther 10:1 („legte Zins aufs Land“); Tilgung der Prüf-Warnung `WORD:Steuer`. |
| `est_029` | DE: `der nächste nach dem König Ahasveros und groß unter den Juden`; EN: `next unto king Ahasuerus, and great among the Jews` | Luther 1912 Esther 10:3 Wortlaut; KJV 1769. |
| `est_030` | DE: `suchte das Beste für sein Volk und redete Frieden für sein ganzes Geschlecht`; EN: `seeking the wealth of his people, and speaking peace to all his seed` | Luther 1912 Esther 10:3 Wortlaut; KJV 1769. |

## Zur menschlichen Entscheidung

1. **Vokabularharmonisierung gemäß Luther 1912 und KJV 1769:**
   - Namen konsequent nach Luther 1912 vereinheitlicht: `Mardochai` (Esther 2:5 u. ö., statt Mordechai), `Vasthi` (Esther 1:11, statt Waschti), `Ahasveros` (Esther 1:1), `Zeres` (Esther 5:14, statt Seresch).
   - In Englisch nach KJV 1769: `Mordecai`, `Vashti`, `Ahasuerus`, `Zeresh`.
   - Vokabeln der Luther 1912 übernommen: `Zentner Silber` (Esther 3:9), `Zins` (Esther 10:1, statt modernem `Steuer`), `der nächste nach dem König` (Esther 10:3), `an die Beute legten sie ihre Hände nicht` (Esther 9:10).
   - Tilgung von Fremdwörtern: `Steuer` in `est_028` durch `Zins` ersetzt.

2. **Antike Währungs- und Gewichtserklärung (`est_008`):**
   - In Esther 3:9 erbot sich Haman, für die Vernichtung der Juden „zehntausend Zentner Silber“ (KJV: „ten thousand talents of silver“ = ca. 340 Tonnen Silber) in die königlichen Schatzkammern darzuwägen. Diese immense Bestechungssumme wurde historisch dokumentiert und beibehalten.
