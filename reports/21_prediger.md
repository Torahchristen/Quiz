# Review Report: 21_prediger.json

## Uebersicht
- Gepruefte Datei: `21_prediger.json`
- Englische Datei: `en/21_prediger.json`
- Anzahl Fragen: 40
- Ueberpruefte Erklaerungen (DE): 0
- Ueberpruefte Erklaerungen (EN): 0
- Bereinigte Erklaerungen: 40 (auf Minimalismus zurueckgesetzt, alle Template-Texte bereinigt)

## Sprachliche Anpassungen (Luther 1912)
- Exakte Uebernahme des Luther-1912-Wortlauts aus der Versdatenbank:
  - Prediger 1:2: `Es ist alles ganz eitel, sprach der Prediger, es ist alles ganz eitel`.
  - Prediger 2:14: `daß es einem geht wie dem andern`.
  - Prediger 3:11: `und läßt ihr Herz sich ängsten, wie es gehen solle in der Welt` (Beseitigung moderner/Schlachter Formulierungen wie 'Ewigkeit ins Herz gelegt', die im hebraeischen Masoretischen Text als olam und von Luther als 'Welt' bzw. KJV 'world' uebersetzt wurden).
  - Prediger 5:4: `so verziehe nicht, es zu halten` ('Nicht zu verziehen, es zu halten').
  - Prediger 7:1: `Ein guter Ruf ist besser denn gute Salbe` (Referenz von 7:2 auf 7:1 korrigiert).
  - Prediger 9:15: `und kein Mensch gedachte desselben armen Mannes`.
  - Prediger 10:1: `Schädliche Fliegen verderben gute Salben` ('Schädliche Fliegen' nach Luther 1912 statt Schlachter 'Tote Fliegen').
  - Prediger 11:1: `Laß dein Brot über das Wasser fahren`.
  - Prediger 12:1: `Gedenke an deinen Schöpfer in deiner Jugend`.
  - Prediger 12:7: `der Staub muß wieder zu der Erde kommen ... und der Geist wieder zu Gott`.
  - Prediger 12:12: `viel Büchermachens ist kein Ende`.
  - Prediger 2:24: `daß er esse und trinke und seine Seele guter Dinge sei in seiner Arbeit`.
  - Prediger 6:3: `eine unzeitige Geburt ist besser denn er` ('unzeitige Geburt' nach Luther 1912).
  - Prediger 6:9: `das gegenwärtige Gut gebrauchen, denn nach anderm gedenken`.
  - Prediger 8:4: `In des Königs Wort ist Gewalt; und wer mag zu ihm sagen: Was machst du?`.
  - Prediger 8:11: `Weil nicht alsbald geschieht ein Urteil über die bösen Werke`.
  - Prediger 10:16: `Weh dir, Land, dessen König ein Kind ist, und dessen Fürsten in der Frühe speisen`.
  - Prediger 11:6: `Frühe säe deinen Samen und laß deine Hand des Abends nicht ab`.
- Negationshervorhebung: `NICHT` in pred_032 grossgeschrieben.

## Aenderungen an Fragen und Optionen

