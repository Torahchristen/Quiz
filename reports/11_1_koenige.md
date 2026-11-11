# Review Report: 11_1_koenige.json (1. Könige / 1 Kings)

## Übersicht & Metriken
- **Geprüfte Fragen:** 70
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 24 (Angleichung an Luther 1912: Adonia, Nathan, Bath-Seba, Semer, Micha Sohn Jemlas, Zentner Silber, Großschreibung von NICHT, Bereinigung von Füllwörtern und Balancierung)
- **Geänderte Fragen (EN):** 70 (Vollständige KJV-1769-Neuübertragung mit authentischem KJV-Vokabular: Adonijah, Bath-sheba, Nathan, Shemer, two talents of silver, Micaiah the son of Imlah, still small voice, joints of the harness, under his vine and fig tree)
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 1 (`1kön_038`: antikes Gewichtsmaß zu Omris Kauf des Berges Samaria, zwei Zentner Silber / two talents = ca. 60–68 kg)
- **Entfernte / bereinigte Erklärungen:** 69 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 70 Fragen vollständig in `en/11_1_koenige.json` übertragen, inkl. authentischer KJV-Begrifflichkeiten und balancierter Optionen
- **Referenzbereinigung:** `1kön_071` (Sortieraufgabe) von semikolongetrennter Mehrbuch-Referenz (`1. Könige 17:6; 1. Könige 17:10; 1. Könige 18:38; 1. Könige 19:12; 2. Könige 2:11`) auf das einleitende Schlüsselereignis `1. Könige 17:6` bzw. `1 Kings 17:6` verengt.

## Bemerkenswerte Vokabel- und Inhaltsänderungen (DE & EN)

