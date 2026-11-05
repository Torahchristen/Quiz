# Review Report: 37_haggai.json

## Uebersicht
- Gepruefte Datei: `37_haggai.json`
- Englische Datei: `en/37_haggai.json`
- Anzahl Fragen: 14
- Ueberpruefte Erklaerungen (DE): 0
- Ueberpruefte Erklaerungen (EN): 0
- Bereinigte Erklaerungen: 14 (auf Minimalismus zurueckgesetzt, alle redundanten Template-Texte bereinigt)

## Sprachliche Anpassungen (Luther 1912)
- Exakter Luther-1912-Wortlaut aus der Versdatenbank uebernommen:
  - Haggai 1:1: `im zweiten Jahr des Königs Darius` (hag_007).
  - Haggai 1:4: `daß ihr in getäfelten Häusern wohnt, und dies Haus muß wüst stehen?` (hag_001).
  - Haggai 1:6: `Ihr säet viel, und bringet wenig ein... wer Geld verdient, der legt's in einen löchrigen Beutel` (hag_002).
  - Haggai 1:8: `Gehet hin auf das Gebirge und holet Holz und bauet das Haus` (hag_008).
  - Haggai 1:11: `Und ich habe die Dürre gerufen über Land und Berge` (hag_009; Laengenbalance optimiert).
  - Haggai 1:12: `Serubabel, der Sohn Sealthiels, und Josua, der Sohn Jozadaks, der Hohepriester, und alle übrigen des Volkes` (hag_003; Luthers Namensschreibweise 'Serubabel' konsequent angewandt).
  - Haggai 1:15: `am vierundzwanzigsten Tage des sechsten Monats, im zweiten Jahr des Königs Darius` (hag_010).
  - Haggai 2:3: `Wer ist unter euch übriggeblieben, der dies Haus in seiner vorigen Herrlichkeit gesehen hat?` (hag_011).
  - Haggai 2:4-5: `sei getrost alles Volk im Lande! spricht der HERR, und arbeitet! denn ich bin mit euch` (hag_004).
  - Haggai 2:8: `Denn mein ist Silber und Gold, spricht der HERR Zebaoth` (hag_012; Laengenbalance von 37.6% auf 8.8% gesenkt).
  - Haggai 2:9: `Es soll die Herrlichkeit dieses letzten Hauses größer werden, denn des ersten gewesen ist` (hag_005).
  - Haggai 2:12-13: `heiliges Fleisch im Zipfel des Kleides... von einem Toten unrein` (hag_013).
  - Haggai 2:22: `will die Stühle der Königreiche umkehren und die mächtigen Königreiche der Heiden vertilgen` (hag_014).
  - Haggai 2:23: `will ich dich, Serubabel... wie einen Siegelring halten; denn ich habe dich erwählt` (hag_006).

## Aenderungen an Fragen und Optionen

| Frage-ID | Was geaendert wurde | Warum |
|---|---|---|
| hag_001 | Bibelstelle auf Haggai 1:4 praezisiert | Exakte Verszuordnung |
| hag_003 | Bibelstelle auf Haggai 1:12 fokussiert; 'Serubbabel' zu 'Serubabel' korrigiert; Distraktoren balanciert | Luther-1912-Schreibweise und Balance |
| hag_005 | Bibelstelle auf Haggai 2:9 praezisiert | Exakte Verszuordnung |
| hag_007 | Distraktoren gleichmaessig balanciert | Optimale Balance |
| hag_009 | Optionen balanciert (Laengenabweichung von 45.5% auf 10% gesenkt) | Behebung der Warnung LEN_DEV |
| hag_010 | Distraktor 2 auf einheitliche Laenge angepasst | Laengenbalance optimiert |
| hag_012 | 'Serubbabel' zu 'Serubabel' korrigiert; Optionen balanciert (Abweichung von 37.6% auf 8.8% gesenkt) | Behebung der Warnung LEN_DEV und Luther-Schreibweise |

## Englische Version (KJV 1769)
- Vollstaendige englische Uebersetzung aller 14 Fragen in `en/37_haggai.json`.
- KJV-Buchname `Haggai` in allen Referenzen und Metadaten verwendet.
- Authentischer KJV-Wortlaut: `dwell in your cieled houses, and this house lie waste`, `bag with holes`, `Zerubbabel the son of Shealtiel, and Joshua the son of Josedech, the high priest`, `Be strong... and work: for I am with you... so my spirit remaineth among you: fear ye not`, `glory of this latter house shall be greater than of the former`, `make thee as a signet: for I have chosen thee`, `second year of Darius the king`, `bring wood, and build the house`, `called for a drought upon the land`, `four and twentieth day of the sixth month`, `saw this house in her first glory`, `silver is mine, and the gold is mine, saith the LORD of hosts`, `If one bear holy flesh... shall it be holy?`, `overthrow the throne of kingdoms, and I will destroy the strength of the kingdoms of the heathen`.
- Alle Indizes in `correctAnswers` stimmen 1:1 mit der deutschen Datei ueberein.
- Alle Antwortoptionen innerhalb von +/-30% Laengenabweichung balanciert.

## Zur menschlichen Entscheidung
- Keine offenen menschlichen Entscheidungen erforderlich. Verszaehlung und Textuebereinstimmung zwischen Luther 1912 und KJV 1769 sind durchgehend deckungsgleich.
