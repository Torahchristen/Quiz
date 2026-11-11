# Review Report: 19_psalmen.json

## Uebersicht
- Gepruefte Datei: `19_psalmen.json`
- Englische Datei: `en/19_psalmen.json`
- Anzahl Fragen: 126
- Ueberpruefte Erklaerungen (DE): 0
- Ueberpruefte Erklaerungen (EN): 0
- Bereinigte Erklaerungen: 126 (auf Minimalismus zurueckgesetzt, alle Template-Texte bereinigt)

## Sprachliche Anpassungen (Luther 1912)
- Exakte Uebernahme des Luther-1912-Wortlauts aus der Versdatenbank:
  - Psalm 4:8: `ganz mit Frieden, denn allein du, HERR, hilfst mir, daß ich sicher wohne` (statt moderner Paraphrase 'lässt ihn sicher wohnen').
  - Psalm 5:3: `frühe will ich mich zu dir schicken und aufmerken` (statt 'Früh am Morgen').
  - Psalm 17:8: `beschirme mich unter dem Schatten deiner Flügel` (Luther 1912: 'beschirme', nicht modern 'birg').
  - Psalm 24:1: `Die Erde ist des HERRN und was darinnen ist` (Beseitigung von 'samt allem').
  - Psalm 27:4: `zu schauen die schönen Gottesdienste des HERRN` (exakter Wortlaut 'schauen' statt 'sehen').
  - Psalm 37:4: `der wird dir geben, was dein Herz wünschet` (exakte Zukunftsform 'wird geben').
  - Psalm 42:1: `Wie der Hirsch schreit nach frischem Wasser` ('schreit' nach Luther 1912 statt Schlachter 'lechzt').
  - Psalm 51:10: `ein reines Herz zu schaffen und einen neuen, gewissen Geist zu geben` ('gewissen Geist' gemaess Luther 1912).
  - Psalm 55:6: `daß ich flöge und wo bliebe` ('wo zu bleiben' gemaess Luther 1912 statt Schlachter 'eine Bleibe zu finden').
  - Psalm 107:29: `daß die Wellen sich legten` ('dass sich die Wellen legen').
  - Psalm 110:4: `Du bist ein Priester ewiglich nach der Weise Melchisedeks`.
  - Psalm 122:1: `Wir wollen ins Haus des HERRN gehen`.
  - Psalm 141:2: `Räuchopfer` / `Räucheropfer` und `Abendopfer`.
  - Psalm 128:3: Weib als `fruchtbarer Weinstock`, Kinder als `Ölzweige um deinen Tisch`.
- Negationshervorhebung: `NICHT` in ps_076 und ps_085 grossgeschrieben.
- Referenzbereinigung:
  - ps_088: Semicolon-Referenz `Psalmen 150:4; Psalmen 150:5` korrigiert zu `Psalmen 150:4-5`.
- Versnummernabgleich Luther 1912 vs. KJV 1769:
  - Luther 1912 fuehrt Psalm-Ueberschriften im ersten Vers mit (z.B. Psalm 3:1, Psalm 51:1). Die Zaehlung der nummerierten Verse stimmt in allen 150 Psalmen 1:1 mit KJV 1769 ueberein (jeweils identische Versanzahl pro Kapitel). Die englischen Referenzen wurden als `Psalm X:Y` angelegt.

## Aenderungen an Fragen und Optionen