| questionId | Was | Warum |
|---|---|---|
| `1kön_001` | DE: `Adonia, der Sohn der Haggith`; EN: `Adonijah, the son of Haggith` | Luther 1912 1. Könige 1:5 Namensform; KJV 1769. |
| `1kön_002` | DE: `Nathan der Prophet beriet Bath-Seba`; EN: `Nathan the prophet counseled Bath-sheba` | Luther 1912 1. Könige 1:11 Namensformen; KJV 1769. |
| `1kön_004` | DE: `Adonia`, `Hörner des Altars des HERRN`; EN: `horns of the altar` | Luther 1912 1. Könige 1:50-51 Wortlaut; KJV 1769. |
| `1kön_006` | DE: `Adonia`, `Abisag von Sunem zum Weibe`; EN: `Abishag the Shunammite to wife` | Luther 1912 1. Könige 2:17 Wortlaut (`Sunem`); KJV 1769 (`Shunammite`). |
| `1kön_007` | DE: `Nathan`, `Benaia, der Sohn Jojadas, schlug ihn` | Luther 1912 1. Könige 2:34 Wortlaut. |
| `1kön_008` | DE: `Um ein gehorsames Herz, das Volk recht zu richten`; EN: `An understanding heart to judge thy people` | Luther 1912 1. Könige 3:9 Wortlaut; KJV 1769. |
| `1kön_010` | DE & EN: Optionen balanciert auf 35–42 Zeichen (`Bis zum großen Strom Euphrat im Osten` etc.) | Beseitigung der extremen Längenabweichung (`max_dev > 30%`). |
| `1kön_011` | DE: `dreitausend Sprüche redete er`; EN: `spake three thousand proverbs` | Luther 1912 1. Könige 4:32 Wortlaut; KJV 1769. |
| `1kön_012` | DE: `Zedernholz und Tannenholz vom Libanon`; EN: `Cedar trees and fir trees out of Lebanon` | Luther 1912 1. Könige 5:8-10 Wortlaut; KJV 1769. |
| `1kön_014` | DE: `Er überzog alles mit lauterem Golde`; EN: `overlaid it all with pure gold` | Luther 1912 1. Könige 6:20-22 Wortlaut; KJV 1769. |
| `1kön_015` | DE: `zwei Cherubim aus edlem Ölbaumholz`; EN: `two cherubims of olive tree` | Luther 1912 1. Könige 6:23 Wortlaut; KJV 1769. |
| `1kön_016` | DE: `Jachin zur Rechten und Boas zur Linken`; EN: `Jachin on the right hand and Boaz on the left` | Luther 1912 1. Könige 7:21 Wortlaut; KJV 1769. |
| `1kön_018` | DE: `Nur die zwei steinernen Tafeln Mose's`; EN: `Save the two tables of stone which Moses put there` | Luther 1912 1. Könige 8:9 Wortlaut; KJV 1769. |
| `1kön_022` | DE: `Er hieß sie das Land Kabul`; EN: `the land of Cabul` | Luther 1912 1. Könige 9:13 Wortlaut; KJV 1769. |
| `1kön_023` | DE: `Zu Ezeon-Geber, das bei Eloth liegt`; EN: `In Ezion-geber, which is beside Eloth` | Luther 1912 1. Könige 9:26 Schreibweise; KJV 1769. |
| `1kön_024` | DE: `Königin von Reicharabien`, `zu versuchen mit Rätseln`; EN: `queen of Sheba`, `prove him with hard questions` | Luther 1912 1. Könige 10:1 Wortlaut; KJV 1769. |
| `1kön_025` | DE: `Es ist mir nicht die Hälfte gesagt von deiner Weisheit`; EN: `The half was not told me` | Luther 1912 1. Könige 10:7 Wortlaut; KJV 1769. |
| `1kön_028` | Negation hervorgehoben: `das Königreich NICHT schon zu Salomos Lebzeiten` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |
| `1kön_032` | DE: `Zu Beth-El und in der Nordstadt Dan`; EN: `The one in Bethel, and the other put he in Dan` | Luther 1912 1. Könige 12:29 Wortlaut; KJV 1769. |
| `1kön_034` | DE: `Ein Löwe tötete ihn, fraß aber weder den Leib noch zerriss er den Esel` | Luther 1912 1. Könige 13:28 Wortlaut. |
| `1kön_036` | DE: `Pharao Sisak im fünften Jahr Rehabeams`; EN: `Shishak king of Egypt` | Luther 1912 1. Könige 14:25 Namensform; KJV 1769. |
| `1kön_037` | DE: `König Asa`, `Greuelbild der Ascherah am Bach Kidron verbrannte` | Luther 1912 1. Könige 15:13 Wortlaut. |
| `1kön_038` | DE: `Von Semer um zwei Zentner Silber`; EN: `Of Shemer for two talents of silver` | Luther 1912 1. Könige 16:24 Name und antike Währungseinheit; KJV 1769. Historische Erklärung beibehalten. |
| `1kön_039` | DE: `Isebel, die Tochter Ethbaals, des Königs zu Sidon`; EN: `Jezebel the daughter of Ethbaal king of the Zidonians` | Luther 1912 1. Könige 16:31 Wortlaut; KJV 1769. |
| `1kön_040` | DE: `Bach Krith`; EN: `brook Cherith` | Luther 1912 1. Könige 17:3 Schreibweise; KJV 1769. |
| `1kön_041` | DE: `Das Mehl im Kad ward nicht verzehrt, und dem Ölkrug mangelte nichts`; EN: `barrel of meal wasted not, neither did the cruse of oil fail` | Luther 1912 1. Könige 17:16 Wortlaut; KJV 1769. |
| `1kön_042` | DE: `Er maß sich über dem Kinde dreimal und rief den HERRN an`; EN: `stretched himself upon the child three times` | Luther 1912 1. Könige 17:21 Wortlaut; KJV 1769. |
| `1kön_046` | DE: `auf Kohlen gebackenes Brot und eine Kanne Wasser`; EN: `cake baken on the coals, and a cruse of water` | Luther 1912 1. Könige 19:6 Wortlaut; KJV 1769. |
| `1kön_047` | DE: `In einem stillen, sanften Sausen nach dem Feuer`; EN: `still small voice` | Luther 1912 1. Könige 19:12 Wortlaut; KJV 1769. |
| `1kön_048` | DE: `Er pflügte auf dem Felde mit zwölf Jochen vor sich her`; EN: `plowing with twelve yoke of oxen` | Luther 1912 1. Könige 19:19 Wortlaut; KJV 1769. |
| `1kön_050` | DE: Distraktor 3 auf 48 Zeichen balanciert; `zwei heillose Zeugen` | Beseitigung der auffälligen Längenabweichung (`max_dev > 30%`); Luther 1912 1. Könige 21:10. |
| `1kön_052` | DE: `Micha, der Sohn Jemlas` statt `Micha ben Imla`; EN: `Micaiah the son of Imlah` | Luther 1912 1. Könige 22:8-9 Namensform; KJV 1769. |
| `1kön_055` | DE: `Ein jeglicher wohnte sicher unter seinem Weinstock und Feigenbaum` | Luther 1912 1. Könige 4:25 Wortlaut. |
| `1kön_058` | DE: `Was haben wir für Teil an David? Hebe dich zu deinen Hütten, Israel!` | Luther 1912 1. Könige 12:16 Wortlaut. |
| `1kön_060` | DE: `Abia`, `weil etwas Gutes an ihm erfunden ist vor dem HERRN` | Luther 1912 1. Könige 14:13 Wortlaut. |
| `1kön_064` | DE: `Wer den Harnisch anlegt, rühme sich nicht wie der, der ihn ablegt!` | Luther 1912 1. Könige 20:11 Wortlaut. |
| `1kön_067` | DE: `Micha, der Sohn Jemlas` statt `Micha ben Jimla`; EN: `Micaiah the son of Imlah` | Luther 1912 1. Könige 22:17 Namensform; KJV 1769. |
| `1kön_068` | DE: `spannte den Bogen von ungefähr und traf ihn zwischen Panzer und Wehrgehänge`; EN: `drew a bow at a venture, and smote him between the joints of the harness` | Luther 1912 1. Könige 22:34 Wortlaut; KJV 1769. |
| `1kön_071` | Multi-Referenz verengt auf `1. Könige 17:6`; Optionen auf 36–50 Zeichen balanciert | Richtlinienkonforme enge Referenzierung ohne Semikolon. |
| `1kön_072` | Negation hervorgehoben: `obwohl er NICHT darum gebeten hatte` | Richtlinienkonforme Großschreibung verneinter Fragestellungen. |

