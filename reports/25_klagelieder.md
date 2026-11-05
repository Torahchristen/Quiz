# Review Report: 25_klagelieder.json

## Uebersicht
- Gepruefte Datei: `25_klagelieder.json`
- Englische Datei: `en/25_klagelieder.json`
- Anzahl Fragen: 18
- Ueberpruefte Erklaerungen (DE): 0
- Ueberpruefte Erklaerungen (EN): 0
- Bereinigte Erklaerungen: 18 (auf Minimalismus zurueckgesetzt, alle Template-Texte bereinigt)

## Sprachliche Anpassungen (Luther 1912)
- Exakter Luther-1912-Wortlaut aus der Versdatenbank uebernommen:
  - Klagelieder 1:1: `Wie liegt die Stadt so wüst, die voll Volks war!` (klag_001).
  - Klagelieder 1:2: `alle ihre Freunde sind ihr untreu und ihre Feinde geworden` (kla_015).
  - Klagelieder 1:12: `Schauet doch und sehet, ob irgend ein Schmerz sei wie mein Schmerz` (kla_005).
  - Klagelieder 2:1: `Er hat die Herrlichkeit Israels vom Himmel auf die Erde geworfen` (kla_006).
  - Klagelieder 2:11: `die jungen Kinder und Säuglinge auf den Gassen in der Stadt verschmachteten` (kla_007).
  - Klagelieder 2:19: `schütte dein Herz aus vor dem Herrn wie Wasser` (kla_008).
  - Klagelieder 3:22-23: `Die Güte des HERRN ist's, daß wir nicht gar aus sind; seine Barmherzigkeit hat noch kein Ende` (klag_002).
  - Klagelieder 3:24: `Der HERR ist mein Teil, spricht meine Seele; darum will ich auf ihn hoffen` (kla_016).
  - Klagelieder 3:26-27: `Es ist ein köstlich Ding, geduldig sein und auf die Hülfe des HERRN hoffen` (kla_010).
  - Klagelieder 3:31-32: `Denn der Herr verstößt nicht ewiglich; sondern er betrübt wohl, und erbarmt sich wieder nach seiner Güte` (kla_017).
  - Klagelieder 3:40: `Und laßt uns erforschen und prüfen unser Wesen und uns zum HERRN bekehren!` (kla_018).
  - Klagelieder 4:1: `Wie ist das Gold so gar verdunkelt und das feine Gold so wandelbar geworden` (kla_011).
  - Klagelieder 4:6: `Die Missetat der Tochter meines Volks ist größer denn die Sünde Sodoms` (kla_019).
  - Klagelieder 4:10: `Die barmherzigen Weiber haben ihre Kinder selbst müssen kochen, daß sie ihnen zur Speise würden` (kla_012).
  - Klagelieder 4:19: `Unsre Verfolger waren schneller denn die Adler unter dem Himmel` (kla_020).
  - Klagelieder 4:20: `Der Odem unsers Lebens, der Gesalbte des HERRN` (kla_013).
  - Klagelieder 5:19: `Aber du, HERR, der du ewiglich bleibst und dein Thron für und für` (kla_014).
  - Klagelieder 5:21: `Bringe uns, HERR, wieder zu dir, daß wir wieder heimkommen; erneuere unsre Tage wie vor alters!` (klag_003).

## Aenderungen an Fragen und Optionen

| Frage-ID | Was geaendert wurde | Warum |
|---|---|---|
| klag_001 | Option 1 auf 'Wie die Stadt so wüst liegt...' angepasst | Exakter Luther-1912-Wortlaut Klagelieder 1:1 |
| kla_007 | Optionen balanciert und auf 'verschmachten' praezisiert | Beseitigung von LEN_DEV=54% und exakter Verswortlaut |
| kla_012 | Option 3 auf 'zur Speise würden' praezisiert; Distraktoren balanciert | Exakter Luther-1912-Wortlaut und Laengenbalance |
| kla_013 | Option 1 auf 'Der Gesalbte des HERRN, der unser Odem war' angepasst | Exakter Luther-1912-Wortlaut ('Odem unsers Lebens') |
| kla_015 | Optionen auf einheitliche Laenge balanciert | Laengenangleichung (0% Abweichung) |
| kla_018 | Optionen balanciert | Beseitigung von LEN_DEV=32% |
| kla_019 | Optionen balanciert | Laengenangleichung (0% Abweichung) |
| kla_020 | Optionen balanciert | Laengenangleichung |

## Englische Version (KJV 1769)
- Vollstaendige englische Uebersetzung aller 18 Fragen in `en/25_klagelieder.json`.
- KJV-Buchname `Lamentations` konsequent in allen Referenzen und Metadaten verwendet.
- Verwendung des authentischen KJV-Wortlauts (z.B. `How doth the city sit solitary`, `become as a widow`, `she weepeth sore in the night`, `dealt treacherously`, `Is it nothing to you, all ye that pass by?`, `sorrow like unto my sorrow`, `cast down from heaven unto the earth the beauty of Israel`, `children and the sucklings swoon in the streets`, `pour out thine heart like water before the face of the Lord`, `It is of the LORD’s mercies that we are not consumed`, `compassions fail not`, `new every morning`, `The LORD is my portion`, `quietly wait for the salvation of the LORD`, `bear the yoke in his youth`, `though he cause grief, yet will he have compassion`, `search and try our ways, and turn again to the LORD`, `gold become dim`, `hands of the pitiful women have sodden their own children`, `swifter than the eagles of the heaven`, `The breath of our nostrils, the anointed of the LORD`, `Thou, O LORD, remainest for ever`, `Turn thou us unto thee, O LORD, and we shall be turned; renew our days as of old`).
- Alle `correctAnswers`-Indizes stimmen 1:1 mit der deutschen Fassung ueberein.
- Verszaehlung: KJV und Luther 1912 stimmen in allen 5 Kapiteln exakt ueberein.

## Zur menschlichen Entscheidung
- In kla_013 uebersetzt Martin Luther 'ruach appeinu' mit 'Der Odem unsers Lebens', waehrend die KJV woertlicher 'The breath of our nostrils' uebersetzt. Beide Sprachfassungen folgen treu ihrem jeweiligen Bibeltext.
- In kla_019 verwendet Luther 1912 die historische Vergleichspartikel 'größer denn' (KJV 'greater than').
