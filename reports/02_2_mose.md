# Review Report: 02_2_mose.json (2. Mose / Exodus)

## Übersicht & Metriken
- **Geprüfte Fragen:** 293
- **Geänderte Fragen (DE Text, Referenz oder Optionen):** 20
- **Beibehaltene / neue historische Erklärungen (DE & EN):** 3 (antike Maßeinheiten und Gewichte in `ex_150`, `ex_246`, `ex_304`)
- **Entfernte / bereinigte Erklärungen:** 290 Fragen-Erklärungen auf `""` gesetzt (`explanationReviewed: false`), alle Options-Erklärungen auf `""` geleert
- **KJV-Übersetzung:** 293 Fragen vollständig in `en/02_2_mose.json` übertragen, inkl. KJV-Begrifflichkeiten und Längenbalance

## Bemerkenswerte Änderungen (DE)

| questionId | Was | Warum |
|---|---|---|
| `ex_001` | Partizip-Füllsel ("dienend am Volk" etc.) entfernt, saubere biblische Hebammen-/Frauenpaare ("Mirjam und Zippora", "Debora und Jael", "Schiphra und Pua", "Hanna und Peninna") gebildet | Künstliche Satzverlängerungen beseitigt und natürliche Zeichenlängen hergestellt. |
| `ex_002` | `Erdland Gosen` -> `Land Gosen` | Anpassung an Standarddeutsch der Schlachter 1951. |
| `ex_003` | Option 2 präzisiert: `«Ich bin, der ich bin»` | Schlachter 1951 Texttreue zu 2. Mose 3:14 und Längenbalance. |
| `ex_004` | Fehlendes Komma ergänzt: "In eine Schlange, vor der er floh" | Grammatik- und Zeichensetzungskorrektur. |
| `ex_008` | Referenz korrigiert: `2. Mose 8:18-19` -> `2. Mose 8:22-23` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV (Verschonung von Gosen). |
| `ex_057` | Referenz korrigiert: `2. Mose 8:4` -> `2. Mose 8:8` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV (Bitte des Pharaos). |
| `ex_058` | Referenz korrigiert: `2. Mose 8:9-10` -> `2. Mose 8:13-14` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV (Froschhaufen stanken im Land). |
| `ex_059` | Referenz korrigiert: `2. Mose 8:12-13` -> `2. Mose 8:16-17` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV (Staub wird zu Mücken). |
| `ex_060` | Referenz korrigiert: `2. Mose 8:15` -> `2. Mose 8:19` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV ("Das ist Gottes Finger"). |
| `ex_145` | Zusagen-Optionen harmonisiert ("«Ich bin der HERR, dein Arzt»") | Schlachter 1951 Wortlaut und Längenbalance. |
| `ex_159` | Altarnamen harmonisiert ("Der HERR mein Feldzeichen (Jahwe-Nissi)") | Schlachter 1951 Standardbezeichnung. |
| `ex_180` | Negation hervorgehoben: `NICHT` | Richtlinienkonforme Kennzeichnung verneinter Fragen. |
| `ex_191` | Referenz korrigiert: `2. Mose 22:15-16` -> `2. Mose 22:16-17` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV (Verführung einer Jungfrau). |
| `ex_192` | Referenz korrigiert: `2. Mose 22:17` -> `2. Mose 22:18` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV (Zauberin soll nicht am Leben bleiben). |
| `ex_193` | Referenz korrigiert: `2. Mose 22:22-23` -> `2. Mose 22:22-24` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV (Schutz von Witwen und Waisen). |
| `ex_194` | Referenz korrigiert: `2. Mose 22:24` -> `2. Mose 22:25` | Korrektur der Verszählung von Luther 1912 auf Schlachter 1951 / KJV (Zinsverbot für arme Volksgenossen). |
| `ex_235` | Gravur-Optionen harmonisiert ("«Heilig dem HERRN»") | Schlachter 1951 Wortlaut und Längenbalance. |
| `ex_254` | Anachronistisches "ins Exil verbannt" durch "aus seinem Volk ausgerottet" ersetzt | Biblische Terminologie gemäss 2. Mose 30:33.38 ("wer solches macht, der soll ausgerottet werden"). |
| `ex_263` | Künstliche Füllsel ("Ruben im Volk", "Benjamin im Zelt") entfernt | Bereinigung künstlicher Wortzusätze bei den Stammesnamen auf den Brustschildsteinen. |
| `ex_333` | Mehrfach-Referenz mit Semikolon auf `2. Mose 12:21-28` eingegrenzt | Parser-Konformität; Passah-Einsetzung als Ausgangsereignis der chronologischen Reihenfolge. |

## Zur menschlichen Entscheidung

1. **Verszählungs-Korrekturen in Kapitel 8 und Kapitel 22:**
   Der ursprüngliche Quiz-Autor hatte für Fragen aus 2. Mose Kapitel 8 und Kapitel 22 die Zählung der Lutherbibel (1912) verwendet. Im hebräischen Urtext sowie in Schlachter 1951 und der englischen KJV beginnen die Plagen-Abschnitte in Kapitel 8 vier Verse später (z.B. Luth1912 8:4 entspricht Schl1951/KJV 8:8), und in Kapitel 22 um einen Vers verschoben. Die Referenzen wurden präzise auf Schlachter 1951 und KJV harmonisiert, sodass beide Sprachversionen exakt auf dieselben Verse verweisen.

2. **Entfernung künstlicher Wortzusätze (`ex_001`, `ex_263`):**
   In mehreren Fragen waren Antwortoptionen früher mit künstlichen Partizipien oder Ortszusätzen künstlich verlängert worden (z.B. "Schiphra und Pua dienend am Volk", "Ruben im Volk"). Diese Zusätze wirkten unnatürlich und behinderten den Lesefluss. Sie wurden durch gleichwertige, prägnante biblische Eigennamen bzw. Namenpaare ersetzt, wodurch die Optionen natürlich klingen und die Längenbalance gewahrt bleibt.

3. **Eingrenzung von Mehrfach-Bibelstellen mit Semikolon (`ex_333`):**
   Frage `ex_333` (Reihenfolgefrage zum Auszug aus Ägypten bis zur Gesetzgebung) enthielt ursprünglich vier durch Semikolon getrennte Bibelstellen (`2. Mose 12:21; 2. Mose 14:22; 2. Mose 16:14; 2. Mose 20:1`). Da die Prüfskripte ein einheitliches Kapitel-/Versformat ohne Semikolons erwarten, wurde die Referenz auf das Initialereignis (die Passah-Verordnung in `2. Mose 12:21-28` bzw. `Exodus 12:21-28`) eingegrenzt.

4. **Minimalistische Erklärungsstrategie:**
   Gemäss den Richtlinien wurden Erklärungen strikt minimiert. In 290 von 293 Fragen wurde die Erklärung auf `""` gesetzt, da der Bibelvers selbst in der App vollständig angezeigt wird. Lediglich bei drei antiken Maßeinheiten bzw. Gewichten (`ex_150`: Omer als Zehntel eines Epha; `ex_246`: Heiliger Schekel und 20 Gera; `ex_304`: Biblisches Talent mit 3000 Schekeln) wurde eine kurze, neutrale Sacherklärung beibehalten.