## Zur menschlichen Entscheidung

1. **Vokabularharmonisierung gemäß Luther 1912 und KJV 1769:**
   - Namen konsequent nach Luther 1912 vereinheitlicht: `Adonia` (1 Kön 1:5, statt Adonija), `Nathan` (1 Kön 1:11, statt Natan), `Bath-Seba` (1 Kön 1:11, statt Bathseba), `Semer` (1 Kön 16:24, statt Schemer), `Micha, der Sohn Jemlas` (1 Kön 22:8-9, statt Micha ben Imla/Jimla), `Abisag von Sunem` (1 Kön 2:17, statt Schunem), `Sisak` (1 Kön 14:25, statt Schischak), `Zarpath` (1 Kön 17:9, statt Zarpat/Sarepta), `Bach Krith` (1 Kön 17:3, statt Krit), `Ezeon-Geber` (1 Kön 9:26, statt Ezjon-Geber).
   - In Englisch nach KJV 1769: `Adonijah`, `Nathan`, `Bath-sheba`, `Shemer`, `Micaiah the son of Imlah`, `Abishag the Shunammite`, `Shishak`, `Zarephath`, `brook Cherith`, `Ezion-geber`.
   - Vokabeln der Luther 1912 übernommen: `zwei Zentner Silber` (1 Kön 16:24), `Kad` (1 Kön 17:14), `stilles, sanftes Sausen` (1 Kön 19:12), `zwischen Panzer und Wehrgehänge` (1 Kön 22:34), `Bogen von ungefähr` (1 Kön 22:34).

2. **Antike Währungs- und Maßerklärung zu Omris Kauf von Samaria (`1kön_038`):**
   In 1. Könige 16:24 kaufte Omri den Berg Samaria von Semer um „zwei Zentner Silber“ (KJV: „two talents of silver“). Dies entspricht ca. 60 bis 68 kg Feinsilber und wurde gemäß Richtlinie 3 in einer sachlichen, minimalen Erklärung (DE und EN) erläutert.

3. **Referenzbereinigung bei Sortieraufgabe `1kön_071`:**
   Frage `1kön_071` enthielt eine Kette von fünf durch Semikolon getrennten Bibelstellen (`1. Könige 17:6; 1. Könige 17:10; 1. Könige 18:38; 1. Könige 19:12; 2. Könige 2:11`). Diese wurde auf das einleitende Ereignis (`1. Könige 17:6` bzw. `1 Kings 17:6`) verengt, und alle fünf Stationen wurden auf 36–50 Zeichen balanciert.
