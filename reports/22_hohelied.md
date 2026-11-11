# Review Report: 22_hohelied.json

## Uebersicht
- Gepruefte Datei: `22_hohelied.json`
- Englische Datei: `en/22_hohelied.json`
- Anzahl Fragen: 26
- Ueberpruefte Erklaerungen (DE): 0
- Ueberpruefte Erklaerungen (EN): 0
- Bereinigte Erklaerungen: 26 (auf Minimalismus zurueckgesetzt, alle Template-Texte bereinigt)

## Sprachliche Anpassungen (Luther 1912)
- Exakter Luther-1912-Wortlaut aus der Versdatenbank uebernommen:
  - Hohelied 2:2: `Wie eine Rose unter den Dornen` ('Rose' nach Luther 1912 statt Schlachter/KJV 'Lilie').
  - Hohelied 3:7: `sechzig Starke aus den Starken in Israel` ('Starke' nach Luther 1912).
  - Hohelied 5:6: `war er weg und gegangen` ('weg und gegangen' nach Luther 1912 statt Schlachter 'entwichen').
  - Hohelied 6:13: Namensform `Sulamith` beibehalten (KJV `Shulamite`).
  - Hohelied 7:12: `früh aufstehen zu den Weinbergen`.
  - Hohelied 8:14: `auf den Würzbergen` ('Würzbergen' nach Luther 1912 statt Schlachter 'Balsamberge').
  - Hohelied 8:7: `so gälte es alles nichts` ('gälte alles nichts' nach Luther 1912 statt Schlachter 'wird er nur verachtet').
  - Hohelied 6:4: Namensform `Thirza` gemaess Luther 1912.
  - Hohelied 1:7: `wo du ruhest im Mittage` ('ruht am Mittag' nach Luther 1912 statt Schlachter 'lagert').
  - Hohelied 2:10: `Stehe auf, meine Freundin` ('Stehe auf' nach Luther 1912 statt Schlachter 'Mache dich auf').
  - Hohelied 3:9-10: `eine Sänfte machen ... die Decke golden` ('Sänfte' und 'Decke' nach Luther 1912).
  - Hohelied 5:10: `Mein Freund ist weiß und rot, auserkoren unter vielen Tausenden` ('auserkoren' nach Luther 1912 statt Elberfelder/Schlachter 'ein Panier').
  - Hohelied 6:3: `Mein Freund ist mein, und ich bin sein` ('Freund' nach Luther 1912).
- Negationshervorhebung: `NICHT` in hld_013 grossgeschrieben.
- Referenzbereinigung:
  - hld_025: Komma-Referenz `Hohelied 5:10, 16` auf den tatsaechlich abgefragten Vers `Hohelied 5:10` (KJV `Song of Solomon 5:10`) praezisiert.

## Aenderungen an Fragen und Optionen

| Frage-ID | Was geaendert wurde | Warum |
|---|---|---|
| hld_003 | 'Rose unter den Dornen' eingesetzt und Distraktoren balanciert | Luther 1912 verwendet 'Rose' (Schlachter 'Lilie'); KJV verwendet 'lily' |
| hld_006 | Option 3 auf 'umgeben von sechzig Starken' praezisiert; Distraktoren balanciert | Exakter Bibelwortlaut Hohelied 3:7 ('sechzig Starke') |
| hld_008 | Option 1 auf 'Er war weg und gegangen' angepasst | Exakter Luther-1912-Wortlaut (Schlachter: 'entwichen') |
| hld_010 | Optionen auf einheitliche Laenge balanciert | Beseitigung von LEN_DEV=54% |
| hld_013 | Negation 'NICHT' grossgeschrieben; Optionen balanciert | Richtlinienkonforme Negationshervorhebung und Balance |
| hld_015 | Option 0 auf 'Früh aufzustehen zu den Weinbergen' angepasst | Exakter Luther-1912-Wortlaut Hohelied 7:12 |
| hld_017 | Option 2 auf 'auf den Würzbergen' angepasst | Luther 1912 verwendet 'Würzbergen' (Schlachter 'Balsamberge') |
| hld_018 | Option 3 auf 'Es gälte alles nichts' angepasst; Distraktoren balanciert | Exakter Textbefund Hohelied 8:7 |
| hld_020 | Namensschreibweise 'Thirza' gemaess Luther 1912; Optionen balanciert | Exakte Luther-1912-Orthographie und Laengenangleichung |
| hld_021 | Option 0 auf 'wo er weidet und wo er ruht am Mittag' angepasst | Luther 1912 'ruhest' statt Schlachter 'lagert' |
| hld_022 | Option 1 auf 'Stehe auf, meine Freundin' angepasst | Luther 1912 'Stehe auf' statt Schlachter 'Mache dich auf' |
| hld_023 | Frage und Optionen auf 'Sänfte' und 'goldene Decke' angepasst | Exakter Luther-1912-Wortlaut Hohelied 3:9-10 |
| hld_025 | Bibelreferenz auf 'Hohelied 5:10' praezisiert; 'auserkoren' eingesetzt | Komma-Referenz unzulaessig; Beseitigung von 'ein Panier' |
| hld_026 | Option 1 auf 'Mein Freund ist mein, und ich bin sein' angepasst | Exakter Luther-1912-Wortlaut Hohelied 6:3 |

## Englische Version (KJV 1769)
- Vollstaendige englische Uebersetzung aller 26 Fragen in `en/22_hohelied.json`.
- KJV-Buchname `Song of Solomon` konsequent in allen Referenzen und Metadaten verwendet.
- Verwendung des authentischen KJV-Wortlauts (z.B. `better than wine`, `tents of Kedar`, `lily among thorns`, `little foxes, that spoil the vines`, `pillars of smoke`, `chariot of the wood of Lebanon`, `garden inclosed`, `withdrawn himself, and was gone`, `took away my veil`, `Shulamite`, `terrible as an army with banners`, `love is strong as death`, `many waters cannot quench love`, `palm tree`, `spices`, `chiefest among ten thousand`, `he feedeth among the lilies`).
- Alle `correctAnswers`-Indizes stimmen 1:1 mit der deutschen Fassung ueberein.
- Verszaehlung: Identische Kapitel- und Verszaehlung in allen 8 Kapiteln.

## Zur menschlichen Entscheidung
- In hld_003 uebersetzt Luther 1912 die hebraeische Wendung mit 'Rose unter den Dornen', waehrend die KJV 'lily among thorns' hat. In beiden Sprachfassungen wurde jeweils exakt der Wortlaut der jeweiligen Zieluebersetzung gewahrt.
- In hld_025 wurde die uneinheitliche Bibelstellenangabe `Hohelied 5:10, 16` auf den tatsaechlich abgefragten Vers `Hohelied 5:10` (KJV `Song of Solomon 5:10`) verengt.