| Frage-ID | Was geaendert wurde | Warum |
|---|---|---|
| pred_001 | Optionen auf einheitliche Laenge balanciert | Vermeidung von LEN_DEV=38% |
| pred_004 | Richtige Option und Distraktoren sprachlich praezisiert | Beseitigung nicht-biblischer Wendungen und Laengenangleichung |
| pred_006 | Frage und Optionen an Luther 1912 Prediger 3:11 angepasst ('lässt ihr Herz sich ängsten, wie es gehen solle in der Welt') | Beseitigung modern-theologischer Schlachter-Paraphrasen ('Ewigkeit') |
| pred_008 | Option 0 auf 'Nicht zu verziehen, es zu halten' praezisiert | Exakter Luther-1912-Wortlaut Prediger 5:4 |
| pred_010 | Bibelreferenz von Prediger 7:2 auf Prediger 7:1 korrigiert | Vers 1 enthaelt den Vergleich 'guter Ruf / gute Salbe' |
| pred_013 | Option 1 auf 'kein Mensch gedachte seiner' angepasst | Exakter Textbefund Prediger 9:15 |
| pred_014 | 'Schädliche Fliegen' nach Luther 1912 eingesetzt | Luther-Wortlaut (Schlachter: 'Tote Fliegen') |
| pred_015 | Distraktoren balanciert | Ausgewogene Laengenverteilung |
| pred_016 | Option 0 und Distraktoren balanciert | Vermeidung von LEN_DEV=57% |
| pred_023 | Option 3 auf 'Staub kommt wieder zur Erde...' angepasst | Exakter Bibelwortlaut Prediger 12:7 |
| pred_024 | Optionen balanciert | Vermeidung von LEN_DEV=48% |
| pred_026 | Option 0 und Frage sprachlich praezisiert | Exakter Bibelvers Prediger 2:24 |
| pred_031 | Optionen balanciert | Ausgewogene Distraktoren |
| pred_032 | Negation 'NICHT' grossgeschrieben; 'unzeitige Geburt' eingesetzt | Richtlinienkonforme Negation und Luther-1912-Wortlaut |
| pred_033 | Option 3 auf 'gegenwärtige Gut gebrauchen' angepasst | Exakter Luther-1912-Wortlaut Prediger 6:9 |
| pred_034 | Option 0 auf 'In seinem Wort ist Gewalt...' angepasst | Exakter Bibelwortlaut Prediger 8:4 |
| pred_035 | Option 1 auf 'Weil nicht alsbald ein Urteil...' praezisiert | Exakter Luther-1912-Wortlaut Prediger 8:11 |
| pred_039 | Option 1 auf 'in der Frühe speisen' angepasst | Exakter Luther-1912-Wortlaut Prediger 10:16 |
| pred_040 | Option 2 auf 'Frühe zu säen...' angepasst | Exakter Textbefund Prediger 11:6 |

## Englische Version (KJV 1769)
- Vollstaendige englische Uebersetzung aller 40 Fragen in `en/21_prediger.json`.
- Verwendung des authentischen KJV-Wortlauts (z.B. `vanity of vanities`, `vexation of spirit`, `one event happeneth to them all`, `time to every purpose under the heaven`, `set the world in their heart`, `threefold cord`, `defer not to pay it`, `he that loveth silver shall not be satisfied`, `good name is better than precious ointment`, `house of mourning`, `poor wise man delivered the city`, `dead flies`, `cast thy bread upon the waters`, `silver cord be loosed, or the golden bowl be broken`, `fear God, and keep his commandments`, `no new thing under the sun`, `words of the wise are as goads`, `untimely birth`, `sight of the eyes than the wandering of the desire`, `power of the king's word`).
- Option-Indizes (`correctAnswers`) stimmen exakt mit der deutschen Fassung ueberein.
- Verszaehlung: Identische Kapitel- und Verszaehlung zwischen Luther 1912 und KJV 1769 in allen 12 Kapiteln.

## Zur menschlichen Entscheidung
- In pred_006 wurde die Frage vom modernen Schlachter-Wortlaut ('Was hat Gott ins Herz gelegt? - Die Ewigkeit') an den authentischen Luther-1912-Text ('Er lässt ihr Herz sich ängsten, wie es gehen solle in der Welt') und KJV ('He hath set the world in their heart, so that no man can find it out') angepasst.
- In pred_010 wurde die fehlerhafte Bibelstellenangabe `Prediger 7:2` auf `Prediger 7:1` (KJV `Ecclesiastes 7:1`) korrigiert, da erst Vers 1 die Aussage 'Ein guter Ruf ist besser denn gute Salbe' / 'A good name is better than precious ointment' enthaelt.
