# Gesamtbericht: Prüfung, Überarbeitung und KJV-Übersetzung aller 66 Quizdateien

## 1. Gesamtergebnis

- **Geprüfte Bücher / Dateien:** 66 von 66 (`01_1_mose.json` bis `66_offenbarung.json`)
- **Englische KJV-Dateien (`en/`):** 66 von 66 (`en/01_1_mose.json` bis `en/66_offenbarung.json` sowie `en/catalog.json`)
- **Geprüfte Fragen insgesamt:** 4754 (DE) + 4754 (EN) = 9508
- **Fragen mit Überarbeitung im Deutschen:** 2204 (davon 1409 Fragetexte, 2027 Fragen mit angepassten Antwortoptionen, 125 präzisierte/korrigierte Bibelstellen)
- **Beibehaltene/neu verfasste notwendige Sacherklärungen (DE / EN):** 46 / 46 (alle rein verswiederholenden Template-Erklärungen sowie Options-Templates wurden auf `""` und `explanationReviewed: false` bereinigt)
- **Validierungsstatus (`scripts/validate_quizzes.py`):** 0 kritische Fehler, 0 Inkonsistenzen, 0 Qualitätswarnungen
- **Synchronisationsstatus:** Alle 66 deutschen JSON-Dateien nach `BibelQuiz/quizzes/json/` kopiert; alle 66 Markdown-Dateien via `scripts/sync_all_md.py` aktualisiert
- **Vollständige Vorher-/Nachher-Dokumentation:** siehe `reports/AENDERUNGEN_VORHER_NACHHER.md`

## 2. Zahlen pro Datei

| Datei | Buch (DE / EN) | Übersetzung (DE) | Fragen | Geändert | Fragetext | Optionen | Bibelstelle | Erkl. (DE/EN) | Einzelbericht |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: | :---: | :--- |
| `01_1_mose.json` | 1. Mose (Genesis) / Genesis | Schlachter (Revision von 1951) | 296 | 118 | 32 | 88 | 13 | 17 / 17 | `reports/01_1_mose.md` |
| `02_2_mose.json` | 2. Mose (Exodus) / Exodus | Schlachter (Revision von 1951) | 293 | 53 | 9 | 44 | 10 | 3 / 3 | `reports/02_2_mose.md` |
| `03_3_mose.json` | 3. Mose (Levitikus) / Leviticus | Schlachter (Revision von 1951) | 173 | 38 | 35 | 32 | 0 | 3 / 3 | `reports/03_3_mose.md` |
| `04_4_mose.json` | 4. Mose (Numeri) / Numbers | Schlachter (Revision von 1951) | 246 | 47 | 42 | 32 | 2 | 3 / 3 | `reports/04_4_mose.md` |
| `05_5_mose.json` | 5. Mose (Deuteronomium) / Deuteronomy | Schlachter (Revision von 1951) | 238 | 60 | 31 | 25 | 17 | 2 / 2 | `reports/05_5_mose.md` |
| `06_josua.json` | Josua / Joshua | Luther 1912 | 146 | 64 | 44 | 58 | 1 | 1 / 1 | `reports/06_josua.md` |
| `07_richter.json` | Richter / Judges | Luther 1912 | 140 | 122 | 107 | 101 | 2 | 1 / 1 | `reports/07_richter.md` |
| `08_rut.json` | Rut / Ruth | Luther 1912 | 31 | 31 | 31 | 29 | 0 | 2 / 2 | `reports/08_rut.md` |
| `09_1_samuel.json` | 1. Samuel / 1 Samuel | Luther 1912 | 111 | 26 | 9 | 18 | 1 | 1 / 1 | `reports/09_1_samuel.md` |
| `10_2_samuel.json` | 2. Samuel / 2 Samuel | Luther 1912 | 80 | 80 | 68 | 80 | 0 | 1 / 1 | `reports/10_2_samuel.md` |
| `11_1_koenige.json` | 1. Könige / 1 Kings | Luther 1912 | 70 | 68 | 66 | 68 | 1 | 1 / 1 | `reports/11_1_koenige.md` |
| `12_2_koenige.json` | 2. Könige / 2 Kings | Luther 1912 | 77 | 77 | 70 | 76 | 0 | 2 / 2 | `reports/12_2_koenige.md` |
| `13_1_chronik.json` | 1. Chronik / 1 Chronicles | Luther 1912 | 85 | 84 | 76 | 83 | 0 | 3 / 3 | `reports/13_1_chronik.md` |
| `14_2_chronik.json` | 2. Chronik / 2 Chronicles | Luther 1912 | 100 | 100 | 85 | 100 | 0 | 1 / 1 | `reports/14_2_chronik.md` |
| `15_esra.json` | Esra / Ezra | Luther 1912 | 30 | 30 | 30 | 30 | 0 | 0 / 0 | `reports/15_esra.md` |
| `16_nehemia.json` | Nehemia / Nehemiah | Luther 1912 | 39 | 39 | 37 | 39 | 0 | 1 / 1 | `reports/16_nehemia.md` |
| `17_esther.json` | Esther / Esther | Luther 1912 | 30 | 30 | 29 | 30 | 0 | 1 / 1 | `reports/17_esther.md` |
| `18_hiob.json` | Hiob / Job | Luther 1912 | 141 | 140 | 132 | 140 | 2 | 1 / 1 | `reports/18_hiob.md` |
| `19_psalmen.json` | Psalmen / Psalms | Luther 1912 | 126 | 23 | 2 | 20 | 1 | 0 / 0 | `reports/19_psalmen.md` |
| `20_sprueche.json` | Sprüche / Proverbs | Luther 1912 | 92 | 41 | 3 | 41 | 0 | 0 / 0 | `reports/20_sprueche.md` |
| `21_prediger.json` | Prediger / Ecclesiastes | Luther 1912 | 40 | 19 | 6 | 19 | 1 | 0 / 0 | `reports/21_prediger.md` |
| `22_hohelied.json` | Hohelied / Song of Solomon | Luther 1912 | 26 | 14 | 2 | 14 | 1 | 0 / 0 | `reports/22_hohelied.md` |
| `23_jesaja.json` | Jesaja / Isaiah | Luther 1912 | 196 | 58 | 1 | 57 | 2 | 0 / 0 | `reports/23_jesaja.md` |
| `24_jeremia.json` | Jeremia / Jeremiah | Luther 1912 | 157 | 24 | 3 | 24 | 0 | 0 / 0 | `reports/24_jeremia.md` |
| `25_klagelieder.json` | Klagelieder / Lamentations | Luther 1912 | 18 | 8 | 0 | 8 | 0 | 0 / 0 | `reports/25_klagelieder.md` |
| `26_hesekiel.json` | Hesekiel / Ezekiel | Luther 1912 | 139 | 22 | 2 | 18 | 4 | 0 / 0 | `reports/26_hesekiel.md` |
| `27_daniel.json` | Daniel / Daniel | Luther 1912 | 37 | 9 | 2 | 7 | 1 | 0 / 0 | `reports/27_daniel.md` |
| `28_hosea.json` | Hosea / Hosea | Luther 1912 | 43 | 2 | 0 | 2 | 0 | 0 / 0 | `reports/28_hosea.md` |
| `29_joel.json` | Joel / Joel | Luther 1912 | 18 | 1 | 1 | 0 | 1 | 0 / 0 | `reports/29_joel.md` |
| `30_amos.json` | Amos / Amos | Luther 1912 | 27 | 24 | 18 | 22 | 2 | 0 / 0 | `reports/30_amos.md` |
| `31_obadja.json` | Obadja / Obadiah | Luther 1912 | 10 | 10 | 7 | 10 | 0 | 0 / 0 | `reports/31_obadja.md` |
| `32_jona.json` | Jona / Jonah | Luther 1912 | 20 | 20 | 15 | 20 | 7 | 0 / 0 | `reports/32_jona.md` |
| `33_micha.json` | Micha / Micah | Luther 1912 | 21 | 21 | 17 | 21 | 2 | 0 / 0 | `reports/33_micha.md` |
| `34_nahum.json` | Nahum / Nahum | Luther 1912 | 16 | 16 | 11 | 16 | 4 | 0 / 0 | `reports/34_nahum.md` |
| `35_habakuk.json` | Habakuk / Habakkuk | Luther 1912 | 18 | 10 | 0 | 10 | 4 | 0 / 0 | `reports/35_habakuk.md` |
| `36_zephanja.json` | Zephanja / Zephaniah | Luther 1912 | 18 | 10 | 1 | 8 | 5 | 0 / 0 | `reports/36_zephanja.md` |
| `37_haggai.json` | Haggai / Haggai | Luther 1912 | 14 | 7 | 0 | 5 | 3 | 0 / 0 | `reports/37_haggai.md` |
| `38_sacharja.json` | Sacharja / Zechariah | Luther 1912 | 42 | 19 | 2 | 19 | 0 | 0 / 0 | `reports/38_sacharja.md` |
| `39_maleachi.json` | Maleachi / Malachi | Luther 1912 | 20 | 5 | 0 | 5 | 0 | 0 / 0 | `reports/39_maleachi.md` |
| `40_matthaeus.json` | Matthäus / Matthew | Schlachter (Revision von 1951) | 148 | 40 | 0 | 40 | 3 | 0 / 0 | `reports/40_matthaeus.md` |
| `41_markus.json` | Markus / Mark | Schlachter (Revision von 1951) | 80 | 16 | 0 | 16 | 0 | 0 / 0 | `reports/41_markus.md` |
| `42_lukas.json` | Lukas / Luke | Schlachter (Revision von 1951) | 126 | 35 | 1 | 34 | 3 | 0 / 0 | `reports/42_lukas.md` |
| `43_johannes.json` | Johannes / John | Schlachter (Revision von 1951) | 110 | 42 | 2 | 38 | 2 | 0 / 0 | `reports/43_johannes.md` |
| `44_apostelgeschichte.json` | Apostelgeschichte / Acts | Schlachter (Revision von 1951) | 145 | 26 | 0 | 19 | 8 | 0 / 0 | `reports/44_apostelgeschichte.md` |
| `45_roemer.json` | Römer / Romans | Schlachter (Revision von 1951) | 80 | 19 | 1 | 17 | 1 | 0 / 0 | `reports/45_roemer.md` |
| `46_1_korinther.json` | 1. Korinther / 1 Corinthians | Schlachter (Revision von 1951) | 80 | 19 | 0 | 19 | 1 | 0 / 0 | `reports/46_1_korinther.md` |
| `47_2_korinther.json` | 2. Korinther / 2 Corinthians | Schlachter (Revision von 1951) | 65 | 8 | 0 | 8 | 0 | 0 / 0 | `reports/47_2_korinther.md` |
| `48_galater.json` | Galater / Galatians | Schlachter (Revision von 1951) | 31 | 31 | 29 | 30 | 0 | 0 / 0 | `reports/48_galater.md` |
| `49_epheser.json` | Epheser / Ephesians | Schlachter (Revision von 1951) | 31 | 31 | 28 | 31 | 0 | 0 / 0 | `reports/49_epheser.md` |
| `50_philipper.json` | Philipper / Philippians | Schlachter (Revision von 1951) | 20 | 20 | 20 | 20 | 0 | 0 / 0 | `reports/50_philipper.md` |
| `51_kolosser.json` | Kolosser / Colossians | Schlachter (Revision von 1951) | 20 | 20 | 20 | 20 | 0 | 0 / 0 | `reports/51_kolosser.md` |
| `52_1_thessalonicher.json` | 1. Thessalonicher / 1 Thessalonians | Schlachter (Revision von 1951) | 25 | 25 | 25 | 24 | 0 | 0 / 0 | `reports/52_1_thessalonicher.md` |
| `53_2_thessalonicher.json` | 2. Thessalonicher / 2 Thessalonians | Schlachter (Revision von 1951) | 15 | 14 | 12 | 14 | 0 | 0 / 0 | `reports/53_2_thessalonicher.md` |
| `54_1_timotheus.json` | 1. Timotheus / 1 Timothy | Schlachter (Revision von 1951) | 30 | 30 | 30 | 30 | 0 | 0 / 0 | `reports/54_1_timotheus.md` |
| `55_2_timotheus.json` | 2. Timotheus / 2 Timothy | Schlachter (Revision von 1951) | 20 | 20 | 20 | 20 | 0 | 0 / 0 | `reports/55_2_timotheus.md` |
| `56_titus.json` | Titus / Titus | Schlachter (Revision von 1951) | 15 | 15 | 15 | 15 | 0 | 0 / 0 | `reports/56_titus.md` |
| `57_philemon.json` | Philemon / Philemon | Schlachter (Revision von 1951) | 5 | 5 | 5 | 5 | 0 | 1 / 1 | `reports/57_philemon.md` |
| `58_hebraeer.json` | Hebräer / Hebrews | Schlachter (Revision von 1951) | 66 | 66 | 66 | 64 | 5 | 0 / 0 | `reports/58_hebraeer.md` |
| `59_jakobus.json` | Jakobus / James | Schlachter (Revision von 1951) | 25 | 25 | 25 | 24 | 3 | 0 / 0 | `reports/59_jakobus.md` |
| `60_1_petrus.json` | 1. Petrus / 1 Peter | Schlachter (Revision von 1951) | 25 | 25 | 25 | 25 | 2 | 0 / 0 | `reports/60_1_petrus.md` |
| `61_2_petrus.json` | 2. Petrus / 2 Peter | Schlachter (Revision von 1951) | 15 | 15 | 15 | 15 | 3 | 0 / 0 | `reports/61_2_petrus.md` |
| `62_1_johannes.json` | 1. Johannes / 1 John | Schlachter (Revision von 1951) | 25 | 25 | 25 | 25 | 1 | 0 / 0 | `reports/62_1_johannes.md` |
| `63_2_johannes.json` | 2. Johannes / 2 John | Schlachter (Revision von 1951) | 5 | 5 | 5 | 5 | 0 | 0 / 0 | `reports/63_2_johannes.md` |
| `64_3_johannes.json` | 3. Johannes / 3 John | Schlachter (Revision von 1951) | 5 | 5 | 5 | 5 | 0 | 0 / 0 | `reports/64_3_johannes.md` |
| `65_judas.json` | Judas / Jude | Schlachter (Revision von 1951) | 5 | 5 | 5 | 5 | 0 | 0 / 0 | `reports/65_judas.md` |
| `66_offenbarung.json` | Offenbarung / Revelation | Schlachter (Revision von 1951) | 113 | 47 | 4 | 40 | 6 | 1 / 1 | `reports/66_offenbarung.md` |
| **Gesamt (66 Dateien)** | **Alle 66 Bücher** | **Schlachter 1951 / Luther 1912** | **4754** | **2204** | **1409** | **2027** | **125** | **46 / 46** | `reports/*.md` |

