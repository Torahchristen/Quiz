# Review Report: 27_daniel.json

## Uebersicht
- Gepruefte Datei: `27_daniel.json`
- Englische Datei: `en/27_daniel.json`
- Anzahl Fragen: 37
- Ueberpruefte Erklaerungen (DE): 0
- Ueberpruefte Erklaerungen (EN): 0
- Bereinigte Erklaerungen: 37 (auf Minimalismus zurueckgesetzt, alle redundanten Template-Texte bereinigt)

## Sprachliche Anpassungen (Luther 1912)
- Exakter Luther-1912-Wortlaut aus der Versdatenbank uebernommen:
  - Daniel 1:15: `schöner und besser bei Leibe denn alle Knaben` (dan_013).
  - Daniel 4:34: `hob ich, Nebukadnezar, meine Augen auf gen Himmel und kam wieder zur Vernunft und lobte den Höchsten` (dan_018; vorher nach hebraeischer Verszaehlung als 4:31 angegeben).
  - Daniel 6:26-27: `er ist der lebendige Gott, der ewiglich bleibt` (dan_022).
  - Daniel 7:6: `gleich einem Parder` gemaess Luther 1912 (dan_040; vorher moderner Begriff 'Panther').
  - Daniel 9:2: Namensschreibung `Chebar` (dan_027; vorher 'Kebar').
  - Daniel 10:5-6: `Mann in Leinwand... goldener Gürtel... Leib wie ein Türkis` (dan_029).
  - Daniel 11:2: `drei Könige in Persien; der vierte aber wird größeren Reichtum sammeln` (dan_031).
- Korrektur von Verszaehlungsdifferenzen:
  - Daniel 4:31 -> `Daniel 4:34` (dan_018; in Luther 1912 und KJV 1769 steht Nebukadnezars Wiederherstellung in Vers 34, waehrend hebraeische/moderne Zaehlungen hier Vers 31 fuehren).
  - Daniel 6:11-17 -> `Daniel 6:10-16` im Fragetext (dan_007; an die praezise Referenz Daniel 6:10-16 angeglichen).

## Aenderungen an Fragen und Optionen

| Frage-ID | Was geaendert wurde | Warum |
|---|---|---|
| dan_007 | Fragetext auf '(Daniel 6:10-16)' angeglichen | Konsistenz mit bibleReference |
| dan_013 | Optionen balanciert | Beseitigung von LEN_DEV=31% |
| dan_018 | Fragetext und Bibelstelle von 4:31 auf 4:34 korrigiert | Verszaehlung nach Luther 1912 und KJV 1769 |
| dan_022 | Distraktoren balanciert | Beseitigung von LEN_DEV=33% |
| dan_027 | Distraktor auf 'Wasser Chebar' korrigiert; Optionen balanciert | Exakte Luther-1912-Orthographie und Beseitigung von LEN_DEV=36% |
| dan_028 | Optionen balanciert | Beseitigung von LEN_DEV=36% |
| dan_029 | Distraktoren balanciert | Beseitigung von LEN_DEV=33% |
| dan_031 | Distraktoren balanciert | Beseitigung von LEN_DEV=34% |
| dan_040 | Option 3 auf 'Der Parder mit vier Flügeln' angepasst | Exakter Luther-1912-Wortlaut (Parder statt Panther) |

## Englische Version (KJV 1769)
- Vollstaendige englische Uebersetzung aller 37 Fragen in `en/27_daniel.json`.
- KJV-Buchname `Daniel` konsequent in allen Referenzen und Metadaten verwendet.
- Verwendung des authentischen KJV-Wortlauts (z.B. `defile himself with the portion of the king's meat`, `image's head was of fine gold, breast and arms of silver`, `stone that smote the image became a great mountain`, `like the Son of God`, `drive thee from men, and thy dwelling shall be with the beasts`, `MENE, MENE, TEKEL, UPHARSIN`, `cast into the den of lions`, `dreadful and terrible, and strong exceedingly`, `Son of man came with the clouds of heaven`, `man Gabriel`, `Michael, one of the chief princes`, `fairer and fatter in flesh`, `Blessed be the name of God for ever and ever`, `tree in the midst of the earth`, `mine understanding returned unto me, and I blessed the most High`, `drank wine in the golden vessels`, `numbered thy kingdom, and finished it`, `living God of Daniel`, `ram having two horns and rough goat`, `little horn waxed exceeding great`, `Unto two thousand and three hundred days`, `accomplish seventy years in the desolations of Jerusalem`, `Seventy weeks are determined`, `clothed in linen, whose loins were girded with fine gold of Uphaz`, `three kings in Persia; and the fourth shall be far richer`, `king of the south and king of the north`, `abomination that maketh desolate`, `Michael stand up, the great prince`, `they that be wise shall shine as the brightness of the firmament`, `go thy way till the end be: for thou shalt rest, and stand in thy lot`, `windows being open in his chamber toward Jerusalem`).
- Alle `correctAnswers`-Indizes stimmen 1:1 mit der deutschen Fassung ueberein (einschliesslich ordering-Fragen dan_039 und dan_040 sowie multiple_choice dan_037).
- Verszaehlung: KJV und Luther 1912 stimmen in allen 12 Kapiteln des Buches Daniel exakt ueberein.

## Zur menschlichen Entscheidung
- In dan_018 war im Ausgangstext Daniel 4:31 genannt, was der hebraeischen Zaehlung entspricht (wo Kapitel 4 mit Vers 4 beginnt und 3:31-33 vorgelagert ist). Sowohl in Luther 1912 als auch in KJV 1769 steht der Bericht von Nebukadnezars Wiederherstellung in Vers 34. Die Stelle wurde entsprechend auf Daniel 4:34 vereinheitlicht.
- In dan_040 wurde das dritte Tier in der Luther-Fassung getreu als 'Parder' (KJV 'leopard') wiedergegeben.