| Frage-ID | Was geaendert wurde | Warum |
|---|---|---|
| ps_004 | Distraktor 0 gekuerzt, Distraktoren sprachlich angeglichen | Laengenbalance zur Vermeidung von LEN_DEV |
| ps_005 | Optionen sprachlich an Psalm 4:8 angepasst ('hilft ihm, dass er sicher wohnt') | Exakter Luther-1912-Wortlaut und Laengenausgleich |
| ps_006 | Richtige Option an Psalm 5:3 angepasst ('Frühe, wenn er sich zu ihm schickt und aufmerkt') | Exakter Luther-1912-Wortlaut ('frühe') |
| ps_013 | Richtige Option an Luther 1912 angepasst ('beschirme mich') | Exakter Textbefund ('beschirme' statt 'birg') |
| ps_024 | Option 3 auf 'Dem HERRN, und was darinnen ist' praezisiert | Beseitigung nicht-biblischer Fuellwoerter |
| ps_027 | Richtige Option auf 'schauen' statt 'sehen' praezisiert | Exakter Luther-1912-Wortlaut |
| ps_033 | Richtige Option auf 'wird ihm geben' angepasst | Exakter Textbefund |
| ps_035 | Richtige Option auf 'schreit' angepasst | Luther 1912 verwendet 'schreit' (Schlachter 'lechzt') |
| ps_041 | Distraktoren balanciert | Ausgewogene Laengenverteilung |
| ps_042 | Richtige Option auf 'wo zu bleiben' angepasst | Luther 1912 'wo bliebe' statt Schlachter 'Bleibe finden' |
| ps_053 | correctAnswers von [0, 1, 2] auf [2, 0, 1] korrigiert | Chronologische Textreihenfolge in Psalm 1:1: Wandeln (2), Treten (0), Sitzen (1) |
| ps_061 | Richtige Option sprachlich praezisiert; Distraktoren balanciert | Exakter Bibelwortlaut und Balance |
| ps_063 | Distraktorenlaengen angeglichen | Vermeidung extremer Laengendifferenzen |
| ps_074 | Optionen exakt nach Luther 1912 zitiert | Exakter Wortlaut |
| ps_076 | Negation 'NICHT' grossgeschrieben | Richtlinienkonforme Negationshervorhebung |
| ps_081 | Distraktorlaengen und richtige Option ausgewogen formuliert | Vermeidung von CORRECT_LONGEST |
| ps_085 | Negation 'NICHT' grossgeschrieben | Richtlinienkonforme Negationshervorhebung |
| ps_088 | Bibelreferenz auf 'Psalmen 150:4-5' korrigiert | Semicolon-Referenz unzulaessig; einheitlicher Versbereich |
| ps_091 | Distraktor 1 auf 'Untadelig' angepasst | Laengenausgleich zur Vermeidung von LEN_DEV |
| ps_102 | Distraktoren und richtige Option auf einheitliche Laenge gebracht | Laengenangleichung zur Vermeidung von LEN_DEV |
| ps_116 | Distraktoren verlaengert | Laengenangleichung |
| ps_120 | Distraktoren verlaengert | Vermeidung von CORRECT_LONGEST |
| ps_121 | Distraktoren und richtige Option balanciert | Laengenangleichung |
| ps_124 | Distraktoren auf einheitliche Laenge gebracht | Laengenangleichung |

## Englische Version (KJV 1769)
- Vollstaendige Uebersetzung aller 126 Fragen in `en/19_psalmen.json`.
- Verwendung des authentischen KJV-Wortlauts (z.B. `rivers of water`, `chaff which the wind driveth away`, `babes and sucklings`, `furnace of earth, purified seven times`, `apple of the eye`, `horn of my salvation`, `valley of the shadow of death`, `broken heart`, `horrible pit, out of the miry clay`, `hart panteth after the water brooks`, `father of the fatherless`, `bottle`, `head stone of the corner`, `lamp unto my feet`, `heritage of the LORD`, `fearfully and wonderfully made`).
- Option-Indizes (`correctAnswers`) stimmen in DE und EN 1:1 ueberein.
- Verszaehlung: In allen 150 Psalmen stimmt die Versanzahl von Luther 1912 und KJV 1769 ueberein. Ueberschriften wurden gemaess Vers 1 verortet.

## Zur menschlichen Entscheidung
- In ps_053 (Sortierfrage zu Psalm 1:1) war in der Quelldatei faelschlicherweise `correctAnswers: [0, 1, 2]` hinterlegt, obwohl Option 2 ('wandelt im Rat'), Option 0 ('tritt auf den Weg') und Option 1 ('sitzt, da die Spötter sitzen') heisst. Selbst die urspruenglichen Option-Erklaerungen bestaetigten, dass Option 2 an Stelle 1, Option 0 an Stelle 2 und Option 1 an Stelle 3 gehoert. Die Reihenfolge wurde auf `[2, 0, 1]` korrigiert.
- In ps_088 (Psalm 150:4-5) wurde die Semicolon-Referenz `Psalmen 150:4; Psalmen 150:5` in den gueltigen Versbereich `Psalmen 150:4-5` (KJV: `Psalm 150:4-5`) geaendert.