## 3. Fragen mit geänderter Lösung (`correctAnswers`)

Bei keiner der 4.754 Fragen musste das Array `correctAnswers` gegenüber dem Ausgangszustand (`main`) geändert werden; wo Antwortoptionen sprachlich an die Bibelübersetzung angepasst wurden, blieb die richtige Antwort durchgehend am bestehenden Lösungsindex.

> **Nachtrag (Inhaltsprüfung):** Die Prüfung in [`PRUEFBERICHT_INHALT_UEBERSETZUNG.md`](./PRUEFBERICHT_INHALT_UEBERSETZUNG.md) ergab, dass bei `ps_061`, `ps_063`, `ps_074` und `apg_136` durch das Umsortieren der Optionen der unveränderte Index auf einen falschen Distraktor zeigte. Diese Lösungen wurden in DE und EN korrigiert; alle weiteren Korrekturen stehen in [`KORREKTUREN_UMSETZUNG.md`](./KORREKTUREN_UMSETZUNG.md).

## 4. Korrigierte und präzisierte Bibelstellen (`bibleReference`)

| Datei | questionId | Vorher (DE) | Nachher (DE) | Nachher (EN KJV) | Frage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `01_1_mose.json` | `1mose_139` | `1. Mose 38:29-30; Matthäus 1:3` | `1. Mose 38:29-30` | `Genesis 38:29-30` | Wie hießen die Zwillinge, die Tamar gebar, und welche theologische Bedeutung hat der Erstgeborene in Bezug auf den Messias? |
| `01_1_mose.json` | `1mose_182` | `1. Mose 47:22; 47:26` | `1. Mose 47:22` | `Genesis 47:22` | Welche gesellschaftliche Gruppe war laut Gesetz (1. Mose 47:22, 26) von Josephs radikaler Verstaatlichungspolitik während der Hungersnot ausgeschlossen? |
| `01_1_mose.json` | `1mose_188` | `1. Mose 48:14; 48:17` | `1. Mose 48:14` | `Genesis 48:14` | Wie vollzog Jakob die Handauflegung bei Josephs Söhnen? |
| `01_1_mose.json` | `1mose_246` | `1. Mose 49:31; 50:13` | `1. Mose 49:29-31` | `Genesis 49:29-31` | Welche biblischen Personen wurden in der berühmten Grabeshöhle Machpelah bei Hebron (Mamre) begraben? |
| `01_1_mose.json` | `1mose_264` | `1. Mose 13:18; 15:1-12` | `1. Mose 15:12` | `Genesis 15:12` | Wo fand der schauerliche Bundesschluss zwischen den Stücken statt, bei dem Abram in einen tiefen Schlaf und dichte Finsternis fiel? |
| `01_1_mose.json` | `1mose_278` | `1. Mose 24:2-4; 24:22` | `1. Mose 24:2-4` | `Genesis 24:2-4` | Nach christlicher (typologischer) Auslegung – Schickt Abraham seinen ältesten, unbenannten Knecht aus, um eine Braut für seinen Sohn Isaak zu werben. Welche göttliche Instanz wird durch diesen Knecht prophetisch abgebildet? |
| `01_1_mose.json` | `1mose_279` | `1. Mose 6:16; 7:16` | `1. Mose 6:16` | `Genesis 6:16` | Nach christlicher (typologischer) Auslegung – Warum gilt die Arche Noahs in der christlichen Auslegung als Typus-Bild auf das Heil in Jesus Christus? |
| `01_1_mose.json` | `1mose_280` | `1. Mose 28:12; Johannes 1:51` | `1. Mose 28:12` | `Genesis 28:12` | Nach christlicher (typologischer) Auslegung – Als Jakob die Himmelsleiter im Traum sieht, auf der Engel Gottes auf- und niedersteigen, welches messianische Geheimnis lüftet Jesus selbst im Johannesevangelium darüber? |
| `01_1_mose.json` | `1mose_287` | `1. Mose 4:8-10; Matthäus 23:35` | `1. Mose 4:8-10` | `Genesis 4:8-10` | Nach christlicher (typologischer) Auslegung – Warum wird Abel in der Theologie als der erste „Märtyrer“ und als Typus auf den gerechten Tod Jesu Christi gesehen? |
| `01_1_mose.json` | `1mose_325` | `1. Mose 4:1-2; 1. Mose 4:25` | `1. Mose 4:1-25` | `Genesis 4:1-25` | Welche drei Söhne Adams und Evas werden in 1. Mose 4 genannt? |
| `01_1_mose.json` | `1mose_326` | `1. Mose 19:26; 1. Mose 19:30` | `1. Mose 19:15-30` | `Genesis 19:15-30` | Wer aus der Familie Lots überlebte nach 1. Mose 19 den Untergang Sodoms? |
| `01_1_mose.json` | `1mose_327` | `1. Mose 1:3; 1. Mose 1:6; 1. Mose 1:11; 1. Mose 1:16; 1. Mose 1:27` | `1. Mose 1:1-31` | `Genesis 1:1-31` | Bringe die Schöpfungswerke nach 1. Mose 1 in die richtige Reihenfolge. |
| `01_1_mose.json` | `1mose_329` | `1. Mose 6:14; 1. Mose 7:10; 1. Mose 8:4; 1. Mose 8:11; 1. Mose 9:13` | `1. Mose 6:14-22` | `Genesis 6:14-22` | Bringe diese Ereignisse um Noah und die Sintflut in die richtige Reihenfolge. |
| `02_2_mose.json` | `ex_008` | `2. Mose 8:18-19` | `2. Mose 8:22-23` | `Exodus 8:22-23` | Welches Gebiet verschonte Gott ab der vierten Plage der Hundsfliegen vor den Wüstenschwärmen? |
| `02_2_mose.json` | `ex_057` | `2. Mose 8:4` | `2. Mose 8:8` | `Exodus 8:8` | Welches Versprechen gab Pharao Mose, um die Froschplage abzuwenden? |
| `02_2_mose.json` | `ex_058` | `2. Mose 8:9-10` | `2. Mose 8:13-14` | `Exodus 8:13-14` | Was geschah mit den Fröschen, nachdem Gott das Gebet Moses erhörte? |
| `02_2_mose.json` | `ex_059` | `2. Mose 8:12-13` | `2. Mose 8:16-17` | `Exodus 8:16-17` | Aus welchem Material entstanden die Stechmücken bei der dritten Plage? |
| `02_2_mose.json` | `ex_060` | `2. Mose 8:15` | `2. Mose 8:19` | `Exodus 8:19` | Was bekannten die Zauberer, als sie die Mückenplage nicht nachahmen konnten? |
| `02_2_mose.json` | `ex_191` | `2. Mose 22:15-16` | `2. Mose 22:16-17` | `Exodus 22:16-17` | Was musste ein Mann tun, der eine unverlobte Jungfrau verführte und bei ihr lag? |
| `02_2_mose.json` | `ex_192` | `2. Mose 22:17` | `2. Mose 22:18` | `Exodus 22:18` | Welches unumstößliche Gebot erließ Gott bezüglich einer Zauberin im Land? |
| `02_2_mose.json` | `ex_193` | `2. Mose 22:22-23` | `2. Mose 22:22-24` | `Exodus 22:22-24` | Womit drohte Gott, falls Fremdlinge, Witwen und Waisen im Volk unterdrückt würden? |
| `02_2_mose.json` | `ex_194` | `2. Mose 22:24` | `2. Mose 22:25` | `Exodus 22:25` | Welche Einschränkung galt beim Geldleihen an einen Armen aus dem Volk Gottes? |
| `02_2_mose.json` | `ex_333` | `2. Mose 12:21; 2. Mose 14:22; 2. Mose 16:14; 2. Mose 20:1` | `2. Mose 12:21-28` | `Exodus 12:21-28` | Bringe diese Ereignisse des Auszugs in die richtige Reihenfolge. |
| `04_4_mose.json` | `num_111` | `4. Mose 17:3-4` | `4. Mose 16:38-39` | `Numbers 16:38-39` | Was befahl Gott Eleasar mit den bronzenen Räucherpfannen der Getöteten zu tun? |
| `04_4_mose.json` | `num_112` | `4. Mose 17:11-13` | `4. Mose 16:47-48` | `Numbers 16:47-48` | Womit trat Aaron zwischen die Toten und die Lebenden, um die Plage im Volk zu stoppen? |
| `05_5_mose.json` | `dtn_085` | `5. Mose 13:6` | `5. Mose 13:5` | `Deuteronomy 13:5` | Was sollte mit einem Propheten geschehen, der Zeichen tat, aber zum Götzendienst aufrief? |
| `05_5_mose.json` | `dtn_086` | `5. Mose 13:4` | `5. Mose 13:3` | `Deuteronomy 13:3` | Warum ließ Gott es zuweilen zu, dass ein Verführer echte Zeichen oder Wunder tat? |
| `05_5_mose.json` | `dtn_087` | `5. Mose 13:7-11` | `5. Mose 13:6-9` | `Deuteronomy 13:6-9` | Wer sollte gesteinigt werden, wenn er heimlich zum Abfall vom HERRN verführte? |
| `05_5_mose.json` | `dtn_088` | `5. Mose 13:13-17` | `5. Mose 13:12-16` | `Deuteronomy 13:12-16` | Welches Gericht verlangte das Gesetz über eine israelitische Stadt, die dem Götzendienst verfiel? |
| `05_5_mose.json` | `dtn_089` | `5. Mose 13:18` | `5. Mose 13:17` | `Deuteronomy 13:17` | Was durfte von den erbeuteten Gütern aus einer gebannten Stadt behalten werden? |
| `05_5_mose.json` | `dtn_090` | `5. Mose 13:12` | `5. Mose 13:11` | `Deuteronomy 13:11` | Welches Ziel sollte die strenge Bestrafung von Verführern in ganz Israel bewirken? |
| `05_5_mose.json` | `dtn_091` | `5. Mose 13:15` | `5. Mose 13:14` | `Deuteronomy 13:14` | Welcher Schritt musste vor dem Vollzug des Gerichts an einer beschuldigten Stadt erfolgen? |
| `05_5_mose.json` | `dtn_155` | `5. Mose 23:4-5` | `5. Mose 23:3-4` | `Deuteronomy 23:3-4` | Welches Heidenvolk durfte selbst bis ins zehnte Geschlecht NICHT in die Gemeinde kommen? |
| `05_5_mose.json` | `dtn_156` | `5. Mose 23:8-9` | `5. Mose 23:7-8` | `Deuteronomy 23:7-8` | Ab welchem Geschlecht durften Nachkommen der Edomiter und Ägypter aufgenommen werden? |
| `05_5_mose.json` | `dtn_157` | `5. Mose 23:13-15` | `5. Mose 23:12-14` | `Deuteronomy 23:12-14` | Womit musste jeder Krieger im Feldlager für die Reinheit ausgerüstet sein? |
| `05_5_mose.json` | `dtn_158` | `5. Mose 23:16-17` | `5. Mose 23:15-16` | `Deuteronomy 23:15-16` | Wie sollte Israel mit einem entflohenen Knecht aus dem Ausland umgehen? |
| `05_5_mose.json` | `dtn_159` | `5. Mose 23:19` | `5. Mose 23:18` | `Deuteronomy 23:18` | Welche zweierlei Einnahmen durften keinesfalls als Gelübdeopfer gebracht werden? |
| `05_5_mose.json` | `dtn_160` | `5. Mose 23:20-21` | `5. Mose 23:19-20` | `Deuteronomy 23:19-20` | Von wem durfte der Israelite Zinsen nehmen im Erdlande, das er einnahm? |
| `05_5_mose.json` | `dtn_161` | `5. Mose 23:24-25` | `5. Mose 23:24` | `Deuteronomy 23:24` | Was war jemandem erlaubt, der durch den Weinberg seines Nächsten ging? |
| `05_5_mose.json` | `dtn_198` | `5. Mose 29:4` | `5. Mose 29:5` | `Deuteronomy 29:5` | Welches ständige Wunder an der Kleidung bezeugte Gottes Treue während der Wüstenjahre? |
| `05_5_mose.json` | `dtn_201` | `5. Mose 29:22` | `5. Mose 29:23` | `Deuteronomy 29:23` | Mit welchen zerstörten Städten vergleicht die Schrift das gerichtete Erdland? |
| `05_5_mose.json` | `dtn_203` | `5. Mose 29:28` | `5. Mose 29:29` | `Deuteronomy 29:29` | Welcher fundamentale Grundsatz unterscheidet göttliches Geheimnis und Offenbarung am Ende von Kapitel 29? |
| `06_josua.json` | `jos_146` | `Josua 3:17; Josua 6:20; Josua 7:4; Josua 9:3` | `Josua 3:17` | `Joshua 3:17` | Bringe diese Ereignisse aus dem Buch Josua in die richtige Reihenfolge. |
| `07_richter.json` | `ri_139` | `Richter 4:4; Richter 4:21` | `Richter 4:4-22` | `Judges 4:4-22` | Welche zwei Frauen spielten nach Richter 4 die Hauptrolle im Sieg über den Feldhauptmann Sisera? |
| `07_richter.json` | `ri_140` | `Richter 3:9; Richter 3:15; Richter 4:4; Richter 6:11; Richter 13:24` | `Richter 3:9` | `Judges 3:9` | Bringe diese Richter in der Reihenfolge ihres Auftretens im Buch der Richter. |
| `09_1_samuel.json` | `1sam_119` | `1. Samuel 16:13; 1. Samuel 17:49; 1. Samuel 19:10; 1. Samuel 31:6; 2. Samuel 2:4` | `1. Samuel 16:13` | `1 Samuel 16:13` | Bringe diese Stationen im Leben Davids in die richtige Reihenfolge. |
| `11_1_koenige.json` | `1kön_071` | `1. Könige 17:6; 1. Könige 17:10; 1. Könige 18:38; 1. Könige 19:12; 2. Könige 2:11` | `1. Könige 17:6` | `1 Kings 17:6` | Bringe diese Ereignisse aus dem Leben Elias in die richtige Reihenfolge. |
| `18_hiob.json` | `hi_012` | `Hiob 13:4; 16:2` | `Hiob 16:2` | `Job 16:2` | Wie bezeichnete Hiob seine drei Freunde angesichts ihrer harten Zurechtweisungen? |
| `18_hiob.json` | `hi_019` | `Hiob 40:15; 41:1` | `Hiob 40:15` | `Job 40:15` | Welche zwei gewaltigen Geschöpfe werden in den Reden Gottes geschildert? |
| `19_psalmen.json` | `ps_088` | `Psalmen 150:4; Psalmen 150:5` | `Psalmen 150:4-5` | `Psalm 150:4-5` | Welche zwei Instrumente nennt Psalm 150:4-5 zum Lob Gottes? |
| `21_prediger.json` | `pred_010` | `Prediger 7:2` | `Prediger 7:1` | `Ecclesiastes 7:1` | Womit vergleicht Prediger 7:1 einen guten Ruf? |
| `22_hohelied.json` | `hld_025` | `Hohelied 5:10, 16` | `Hohelied 5:10` | `Song of Solomon 5:10` | Wie rühmt die Braut ihren Geliebten in Hohelied 5:10? |
| `23_jesaja.json` | `jes_193` | `Jesaja 64:5` | `Jesaja 64:6` | `Isaiah 64:6` | Wie bekennt das Volk seine Sünde in Jesaja 64:5? |
| `23_jesaja.json` | `jes_194` | `Jesaja 64:7` | `Jesaja 64:8` | `Isaiah 64:8` | Mit welchem Bild unterwirft sich das Volk in Jesaja 64:7 dem HERRN? |
| `26_hesekiel.json` | `hes_060` | `Hesekiel 6:7; 11:12` | `Hesekiel 6:7` | `Ezekiel 6:7` | Welchen Zweck nennt der HERR immer wieder für seine Taten (Hesekiel 6:7)? |
| `26_hesekiel.json` | `hes_061` | `Hesekiel 17:3.12` | `Hesekiel 17:3-12` | `Ezekiel 17:3-12` | Wen stellt der große Adler in Hesekiel 17:3-12 dar? |
| `26_hesekiel.json` | `hes_067` | `Hesekiel 19:4.9` | `Hesekiel 19:4-9` | `Ezekiel 19:4-9` | Wohin wurden die beiden jungen Löwen geführt (Hesekiel 19:4-9)? |
| `26_hesekiel.json` | `hes_147` | `Hesekiel 23:12; Hesekiel 23:14-16` | `Hesekiel 23:12-16` | `Ezekiel 23:12-16` | Mit wem buhlte Oholiba (Jerusalem) nach Hesekiel 23:12-16 in ihrer Hurerei? |
| `27_daniel.json` | `dan_018` | `Daniel 4:31-34` | `Daniel 4:34` | `Daniel 4:34` | Was tat Nebukadnezar, als sein Verstand zurückkehrte (Daniel 4:34)? |
| `29_joel.json` | `joe_008` | `Joel 3:2.12` | `Joel 3:2` | `Joel 3:2` | Wo versammelt der HERR die Heiden zum Gericht (Joel 3:2)? |
| `30_amos.json` | `am_019` | `Amos 7:2-6` | `Amos 7:2` | `Amos 7:2` | Wie bat Amos in Amos 7:2 um Verschonung für das Volk? |
| `30_amos.json` | `am_020` | `Amos 7:7-9` | `Amos 7:7-8` | `Amos 7:7-8` | Was hielt der Herr nach Amos 7:7 in seiner Hand? |
| `32_jona.json` | `jon_001` | `Jona 1:1-3` | `Jona 1:3` | `Jonah 1:3` | Wohin wollte Jona vor dem HERRN fliehen (Jona 1:3)? |
| `32_jona.json` | `jon_002` | `Jona 1:5-7` | `Jona 1:5` | `Jonah 1:5` | Was taten die Schiffsleute im Ungewitter (Jona 1:5)? |
| `32_jona.json` | `jon_005` | `Jona 2:4-7` | `Jona 2:6` | `Jonah 2:6` | Wie beschreibt Jona seine Not im Leibe des Fisches (Jona 2:6)? |
| `32_jona.json` | `jon_008` | `Jona 3:6-8` | `Jona 3:6` | `Jonah 3:6` | Wie reagierte der König von Ninive nach Jona 3:6? |
| `32_jona.json` | `jon_010` | `Jona 4:1-3` | `Jona 4:2` | `Jonah 4:2` | Warum zürnte Jona über die Verschonung Ninives (Jona 4:2)? |
| `32_jona.json` | `jon_012` | `Jona 4:10-11` | `Jona 4:11` | `Jonah 4:11` | Mit welcher Frage schließt das Buch Jona (Jona 4:11)? |
| `32_jona.json` | `jon_013` | `Jona 1:3; Jona 1:7; Jona 1:15; Jona 2:1; Jona 4:7` | `Jona 1:3` | `Jonah 1:3` | Bringe diese Ereignisse aus dem Buch Jona in die richtige Reihenfolge. |
| `33_micha.json` | `mi_019` | `Micha 7:1-6` | `Micha 7:2` | `Micah 7:2` | Wie klagt der Prophet in Micha 7:2 über die Menschen im Lande? |
| `33_micha.json` | `mi_020` | `Micha 7:7-8` | `Micha 7:8` | `Micah 7:8` | Was spricht der Prophet in Micha 7:8 gegen seine Feindin? |
| `34_nahum.json` | `nah_004` | `Nahum 2:3-4` | `Nahum 2:4` | `Nahum 2:4` | Wie schildert Nahum 2:4 den Ansturm der Wagen? |
| `34_nahum.json` | `nah_006` | `Nahum 2:11-13` | `Nahum 2:12` | `Nahum 2:12` | Mit welchem Tier beschreibt Nahum 2:12 die einstige Macht Ninives? |
| `34_nahum.json` | `nah_008` | `Nahum 3:8-10` | `Nahum 3:8` | `Nahum 3:8` | Welche Stadt hält Nahum 3:8 Ninive als warnendes Beispiel vor? |
| `34_nahum.json` | `nah_009` | `Nahum 3:18-19` | `Nahum 3:18` | `Nahum 3:18` | Mit welcher Klage an den König von Assur schließt Nahum 3:18? |
| `35_habakuk.json` | `hab_001` | `Habakuk 1:2-4` | `Habakuk 1:2` | `Habakkuk 1:2` | Womit beginnt Habakuk seine Klage (Habakuk 1:2)? |
| `35_habakuk.json` | `hab_002` | `Habakuk 1:5-6` | `Habakuk 1:6` | `Habakkuk 1:6` | Wen will der HERR nach Habakuk 1:6 erwecken? |
| `35_habakuk.json` | `hab_003` | `Habakuk 1:12-13` | `Habakuk 1:13` | `Habakkuk 1:13` | Welche Frage stellt Habakuk in Habakuk 1:13? |
| `35_habakuk.json` | `hab_008` | `Habakuk 3:3-4` | `Habakuk 3:3` | `Habakkuk 3:3` | Wie schildert Habakuk 3:3 das Erscheinen Gottes? |
| `36_zephanja.json` | `zef_001` | `Zephanja 1:2-3` | `Zephanja 1:3` | `Zephaniah 1:3` | Was kündigt Zephanja 1:3 zu Beginn an? |
| `36_zephanja.json` | `zef_004` | `Zephanja 2:1-3` | `Zephanja 2:3` | `Zephaniah 2:3` | Welchen Rat gibt Zephanja 2:3? |
| `36_zephanja.json` | `zef_005` | `Zephanja 2:4-9` | `Zephanja 2:9` | `Zephaniah 2:9` | Was geschieht mit Moab und Ammon (Zephanja 2:9)? |
| `36_zephanja.json` | `zef_007` | `Zephanja 3:1-4` | `Zephanja 3:3` | `Zephaniah 3:3` | Wie urteilt Zephanja 3:3 über die Führer Jerusalems? |
| `36_zephanja.json` | `zef_008` | `Zephanja 3:12-13` | `Zephanja 3:12` | `Zephaniah 3:12` | Was lässt der HERR nach Zephanja 3:12 übrig? |
| `37_haggai.json` | `hag_001` | `Haggai 1:2-4` | `Haggai 1:4` | `Haggai 1:4` | Was hielt Haggai 1:4 dem Volk vor? |
| `37_haggai.json` | `hag_003` | `Haggai 1:12-14` | `Haggai 1:12` | `Haggai 1:12` | Wer gehorchte dem Wort des HERRN nach Haggai 1:12? |
| `37_haggai.json` | `hag_005` | `Haggai 2:7-9` | `Haggai 2:9` | `Haggai 2:9` | Was kündigt der HERR für das zweite Haus an (Haggai 2:9)? |
| `40_matthaeus.json` | `mt_061` | `Matthäus 13:3-8; 13:18-23` | `Matthäus 13:3-23` | `Matthew 13:3-23` | Welcher Ackerboden brachte im Gleichnis vom Sämann Frucht hervor? |
| `40_matthaeus.json` | `mt_147` | `Matthäus 4:3; Matthäus 4:5-6; Matthäus 4:8-9` | `Matthäus 4:1-11` | `Matthew 4:1-11` | Bringe die drei Versuchungen Jesu nach Matthäus 4 in die richtige Reihenfolge. |
| `40_matthaeus.json` | `mt_148` | `Matthäus 26:26; Matthäus 26:36; Matthäus 26:47; Matthäus 27:11; Matthäus 27:35; Matthäus 28:6` | `Matthäus 26:26` | `Matthew 26:26` | Bringe diese Ereignisse der Leidensgeschichte Jesu in die richtige Reihenfolge. |
| `42_lukas.json` | `lk_039` | `Lukas 8:40-42; 8:49-56` | `Lukas 8:40-56` | `Luke 8:40-56` | Wie alt war die Tochter des Jairus, die Jesus vom Tode auferweckte? |
| `42_lukas.json` | `lk_125` | `Lukas 1:38; Lukas 2:7; Lukas 2:16; Matthäus 2:11; Matthäus 2:14` | `Lukas 1:38` | `Luke 1:38` | Bringe diese Ereignisse der Weihnachtsgeschichte in die richtige Reihenfolge. |
| `42_lukas.json` | `lk_126` | `Lukas 15:12; Lukas 15:15; Lukas 15:20; Lukas 15:23` | `Lukas 15:11-24` | `Luke 15:11-24` | Bringe die Stationen im Gleichnis vom verlorenen Sohn nach Lukas 15 in die richtige Reihenfolge. |
| `43_johannes.json` | `joh_109` | `Johannes 2:9; Johannes 4:50; Johannes 6:11; Johannes 9:7; Johannes 11:43` | `Johannes 2:11` | `John 2:11` | Bringe diese Zeichen Jesu im Johannesevangelium in die richtige Reihenfolge. |
| `43_johannes.json` | `joh_110` | `Johannes 20:14; Lukas 24:15; Johannes 20:19; Johannes 20:26` | `Johannes 20:19` | `John 20:19` | Bringe diese Erscheinungen des Auferstandenen in die richtige Reihenfolge. |
| `44_apostelgeschichte.json` | `apg_048` | `Apostelgeschichte 10:7-8; 10:19` | `Apostelgeschichte 10:19` | `Acts 10:19` | Wie viele Männer schickte Kornelius nach Joppe, um Petrus zu sich zu rufen? |
| `44_apostelgeschichte.json` | `apg_063` | `Apostelgeschichte 13:7; 13:12` | `Apostelgeschichte 13:7-12` | `Acts 13:7-12` | Welcher römische Statthalter auf Zypern kam durch das Wunder zum Glauben? |
| `44_apostelgeschichte.json` | `apg_073` | `Apostelgeschichte 15:20; 15:28-29` | `Apostelgeschichte 15:28-29` | `Acts 15:28-29` | Welche Enthaltungen wurden den gläubigen Heiden im Aposteldekret auferlegt? |
| `44_apostelgeschichte.json` | `apg_083` | `Apostelgeschichte 17:19; 17:22` | `Apostelgeschichte 17:19-22` | `Acts 17:19-22` | Auf welchem Felsenhügel hielt Paulus Seine bekannte Rede vor den Athenern? |
| `44_apostelgeschichte.json` | `apg_105` | `Apostelgeschichte 21:31-33; 23:26` | `Apostelgeschichte 23:26` | `Acts 23:26` | Welcher römische Oberst rettete Paulus vor der wütenden Volksmenge? |
| `44_apostelgeschichte.json` | `apg_123` | `Apostelgeschichte 25:13; 25:22` | `Apostelgeschichte 25:13-22` | `Acts 25:13-22` | Welcher König besuchte Cäsarea und wollte die Sache des Paulus hören? |
| `44_apostelgeschichte.json` | `apg_135` | `Apostelgeschichte 27:37; 27:44` | `Apostelgeschichte 27:37-44` | `Acts 27:37-44` | Wie viele Personen befanden sich insgesamt an Bord des gestrandeten Schiffes? |
| `44_apostelgeschichte.json` | `apg_145` | `Apostelgeschichte 2:4; Apostelgeschichte 7:59; Apostelgeschichte 9:18; Apostelgeschichte 10:44; Apostelgeschichte 15:6` | `Apostelgeschichte 1:8` | `Acts 1:8` | Bringe diese Ereignisse der Apostelgeschichte in die richtige Reihenfolge. |
| `45_roemer.json` | `roem_074` | `Römer 15:24; 15:28` | `Römer 15:24` | `Romans 15:24` | Welches ferne Reiseziel plante Paulus nach Seinem beabsichtigten Besuch in Rom? |
| `46_1_korinther.json` | `1kor_070` | `1. Korinther 14:33; 14:40` | `1. Korinther 14:40` | `1 Corinthians 14:40` | Welches goldene Schlussgebot gibt Paulus für die Gestaltung aller Gottesdienste? |
| `58_hebraeer.json` | `hebr_024` | `Hebräer 5:12-14` | `Hebräer 5:12` | `Hebrews 5:12` | Wessen sind die Unmündigen nach Hebräer 5:12 bedürftig geworden? |
| `58_hebraeer.json` | `hebr_028` | `Hebräer 6:13-14` | `Hebräer 6:13` | `Hebrews 6:13` | Bei wem schwor Gott dem Abraham die Verheißung (Hebräer 6:13)? |
| `58_hebraeer.json` | `hebr_032` | `Hebräer 7:2; 7:4` | `Hebräer 7:4` | `Hebrews 7:4` | Welchen Anteil gab Abraham dem Melchisedek von der Beute (Hebräer 7:4)? |
| `58_hebraeer.json` | `hebr_047` | `Hebräer 10:5-7` | `Hebräer 10:5` | `Hebrews 10:5` | Was hat Gott dem Sohne zubereitet nach Hebräer 10:5? |
| `58_hebraeer.json` | `hebr_053` | `Hebräer 11:5-6` | `Hebräer 11:5` | `Hebrews 11:5` | Welches Zeugnis empfing Henoch vor seiner Entrückung (Hebräer 11:5)? |
| `59_jakobus.json` | `jak_022` | `Jakobus 5:7-8` | `Jakobus 5:7` | `James 5:7` | Welches Vorbild der Geduld führt Jakobus in Jakobus 5:7 an? |
| `59_jakobus.json` | `jak_024` | `Jakobus 5:14-15` | `Jakobus 5:14` | `James 5:14` | Was sollen die Ältesten der Gemeinde mit einem Kranken tun (Jakobus 5:14)? |
| `59_jakobus.json` | `jak_025` | `Jakobus 5:16-18` | `Jakobus 5:17` | `James 5:17` | Welcher Prophet wird in Jakobus 5:17 als Beispiel für ein ernstes Gebet genannt? |
| `60_1_petrus.json` | `1petr_007` | `1. Petrus 2:4-6` | `1. Petrus 2:4` | `1 Peter 2:4` | Als was wird der Herr in 1. Petrus 2:4 beschrieben? |
| `60_1_petrus.json` | `1petr_009` | `1. Petrus 2:13-14` | `1. Petrus 2:13` | `1 Peter 2:13` | Wie sollen sich Gläubige menschlicher Ordnung unterordnen (1. Petrus 2:13)? |
| `61_2_petrus.json` | `2petr_005` | `2. Petrus 1:20-21` | `2. Petrus 1:21` | `2 Peter 1:21` | Wie entstand nach 2. Petrus 1:21 die Weissagung der Schrift? |
| `61_2_petrus.json` | `2petr_008` | `2. Petrus 2:7-8` | `2. Petrus 2:7` | `2 Peter 2:7` | Wen rettete Gott nach 2. Petrus 2:7 aus Sodom heraus? |
| `61_2_petrus.json` | `2petr_009` | `2. Petrus 2:15-16` | `2. Petrus 2:15` | `2 Peter 2:15` | Wer liebte den Lohn der Ungerechtigkeit nach 2. Petrus 2:15? |
| `62_1_johannes.json` | `1joh_018` | `1. Johannes 4:8; 4:16` | `1. Johannes 4:8` | `1 John 4:8` | Welche Aussage über das Wesen Gottes steht in 1. Johannes 4:8? |
| `66_offenbarung.json` | `off_002` | `Offenbarung 1:16; 1:20` | `Offenbarung 1:16` | `Revelation 1:16` | Was hielt der Verklärte in Seiner rechten Hand in der ersten Vision? |
| `66_offenbarung.json` | `off_081` | `Offenbarung 17:1; 17:3` | `Offenbarung 17:1-3` | `Revelation 17:1-3` | Wo sitzt die große Hure nach der Schau im siebzehnten Kapitel? |
| `66_offenbarung.json` | `off_094` | `Offenbarung 19:11; 19:13` | `Offenbarung 19:11-13` | `Revelation 19:11-13` | Welchen Namen trägt der siegreiche Reiter auf dem weißen Pferd? |
| `66_offenbarung.json` | `off_098` | `Offenbarung 20:3; 20:7` | `Offenbarung 20:3` | `Revelation 20:3` | Was geschieht mit Satan nach dem Ablauf der tausend Jahre? |
| `66_offenbarung.json` | `off_112` | `Offenbarung 2:1; Offenbarung 2:8; Offenbarung 2:12; Offenbarung 2:18` | `Offenbarung 2:1` | `Revelation 2:1` | Bringe die ersten vier Sendschreiben der Offenbarung in die richtige Reihenfolge. |
| `66_offenbarung.json` | `off_113` | `Offenbarung 6:2; Offenbarung 6:4; Offenbarung 6:5; Offenbarung 6:8` | `Offenbarung 6:2` | `Revelation 6:2` | Bringe die vier Reiter der ersten vier Siegel nach ihrer Pferdefarbe in die richtige Reihenfolge. |

## 5. Beibehaltene / neu verfasste Sacherklärungen (`explanationReviewed: true`)

Gemäß Vorgabe wurden Erklärungen nur dort gesetzt, wo ein echter sachlicher Mehrwert über den Bibelvers hinaus besteht (insbesondere antike Maße, Gewichte, Münzen, Bräuche oder Wortbedeutungen):

| Datei | questionId | Bibelstelle | Erklärung (DE) | Erklärung (EN) |
| :--- | :--- | :--- | :--- | :--- |
| `01_1_mose.json` | `1mose_271` | `1. Mose 37:28` | Josephs Verwerfung durch seine Brüder und der Verkauf für Silberlinge weist typologisch auf Jesus Christus hin, der von Seinem Volk verworfen und für dreißig Silberlinge verraten wurde [ref:Matthäus 26:15]. | Joseph's rejection by his brothers and sale for pieces of silver typifies Jesus Christ, who was rejected by His own people and betrayed for thirty pieces of silver [ref:Matthew 26:15]. |
| `01_1_mose.json` | `1mose_272` | `1. Mose 14:18-20` | Der Hebräerbrief deutet Melchisedeks Erscheinen ohne verzeichneten Stammbaum als Vorbild auf das ewige Priestertum des Sohnes Gottes [ref:Hebräer 7:1-3]. | The Epistle to the Hebrews interprets Melchizedek's appearance without recorded genealogy as a type of the eternal priesthood of the Son of God [ref:Hebrews 7:1-3]. |
| `01_1_mose.json` | `1mose_273` | `1. Mose 22:6` | Dass Isaak das Holz für sein eigenes Brandopfer auf den Berg trug, wird als Vorausbeschattung von Christus gedeutet, der Sein Kreuz nach Golgatha trug [ref:Johannes 19:17]. | Isaac carrying the wood for his own burnt offering up the mountain foreshadows Christ bearing His cross to Golgotha [ref:John 19:17]. |
| `01_1_mose.json` | `1mose_274` | `1. Mose 49:10` | Der Name Schilo in Jakobs Segensspruch über Juda weist prophetisch auf den messianischen Friedensfürsten hin [ref:1. Mose 49:10; Jesaja 9:5]. | The name Shiloh in Jacob's blessing upon Judah prophetically points to the messianic Prince of Peace [ref:Genesis 49:10; Isaiah 9:6]. |
| `01_1_mose.json` | `1mose_275` | `1. Mose 35:18` | Die beiden Namen spiegeln die zwei Aspekte des Messias wider: den leidenden Schmerzensmann [ref:Jesaja 53:3] und den zur Rechten Gottes erhöhten Herrscher [ref:Hebräer 1:3]. | The two names reflect the two aspects of the Messiah: the suffering Man of Sorrows [ref:Isaiah 53:3] and the exalted Ruler at God's right hand [ref:Hebrews 1:3]. |
| `01_1_mose.json` | `1mose_276` | `1. Mose 22:13` | Der anstelle Isaaks geopferte Widder ist ein alttestamentliches Vorbild auf das stellvertretende Sühnopfer Jesu Christi [ref:Johannes 1:29; Hebräer 10:10-14]. | The ram sacrificed in Isaac's stead is an Old Testament type of the substitutionary sacrifice of Jesus Christ [ref:John 1:29; Hebrews 10:10-14]. |
| `01_1_mose.json` | `1mose_277` | `1. Mose 40:21-22` | Die zwei Gefährten Josephs erinnern typologisch an die zwei Übeltäter am Kreuz, von denen einer Begnadigung empfing und der andere starb [ref:Lukas 23:39-43]. | Joseph's two fellow prisoners typologically foreshadow the two thieves crucified with Christ, one receiving mercy and the other condemned [ref:Luke 23:39-43]. |
| `01_1_mose.json` | `1mose_278` | `1. Mose 24:2-4` | Der namenlose Knecht, der eine Braut für den Sohn sucht und reich beschenkt, wird typologisch als Bild auf das Wirken des Heiligen Geistes gesehen [ref:Johannes 16:13-14]. | The unnamed servant seeking and adorning a bride for the son is viewed typologically as a picture of the Holy Spirit's ministry [ref:John 16:13-14]. |
| `01_1_mose.json` | `1mose_279` | `1. Mose 6:16` | Die einzige rettende Tür der Arche gilt typologisch als Hinweis auf Jesus Christus als die einzige Tür zum Heil [ref:Johannes 10:9; 1. Petrus 3:20-21]. | The single door of salvation in the ark is seen typologically as pointing to Jesus Christ as the only door of salvation [ref:John 10:9; 1 Peter 3:20-21]. |
| `01_1_mose.json` | `1mose_280` | `1. Mose 28:12` | Jesus bezieht die Himmelsleiter im Johannesevangelium direkt auf sich selbst als den Mittler zwischen Himmel und Erde [ref:Johannes 1:51]. | In the Gospel of John, Jesus applies Jacob's ladder directly to Himself as the Mediator between heaven and earth [ref:John 1:51]. |
| `01_1_mose.json` | `1mose_282` | `1. Mose 15:9-18` | Das Hindurchschreiten Gottes allein bezeugt Seinen einseitigen, bedingungslosen Gnadenbund mit Abraham [ref:1. Mose 15:17; Hebräer 6:13-18]. | God alone passing through the pieces signifies His unilateral, unconditional covenant of grace with Abraham [ref:Genesis 15:17; Hebrews 6:13-18]. |
| `01_1_mose.json` | `1mose_283` | `1. Mose 41:40-44` | Josephs Erniedrigung in die Tiefe und anschließende Erhöhung über ganz Ägypten spiegelt Christi Erniedrigung und Verherrlichung wider [ref:Philipper 2:8-11]. | Joseph's descent into humiliation followed by exaltation over Egypt mirrors the humiliation and exaltation of Jesus Christ [ref:Philippians 2:8-11]. |
| `01_1_mose.json` | `1mose_284` | `1. Mose 48:13-19` | Jakob segnet Ephraim vor Manasse und kreuzt prophetisch die Hände, was Gottes freie Gnadenwahl vor menschlicher Herkunft darstellt [ref:Römer 9:11-12]. | Jacob crosses his hands to bless younger Ephraim over Manasseh, illustrating God's election of grace above human seniority [ref:Romans 9:11-12]. |
| `01_1_mose.json` | `1mose_285` | `1. Mose 41:45` | Dass Joseph in der Zeit seiner Verwerfung durch seine Brüder eine heidnische Braut nahm, deutet typologisch auf die Errettung der Heiden hin [ref:Epheser 3:6]. | Joseph taking a Gentile bride during his rejection by his brethren typologically points to the calling of the Gentiles into the church [ref:Ephesians 3:6]. |
| `01_1_mose.json` | `1mose_286` | `1. Mose 3:21` | Die Fellröcke setzten das erste Blutvergießen eines Opfers voraus, um die Schuld des Menschen stellvertretend zu bedecken [ref:Hebräer 9:22]. | The coats of skins required the shedding of animal blood to cover man's guilt, foreshadowing Christ's covering righteousness [ref:Hebrews 9:22]. |
| `01_1_mose.json` | `1mose_287` | `1. Mose 4:8-10` | Jesus bezeichnet Abel als den ersten unschuldig ermordeten Gerechten [ref:Matthäus 23:35], dessen Blut jedoch nach Vergeltung rief [ref:Hebräer 12:24]. | Jesus calls Abel the first innocent martyr [ref:Matthew 23:35], whose blood cried for vengeance, unlike Christ's blood of grace [ref:Hebrews 12:24]. |
| `01_1_mose.json` | `1mose_299` | `1. Mose 14:18-19` | Abrahams Zehntabgabe an Melchisedek bezeugt laut Hebräerbrief die Überlegenheit dieses Priestertums über das levitische Priestertum [ref:Hebräer 7:4-7]. | Abraham giving tithes to Melchizedek demonstrates the superiority of Melchizedek's priesthood over the Levitical priesthood [ref:Hebrews 7:4-7]. |
| `02_2_mose.json` | `ex_150` | `2. Mose 16:16` | Ein Gomer (oder Omer) entspricht etwa 2,2 Litern bzw. dem zehnten Teil eines Epha (2. Mose 16:36). | An omer is approximately 2.2 liters, or the tenth part of an ephah (Exodus 16:36). |
| `02_2_mose.json` | `ex_246` | `2. Mose 30:13-15` | Ein Schekel des Heiligtums wog etwa 11,4 Gramm Silber; zwanzig Gera bildeten einen Schekel. | A shekel of the sanctuary was approximately 11.4 grams of silver; twenty gerahs made a shekel. |
| `02_2_mose.json` | `ex_304` | `2. Mose 38:24` | Ein biblisches Talent wog rund 30 bis 34 Kilogramm (entsprechend 3000 Schekeln). | A biblical talent weighed approximately 30 to 34 kilograms (corresponding to 3,000 shekels). |
| `03_3_mose.json` | `lev_030` | `3. Mose 5:11` | Ein Epha entspricht etwa 22 Litern; ein Zehntel-Epha war somit rund 2,2 Liter Feinmehl als Tagesration eines einfachen Mannes. | An ephah is approximately 22 liters; the tenth part of an ephah was about 2.2 liters of fine flour (the daily ration of a poor man). |
| `03_3_mose.json` | `lev_171` | `3. Mose 27:3` | Ein heiliger Schekel wog etwa 11,4 Gramm Silber; zwanzig Gera bildeten einen Schekel (3. Mose 27:25). | A shekel of the sanctuary was approximately 11.4 grams of silver; twenty gerahs made a shekel (Leviticus 27:25). |
| `03_3_mose.json` | `lev_173` | `3. Mose 27:15-19` | Ein Homer (Chomer) fasste etwa 220 Liter Getreidesaat; fünfzig Schekel Silber entsprachen rund 570 Gramm Silber. | An homer held approximately 220 liters of barley seed; fifty shekels of silver corresponded to about 570 grams of silver. |
| `04_4_mose.json` | `num_021` | `4. Mose 3:47` | Ein heiliger Schekel wog etwa 11,4 Gramm Silber (entspricht 20 Gera). Fünf Schekel entsprachen somit rund 57 Gramm Silber je Erstgeborenem. | A sanctuary shekel was about 11.4 grams of silver (equal to 20 gerahs). Five shekels amounted to approximately 57 grams of silver per firstborn. |
| `04_4_mose.json` | `num_031` | `4. Mose 5:15` | Ein Epha entspricht rund 22 Litern, ein Zehntel somit etwa 2,2 Litern Gerstenmehl. Das Eifersuchtsopfer wurde ohne Öl und ohne Weihrauch dargebracht. | An ephah equals about 22 liters, so a tenth deal is about 2.2 liters of barley meal. The jealousy offering was brought without oil or frankincense. |
| `04_4_mose.json` | `num_046` | `4. Mose 7:13` | Nach dem heiligen Schekel (ca. 11,4 Gramm) wog die Schüssel rund 1,5 kg Silber und das Sprengbecken etwa 800 Gramm Silber. | According to the sanctuary shekel (about 11.4 grams), the charger weighed around 1.5 kg of silver and the bowl about 800 grams of silver. |
| `05_5_mose.json` | `dtn_099` | `5. Mose 15:1-2` | Das Erlassjahr (Schemitta) fand alle sieben Jahre statt. Israelitischen Schuldnern wurden alle Darlehensschulden vollständig erlassen. | The year of release (Shemittah) occurred every seven years. Debts owed by fellow Israelites were fully released. |
| `05_5_mose.json` | `dtn_154` | `5. Mose 22:28-29` | Fünfzig Silberschekel entsprachen etwa 570 Gramm Silber als festgesetztes Brautgeld an den Brautvater. | Fifty shekels of silver amounted to approximately 570 grams of silver as the established dowry paid to the father. |
| `06_josua.json` | `jos_016` | `Josua 3:4` | Zweitausend Ellen entsprechen einer Wegstrecke von etwa 900 bis 1000 Metern. | Two thousand cubits corresponds to an ancient distance of approximately 900 to 1,000 metres (about half a mile). |
| `07_richter.json` | `ri_055` | `Richter 8:24-27` | Das Ephod war ursprünglich ein priesterliches Schulterkleid zur Befragung Gottes. Gideons goldenes Kultobjekt in Ophra führte Israel jedoch zur Abgötterei. | An ephod was originally a priestly garment used in seeking divine counsel. However, Gideon's golden object set up in Ophrah became an idolatrous snare unto Israel. |
| `08_rut.json` | `rut_015` | `Rut 2:20` | Ein Epha war ein altes biblisches Hohlmaß für Getreide und entsprach etwa 20 bis 22 Litern (Rut 2:17). | An ephah was an ancient biblical dry measure for grain, equal to about 20 to 22 liters (Ruth 2:17). |
| `08_rut.json` | `rut_025` | `Rut 4:7-8` | Das Ausziehen des Schuhs war in Israel ein altes Rechtszeichen, um den Verzicht auf das Betretungs- und Erbrecht öffentlich zu bezeugen (Rut 4:7-8). | Plucking off the shoe was an ancient custom in Israel to openly attest the relinquishment of property and right of redemption (Ruth 4:7-8). |
| `09_1_samuel.json` | `1sam_070` | `1. Samuel 17:4` | Sechs Ellen und eine Handbreit entsprechen einer Körpergröße von etwa 2,90 bis 3,00 Metern (eine Elle ca. 45–50 cm, eine Spanne ca. 22 cm). | Six cubits and a span corresponds to an extraordinary height of approximately 9 feet 9 inches (nearly 3 metres). |
| `10_2_samuel.json` | `2sam_045` | `2. Samuel 14:25-26` | Zweihundert Lot (nach dem königlichen Gewicht; im Hebräischen 200 Schekel) entsprechen einem beachtlichen Gewicht von rund 2,3 Kilogramm [ref:2. Samuel 14:26]. | Two hundred shekels after the king's weight corresponds to about 2.3 kilograms (around 5 pounds) of hair [ref:2 Samuel 14:26]. |
| `11_1_koenige.json` | `1kön_038` | `1. Könige 16:23-24` | Zwei Zentner Silber (im Hebräischen 2 Talente) entsprachen etwa 60 bis 68 Kilogramm Feinsilber [ref:1. Könige 16:24]. | Two talents of silver corresponded to about 60 to 68 kilograms (roughly 130 to 150 pounds) of silver [ref:1 Kings 16:24]. |
| `12_2_koenige.json` | `2kön_016` | `2. Könige 15:19-20` | Tausend Zentner Silber (im Hebräischen 1000 Talente) entsprachen einer gewaltigen Tributsumme von rund 30 bis 34 Tonnen Silber [ref:2. Könige 15:19]. | A thousand talents of silver was a vast tribute of roughly 30 to 34 metric tons (about 75,000 pounds) of silver [ref:2 Kings 15:19]. |
| `12_2_koenige.json` | `2kön_051` | `2. Könige 7:1` | Ein hebräisches Maß (Sea; Luther: Scheffel) fasste etwa 7,3 Liter Getreide, das nun zu einem spottbilligen Preis von einem Silberling verkauft wurde [ref:2. Könige 7:1]. | A measure (Hebrew seah) contained about 7.3 litres (roughly 1.6 gallons) of grain, sold for a single shekel at the gate [ref:2 Kings 7:1]. |
| `13_1_chronik.json` | `1chr_020` | `1. Chronik 20:1-2` | Ein Zentner Gold (im Hebräischen 1 Talent) entsprach einem Gewicht von rund 30 bis 34 Kilogramm Feingold [ref:1. Chronik 20:2]. | A talent of gold corresponded to a weighty crown of about 30 to 34 kilograms (roughly 66 to 75 pounds) of gold [ref:1 Chronicles 20:2]. |
| `13_1_chronik.json` | `1chr_023` | `1. Chronik 21:22-25` | Sechshundert Lot Gold entsprachen etwa 6,8 bis 7 Kilogramm Gold [ref:1. Chronik 21:25]. | Six hundred shekels of gold by weight was approximately 6.8 to 7 kilograms (about 15 pounds) of gold [ref:1 Chronicles 21:25]. |
| `13_1_chronik.json` | `1chr_032` | `1. Chronik 29:3-5` | 3.000 Zentner (Talente) Gold entsprachen etwa 100 Tonnen Feingold [ref:1. Chronik 29:4]. | 3,000 talents of gold corresponded to approximately 100 metric tons of gold [ref:1 Chronicles 29:4]. |
| `14_2_chronik.json` | `2chr_053` | `2. Chronik 8:18` | Die Knechte Hurams holten mit Salomos Knechten 450 Zentner Gold aus Ophir (KJV: 450 talents of gold, ca. 15 Tonnen Feingold) [ref:2. Chronik 8:18]. | The servants of Huram with Solomon's servants brought 450 talents of gold from Ophir (approx. 15 metric tons) [ref:2 Chronicles 8:18]. |
| `16_nehemia.json` | `neh_030` | `Nehemia 10:32` | Die Gemeinde verpflichtete sich jährlich zum dritten Teil eines Schekels (ca. 3,8 g Silber) für den Dienst im Tempel [ref:Nehemia 10:32]. | The congregation charged themselves yearly with the third part of a shekel (approx. 3.8 g of silver) for the temple service [ref:Nehemiah 10:32]. |
| `17_esther.json` | `est_008` | `Esther 3:9` | Haman erbot sich, zehntausend Zentner Silber (KJV: 10,000 talents of silver, ca. 340 Tonnen) in die Schatzkammer zu wägen [ref:Esther 3:9]. | Haman offered to pay ten thousand talents of silver (approx. 340 metric tons) into the king's treasuries [ref:Esther 3:9]. |
| `18_hiob.json` | `hi_029` | `Hiob 42:11` | Jeder gab ihm ein Stück Geld (hebr. Kesita, ein altes Gewichts- oder Geldstück) und einen goldenen Ring bzw. Stirnband [ref:Hiob 42:11]. | Every man gave him a piece of money (Heb. kesitah, an ancient uncoined weight of silver) and an earring of gold [ref:Job 42:11]. |
| `57_philemon.json` | `phlm_002` | `Philemon 1:11-16` | Der Name Onesimus bedeutet «nützlich» oder «ersprießlich». Paulus spielt in Philemon 1:11 darauf an: Einst war er unnütz, nun aber nützlich im Herrn. | The name Onesimus signifies 'profitable' or 'useful'. Paul plays upon this in Philemon 1:11: which in time past was to thee unprofitable, but now profitable to thee and to me. |
| `66_offenbarung.json` | `off_028` | `Offenbarung 6:6` | Ein Maß (griech. Chönix, ca. 1 Liter) entsprach dem täglichen Grundbedarf an Weizen; ein Denar war der übliche Tageslohn eines Arbeiters [ref:Offenbarung 6:6]. | A measure (Greek choenix, about one quart) was a worker's daily wheat ration; a penny (denarius) was the standard daily wage for a labourer [ref:Revelation 6:6]. |

## 6. Punkte zur menschlichen Entscheidung und Übersetzungsbesonderheiten

1. **Wortlaut der deutschen Bibelquelle (`bible_data.json`):**
   - In `01_1_mose.json` bis `05_5_mose.json` und `40_matthaeus.json` bis `66_offenbarung.json` wurden konsequent die Begriffe der hinterlegten Schlachter-1951-Textfassung verwendet (einschließlich `Erdland`, `Erdland Gosen`, `Erdland Kanaan`, `Erdland Midian`, `Strohhäcksel`, `Ziegelstreichen`, `Ofenruß`, `Blattern`, `Sühnedeckel`, `Seehundsfellen`, `wertschätzen`, `in den himmlischen Regionen`, `Lukas, der geliebte Heiler`), während für Gottesnamen und Grundbegriffe Standarddeutsch (`Gott`, `der HERR`, `Ägypten`, `Frieden`) statt der Transkriptionen `Älohim`, `JHWH`, `Mizraim`, `Schalom` genutzt wird.
   - In `06_josua.json` bis `39_maleachi.json` wurde durchgehend der exakte Wortlaut der Luther-1912-Übersetzung aus `bible_data.json` eingesetzt.
2. **Abweichungen zwischen Luther 1912 / Schlachter 1951 und King James Version (1769):**
   - Wo der deutsche Bibeltext und die KJV unterschiedliche Begriffe verwenden (z. B. 2. Mose 26:14 `Seehundsfellen` vs. KJV `badgers' skins`; Prediger 3:11 `lässt ihr Herz sich ängsten, wie es gehen solle in der Welt` vs. KJV `he hath set the world in their heart`; Hohelied 2:2 `Rose unter den Dornen` vs. KJV `lily among thorns`; Hosea 3:2 `anderthalb Scheffel Gerste` vs. KJV `an homer of barley, and an half homer of barley`), folgt die deutsche Frage exakt dem deutschen Bibeltext und die englische Frage exakt dem KJV-Text.
   - Verszählungsunterschiede zwischen der deutschen Vorlage und der KJV (u. a. in 2. Mose 21:37 / 22:1, 4. Mose 17 / 16, 4. Mose 30:1 / 29:40, 5. Mose 13:1 / 12:32, 5. Mose 28:69 / 29:1, 1. Samuel 21:1 / 20:42, 1.Samuel 24:1 / 23:29, 1. Könige 4-5 und 22, Hesekiel 21, Daniel 3-4 und 6) wurden in `en/` über den Versinhalt zugeordnet.
   - Detaillierte Einzelfallhinweise je Buch finden sich im Abschnitt `## Zur menschlichen Entscheidung` des jeweiligen Berichts `reports/<datei>.md`.
