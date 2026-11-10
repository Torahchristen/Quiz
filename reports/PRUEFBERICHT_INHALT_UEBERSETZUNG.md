# Prüfbericht: Inhalt und Übersetzung aller Quizfragen

> **Geprüfter Stand:** Branch `review-and-english`, Commit `e4a30a5` – verglichen mit `main`  
> **Grundtext DE:** `BibelQuiz/assets/bible_data.json` · **Grundtext EN:** `Quiz/sources/kjv` (KJV)  
> **Maschinenlesbar:** [`PRUEFBEFUNDE.json`](./PRUEFBEFUNDE.json)

> [!TIP]
> **Status: umgesetzt.** Alle Befunde wurden korrigiert; die Gegenüberstellung alt → neu steht in [`KORREKTUREN_UMSETZUNG.md`](./KORREKTUREN_UMSETZUNG.md). Der Bericht unten zeigt den Stand **vor** der Korrektur.

## Inhalt

1. [Ergebnis auf einen Blick](#ergebnis-auf-einen-blick)
2. [Kernbefunde](#kernbefunde)
3. [Übersicht nach Datei](#übersicht-nach-datei)
4. [🔴 Schwere Fehler (123)](#schwere-fehler)
5. [🟠 Mittlere Fehler (120)](#mittlere-fehler)
6. [🟡 Kleinere Fehler (597)](#kleinere-fehler)
7. [Zentral geprüft: Namen und Versbereiche](#zentral-geprüft-namen-und-versbereiche)
8. [Vorgehen und Legende](#vorgehen-und-legende)

---

## Ergebnis auf einen Blick

| | Anzahl |
| :-- | --: |
| Inhaltlich geprüfte Fragen (DE + EN) | **4754** von 4754 |
| Bestätigte Befunde gesamt | **840** |
| 🔴 schwer – Lösung falsch, mehrdeutig oder Frage unbrauchbar | **123** |
| 🟠 mittel – DE/EN inhaltlich abweichend, Faktenfehler | **120** |
| 🟡 klein – Wortlaut, Sprache, abweichende Distraktoren | **597** |
| Von der Gegenprüfung verworfen | 11 |

**Woher kommen die Fehler?**

| Ursprung | alle | davon 🔴 schwer |
| :-- | --: | --: |
| in der neuen EN-Fassung entstanden | 500 | 87 |
| durch die Überarbeitung entstanden | 209 | 28 |
| war schon in `main` | 124 | 8 |
| unbekannt | 7 | 0 |

**Nach Art:** DE/EN weicht ab 447 · Sprachfehler 125 · Mehrere richtig 73 · Inhaltlicher Fehler 72 · Falsche Lösung 55 · KJV-Wortlaut 38 · Bibelstelle 27 · Sonstiges 3

> [!NOTE]
> **Formal ist alles in Ordnung:** DE und EN stimmen in IDs, Reihenfolge, Typ, Schwierigkeit, Lösungsindizes und Optionsanzahl überein, `correctAnswers` ist gegenüber `main` unverändert, und jede Bibelstelle existiert im hinterlegten Text. Die Fehler liegen im **Inhalt** der Optionen und Fragen.

---

## Kernbefunde

### 1. `en/44_apostelgeschichte.json` ist großflächig unbrauchbar

Bei **78 von 145** Fragen ist die englische Lösung falsch oder die EN-Frage eine andere als die DE-Frage. Ab etwa `apg_007` sind die EN-Fragen gegenüber DE verschoben und die Optionen neu sortiert, der Lösungsindex wurde aber aus DE übernommen.

➜ **Empfehlung:** Datei komplett neu aus der DE-Fassung übersetzen, statt einzeln zu korrigieren.

### 2. Lösungen durch Umsortieren der Optionen zerstört

Optionen wurden umformuliert und umsortiert, der Index in `correctAnswers` blieb stehen. Die Lösung zeigt dadurch jetzt auf einen falschen Distraktor:

| Frage | jetzt als richtig markiert | eigentlich richtig |
| :-- | :-- | :-- |
| `ps_063` (Ps 110:4) | „Du bist ein Richter ewiglich im Hause … Davids“ | „Du bist ein Priester ewiglich nach der Weise Melchisedeks“ |
| `ps_061` (Ps 107:29) | „Er verwandelt das Ungewitter, dass sanfter Wind weht“ | „Er stillt das Ungewitter, dass sich die Wellen legen“ |
| `apg_136` (Apg 28:1) | „Auf Zypern“ | „Auf Melite“ (in `main`: „Auf Malta“) |

Die Aussage in `SUMMARY.md`, `correctAnswers` sei nie geändert worden, stimmt formal – verdeckt aber genau diesen Fehler.

### 3. Distraktoren wurden ebenfalls richtig

Beim Angleichen an den Bibelwortlaut wurde ein Distraktor zur Umschreibung oder Kopie der Lösung – es gibt dann zwei richtige Antworten. Gehäuft in 2. Mose: `ex_102`, `ex_104`, `ex_169`, `ex_171`, `ex_218`, `ex_228`, `ex_241`, `ex_270`, `ex_273`, `ex_276`, `ex_325`; außerdem `1sam_011`, `1mose_019`.

### 4. EN-Fragen um eine Position verrutscht

In einzelnen Blöcken fragt EN etwas anderes als DE: `hes_126`–`hes_130`, `mt_069`, `mt_081`, `mt_082`, `hos_022`, `hos_024`.

### 5. EN-Distraktoren frei erfunden statt übersetzt

Größte Gruppe der kleineren Befunde. Meist harmlos, aber DE und EN sind dann nicht dasselbe Quiz – und vereinzelt ist ein neu erfundener EN-Distraktor zufällig richtig.

> [!WARNING]
> **Grundtext 1.–5. Mose und NT:** Der hinterlegte Text ist eine eigene Revision der Schlachter 1951 (z. B. „Im Anfang erschuf Älohim die Himmel und das Erdland“). Bei der Prüfung wurde für diese Bücher nur der Inhalt verglichen; bei der Korrektur wurden DE-Zitate an diesen Text angeglichen.

---

## Übersicht nach Datei

| Datei | 🔴 | 🟠 | 🟡 | gesamt |
| :-- | --: | --: | --: | --: |
| `01_1_mose.json` | **5** | **17** | **41** | 63 |
| `02_2_mose.json` | **12** | **8** | **45** | 65 |
| `03_3_mose.json` | **1** | **4** | **31** | 36 |
| `04_4_mose.json` | **1** | **5** | **35** | 41 |
| `05_5_mose.json` | **3** | **5** | **27** | 35 |
| `06_josua.json` | **1** | **2** | **11** | 14 |
| `07_richter.json` | **1** | **6** | **12** | 19 |
| `08_rut.json` | · | **1** | **2** | 3 |
| `09_1_samuel.json` | **2** | **1** | **8** | 11 |
| `10_2_samuel.json` | **1** | · | · | 1 |
| `11_1_koenige.json` | · | **2** | **5** | 7 |
| `12_2_koenige.json` | · | **2** | **6** | 8 |
| `13_1_chronik.json` | · | · | **7** | 7 |
| `14_2_chronik.json` | · | **2** | **9** | 11 |
| `15_esra.json` | · | · | **1** | 1 |
| `16_nehemia.json` | · | · | **2** | 2 |
| `17_esther.json` | · | **1** | **1** | 2 |
| `18_hiob.json` | · | **1** | **9** | 10 |
| `19_psalmen.json` | **3** | **2** | **3** | 8 |
| `20_sprueche.json` | **1** | **3** | **5** | 9 |
| `21_prediger.json` | · | **2** | **3** | 5 |
| `23_jesaja.json` | **1** | **5** | **33** | 39 |
| `24_jeremia.json` | **1** | **4** | **12** | 17 |
| `25_klagelieder.json` | · | · | **1** | 1 |
| `26_hesekiel.json` | **5** | **1** | **8** | 14 |
| `27_daniel.json` | · | · | **2** | 2 |
| `28_hosea.json` | **2** | **1** | **1** | 4 |
| `29_joel.json` | · | **1** | **1** | 2 |
| `30_amos.json` | · | · | **1** | 1 |
| `32_jona.json` | · | · | **2** | 2 |
| `33_micha.json` | · | **1** | · | 1 |
| `34_nahum.json` | · | · | **1** | 1 |
| `35_habakuk.json` | · | **1** | **2** | 3 |
| `36_zephanja.json` | · | **3** | **4** | 7 |
| `38_sacharja.json` | **1** | **1** | **16** | 18 |
| `39_maleachi.json` | · | **1** | **11** | 12 |
| `40_matthaeus.json` | **10** | **5** | **14** | 29 |
| `41_markus.json` | · | **2** | **22** | 24 |
| `42_lukas.json` | **3** | **3** | **29** | 35 |
| `43_johannes.json` | **1** | **1** | **31** | 33 |
| `44_apostelgeschichte.json` | **64** | **13** | **14** | 91 |
| `45_roemer.json` | · | **1** | **15** | 16 |
| `46_1_korinther.json` | **2** | **5** | **50** | 57 |
| `47_2_korinther.json` | · | **2** | **8** | 10 |
| `48_galater.json` | · | · | **3** | 3 |
| `49_epheser.json` | **1** | · | · | 1 |
| `50_philipper.json` | · | · | **2** | 2 |
| `51_kolosser.json` | · | · | **3** | 3 |
| `52_1_thessalonicher.json` | · | · | **2** | 2 |
| `53_2_thessalonicher.json` | · | · | **1** | 1 |
| `55_2_timotheus.json` | · | · | **1** | 1 |
| `56_titus.json` | · | · | **1** | 1 |
| `58_hebraeer.json` | · | **1** | **2** | 3 |
| `59_jakobus.json` | · | **1** | **5** | 6 |
| `61_2_petrus.json` | · | **1** | · | 1 |
| `62_1_johannes.json` | · | · | **5** | 5 |
| `64_3_johannes.json` | · | · | **1** | 1 |
| `66_offenbarung.json` | **1** | **2** | **30** | 33 |

---

<a id="schwere-fehler"></a>

## 🔴 Schwere Fehler (123)

_Lösung falsch, mehrere Antworten richtig oder Frage in DE/EN unbrauchbar. Diese zuerst korrigieren._

### 📄 `01_1_mose.json` (5)

#### `1mose_019` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** DE-Distraktor 2 gibt genau den Inhalt von 1. Mose 3:15 wieder (der Same der Frau zertritt den Kopf, die Schlange trifft die Ferse) und ist damit ebenfalls richtig. Die Frage ist mehrdeutig. Die EN-Option 2 hat außerdem einen ganz anderen Inhalt ("crowned with horns").

**Aktuell DE** · _1. Mose 3:15_  
Welches Urteil sprach Gott der HERR über die Schlange und ihren Samen aus?

- ⬜ Dass sie für immer fliegen und im Meer leben müsse
- ⬜ Dass sie fortan nur noch giftige Pflanzen fressen darf
- ⬜ Dass sie den Kopf zertreten bekommt und in die Ferse sticht
- ✅ **Feindschaft zwischen ihrem Samen und dem Samen der Frau** ← _als richtig markiert_

**Aktuell EN** · _Genesis 3:15_  
What judgment did the LORD God pronounce upon the serpent and its seed?

- ⬜ That it should fly and dwell forever in the depths of the sea
- ⬜ That it should henceforth eat only poisonous herbs of field
- ⬜ That its head would be crowned with horns to crawl in dust
- ✅ **Enmity between its seed and the seed of the blessed woman** ← _als richtig markiert_

> 📖 **Beleg:** DE 2: "Dass sie den Kopf zertreten bekommt und in die Ferse sticht" / DE-TEXT: "derselbe soll dir den Kopf wegschnappen, und du wirst ihm die Ferse wegschnappen"; EN 2: "That its head would be crowned with horns to crawl in dust"

> ✏️ **Korrekturvorschlag:** DE-Option 2 durch einen eindeutig falschen Distraktor ersetzen, der der EN-Option entspricht, z. B. „Dass ihr Haupt mit Hörnern gekrönt werde und sie im Staub kriechen müsse“, oder z. B. „Dass sie fortan in der Wüste ohne Wasser leben müsse“ (DE und EN gleich).

<sub>🔎 Gegenprüfung: Trifft zu. DE-Option 2 gibt den zweiten Teil von 3:15 wieder (Kopf/Ferse) und ist damit ebenfalls richtig. EN-Option 2 ("crowned with horns") hat einen anderen Inhalt. Die DE-Option 2 muss durch einen eindeutig falschen Distraktor ersetzt werden, der in DE und EN gleich lautet.</sub>

---

#### `1mose_102` · Mehrere richtig

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN-Option 1 lautet ebenfalls „Naphtali“ mit fast demselben Zitat wie die richtige Option 2. Damit sind in EN zwei Optionen richtig. In DE ist Option 1 „Gad“ mit anderem Inhalt.

**Aktuell EN** · _Genesis 30:8_  
What name did Rachel give to Bilhah's second son, and what meaning did she express?

- ⬜ Dan; "God hath judged me and hath also heard my voice in affliction"
- ⬜ Naphtali; "With great wrestlings have I wrestled, and have prevailed"
- ✅ **Naphtali; "With great wrestlings have I wrestled with my sister, and have prevailed!"** ← _als richtig markiert_
- ⬜ Asher; "Happy am I, for the daughters will call me blessed"

> 📖 **Beleg:** EN 1: "Naphtali; \"With great wrestlings have I wrestled, and have prevailed\"" / EN 2 [x]: "Naphtali; \"With great wrestlings have I wrestled with my sister, and have prevailed!\""; DE 1: "Gad; „Glück zu! …“"

> ✏️ **Korrekturvorschlag:** EN-Option 1: "Gad; \"A troop cometh: for a band of valiant sons goeth forth to battle for me!\"" (entsprechend DE-Option 1).

<sub>🔎 Gegenprüfung: Trifft zu. EN-Option 1 ist eine Kurzfassung der KJV-Aussage zu Naphtali und damit ebenfalls richtig. In EN gibt es also zwei korrekte Optionen. Die vorgeschlagene Gad-Option entspricht DE-Option 1.</sub>

---

#### `1mose_191` · Mehrere richtig

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** In EN ist Distraktor 1 inhaltlich identisch mit der richtigen Option 3 (Landstück, das den Amoritern mit Schwert und Bogen genommen wurde). Die Frage hat dadurch zwei richtige Antworten. Die EN-Distraktoren passen außerdem nicht zu den DE-Optionen: DE0 Machpela / EN0 Silber und Gold aus Haran, DE1 Erstgeburtsrecht / EN1 Amoriter-Anteil, DE2 Brunnen von Beerseba / EN2 Machpela.

**Aktuell EN** · _Genesis 48:22_  
What special portion did dying Jacob bestow upon Joseph above his brethren?

- ⬜ All the silver and gold brought out of Haran into the land of Canaan
- ⬜ One portion taken out of the hand of the Amorite with his sword and bow
- ⬜ The cave of Machpelah to be Joseph's exclusive family burial tomb
- ✅ **One portion above his brethren, taken from the hand of the Amorite with sword and bow** ← _als richtig markiert_

> 📖 **Beleg:** EN 1: "One portion taken out of the hand of the Amorite with his sword and bow" / EN 3 [x]: "One portion above his brethren, taken from the hand of the Amorite with sword and bow"

> ✏️ **Korrekturvorschlag:** EN-Option 1 an DE angleichen: "The birthright with a double portion of all the flocks and silver"; EN 0 = "The burial place in the cave of Machpelah, which Abraham bought of the Hittites"; EN 2 = "The deep well of Beer-sheba with the fruitful pastures of the south"

<sub>🔎 Gegenprüfung: Bestätigt. EN 1 („One portion taken out of the hand of the Amorite with his sword and bow“) gibt KJV 48:22 inhaltlich richtig wieder und ist damit eine zweite richtige Antwort. Die Distraktor-Zuordnung DE/EN ist ebenfalls verschoben (DE0 Machpela = EN2). Der Korrekturvorschlag passt.</sub>

---

#### `1mose_297` · Falsche Lösung

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Die als richtig markierte Aussage stimmt nicht. Machpela war nicht der einzige Grundbesitz, den die Erzväter in Kanaan erwarben. Jakob kaufte bei Sichem ein Feldstück von den Söhnen Hemors (1. Mose 33:19, vgl. Josua 24:32). Der Spieler lernt hier also etwas Falsches.

**Aktuell DE** · _1. Mose 23:16-20_  
Welche theologische Tragweite hat der Kauf des Ackers Machpelah von den Söhnen Heths durch Abraham?

- ⬜ Es bewies nach hethitischem Recht, dass Abraham ein mächtiger Kaufmann war, der weite Ländereien aufkaufte
- ✅ **Es war der einzige physische Landbesitz, den die Erzväter im verheißenen Land Kanaan zu Lebzeiten legal erwarben** ← _als richtig markiert_
- ⬜ Abraham wurde dadurch von allen hethitischen Stadtältesten feierlich zum erblichen Fürsten und König gekrönt
- ⬜ Es war ein juristischer Scheinkauf, da das felsige Ackerland von den Söhnen Heths bald darauf wieder eingezogen wurde

**Aktuell EN** · _Genesis 23:16-20_  
What was the lasting significance of Abraham's purchase of the field of Machpelah from the sons of Heth?

- ⬜ It proved under Hittite law that Abraham was an earthly land merchant
- ✅ **It was the only physical possession the patriarchs legally acquired in Canaan** ← _als richtig markiert_
- ⬜ Abraham was thereby crowned hereditary prince and king over all Hittites
- ⬜ It was a fictitious purchase soon revoked by the rulers of the land

> 📖 **Beleg:** 1. Mose 33:19: "Und er kaufte das Grundstück, auf welchem er sein Zelt aufschlug, von der Hand der Söhne Hemors ... um hundert Kesitha" / KJV: "he bought a parcel of a field ... for an hundred pieces of money"

> ✏️ **Korrekturvorschlag:** Option 1 umformulieren, z. B.: "Es war der erste rechtmäßig erworbene Grundbesitz Abrahams im verheißenen Land, ein Erbbegräbnis als Unterpfand der Verheißung" / EN: "It was Abraham's first legally purchased possession in the promised land, a buryingplace as a pledge of the promise".

<sub>🔎 Gegenprüfung: Bestätigt. 1. Mose 33:19 (vgl. Jos 24:32, Apg 7:16): Jakob kaufte bei Sichem ein Feldstück für 100 Kesita. Die Aussage 'einziger Landbesitz der Erzväter' ist damit in DE und EN falsch. Korrektur wie vorgeschlagen, z. B. 'der erste rechtmäßig erworbene Grundbesitz Abrahams im verheißenen Land, ein Erbbegräbnis als Unterpfand der Verheißung'.</sub>

---

#### `1mose_314` · DE/EN weicht ab

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE und EN stellen verschiedene Fragen. DE fragt, welche Warnung Abimelech im Traum von Gott erhielt (Lösung: "du bist des Todes ..."). EN fragt, was Abraham dem Abimelech über Sara sagte (Lösung: "She is my sister"). Auch alle Optionen haben einen anderen Inhalt.

**Aktuell DE** · _1. Mose 20:1-3_  
Welche ernste Warnung empfing Abimelech, der König von Gerar, nachts im Traum von Gott?

- ⬜ Dass seine Felder von Heuschrecken heimgesucht würden, weil er fremde Hirten beherbergte
- ✅ **„Siehe, du bist des Todes wegen der Frau, die du genommen hast; denn sie ist verehelicht!“** ← _als richtig markiert_
- ⬜ Dass Abraham Krieger aus Ägypten anwerbe, um die befestigte Königsstadt Gerar zu stürmen
- ⬜ Dass er seinen Thron an Pharao abtreten müsse, wenn er das hebräische Volk nicht freilasse

**Aktuell EN** · _Genesis 20:1-3_  
What did Abraham tell Abimelech king of Gerar concerning his wife Sarah?

- ⬜ He declared she was his adopted daughter taken out of Mesopotamia
- ✅ **"She is my sister"; and Abimelech king of Gerar sent, and took Sarah** ← _als richtig markiert_
- ⬜ He said she was a consecrated priestess of the Most High God of Salem
- ⬜ He claimed she was a noble stranger travelling under his protection

> 📖 **Beleg:** DE: "Welche ernste Warnung empfing Abimelech ... nachts im Traum von Gott?" vs. EN: "What did Abraham tell Abimelech king of Gerar concerning his wife Sarah?"

> ✏️ **Korrekturvorschlag:** EN an DE angleichen: "What solemn warning did Abimelech king of Gerar receive from God in a dream by night?", richtige Option: "Behold, thou art but a dead man, for the woman which thou hast taken; for she is a man's wife". Distraktoren sinngemäß aus DE übersetzen.

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach der Warnung im Traum (20:3), EN nach Abrahams Aussage über Sara (20:2). Frage und alle Optionen weichen voneinander ab. Beide Inhalte stehen in der angegebenen Stelle, aber DE und EN stellen verschiedene Fragen. EN an DE angleichen (KJV 20:3: 'Behold, thou art but a dead man, for the woman which thou hast taken; for she is a man's wife').</sub>

---

### 📄 `02_2_mose.json` (12)

#### `ex_102` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Der Distraktor 0 gibt den Bibeltext wörtlich wieder (DE: 'Er stieß die Räder von ihren Wagen und trieb sie ins Gedränge'; EN: 'He took off their chariot wheels, that they drave them heavily') und ist damit ebenfalls richtig. Zusätzlich ist die markierte DE-Lösung sprachlich verunglückt: 'sodass sie schwer gewohnt waren' ergibt keinen Sinn.

**Aktuell DE** · _2. Mose 14:24-25_  
Was geschah mit den Streitwagen der Ägypter, als sie Israel in das Meer folgten?

- ⬜ Er stieß die Räder von ihren Wagen und trieb sie ins Gedränge
- ⬜ Die Streitwagen versanken im grundlosen Meeresboden
- ⬜ Die feurigen Pferde rissen aus und warfen Reiter ab
- ✅ **Gott hemmte die Räder, sodass sie schwer gewohnt waren** ← _als richtig markiert_

**Aktuell EN** · _Exodus 14:24-25_  
What happened to the chariots of the Egyptians when they pursued Israel into the sea?

- ⬜ He took off their chariot wheels, that they drave them heavily
- ⬜ The chariots sank into the bottomless mud of the deep
- ⬜ The spirited horses ran wild and threw off their riders
- ✅ **The LORD took off their chariot wheels, that they drave heavily** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT 14:25: "und stieß die Räder von ihren Wagen und brachte sie ins Gedränge"; KJV: "took off their chariot wheels, that they drave them heavily"

> ✏️ **Korrekturvorschlag:** Option 0 durch einen falschen Distraktor ersetzen, z. B. DE 'Ein Sturm warf die Wagen um und zerschmetterte sie' / EN 'A storm overturned the chariots and dashed them to pieces'. Option 3 korrigieren in 'Gott stieß die Räder von ihren Wagen, sodass sie nur schwer vorankamen'.

<sub>🔎 Gegenprüfung: Bestätigt. Distraktor 0 gibt in DE und EN fast wörtlich 14:25 wieder und ist damit ebenfalls richtig. Die markierte DE-Option 3 'sodass sie schwer gewohnt waren' ist sinnlos. Distraktor 0 ersetzen und DE 3 z. B. in 'Gott stieß die Räder von ihren Wagen, sodass sie nur mühsam vorankamen' ändern.</sub>

---

#### `ex_104` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Distraktor 0 ('Eine wohlklingende Handpauke in ihre Hand' / 'A timbrel in her hand to lead the praise') ist ebenfalls richtig. Die markierte DE-Option 1 nennt außerdem die 'rechte Hand', was nicht im Text steht.

**Aktuell DE** · _2. Mose 15:20_  
Welches Instrument nahm Miriam die Prophetin beim Jubelgesang am Schilfmeer?

- ⬜ Eine wohlklingende Handpauke in ihre Hand
- ✅ **Eine Handpauke in ihre rechte Hand** ← _als richtig markiert_
- ⬜ Eine zehnsaitige Harfe aus Elfenbein
- ⬜ Ein altes Wüstenhorn aus Widderhorn

**Aktuell EN** · _Exodus 15:20_  
What instrument did Miriam the prophetess take in her hand when leading the song of triumph?

- ⬜ A timbrel in her hand to lead the praise
- ✅ **Miriam the prophetess took a timbrel in her hand** ← _als richtig markiert_
- ⬜ A ten-stringed harp carved out of polished ivory
- ⬜ An ancient desert ram's horn blown by the priests

> 📖 **Beleg:** DE-TEXT 15:20: "nahm das Tamburin in ihre Hand"; KJV: "took a timbrel in her hand"

> ✏️ **Korrekturvorschlag:** Option 0 durch einen falschen Distraktor ersetzen, z. B. DE 'Eine silberne Trompete' / EN 'A trumpet of silver'. Option 1 auf 'Eine Handpauke (Tamburin) in ihre Hand' ändern.

<sub>🔎 Gegenprüfung: Bestätigt. Distraktor 0 (DE 'Handpauke in ihre Hand', EN 'A timbrel in her hand') ist ebenfalls richtig. Die markierte DE-Option nennt die 'rechte Hand', die im Text nicht vorkommt. Distraktor ersetzen und 'rechte' streichen.</sub>

---

#### `ex_169` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die Optionen 1 und 2 sind inhaltlich gleich: DE 'Ein Priesterkönigtum und eine heilige Nation' und 'Ein Priesterkönigtum und heilig Volk'. In EN sind sie sogar identisch, nur Option 2 steht in Anführungszeichen. Option 1 ist also ebenfalls richtig.

**Aktuell DE** · _2. Mose 19:5-6_  
Was versprach Gott dem Volk Israel zu werden, wenn es Seiner Stimme gehorchen würde?

- ⬜ Das reichste Volk unter allen Reichen
- ⬜ Ein Priesterkönigtum und eine heilige Nation
- ✅ **Ein Priesterkönigtum und heilig Volk** ← _als richtig markiert_
- ⬜ Die Herren über alle Könige der Erde

**Aktuell EN** · _Exodus 19:5-6_  
What did God promise Israel they should be unto Him if they obeyed His voice and kept His covenant?

- ⬜ The wealthiest empire among all the nations of earth
- ⬜ A kingdom of priests, and an holy nation
- ✅ **"A kingdom of priests, and an holy nation"** ← _als richtig markiert_
- ⬜ Rulers and tribute-gatherers over all earthly thrones

> 📖 **Beleg:** EN 1: "A kingdom of priests, and an holy nation"; EN 2: "\"A kingdom of priests, and an holy nation\""

> ✏️ **Korrekturvorschlag:** Option 1 durch einen echten Distraktor ersetzen, z. B. DE 'Ein Volk von Kriegern und Eroberern' / EN 'A nation of warriors and conquerors'.

<sub>🔎 Gegenprüfung: Bestätigt. EN 1 und 2 sind wortgleich und unterscheiden sich nur durch die Anführungszeichen. DE 1 und 2 bedeuten dasselbe. Option 1 durch einen echten Distraktor ersetzen.</sub>

---

#### `ex_171` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Distraktor 3 ('Der Tod durch Steinigung oder mit einem Geschoß' / 'Death by stoning or being shot through with weapon') sagt inhaltlich dasselbe wie die richtige Option 0. Die Frage ist dadurch mehrdeutig.

**Aktuell DE** · _2. Mose 19:12-13_  
Welche Strafe drohte jedem Mensch oder Tier, das den heiligen Berg Sinai berührte?

- ✅ **Der Tod durch Steinigung oder Pfeile** ← _als richtig markiert_
- ⬜ Eine schwere Geldstrafe an die Priester
- ⬜ Der Ausschluss aus dem Lager Israels
- ⬜ Der Tod durch Steinigung oder mit einem Geschoß

**Aktuell EN** · _Exodus 19:12-13_  
What penalty was decreed for man or beast that touched the border of Mount Sinai?

- ✅ **He shall surely be stoned, or shot through, and die** ← _als richtig markiert_
- ⬜ A heavy fine of silver paid to the sanctuary
- ⬜ Exclusion from the congregation of Israel for life
- ⬜ Death by stoning or being shot through with weapon

> 📖 **Beleg:** DE-TEXT 19:13: "sonst soll er gesteinigt oder mit einem Geschoß erschossen werden"; KJV: "he shall surely be stoned, or shot through"

> ✏️ **Korrekturvorschlag:** Option 3 ersetzen, z. B. DE 'Er musste vierzig Tage außerhalb des Lagers bleiben' / EN 'He was to remain forty days without the camp'.

<sub>🔎 Gegenprüfung: Bestätigt. Option 3 (DE 'Steinigung oder mit einem Geschoß', EN 'stoning or being shot through') sagt inhaltlich dasselbe wie die richtige Option 0. Die Frage hat damit zwei richtige Antworten. Option 3 ersetzen.</sub>

---

#### `ex_191` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** In der EN-Fassung ist Index 0 als richtig markiert: 'He had to pay a double dowry to her father without marriage'. Das ist laut KJV falsch. Richtig wäre Index 1 'He shall surely endow her to be his wife', der dort als Distraktor steht. Damit stimmt die EN-Lösung auch nicht mit der DE-Lösung überein (DE Index 0 = 'Sie gegen Brautgeld zur Frau nehmen').

**Aktuell EN** · _Exodus 22:16-17_  
What was a man required to do if he enticed a maid that was not betrothed and lay with her?

- ✅ **He had to pay a double dowry to her father without marriage** ← _als richtig markiert_
- ⬜ He shall surely endow her to be his wife
- ⬜ He was banished from the tribe of his fathers for three years
- ⬜ He had to offer a ram for a trespass offering at the altar

> 📖 **Beleg:** KJV 22:16: "he shall surely endow her to be his wife"; EN [x] 0: "He had to pay a double dowry to her father without marriage"

> ✏️ **Korrekturvorschlag:** EN-Optionen tauschen, sodass Index 0 lautet: 'He shall surely endow her to be his wife'. Index 1 dann als Distraktor z. B. 'He had to pay a double dowry to her father without marriage'.

<sub>🔎 Gegenprüfung: Bestätigt. KJV 22:16 'he shall surely endow her to be his wife' steht in EN als Distraktor 1. Markiert ist EN 0 ('double dowry ... without marriage'), und das ist falsch. DE 0 ist korrekt markiert. Abhilfe: EN-Optionen 0 und 1 tauschen bzw. die Markierung auf die korrekte Option setzen.</sub>

---

#### `ex_218` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Option 2 und Option 3 sind inhaltlich gleich und beide richtig. Option 2 gibt den hinterlegten DE-Text sogar wörtlich wieder. Im Englischen sind beide Optionen praktisch identisch.

**Aktuell DE** · _2. Mose 26:14_  
Woraus bestanden die beiden äußeren Schutzdecken, die das Zelt der Begegnung nach oben abdeckten?

- ⬜ Aus weißer Schafwolle und feinem Ziegenhaar
- ⬜ Aus gewobenem Byssus und purpurner Wolle
- ⬜ Aus rötlichen Widderfellen und Seehundsfellen
- ✅ **Aus rot gefärbten Widderfellen und Seekuhfellen** ← _als richtig markiert_

**Aktuell EN** · _Exodus 26:14_  
Of what were the two outermost protective coverings for the tabernacle made?

- ⬜ Of white sheep wool and fine spun goats' hair
- ⬜ Of fine twined linen and costly purple hangings
- ⬜ Of rams' skins dyed red, and a covering of badgers' skins
- ✅ **Of rams' skins dyed red, and badgers' skins above** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT: "eine Decke von rötlichen Widderfellen ... Seehundsfellen oben darüber"; DE 2: "Aus rötlichen Widderfellen und Seehundsfellen" / DE 3: "Aus rot gefärbten Widderfellen und Seekuhfellen"; EN 2: "Of rams' skins dyed red, and a covering of badgers' skins" / EN 3: "Of rams' skins dyed red, and badgers' skins above"

> ✏️ **Korrekturvorschlag:** Option 2 durch einen falschen Distraktor ersetzen, z. B. DE: "Aus Ziegenfellen und Rinderhäuten" / EN: "Of goats' skins and the hides of oxen".

<sub>🔎 Gegenprüfung: Bestätigt. DE 2 (rötliche Widderfelle + Seehundsfelle) gibt 26:14 fast wörtlich wieder, EN 2 und EN 3 sind sinngleich. Es gibt also zwei richtige Antworten.</sub>

---

#### `ex_228` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Im Deutschen ist Distraktor 0 wortgleich mit dem Bibeltext und damit ebenfalls richtig. Es gibt also zwei richtige Antworten. Die EN-Option 0 (Zedernöl) hat einen anderen Inhalt als die DE-Option 0.

**Aktuell DE** · _2. Mose 27:20_  
Welches Öl musste das Volk Israel für den goldenen Leuchter im Heiligtum darbringen?

- ⬜ Lauteres, gestoßenes Olivenöl für den Leuchter
- ✅ **Reines Öl aus gestampften Oliven** ← _als richtig markiert_
- ⬜ Heiliges Salböl nach Priesterrezept
- ⬜ Feines Myrrenöl aus dem Land Arabia

**Aktuell EN** · _Exodus 27:20_  
What oil was Israel commanded to bring for the candlestick to cause the lamp to burn always?

- ⬜ Spiced cedar oil collected from the mountain trees
- ✅ **Pure oil olive beaten for the light to burn** ← _als richtig markiert_
- ⬜ Fragrant holy anointing oil of the high priests
- ⬜ Choice myrrh oil imported from the land of Arabia

> 📖 **Beleg:** DE-TEXT: "lauteres, gestoßenes Olivenöl für den Leuchter"; DE 0: "Lauteres, gestoßenes Olivenöl für den Leuchter" (nicht markiert); DE 1 [x]: "Reines Öl aus gestampften Oliven"; EN 0: "Spiced cedar oil collected from the mountain trees"

> ✏️ **Korrekturvorschlag:** DE-Option 0 an EN angleichen: "Gewürztes Zedernöl von den Bäumen der Berge".

<sub>🔎 Gegenprüfung: Bestätigt. DE 0 ist wortgleich mit 27:20 ('lauteres, gestoßenes Olivenöl für den Leuchter') und nicht markiert. EN 0 (Zedernöl) ist ein anderer Distraktor, daher ist auch die Angleichung nötig.</sub>

---

#### `ex_241` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Distraktor 1 („Webebrust und Hebeschulter“) ist genau das, was 2. Mose 29:27 nennt, und meint inhaltlich dasselbe wie die markierte Antwort 2. In EN sind Option 1 und Option 2 nahezu wortgleich.

**Aktuell DE** · _2. Mose 29:27_  
Welcher Teil des Widders wurde beim Einweihungsopfer als Schwingopfer dargebracht?

- ⬜ Der Kopf und die Hinterläufe des Widders
- ⬜ Die Webebrust und die Hebeschulter des Widders
- ✅ **Die Brust und die rechte Keule des Widders** ← _als richtig markiert_
- ⬜ Die Wolle und die Haut des Opfertieres

**Aktuell EN** · _Exodus 29:27_  
Which parts of the ram of consecration were sanctified as a wave offering and heave offering?

- ⬜ The head and the hindmost portions of the ram
- ⬜ The wave breast and the heave shoulder of the ram
- ✅ **The breast of the wave offering, and shoulder of heave offering** ← _als richtig markiert_
- ⬜ The wool and the entire fleece of the sacrifice

> 📖 **Beleg:** DE-TEXT: "heiligen die Webebrust und die Hebeschulter"; DE 1: "Die Webebrust und die Hebeschulter des Widders"; EN 1: "The wave breast and the heave shoulder of the ram" / EN 2 [x]: "The breast of the wave offering, and shoulder of heave offering"

> ✏️ **Korrekturvorschlag:** Option 1 ersetzen, z. B. DE: "Die Leber und die Nieren des Widders" / EN: "The liver and the two kidneys of the ram".

<sub>🔎 Gegenprüfung: Bestätigt. DE 1 ist der Wortlaut von 29:27 (Webebrust/Hebeschulter), EN 1 und EN 2 sind sinngleich. Damit sind zwei Optionen richtig.</sub>

---

#### `ex_270` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Option 2 und Option 3 sind identisch, im DE fast wörtlich und im EN exakt. Nur Option 3 ist als richtig markiert, deshalb ist Option 2 ebenfalls richtig.

**Aktuell DE** · _2. Mose 33:18_  
Welche kühne Bitte äußerte Mose im vertrauten Gebet auf dem Berg zu Gott?

- ⬜ Er bat um das sofortige Sterben Ägyptens
- ⬜ Gib mir die Macht über alle Völker Kanaans
- ⬜ «Lass mich doch deine Herrlichkeit sehen»
- ✅ **Lass mich doch Deine Herrlichkeit schauen** ← _als richtig markiert_

**Aktuell EN** · _Exodus 33:18_  
What bold prayer did Moses make unto God in the secret place of communion?

- ⬜ He prayed for the immediate destruction of Egypt
- ⬜ "Grant me power over all the kings of Canaan"
- ⬜ "I beseech thee, shew me thy glory"
- ✅ **"I beseech thee, shew me thy glory"** ← _als richtig markiert_

> 📖 **Beleg:** DE 2: «Lass mich doch deine Herrlichkeit sehen» / DE 3 [x]: "Lass mich doch Deine Herrlichkeit schauen"; EN 2 und EN 3: "I beseech thee, shew me thy glory"

> ✏️ **Korrekturvorschlag:** Option 2 ersetzen, z. B. DE: "Gib mir Wasser aus dem Felsen für das Volk" / EN: "Give the people water out of the rock".

<sub>🔎 Gegenprüfung: Bestätigt. EN 2 und EN 3 sind zeichengleich. DE 2 entspricht sogar wörtlicher dem Text ('deine Herrlichkeit sehen') als die markierte DE 3.</sub>

---

#### `ex_273` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Option 0 und Option 2 sind inhaltlich gleich und beide richtig. Option 0 gibt den DE-Text sogar wörtlicher wieder als die markierte Option 2. Im EN sind beide ebenfalls identisch.

**Aktuell DE** · _2. Mose 34:6-7_  
Wie offenbarte Sich Gott vor Mose, als Er in der Wolke herabstieg?

- ⬜ Barmherzig, gnädig, langsam zum Zorn und von großer Huld
- ⬜ Als der Schöpfer der Sterne am Himmel
- ✅ **Barmherzig, gnädig, geduldig und von großer Güte** ← _als richtig markiert_
- ⬜ Als der Richter über alle Heidenvölker

**Aktuell EN** · _Exodus 34:6-7_  
How did the LORD proclaim His name before Moses when He descended in the cloud?

- ⬜ Merciful, gracious, longsuffering, abundant in goodness
- ⬜ As the eternal, sovereign Creator and Preserver of the entire world
- ✅ **The LORD God, merciful and gracious, longsuffering, abundant in goodness** ← _als richtig markiert_
- ⬜ As the strict, righteous Judge executing doom upon all heathen nations

> 📖 **Beleg:** DE-TEXT: "barmherzig und gnädig ..., langsam zum Zorn und von großer Huld"; DE 0: "Barmherzig, gnädig, langsam zum Zorn und von großer Huld"; DE 2 [x]: "Barmherzig, gnädig, geduldig und von großer Güte"; EN 0: "Merciful, gracious, longsuffering, abundant in goodness"

> ✏️ **Korrekturvorschlag:** Option 0 ersetzen, z. B. DE: "Als der Gott, der Missetat niemals heimsucht" / EN: "As a God who never visits iniquity".

<sub>🔎 Gegenprüfung: Bestätigt. DE 0 entspricht 34:6 wörtlich ('langsam zum Zorn und von großer Huld'), EN 0 ist inhaltsgleich mit der markierten EN 2. Es gibt zwei richtige Antworten.</sub>

---

#### `ex_276` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Option 0 („strahlte“) und Option 1 („leuchtete“) sind gleichbedeutend. Option 0 ist sogar der Wortlaut des DE-Texts. Im EN ist Option 0 ein Teil der richtigen Option 1.

**Aktuell DE** · _2. Mose 34:29-30_  
Was stellten Aaron und die Israeliten fest, als Mose mit den Tafeln herabstieg?

- ⬜ Dass die Haut seines Angesichts strahlte
- ✅ **Dass die Haut seines Angesichts leuchtete** ← _als richtig markiert_
- ⬜ Dass die Steintafeln in feurigen Flammen brannten
- ⬜ Dass seine Gewänder vollkommen weiß wurden

**Aktuell EN** · _Exodus 34:29-30_  
What did Aaron and all the children of Israel see when Moses came down from the mount?

- ⬜ That the skin of his face shone
- ✅ **The skin of his face shone; and they were afraid to come nigh him** ← _als richtig markiert_
- ⬜ That the tables of stone were burning with unquenchable fire
- ⬜ That his garments had turned as bright as the noonday light

> 📖 **Beleg:** DE-TEXT: "die Haut seines Angesichtes strahlte"; DE 0: "Dass die Haut seines Angesichts strahlte" / DE 1 [x]: "...leuchtete"; EN 0: "That the skin of his face shone"

> ✏️ **Korrekturvorschlag:** Option 0 ersetzen, z. B. DE: "Dass sein Haar völlig ergraut war" / EN: "That his hair had turned white as snow".

<sub>🔎 Gegenprüfung: Bestätigt. DE 0 ('strahlte') ist der Wortlaut von 34:30 und gleichbedeutend mit DE 1 ('leuchtete'). EN 0 ist ein wörtlicher Teil der richtigen EN 1.</sub>

---

#### `ex_325` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Option 0 und Option 1 sind inhaltlich gleich, im EN sogar wortgleich. Nur Option 0 ist als richtig markiert.

**Aktuell DE** · _2. Mose 3:2-5_  
Was gebot Gott dem Mose, als dieser sich dem brennenden Dornbusch am Horeb näherte?

- ✅ **Er sollte seine Schuhe von den Füßen ausziehen, denn der Ort, darauf er stand, war heiliges Land** ← _als richtig markiert_
- ⬜ Er sollte seine Schuhe von den Füßen ablegen, denn der Ort war heilig
- ⬜ Er sollte mit der Hand in die Flammen greifen, um seine persönliche Unversehrtheit zu erproben
- ⬜ Er sollte Wasser aus dem Felsen schlagen, um den brennenden Busch vor der Vernichtung zu löschen

**Aktuell EN** · _Exodus 3:2-5_  
What did God command Moses when he turned aside to see the burning bush at Horeb?

- ✅ **"Put off thy shoes from off thy feet, for the place is holy ground"** ← _als richtig markiert_
- ⬜ "Put off thy shoes from off thy feet, for the place is holy ground"
- ⬜ He was commanded to touch the flames with his bare hands
- ⬜ He was commanded to strike the rock to quench the bush

> 📖 **Beleg:** DE 0 [x]: "Er sollte seine Schuhe von den Füßen ausziehen, denn der Ort ... war heiliges Land" / DE 1: "Er sollte seine Schuhe von den Füßen ablegen, denn der Ort war heilig"; EN 0 = EN 1: "Put off thy shoes from off thy feet, for the place is holy ground"

> ✏️ **Korrekturvorschlag:** Option 1 ersetzen, z. B. DE: "Er sollte sofort zum Pharao zurückkehren und sich vor ihm niederwerfen" / EN: "He was to return to Pharaoh at once and bow before him".

<sub>🔎 Gegenprüfung: Bestätigt. EN 0 und EN 1 sind zeichengleich, DE 1 ist nur eine Kurzfassung von DE 0. Damit sind zwei Optionen richtig.</sub>

---

### 📄 `03_3_mose.json` (1)

#### `lev_121` · Inhaltlicher Fehler

🔴 **hoch** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die richtige Antwort verkehrt den Sinn: Verboten ist laut Text das ENTBLÖSSEN der Scham von Blutsverwandten, nicht deren 'Verhüllung'. So wie die Option dasteht, wäre das Bedecken verboten. Außerdem ist die Frage ohne Kontext ('durch die Regelungen') sehr vage, während EN klar nach den Bestimmungen über nahe Verwandte fragt.

**Aktuell DE** · _3. Mose 18:6_  
Welches fundamentale Verbot zieht sich durch die Regelungen?

- ⬜ Das Verbot des Handels mit fremdem Gold
- ⬜ Das Verbot des Essens von Fettauswüchsen
- ⬜ Das Verbot der Arbeit am heiligen Sabbat
- ✅ **Die Verhüllung der Blöße naher Blutsverwandter** ← _als richtig markiert_

> 📖 **Beleg:** DE-Option [x] 3: 'Die Verhüllung der Blöße naher Blutsverwandter' – DE-TEXT: 'Niemand soll sich seiner Blutsverwandten nahen, ihre Scham zu entblößen'

> ✏️ **Korrekturvorschlag:** Frage: 'Welches grundlegende Verbot steht am Anfang der Bestimmungen über nahe Verwandte?' Option 3: 'Sich Blutsverwandten nahen, um ihre Blöße zu entblößen'

<sub>🔎 Gegenprüfung: Bestätigt. Die Frage lautet 'Welches Verbot', die richtige Antwort ist aber 'Die Verhüllung der Blöße'. Damit wäre das Bedecken verboten, und der Sinn von 18:6 ('ihre Scham zu entblößen') ist umgekehrt. Die DE-Frage ist ohne Kontext zudem vage. Korrektur: Option 3 'Sich Blutsverwandten zu nahen, um ihre Blöße aufzudecken'. Die Frage an EN angleichen ('...am Anfang der Bestimmungen über nahe Verwandte').</sub>

---

### 📄 `04_4_mose.json` (1)

#### `num_213` · Mehrere richtig

🔴 **hoch** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Der DE-Distraktor 1 heißt „Balaam der moabitische Priester aus Ar“. Balaam ist nur die englische bzw. griechische Namensform von Bileam, also dieselbe Person wie die richtige Antwort. Dadurch ist die Frage mehrdeutig. Im EN-Text steht an dieser Stelle richtigerweise „Balak the king of Moab“.

**Aktuell DE** · _4. Mose 31:8_  
Welcher falsche Prophet wurde zusammen mit den fünf Königen von Midian durchs Schwert getötet?

- ✅ **Bileam der Sohn Beors mit dem Schwert** ← _als richtig markiert_
- ⬜ Balaam der moabitische Priester aus Ar
- ⬜ Og der Riesenkönig aus dem Lande Baschan
- ⬜ Sihon der amoritische König von Hesbon

> 📖 **Beleg:** DE 1: „Balaam der moabitische Priester aus Ar“ / EN 1: „Balak the king of Moab who had hired diviners from Aram“; KJV 31:8: „Balaam also the son of Beor they slew with the sword“

> ✏️ **Korrekturvorschlag:** DE-Option 1: „Balak, der König der Moabiter, der Bileam gedungen hatte“

<sub>🔎 Gegenprüfung: Bestätigt. „Balaam“ ist die griechische bzw. englische Form von Bileam. Der Distraktor nennt also namentlich die Lösungsperson, nur mit einer falschen Beschreibung (Bileam war kein moabitischer Priester aus Ar, er stammte aus Pethor). Wer die Namensform kennt, findet zwei passende Antworten. EN nennt an dieser Stelle korrekt Balak. Vorschlag: DE 1 „Balak, der König der Moabiter, der Bileam gedungen hatte“.</sub>

---

### 📄 `05_5_mose.json` (3)

#### `dtn_029` · Inhaltlicher Fehler

🔴 **hoch** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die DE-Frage fragt, wo Mose den Bund mit der NEUEN Generation 'erneuerte'. Diese Erneuerung geschah im Land Moab (5. Mose 29:1: 'im Lande Moab, außer dem Bund, den er mit ihnen am Horeb gemacht hatte'). Nach dieser Formulierung wäre Option 2 ('Auf den Feldern der Moabiter beim Jordan') richtig und nicht Horeb. 5. Mose 5:2-3 sagt nur, dass der Bund am Horeb geschlossen wurde. Die EN-Frage fragt korrekt danach, wo der Bund geschlossen wurde, und weicht damit von der DE-Frage ab.

**Aktuell DE** · _5. Mose 5:2-3_  
Wo erneuerte Mose den Bund der Zehn Gebote mit der neuen Generation Israels?

- ⬜ Direkt im Allerheiligsten der Stiftshütte
- ✅ **Am Berg Horeb schloss Gott diesen Bund mit uns** ← _als richtig markiert_
- ⬜ Auf den Feldern der Moabiter beim Jordan
- ⬜ In der Oase Kadesch beim Haderwasser

> 📖 **Beleg:** DE-TEXT 5:2: 'JHWH, unser Älohim, hat auf dem Berge Horeb einen Bund mit uns gemacht.' / DE-Frage: 'Wo erneuerte Mose den Bund ... mit der neuen Generation Israels?'

> ✏️ **Korrekturvorschlag:** DE-Frage: 'Wo hatte der HERR, unser Gott, laut Mose den Bund mit der lebenden Generation Israels geschlossen?'

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage fragt, wo Mose den Bund mit der neuen Generation 'erneuerte'. Diese Erneuerung fand in Moab statt (5. Mose 1:5; 29:1), also passt Option 2 ebenso gut, und die Frage ist mehrdeutig bzw. irreführend. Der Text 5:2-3 sagt nur, dass der Bund am Horeb geschlossen wurde. Die DE-Frage sollte wie EN lauten: 'Wo hat der HERR, unser Gott, laut Mose diesen Bund mit den heute Lebenden geschlossen?'</sub>

---

#### `dtn_087` · Falsche Lösung

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage fragt 'Wer sollte gesteinigt werden', alle Optionen beschreiben aber Handlungen. Die markierte DE-Antwort 'ihn anzeigen' gibt den Text falsch wieder: Der hinterlegte Text (V. 9) verlangt, ihn zu töten ('deine Hand soll als erste an ihm sein'). Von Anzeigen ist dort keine Rede. Die EN-Lösung zitiert dagegen richtig 'thine hand shall be first upon him to put him to death'. DE und EN sagen also inhaltlich Verschiedenes.

**Aktuell DE** · _5. Mose 13:6-9_  
Wer sollte gesteinigt werden, wenn er heimlich zum Abfall vom HERRN verführte?

- ⬜ Man sollte die Sache vor der Familie verschweigen
- ⬜ Man sollte ihn mit Geld aus dem Lande schicken
- ⬜ Man sollte für ihn ein privates Sündopfer bringen
- ✅ **Du sollst ihm nicht einwilligen und ihn anzeigen** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT 13:9: 'sondern du sollst ihn unbedingt umbringen; deine Hand soll als erste an ihm sein, ihn zu töten' / DE-Option 3: 'Du sollst ihm nicht einwilligen und ihn anzeigen'

> ✏️ **Korrekturvorschlag:** DE-Frage: 'Was sollte geschehen, wenn ein naher Verwandter heimlich zum Abfall vom HERRN verführte?'; DE-Option 3: 'Nicht einwilligen, ihn nicht schonen – deine Hand soll als erste an ihm sein'

<sub>🔎 Gegenprüfung: Bestätigt. Laut V. 8-9 soll man den Verführer nicht verbergen, sondern töten, die eigene Hand als erste. 'Ihn anzeigen' gibt den Text sachlich falsch wieder. Die Frage 'Wer sollte gesteinigt werden' passt außerdem nicht zu den Optionen, die Handlungen beschreiben. Die Frage wie EN als 'Was war gefordert…' fassen; Antwort: 'Nicht einwilligen, ihn nicht verbergen – deine Hand soll als erste an ihm sein, ihn zu töten'.</sub>

---

#### `dtn_184` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Laut Text ist jedes Eisenwerkzeug am Altar verboten. Damit sind auch die Distraktoren 1 (eiserner Hammer) und 3 (eiserne Säge) verbotene Eisenwerkzeuge, also ebenfalls richtige Antworten. Die Frage ist mehrdeutig.

**Aktuell DE** · _5. Mose 27:5_  
Welches Eisenwerkzeug durfte beim Bau des Altars auf dem Berg Ebal keinesfalls verwendet werden?

- ✅ **Du sollst kein eisernes Werkzeug darüber schwingen** ← _als richtig markiert_
- ⬜ Ein eiserner Hammer zum Zertrümmern der Steine
- ⬜ Ein kupferner Meißel der heidnischen Steinmetze
- ⬜ Eine eiserne Säge zur Glättung der Blöcke

**Aktuell EN** · _Deuteronomy 27:5_  
What tool was strictly forbidden when building the stone altar unto the LORD upon mount Ebal?

- ✅ **Thou shalt not lift up any iron tool upon the stones of the altar** ← _als richtig markiert_
- ⬜ An iron sledge hammer designed to break the sacred stones into pieces
- ⬜ A bronze carving chisel used by skilled heathen stonecutters in Egypt
- ⬜ A heavy iron saw employed in smoothing the flat surfaces of the blocks

> 📖 **Beleg:** DE-TEXT: "über diese sollst du kein Eisen schwingen"; KJV: "thou shalt not lift up any iron tool upon them"; Optionen: "Ein eiserner Hammer…", "Eine eiserne Säge…"

> ✏️ **Korrekturvorschlag:** Die Distraktoren 1 und 3 auf Material oder Handlungen umstellen, die nicht aus Eisen sind bzw. erlaubt wären (z. B. "Ein Altar aus Holz" oder "Gemörtelte Ziegel"). Alternativ die Frage umformulieren: "Welche Vorschrift galt für die Steine des Altars auf dem Berg Ebal?"

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage fragt nach dem verbotenen Eisenwerkzeug, die EN-Frage nach dem verbotenen Werkzeug. Laut 27:5 ist jedes Eisenwerkzeug verboten (KJV "any iron tool", DE "kein Eisen"). Damit sind der eiserne Hammer (1) und die eiserne Säge (3) in beiden Sprachen ebenfalls richtig. Die Distraktoren 1 und 3 müssen weg vom Eisen, z. B. "behauene Steine verwenden" oder "einen Altar aus Holz".</sub>

---

### 📄 `06_josua.json` (1)

#### `jos_084` · Inhaltlicher Fehler

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Josua 12:3 setzt die Beschreibung des Gebiets von Sihon fort (V. 2–3). Og wird erst in V. 4–5 genannt. Das Meer Kinneroth gehörte nach dieser Stelle also zu Sihons Reich, nicht zu Ogs. Wird die Frage auf Sihon korrigiert, ist auch Distraktor 0 (Salzmeer) richtig, denn V. 3 nennt es ebenfalls.

**Aktuell DE** · _Josua 12:3_  
Welches Gewässer im Norden gehörte zum Herrschaftsgebiet des Riesenkönigs Og?

- ⬜ Das große Salzmeer an den Wüstengrenzen
- ✅ **Das Binnenmeer Kinnereth (Genezareth)** ← _als richtig markiert_
- ⬜ Der rote Meerbusen an den Grenzen Edoms
- ⬜ Der Wildbach Kison nahe dem Berg Karmel

**Aktuell EN** · _Joshua 12:3_  
Which northern sea lay within the borders of the kingdom of giant King Og?

- ⬜ The great Salt Sea bordering the desert of Judah
- ✅ **The inland sea of Chinneroth (Chinnereth)** ← _als richtig markiert_
- ⬜ The Red Sea gulf bordering upon the land of Edom
- ⬜ The ancient river Kishon flowing by Mount Carmel

> 📖 **Beleg:** KJV 12:2-3: "Sihon king of the Amorites ... And from the plain to the sea of Chinneroth on the east, and unto the sea of the plain, even the salt sea"; Og erst 12:4

> ✏️ **Korrekturvorschlag:** Frage auf Sihon umstellen: „Bis an welches Meer im Norden reichte das Gebiet des Amoriterkönigs Sihon?“ / „Unto which sea northward did the dominion of Sihon king of the Amorites reach?“. Distraktor 0 (Salzmeer) durch ein Gewässer ersetzen, das in V. 3 nicht vorkommt, z. B. „Der Wildbach Kidron“.

<sub>🔎 Gegenprüfung: Bestätigt. Jos 12,2–3 beschreibt Sihons Gebiet, Og kommt erst in V. 4–5 vor (Hermon, Salcha, Basan, halbes Gilead). Das Meer Kinneroth wird also bei Sihon genannt, die als richtig markierte Antwort steht nicht im Bibeltext. Auch das Salzmeer (Distraktor 0) steht in V. 3. Wird die Frage auf Sihon umgestellt, muss Distraktor 0 ersetzt werden. Den Kison als Ersatz zu nehmen geht nicht, weil er schon Distraktor 3 ist. Daher z. B. „Der Bach Kidron“ oder „Das große Meer (Mittelmeer)“.</sub>

---

### 📄 `07_richter.json` (1)

#### `ri_077` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Fassung stellt eine ganz andere Frage als DE: DE fragt nach dem Grund für Ephraims Zorn (Ri 12,1), EN nach der Losungswort-Probe an den Jordanfurten (Ri 12,5-6). Außerdem ist in EN die falsche Option markiert: Richtig wäre Index 0 (Shibboleth/Sibboleth), markiert ist Index 3 („Gilead … Tob“), was erfunden ist. Die EN-Optionen passen zudem nicht zu den DE-Optionen.

**Aktuell EN** · _Judges 12:1_  
By what password test at the passages of Jordan did the Gileadites detect fleeing Ephraimites?

- ⬜ Say now Shibboleth: and he said Sibboleth: for he could not frame to pronounce it
- ⬜ Say now Jordan: and he said Arnon, confounding the rivers
- ⬜ Say now Jehovah: and he said Baal, according to the heathen
- ✅ **Say now Gilead: and he said Tob, mistaking the country** ← _als richtig markiert_

> 📖 **Beleg:** EN [x] 3: "Say now Gilead: and he said Tob, mistaking the country"; KJV 12:6: "Say now Shibboleth: and he said Sibboleth"; DE fragt: "Warum entbrannte der Zorn der Männer von Ephraim …"

> ✏️ **Korrekturvorschlag:** EN an DE angleichen: "Why was the anger of the men of Ephraim kindled against Jephthah?" mit Optionen 0: "Because he had not divided the gold of the Ammonites", 1: "Because he built an altar of the heathen upon the mountains", 2: "Because he despised the law of Moses in the camp", 3 [x]: "Because he passed over to fight against Ammon and did not call them" (die Shibboleth-Frage gibt es bereits als ri_078).

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach der Schibboleth-Probe (Ri 12,5-6), DE nach Ephraims Zorn (12,1). Gemessen an der eigenen EN-Frage ist Index 3 („Gilead … Tob“) falsch markiert, richtig wäre Index 0. Die Schibboleth-Frage gibt es bereits als ri_078 (dort steht sogar derselbe erfundene Distraktor „Gilead/Tob“). EN deshalb wie vorgeschlagen an DE 12,1 angleichen, [x]=3: „Because he passed over to fight against the children of Ammon and did not call them“.</sub>

---

### 📄 `09_1_samuel.json` (2)

#### `1sam_011` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Distraktor 0 ist inhaltlich identisch mit der markierten Lösung 3. Im EN sind Option 0 und Option 3 sogar wortgleich. Wer Option 0 wählt, antwortet laut Bibeltext richtig, wird aber als falsch gewertet.

**Aktuell DE** · _1. Samuel 4:3-4_  
Welches Heiligtum holten die Israeliten nach der ersten Niederlage bei Eben-Ezer ins Feldlager?

- ⬜ Die Lade des Bundes des HERRN von Silo
- ⬜ Die eherne Schlange aus den Wüstentagen
- ⬜ Das Stiftszelt samt den Opfergeräten
- ✅ **Die Bundeslade des Bundes Gottes aus Silo** ← _als richtig markiert_

**Aktuell EN** · _1 Samuel 4:3-4_  
What sacred object did Israel fetch from Shiloh after their first defeat at Ebenezer?

- ⬜ The ark of the covenant of the LORD out of Shiloh
- ⬜ The brazen altar of burnt offering from the court
- ⬜ The sacred urim and thummim borne by the Levites
- ✅ **The ark of the covenant of the LORD out of Shiloh** ← _als richtig markiert_

> 📖 **Beleg:** DE 0: 'Die Lade des Bundes des HERRN von Silo' / DE 3 [x]: 'Die Bundeslade des Bundes Gottes aus Silo'; EN 0 und EN 3: 'The ark of the covenant of the LORD out of Shiloh'; DE-TEXT 4:3: 'die Lade des Bundes des HERRN von Silo'

> ✏️ **Korrekturvorschlag:** Option 0 durch einen echten Distraktor ersetzen, z. B. DE 'Den goldenen Leuchter aus dem Heiligtum' / EN 'The golden candlestick out of the sanctuary' (oder analog zu EN 1/2: 'Den ehernen Brandopferaltar' / 'Die Urim und Thummim').

<sub>🔎 Gegenprüfung: Bestätigt. DE 0 ist wörtlich der Luthertext von 4:3 ('die Lade des Bundes des HERRN von Silo'), und EN 0 und EN 3 sind wortgleich mit dem KJV-Text. Damit sind zwei Antworten richtig, also ein klarer Bewertungsfehler. Option 0 in beiden Sprachen durch einen echten Distraktor ersetzen, z. B. DE 'Den goldenen Leuchter aus dem Heiligtum' / EN 'The golden candlestick out of the sanctuary'.</sub>

---

#### `1sam_096` · Mehrere richtig

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Der EN-Distraktor 3 ist laut Bibeltext ebenfalls richtig: Ziklag war tatsächlich mit Feuer verbrannt. Damit ist die EN-Frage mehrdeutig. Im DE steht an derselben Stelle ein klar falscher Distraktor (Erdbeben), d. h. EN weicht hier zusätzlich vom DE ab.

**Aktuell EN** · _1 Samuel 30:1-3_  
What disaster did David and his men discover upon their return to the city of Ziklag?

- ✅ **The Amalekites had burned Ziklag and taken women** ← _als richtig markiert_
- ⬜ Saul's warriors had overthrown and slain the men
- ⬜ The men of Judah had plundered their possessions
- ⬜ A great fire had consumed the city to ashes

> 📖 **Beleg:** EN [3]: "A great fire had consumed the city to ashes" – KJV 30:3: "behold, it was burned with fire"; DE [3]: "Ein Erdbeben hatte die Stadt zerstört"

> ✏️ **Korrekturvorschlag:** EN-Option 3 an DE angleichen: "An earthquake had overthrown the city, and many had perished"

<sub>🔎 Gegenprüfung: Bestätigt. KJV 30:1 "burned it with fire" und 30:3 "behold, it was burned with fire". Damit ist EN-Option 3 "A great fire had consumed the city to ashes" sachlich auch richtig, und die Frage hat zwei richtige Antworten. Die Korrektur ist sinnvoll: "An earthquake had overthrown the city, and many had perished", passend zum DE-Distraktor.</sub>

---

### 📄 `10_2_samuel.json` (1)

#### `2sam_069` · Sprachfehler

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die richtige DE-Option sagt, Rizpa habe ein 'Häslein' (kleiner Hase) auf den Fels gebreitet. Im Text steht 'einen Sack' (KJV: sackcloth). Die Lösung ist dadurch sinnentstellt, und der Spieler lernt etwas Falsches.

**Aktuell DE** · _2. Samuel 21:10_  
Wie bewachte Rizpa, die Nebenfrau Sauls, die Leichname ihrer aufgehängten Söhne?

- ⬜ Sie umgab die Leichen mit einer Wache von hundert benjaminitischen Kriegern
- ⬜ Sie errichtete ein steinernes Gewölbe über den Leibern auf dem Fels
- ✅ **Sie breitete ein Häslein auf den Fels und wehrte den Vögeln und Tieren** ← _als richtig markiert_
- ⬜ Sie klagte sieben Tage laut und salbte die Gebeine täglich mit Myrrhe

> 📖 **Beleg:** DE-Option: 'Sie breitete ein Häslein auf den Fels …' / DE-TEXT: 'Da nahm Rizpa … einen Sack und breitete ihn auf den Fels'

> ✏️ **Korrekturvorschlag:** Sie breitete einen Sack auf den Fels und wehrte den Vögeln und Tieren

<sub>🔎 Gegenprüfung: Bestätigt. Die richtige DE-Option lautet 'Sie breitete ein Häslein auf den Fels …'. Im Luthertext steht 'einen Sack' (KJV: sackcloth). Die Lösung ist sinnentstellt und vermittelt etwas Falsches. Korrektur: 'Sie breitete einen Sack auf den Fels und wehrte den Vögeln und Tieren'.</sub>

---

### 📄 `19_psalmen.json` (3)

#### `ps_061` · Falsche Lösung

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Als richtig ist Index 3 markiert (Ungewitter verwandelt, sanfter Wind weht). Laut Bibeltext ist Index 1 richtig (Ungewitter gestillt, Wellen legen sich). In DE und EN steht correctAnswers [3].

**Aktuell DE** · _Psalmen 107:29_  
Was tat der HERR nach Psalm 107:29 mit dem Ungewitter?

- ⬜ Er vertreibt das Ungewitter, dass die Wolken verfliegen
- ⬜ Er stillt das Ungewitter, dass sich die Wellen legen
- ⬜ Er gebietet dem Ungewitter, dass der Regen aufhört
- ✅ **Er verwandelt das Ungewitter, dass sanfter Wind weht** ← _als richtig markiert_

**Aktuell EN** · _Psalm 107:29_  
What did the LORD do to the storm according to Psalm 107:29?

- ⬜ He turned the dark storm that the clouds were scattered away
- ⬜ He maketh the storm a calm, so that the waves thereof are still
- ⬜ He commanded the storm that the heavy rain ceased at once
- ✅ **He changed the storm that a gentle wind blew upon the waters** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT: "und stillte das Ungewitter, daß die Wellen sich legten"; KJV: "He maketh the storm a calm, so that the waves thereof are still."

> ✏️ **Korrekturvorschlag:** correctAnswers in DE und EN auf [1] setzen ("Er stillt das Ungewitter, dass sich die Wellen legen" / "He maketh the storm a calm, so that the waves thereof are still").

<sub>🔎 Gegenprüfung: Bestätigt. Ps 107:29 (Luther 1912: 'stillte das Ungewitter, daß die Wellen sich legten'; KJV: 'maketh the storm a calm, so that the waves thereof are still'). Markiert ist aber [3], richtig ist [1]. Die EN-Option 1 ist sogar wörtlich die KJV. correctAnswers in DE und EN auf [1] setzen.</sub>

---

#### `ps_063` · Falsche Lösung

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Als richtig ist Index 1 markiert ("Richter ewiglich im Hause Davids"). Psalm 110:4 sagt aber "Priester ewiglich nach der Weise Melchisedeks", also Index 3. Der Fehler steht in DE und EN.

**Aktuell DE** · _Psalmen 110:4_  
Was sagt der HERR nach Psalm 110:4 über den Gesalbten?

- ⬜ Du bist ein König ewiglich über alle Völker der ganzen Erde
- ✅ **Du bist ein Richter ewiglich im Hause und Geschlecht Davids** ← _als richtig markiert_
- ⬜ Du bist ein Prophet ewiglich nach dem Vorbild des Mose
- ⬜ Du bist ein Priester ewiglich nach der Weise Melchisedeks

**Aktuell EN** · _Psalm 110:4_  
What hath the LORD sworn concerning his priest in Psalm 110:4?

- ⬜ Thou art an everlasting king over all kingdoms of the wide world
- ✅ **Thou art a righteous judge in the royal house and lineage of David** ← _als richtig markiert_
- ⬜ Thou art an holy prophet according to the pattern of faithful Moses
- ⬜ Thou art a priest for ever after the order of Melchizedek

> 📖 **Beleg:** DE-TEXT: "Du ist ein Priester ewiglich nach der Weise Melchisedeks."; KJV: "Thou art a priest for ever after the order of Melchizedek."

> ✏️ **Korrekturvorschlag:** correctAnswers in DE und EN auf [3] setzen.

<sub>🔎 Gegenprüfung: Bestätigt. Ps 110:4 lautet 'Priester ewiglich nach der Weise Melchisedeks' (KJV: 'priest for ever after the order of Melchizedek'), das ist Option 3. Markiert ist [1] ('Richter ... Hause Davids'), was nicht im Text steht. Die EN-Frage spricht sogar selbst von 'his priest'. In DE und EN auf [3] korrigieren.</sub>

---

#### `ps_074` · Falsche Lösung

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Als richtig ist Index 0 markiert ("Wir wollen zur heiligen Stadt ziehen" / "go up unto the holy mountain of Zion"). Der Text sagt aber "Laßt uns ins Haus des HERRN gehen", also Index 1.

**Aktuell DE** · _Psalmen 122:1_  
Worüber freute sich der Beter nach Psalm 122:1?

- ✅ **Über die Worte: „Wir wollen zur heiligen Stadt ziehen“** ← _als richtig markiert_
- ⬜ Über die Worte: „Wir wollen ins Haus des HERRN gehen“
- ⬜ Über die Worte: „Wir wollen dem König die Treue schwören“
- ⬜ Über die Worte: „Wir wollen am Altar ein Opfer darbringen“

**Aktuell EN** · _Psalm 122:1_  
At what was the psalmist glad according to Psalm 122:1?

- ✅ **When they said: Let us go up unto the holy mountain of Zion** ← _als richtig markiert_
- ⬜ When they said unto me: Let us go into the house of the LORD
- ⬜ When they said: Let us swear allegiance unto the chosen king
- ⬜ When they said: Let us offer solemn sacrifices upon the altar

> 📖 **Beleg:** DE-TEXT: "Ich freute mich über die, so mir sagten: Laßt uns ins Haus des HERRN gehen!"; KJV: "Let us go into the house of the LORD."

> ✏️ **Korrekturvorschlag:** correctAnswers in DE und EN auf [1] setzen.

<sub>🔎 Gegenprüfung: Bestätigt. Ps 122:1: 'Laßt uns ins Haus des HERRN gehen' / 'Let us go into the house of the LORD', das ist Option 1, EN-Option 1 ist wörtlich die KJV. Markiert ist [0] ('zur heiligen Stadt' / 'holy mountain of Zion'), was falsch ist. In DE und EN auf [1] setzen.</sub>

---

### 📄 `20_sprueche.json` (1)

#### `spr_032` · Falsche Lösung

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage fragt, was für den gilt, der seine Missetat leugnet. Die Optionen sind aber nur Personenbezeichnungen (Gerechter, Törigter, Heuchler, Gottloser), und die markierte Antwort 'Der Gottlose' steht nicht im Text. Laut Text gilt: 'dem wird's nicht gelingen'. Die EN-Fassung fragt richtig nach der Folge ('shall not prosper'), DE und EN stimmen also auch nicht überein.

**Aktuell DE** · _Sprüche 28:13_  
Was gilt nach Sprüche 28:13 für den, der seine Missetat leugnet?

- ⬜ Der Gerechte
- ⬜ Der Törigte
- ⬜ Der Heuchler
- ✅ **Der Gottlose** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT: 'Wer seine Missetat leugnet, dem wird's nicht gelingen; wer sie aber bekennt und läßt, der wird Barmherzigkeit erlangen.' / markiert: 'Der Gottlose'

> ✏️ **Korrekturvorschlag:** Optionen analog zu EN neu fassen, z. B. richtig: 'Dem wird's nicht gelingen; wer sie aber bekennt und lässt, wird Barmherzigkeit erlangen'. Distraktoren z. B. 'Er wird von Menschen vergeben, aber von Gott gerichtet' / 'Er hat eine Zeit lang Glück, dann vergeht sein Andenken' / 'Er findet Frieden bei Gefährten, die seine Schuld nicht kennen'.

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Optionen nennen nur Personen. 'Der Gottlose' kommt in Spr 28:13 (Luther) nicht vor, der Text sagt 'dem wird's nicht gelingen'. Die Frage ist so nicht beantwortbar, und DE weicht von EN ab. Der Korrekturvorschlag, die Optionen nach dem Muster von EN neu zu fassen, ist sinnvoll.</sub>

---

### 📄 `23_jesaja.json` (1)

#### `jes_007` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Der DE-Distraktor 0 ist inhaltlich ebenfalls richtig: Der Wolf wohnt beim Lamm bzw. Schaf (V. 6), und der Löwe frisst Stroh (V. 7). Beides steht in der angegebenen Stelle 11:6-9. Auch EN-Distraktor 0 kommt in V. 6-7 sinngemäß vor (Löwe und Ochse, Bär, Mastkalb). Die Frage ist dadurch mehrdeutig.

**Aktuell DE** · _Jesaja 11:6-9_  
Welches Bild des Friedens zeichnet Jesaja 11:6?

- ⬜ Der Wolf wohnt beim Schaf und der Löwe frisst Stroh
- ✅ **Wölfe wohnen bei Lämmern und Parder bei Böcken** ← _als richtig markiert_
- ⬜ Der Wolf meidet das Lamm und der Pardel das Kalb
- ⬜ Die wilden Tiere fliehen in die ferne Wüste

**Aktuell EN** · _Isaiah 11:6-9_  
What picture of peace doth Isaiah 11:6 describe?

- ⬜ The lion shall feed with the ox and the bear with the fat calf
- ✅ **The wolf shall dwell with the lamb and leopard with the kid** ← _als richtig markiert_
- ⬜ The leopard shall sleep with the lion and wolf with the ass
- ⬜ The wild beasts shall flee away together into the wilderness

> 📖 **Beleg:** DE-TEXT V.6: 'Die Wölfe werden bei den Lämmern wohnen' / V.7: 'und Löwen werden Stroh essen wie die Ochsen' / KJV V.7: 'the cow and the bear shall feed ... the lion shall eat straw like the ox'

> ✏️ **Korrekturvorschlag:** DE-Option 0 ersetzen, z. B. 'Der Löwe jagt das Lamm, und der Bär meidet die Kuh'. EN-Option 0 ersetzen, z. B. 'The lion shall hunt the lamb, and the bear shall flee from the cow'.

<sub>🔎 Gegenprüfung: Bestätigt. DE-Option 0 ('Wolf beim Schaf' aus V.6, 'Löwe frisst Stroh' aus V.7) ist inhaltlich ein zutreffendes Friedensbild aus der angegebenen Stelle 11:6-9 und damit faktisch richtig. EN-Option 0 ist eine Mischung aus V.6-7 (Löwe frisst Stroh wie der Ochse, Kuh und Bär weiden, Mastkalb) und ebenfalls mehrdeutig, aber weniger wörtlich. Beide Optionen 0 sollten ersetzt werden.</sub>

---

### 📄 `24_jeremia.json` (1)

#### `jer_043` · Mehrere richtig

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Distraktor 0 sagt inhaltlich dasselbe wie die richtige Antwort 1. Laut Jer 8,8 ist das, was die Schriftgelehrten 'setzen', 'eitel Lüge'. 'Das Gesetz verfälschen und Lügen lehren' ist genau dieser Vorwurf.

**Aktuell DE** · _Jeremia 8:8_  
Was wirft Jeremia 8:8 den Schriftgelehrten vor?

- ⬜ Dass sie das Gesetz des HERRN verfälschen und böse Lügen lehren
- ✅ **Dass der Lügengriffel der Schreiber das Gesetz zur Lüge macht** ← _als richtig markiert_
- ⬜ Dass sie die Gebote Gottes vergessen und fremden Götzen dienen
- ⬜ Dass sie das Wort des HERRN verachten und den Propheten wehren

> 📖 **Beleg:** DE-Option 0: 'Dass sie das Gesetz des HERRN verfälschen und böse Lügen lehren' – DE-TEXT: 'Ist's doch eitel Lüge, was die Schriftgelehrten setzen.'

> ✏️ **Korrekturvorschlag:** Option 0 durch einen klar falschen Vorwurf ersetzen, passend zu EN-Option 0, z. B. 'Dass sie das Gesetz zu viel auslegen und die Hörer verwirren'.

<sub>🔎 Gegenprüfung: Bestätigt. Jer 8,8 (Luther): 'Ist's doch eitel Lüge, was die Schriftgelehrten setzen.' DE-Option 0 ('das Gesetz verfälschen und böse Lügen lehren') erhebt inhaltlich denselben Vorwurf wie die Lösung 1. Damit sind zwei Antworten vertretbar. Option 0 sollte durch einen klar falschen Vorwurf ersetzt werden, sinnvoll angelehnt an EN 0 ('Dass sie das Gesetz zu viel auslegen und die Hörer verwirren').</sub>

---

### 📄 `26_hesekiel.json` (5)

#### `hes_126` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Fassung stellt eine ganz andere Frage als DE. DE fragt nach dem Schmuck des Hauses (Cherubim und Palmlaubwerk, 41:18), EN fragt nach den Priestern, die den Altar versorgen (Söhne Zadoks, 40:46). Die EN-Referenz lautet weiterhin 'Ezekiel 41:18-19', obwohl dort nichts über Zadok steht. Die EN-Fragen von hes_126 bis hes_130 sind offenbar um einen Platz verrutscht.

**Aktuell DE** · _Hesekiel 41:18-19_  
Was zierte nach Hesekiel 41:18 das ganze Haus ringsum?

- ⬜ Granatäpfel und Lilien
- ⬜ Löwen und Ochsen
- ✅ **Cherubim und Palmlaubwerk** ← _als richtig markiert_
- ⬜ Gold und Silber

**Aktuell EN** · _Ezekiel 41:18-19_  
Which priests had charge of the altar according to Ezekiel 40:46?

- ⬜ The sons of Phinehas among the sons of Eleazar
- ⬜ The sons of Gershon among the families of Levi
- ✅ **The sons of Zadok among the sons of Levi** ← _als richtig markiert_
- ⬜ The sons of Ithamar among the houses of Aaron

> 📖 **Beleg:** DE: 'Was zierte nach Hesekiel 41:18 das ganze Haus ringsum?' / EN: 'Which priests had charge of the altar according to Ezekiel 40:46?' – KJV 41:18: 'it was made with cherubims and palm trees'

> ✏️ **Korrekturvorschlag:** EN-Frage zu 41:18 einsetzen, zum Beispiel: 'What adorned all the house round about according to Ezekiel 41:18?' mit den Optionen 0: Pomegranates and lilies; 1: Lions and oxen; 2 [x]: Cherubims and palm trees; 3: Gold and silver.

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Frage zu hes_126 behandelt 40:46 (Söhne Zadoks), die Referenz lautet aber 41:18-19, und DE fragt nach Cherubim und Palmlaubwerk. Die EN-Inhalte von hes_126 bis hes_130 sind um eine Position verschoben. Die Korrektur passt, KJV 41:18 lautet 'made with cherubims and palm trees'.</sub>

---

#### `hes_127` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Fassung passt nicht zu DE. DE fragt, wie der hölzerne Altar genannt wird (41:22, 'der Tisch, der vor dem HERRN stehen soll'). EN fragt nach der Breite der Pfosten in 41:1 (sechs Ellen). Das liegt außerhalb der angegebenen Stelle 41:22, und auch die Lösung ist eine andere.

**Aktuell DE** · _Hesekiel 41:22_  
Wie wurde der hölzerne Altar in Hesekiel 41:22 genannt?

- ⬜ Der Schaubrottisch, auf dem die zwölf Brote liegen
- ⬜ Der Brandopferaltar, auf dem die Opfer verbrannt werden
- ⬜ Der Räucheraltar, auf dem das Räucherwerk brennt
- ✅ **Der Tisch, der vor dem HERRN stehen soll** ← _als richtig markiert_

**Aktuell EN** · _Ezekiel 41:22_  
What was the breadth of the posts of the temple in Ezekiel 41:1?

- ⬜ Three cubits broad on the one side and three on the other
- ⬜ Four cubits broad on the one side and four on the other
- ⬜ Ten cubits broad on the one side and ten on the other
- ✅ **Six cubits broad on the one side, and six on the other** ← _als richtig markiert_

> 📖 **Beleg:** DE: 'Wie wurde der hölzerne Altar in Hesekiel 41:22 genannt?' / EN: 'What was the breadth of the posts of the temple in Ezekiel 41:1?' – KJV 41:22: 'This is the table that is before the LORD.'

> ✏️ **Korrekturvorschlag:** EN: 'What was the altar of wood called in Ezekiel 41:22?' mit den Optionen 0: The table of shewbread; 1: The altar of burnt offering; 2: The altar of incense; 3 [x]: The table that is before the LORD.

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach der Breite der Pfosten in 41:1, während die Referenz 41:22 und die DE-Frage den hölzernen Altar betreffen. Die vorgeschlagene EN-Frage mit der Lösung 'This is the table that is before the LORD' an Index 3 passt zu KJV 41:22.</sub>

---

#### `hes_128` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Fassung passt nicht zu DE. DE fragt, was der Mann beim Messen des Innersten sagte (41:4, 'Dies ist das Allerheiligste'). EN fragt nach den Schnitzereien in 41:18-19. Die angegebene Stelle 41:4 enthält diesen EN-Inhalt nicht.

**Aktuell DE** · _Hesekiel 41:4_  
Was sagte der Mann, als er das Innerste des Hauses maß (Hesekiel 41:4)?

- ✅ **Dies ist das Allerheiligste** ← _als richtig markiert_
- ⬜ Dies ist das Heilige
- ⬜ Dies ist der Vorhof
- ⬜ Dies ist der Altar

**Aktuell EN** · _Ezekiel 41:4_  
What figures were carved upon the temple walls in Ezekiel 41:18-19?

- ✅ **Cherubims and palm trees, every cherub having two faces** ← _als richtig markiert_
- ⬜ Lions and oxen, with golden eagles spreading wings above
- ⬜ Pomegranates and lilies, with golden chains of work round about
- ⬜ Grape clusters and olive boughs, with figures of holy angels

> 📖 **Beleg:** DE: 'Was sagte der Mann, als er das Innerste des Hauses maß (Hesekiel 41:4)?' / EN: 'What figures were carved upon the temple walls in Ezekiel 41:18-19?' – KJV 41:4: 'This is the most holy place.'

> ✏️ **Korrekturvorschlag:** EN: 'What did the man say when he measured the inmost part of the house (Ezekiel 41:4)?' mit den Optionen 0 [x]: This is the most holy place; 1: This is the holy place; 2: This is the outer court; 3: This is the altar.

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach den Schnitzereien in 41:18-19, die Referenz und DE beziehen sich aber auf 41:4 ('This is the most holy place'). Die Korrektur passt.</sub>

---

#### `hes_129` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Fassung passt nicht zu DE. DE fragt nach dem Zweck der heiligen Kammern (42:13). EN fragt nach dem Namen des hölzernen Altars (41:22). Die EN-Referenz 'Ezekiel 42:13' passt nicht zur EN-Frage, und die Lösungen sind verschieden.

**Aktuell DE** · _Hesekiel 42:13_  
Wozu dienten die heiligen Kammern nach Hesekiel 42:13?

- ⬜ Dort wohnten die Leviten, die den Tempel hüteten und den Dienst in den Vorhöfen taten
- ✅ **Dort legen die Priester die hochheiligen Opfer nieder und essen sie** ← _als richtig markiert_
- ⬜ Dort wurden die Vorräte des Tempels gelagert, die Korn, Wein und Öl enthielten
- ⬜ Dort versammelte sich das Volk zu den Festen und aß die Friedensopfer gemeinsam

**Aktuell EN** · _Ezekiel 42:13_  
What was the altar of wood called in Ezekiel 41:22?

- ⬜ The golden hearth of incense before the veil
- ✅ **This is the table that is before the LORD** ← _als richtig markiert_
- ⬜ The holy memorial altar of the covenant
- ⬜ The consecrated place of burnt offerings

> 📖 **Beleg:** DE: 'Wozu dienten die heiligen Kammern nach Hesekiel 42:13?' / EN: 'What was the altar of wood called in Ezekiel 41:22?'

> ✏️ **Korrekturvorschlag:** EN: 'What was the purpose of the holy chambers according to Ezekiel 42:13?' mit der richtigen Option 1: 'There the priests that approach unto the LORD shall eat and lay the most holy things'. Dazu passende Distraktoren zu den DE-Optionen 0, 2 und 3 (Wohnung der Leviten, Vorratslager, Versammlungsort des Volkes).

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach dem Namen des Holzaltars in 41:22, Referenz und DE gehören zu 42:13. Die vorgeschlagene EN-Lösung passt zu KJV ('where the priests that approach unto the LORD shall eat the most holy things: there shall they lay...'). Am Rand: DE-Option 1 sagt 'und essen sie'. Luther 1912 sagt in 42:13 nur 'hineinlegen', das 'essen' steht in KJV. Das kann man stehen lassen.</sub>

---

#### `hes_130` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Fassung passt nicht zu DE. DE fragt, was die Priester beim Verlassen des Heiligtums tun müssen (42:14: Dienstkleider ablegen, andere anziehen). EN fragt, was sie in den heiligen Kammern tun (42:13: das Hochheilige essen). Die Lösungen sind inhaltlich verschieden.

**Aktuell DE** · _Hesekiel 42:14_  
Was mussten die Priester nach Hesekiel 42:14 beim Verlassen des Heiligtums tun?

- ⬜ Ein Opfer darbringen und sich die Hände im Becken gründlich waschen
- ⬜ Die Hände waschen und den Mund mit Wasser ausspülen vor dem Volk
- ✅ **Ihre Dienstkleider in den Kammern ablegen und andere anziehen** ← _als richtig markiert_
- ⬜ Den Altar siebenmal umschreiten und das Volk danach segnen

**Aktuell EN** · _Ezekiel 42:14_  
What were the priests to do in the holy chambers of Ezekiel 42:13?

- ⬜ Anoint the sacred vessels with oil before bringing into temple
- ⬜ Cast the sacred lots to determine the courses of the sanctuary
- ✅ **Eat the most holy things and lay the offerings and sin offering** ← _als richtig markiert_
- ⬜ Wash their garments seven times in pure water before sunset

> 📖 **Beleg:** DE: 'Was mussten die Priester nach Hesekiel 42:14 beim Verlassen des Heiligtums tun?' [x] 'Ihre Dienstkleider in den Kammern ablegen und andere anziehen' / EN: 'What were the priests to do in the holy chambers of Ezekiel 42:13?' [x] 'Eat the most holy things...' – KJV 42:14: 'there they shall lay their garments wherein they minister ... and shall put on other garments'

> ✏️ **Korrekturvorschlag:** EN: 'What must the priests do before going out of the holy place into the utter court (Ezekiel 42:14)?' mit der richtigen Option 2: 'Lay their garments wherein they minister and put on other garments'.

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach 42:13 (das Hochheilige essen), DE und die Referenz nach 42:14 (Dienstkleider ablegen, andere anziehen). Die Korrektur passt zu KJV 42:14.</sub>

---

### 📄 `28_hosea.json` (2)

#### `hos_022` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Frage fragt nach einer ganz anderen Stelle und einem anderen Inhalt als DE: DE fragt nach dem Bild für die Ehebrecher in Hosea 7:4 (Backofen), EN nach dem 'betrüglichen Bogen' aus Hosea 7:16. Die EN-Lösung ('deceitful bow') steht nicht in der hinterlegten Stelle Hosea 7:4-6. Damit ist auch die Bibelstelle für EN falsch.

**Aktuell DE** · _Hosea 7:4-6_  
Welches Bild gebraucht Hosea 7:4 für die Ehebrecher?

- ⬜ Ein Feuer auf dem Berg, das der Bäcker nie löscht
- ⬜ Eine Quelle, die im Sommer versiegt
- ✅ **Einen Backofen, den der Bäcker heizt** ← _als richtig markiert_
- ⬜ Ein Ofen, der erkaltet, wenn der Bäcker schläft

**Aktuell EN** · _Hosea 7:4-6_  
Unto what is the turning of the people compared in Hosea 7:16?

- ⬜ Unto an unfaithful messenger that runneth into the desert
- ⬜ Unto a broken jar that can hold no wine for the feast
- ✅ **They return, but not to the most High: they are like a deceitful bow** ← _als richtig markiert_
- ⬜ Unto a shadow that declineth and leaveth only cold darkness

> 📖 **Beleg:** DE: 'Welches Bild gebraucht Hosea 7:4 für die Ehebrecher?' [x] 'Einen Backofen, den der Bäcker heizt' / EN: 'Unto what is the turning of the people compared in Hosea 7:16?' [x] 'They return, but not to the most High: they are like a deceitful bow' / KJV 7:4: 'They are all adulterers, as an oven heated by the baker'

> ✏️ **Korrekturvorschlag:** EN-Frage an DE angleichen: 'What image does Hosea 7:4 use for the adulterers?' Optionen: 0 'A fire upon the mountain which the baker never quencheth', 1 'A fountain that drieth up in summer', 2 'As an oven heated by the baker' [richtig], 3 'An oven that groweth cold while the baker sleepeth'.

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Frage fragt nach Hosea 7:16 (deceitful bow), bibleReference ist aber Hosea 7:4-6. Weder die Lösung noch V.16 stehen im hinterlegten KJV-Text, DE fragt nach dem Backofen (7:4). EN muss an DE angeglichen werden, z. B. mit der Lösung 'They are all adulterers, as an oven heated by the baker'. Der Vorschlag ist brauchbar.</sub>

---

#### `hos_024` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Frage behandelt einen anderen Vers (Hosea 8:8, Israel als unwertes Gefäß) als DE (Hosea 8:5, das Kalb Samarias). Die EN-Lösung steht nicht in der hinterlegten Stelle Hosea 8:5-6, also ist die Bibelstelle für EN ebenfalls falsch.

**Aktuell DE** · _Hosea 8:5-6_  
Was sagt Hosea 8:5 über das Kalb von Samaria?

- ✅ **Der HERR verwirft es, und sein Zorn ist über Israel ergrimmt** ← _als richtig markiert_
- ⬜ Der HERR segnet es und erhört das Volk, das davor betet
- ⬜ Der HERR duldet es und sieht darüber um seiner Geduld willen hinweg
- ⬜ Der HERR benutzt es als Zeichen seiner Gegenwart unter dem Volk

**Aktuell EN** · _Hosea 8:5-6_  
How is Israel described among the Gentiles in Hosea 8:8?

- ✅ **As a vessel wherein is no pleasure, swallowed up by foes** ← _als richtig markiert_
- ⬜ As a proud crown of gold that was cast down into dust
- ⬜ As a mighty host that fled without a battle before sword
- ⬜ As a noble vine whose pleasant branches were consumed

> 📖 **Beleg:** DE: 'Was sagt Hosea 8:5 über das Kalb von Samaria?' [x] 'Der HERR verwirft es, und sein Zorn ist über Israel ergrimmt' / EN: 'How is Israel described among the Gentiles in Hosea 8:8?' [x] 'As a vessel wherein is no pleasure' / KJV 8:5: 'Thy calf, O Samaria, hath cast thee off; mine anger is kindled against them'

> ✏️ **Korrekturvorschlag:** EN-Frage an DE angleichen: 'What does Hosea 8:5 say concerning the calf of Samaria?' Optionen: 0 'Thy calf, O Samaria, hath cast thee off; mine anger is kindled against them' [richtig], 1 'The LORD blesseth it and heareth them that pray before it', 2 'The LORD suffereth it and winketh at it in his patience', 3 'The LORD useth it as a sign of his presence among the people'.

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Frage behandelt Hosea 8:8 (vessel wherein is no pleasure), bibleReference ist aber Hosea 8:5-6. Die EN-Lösung steht nicht im hinterlegten Text, DE fragt nach dem Kalb Samarias. EN auf 8:5 umstellen, Lösung 'Thy calf, O Samaria, hath cast thee off; mine anger is kindled against them'.</sub>

---

### 📄 `38_sacharja.json` (1)

#### `sach_026` · Inhaltlicher Fehler

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage fragt nach der Reichweite der Herrschaft. Keine Option beantwortet das, die richtige Antwort wäre 'von einem Meer bis ans andere und vom Strom bis an der Welt Ende'. Die markierte Option beschreibt stattdessen das Abtun der Wagen und Rosse. Die EN-Frage fragt anders ('What will the King cut off'). Laut Text ist aber 'ich' (der HERR) derjenige, der abtut, nicht der König.

**Aktuell DE** · _Sacharja 9:10_  
Wie weit reicht die Herrschaft des Königs nach Sacharja 9:10?

- ⬜ Er wird die Wagen in Ephraim und die Rosse zu Jerusalem mehren
- ⬜ Er wird die Rosse und Wagen der Heiden für sein eigenes Heer nehmen
- ✅ **Er wird die Wagen aus Ephraim und die Rosse aus Jerusalem ausrotten** ← _als richtig markiert_
- ⬜ Er wird die Heere aller Völker versammeln und mit ihnen einherziehen

**Aktuell EN** · _Zechariah 9:10_  
What will the King cut off according to Zechariah 9:10?

- ⬜ He will multiply the chariots in Ephraim and the horses in Jerusalem
- ⬜ He will seize the horses and chariots of the heathen for his own hosts
- ✅ **The chariot from Ephraim, the horse from Jerusalem, and the battle bow** ← _als richtig markiert_
- ⬜ He will assemble the armies of all nations and march forth in battle

> 📖 **Beleg:** DE: 'Wie weit reicht die Herrschaft des Königs nach Sacharja 9:10?' – DE-TEXT: 'Denn ich will die Wagen abtun von Ephraim … seine Herrschaft wird sein von einem Meer bis ans andere'

> ✏️ **Korrekturvorschlag:** DE-Frage: 'Was wird nach Sacharja 9:10 abgetan bzw. zerbrochen?' (und analog EN: 'What shall be cut off according to Zechariah 9:10?'). Alternativ die Frage zur Herrschaft beibehalten und als Lösung 'Von einem Meer bis ans andere und vom Strom bis an der Welt Ende' einsetzen.

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage fragt nach der Reichweite der Herrschaft, die markierte Option 2 handelt aber vom Ausrotten von Wagen und Rossen. Keine Option nennt 'von einem Meer bis ans andere'. Außerdem schreiben DE-Option 2 ('Er wird…') und die EN-Frage ('What will the King cut off') das Abtun dem König zu. Laut Luther und KJV tut es aber der HERR ('ich will … abtun' / 'I will cut off'). Korrektur: Frage und Lösung neu formulieren, z. B. 'Was will der HERR nach Sach 9:10 abtun?' mit der Lösung 'Die Wagen von Ephraim und die Rosse von Jerusalem; der Streitbogen wird zerbrochen'. EN entsprechend: 'What will the LORD cut off…'.</sub>

---

### 📄 `40_matthaeus.json` (10)

#### `mt_034` · Inhaltlicher Fehler

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die markierte DE-Lösung sagt, falsche Propheten seien 'an ihren guten Früchten' zu erkennen. Der Text sagt nur 'an ihren Früchten', und gemeint sind gerade schlechte Früchte (der faule Baum bringt böse Früchte). Der Spieler wird damit falsch belehrt.

**Aktuell DE** · _Matthäus 7:15-20_  
Woran lassen sich falsche Propheten nach den Worten Jesu erkennen?

- ⬜ An ihren Prachtgewändern
- ⬜ An Wundern und Zeichen
- ✅ **An ihren guten Früchten** ← _als richtig markiert_
- ⬜ An der Schar der Jünger

> 📖 **Beleg:** DE-Option 2: 'An ihren guten Früchten' – DE-TEXT: 'An ihren Früchten sollt ihr sie erkennen … der faule Baum aber bringt böse Früchte'

> ✏️ **Korrekturvorschlag:** Option 2: 'An ihren Früchten'

<sub>🔎 Gegenprüfung: Bestätigt. Laut Schlachter-Text gilt 'An ihren Früchten sollt ihr sie erkennen' (V. 16, 20), und vom faulen Baum heißt es, er bringe böse Früchte. Mit 'An ihren guten Früchten' ist die markierte Lösung sachlich falsch. Korrektur: 'An ihren Früchten'. EN ist korrekt.</sub>

---

#### `mt_069` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt, warum Petrus zu sinken begann (Wind/Furcht). EN fragt, wie Jesus in der vierten Nachtwache zu den Jüngern kam. Das ist eine andere Frage, und die Antwort steht in V. 25, nicht in 14:29-31.

**Aktuell DE** · _Matthäus 14:29-31_  
Warum begann Petrus zu sinken, als er auf dem Wasser ging?

- ⬜ Ein großer Fisch hielt ihn an den Füßen fest und zog ihn hinab
- ✅ **Er sah den starken Wind und fürchtete sich** ← _als richtig markiert_
- ⬜ Jesus wandte sich von ihm ab und ließ ihn allein auf dem Wasser
- ⬜ Sein nasses Gewand wurde zu schwer, und er verlor das Gleichgewicht

**Aktuell EN** · _Matthew 14:29-31_  
How did Jesus come unto His disciples in the fourth watch of the night on the sea?

- ⬜ In a Roman galley
- ✅ **Walking on the sea** ← _als richtig markiert_
- ⬜ Borne up by angels
- ⬜ In a chariot of fire

> 📖 **Beleg:** DE: "Warum begann Petrus zu sinken ...?" [x] "Er sah den starken Wind und fürchtete sich"; EN: "How did Jesus come unto His disciples in the fourth watch..." [x] "Walking on the sea"; KJV 14:30 "when he saw the wind boisterous, he was afraid"

> ✏️ **Korrekturvorschlag:** EN: "Why did Peter begin to sink when he walked on the water?", Index 1 = "He saw the wind boisterous, and was afraid"; Distraktoren analog zu DE (great fish held him / Jesus turned away / wet garment too heavy).

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Frage (Jesus kommt in der vierten Nachtwache auf dem Meer) gehört zu V. 25 und nicht zu 14:29-31. Inhaltlich ist die EN-Antwort zwar richtig, sie passt aber nicht zur DE-Frage und nicht zur Stelle. Korrektur wie vorgeschlagen.</sub>

---

#### `mt_072` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** In der EN-Fassung ist Option 0 (Essen mit ungewaschenen Händen) als richtig markiert. Nach V. 11 und V. 20 ist genau das falsch. Richtig ist Option 1. Die DE-Lösung (Index 0) ist inhaltlich korrekt, die EN-Optionen sind aber anders sortiert.

**Aktuell EN** · _Matthew 15:10-20_  
What defileth a man according to the teaching of Jesus in Matthew 15:11?

- ✅ **Eating food with unwashen hands at table** ← _als richtig markiert_
- ⬜ Not that which goeth into the mouth; but that which cometh out
- ⬜ Touching the dead body of an unclean beast
- ⬜ Walking in the way of the Gentiles and Samaritans

> 📖 **Beleg:** KJV 15:20 "but to eat with unwashen hands defileth not a man"; EN [x] 0: "Eating food with unwashen hands at table"

> ✏️ **Korrekturvorschlag:** EN-correctAnswers auf 1 setzen ("Not that which goeth into the mouth; but that which cometh out") oder die EN-Optionen in die Reihenfolge der DE-Optionen bringen, sodass Index 0 = "That which cometh out of the mouth, from the heart".

<sub>🔎 Gegenprüfung: Bestätigt. Als EN-Lösung ist Option 0 'Eating food with unwashen hands' markiert, was V. 20 ('to eat with unwashen hands defileth not a man') direkt widerspricht. Richtig ist EN-Option 1. Korrektur: EN correctAnswers auf 1 setzen oder die Optionen tauschen.</sub>

---

#### `mt_073` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** In der EN-Fassung ist Option 1 "Her noble lineage from ancient kings" als richtig markiert. Jesus lobt aber ihren Glauben (V. 28). Richtig wäre EN-Option 2. In DE ist Index 1 = "Ihr beharrlicher Glaube", die Indizes stimmen also nicht überein.

**Aktuell EN** · _Matthew 15:21-28_  
What did Jesus praise in the woman of Canaan whose daughter was vexed with a devil?

- ⬜ Her great alms to the poor of Israel
- ✅ **Her noble lineage from ancient kings** ← _als richtig markiert_
- ⬜ Her persistent and great faith
- ⬜ Her knowledge of the holy scriptures

> 📖 **Beleg:** KJV 15:28 "O woman, great is thy faith"; EN [x] 1: "Her noble lineage from ancient kings"

> ✏️ **Korrekturvorschlag:** EN-Optionen 1 und 2 tauschen: Index 1 = "Her persistent and great faith", Index 2 = "Her noble lineage from ancient kings".

<sub>🔎 Gegenprüfung: Bestätigt. Als EN-Lösung ist Option 1 'Her noble lineage' markiert, laut V. 28 lobt Jesus aber ihren Glauben ('great is thy faith'). Korrektur: EN-Optionen 1 und 2 tauschen oder correctAnswers auf 2 setzen.</sub>

---

#### `mt_075` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** In der EN-Fassung ist "Three baskets full" als richtig markiert. Laut Text waren es sieben Körbe (EN-Option 1). In DE steht "Sieben Körbe" an Index 3.

**Aktuell EN** · _Matthew 15:37_  
How many baskets full of broken meat were taken up after the four thousand were fed?

- ⬜ Twelve baskets full
- ⬜ Seven baskets full
- ⬜ Ten baskets full
- ✅ **Three baskets full** ← _als richtig markiert_

> 📖 **Beleg:** KJV 15:37 "of the broken meat that was left seven baskets full"; EN [x] 3: "Three baskets full"

> ✏️ **Korrekturvorschlag:** EN-Optionen 1 und 3 tauschen: Index 1 = "Three baskets full", Index 3 = "Seven baskets full".

<sub>🔎 Gegenprüfung: Bestätigt. Als EN-Lösung ist 'Three baskets full' markiert, laut KJV 15:37 waren es 'seven baskets full' (EN-Option 1). Korrektur: Optionen 1 und 3 tauschen.</sub>

---

#### `mt_077` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** In der EN-Fassung ist "Thou art John the Baptist risen from the dead" als Bekenntnis des Petrus markiert. Petrus bekennt aber: "Thou art the Christ" (EN-Option 2). In DE ist Index 1 korrekt der Christus.

**Aktuell EN** · _Matthew 16:13-17_  
What confession did Simon Peter make at Caesarea Philippi in answer to Jesus?

- ⬜ Thou art the prophet Elijah who was to appear
- ✅ **Thou art John the Baptist risen from the dead** ← _als richtig markiert_
- ⬜ Thou art the Christ, the Son of the living God
- ⬜ Thou art Jeremiah or one of the ancient prophets

> 📖 **Beleg:** KJV 16:16 "Simon Peter answered and said, Thou art the Christ, the Son of the living God"; EN [x] 1: "Thou art John the Baptist risen from the dead"

> ✏️ **Korrekturvorschlag:** EN-Optionen 1 und 2 tauschen: Index 1 = "Thou art the Christ, the Son of the living God", Index 2 = "Thou art John the Baptist risen from the dead".

<sub>🔎 Gegenprüfung: Bestätigt. Als EN-Lösung ist 'John the Baptist risen from the dead' markiert. Das ist eine Volksmeinung aus V. 14. Petrus bekennt in V. 16 'Thou art the Christ'. Korrektur: EN-Optionen 1 und 2 tauschen.</sub>

---

#### `mt_081` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt, was mit der Gestalt Jesu bei der Verklärung geschah (Angesicht wie die Sonne). EN fragt, welche zwei Gestalten erschienen (Mose und Elias). Das ist der Inhalt von V. 3, nicht von 17:1-2. Die EN-Fassung scheint um eine Frage verrutscht.

**Aktuell DE** · _Matthäus 17:1-2_  
Was geschah mit der Gestalt Jesu bei der Verklärung auf dem Berg?

- ⬜ Er fastete drei Tage im Nebel
- ✅ **Sein Angesicht leuchtete wie die Sonne** ← _als richtig markiert_
- ⬜ Er schwebte über den Jüngern
- ⬜ Engel umgaben ihn mit Schwertern

**Aktuell EN** · _Matthew 17:1-2_  
Which two figures appeared talking with Jesus upon the holy mount of transfiguration?

- ⬜ Abraham and Isaac
- ✅ **Moses and Elias** ← _als richtig markiert_
- ⬜ David and Solomon
- ⬜ Samuel and Daniel

> 📖 **Beleg:** DE [x] "Sein Angesicht leuchtete wie die Sonne"; EN: "Which two figures appeared talking with Jesus..." [x] "Moses and Elias"; KJV 17:2 "his face did shine as the sun"

> ✏️ **Korrekturvorschlag:** EN: "What happened to the appearance of Jesus at the transfiguration?", Index 1 = "His face did shine as the sun"; Distraktoren: He fasted three days in a cloud / He was lifted above the disciples / Angels surrounded him with swords.

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach Mose und Elias (17:3) statt nach der Verklärung des Angesichts (17:2). Die EN-Fragen sind um eins verrutscht. Korrektur: EN 'What happened to the appearance of Jesus...', Index 1 = 'His face did shine as the sun'.</sub>

---

#### `mt_082` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach Mose und Elia (17:3). EN fragt nach dem Leiden des mondsüchtigen Knaben (17:15). Das ist eine andere Frage, und sie steht nicht in der angegebenen Stelle 17:3.

**Aktuell DE** · _Matthäus 17:3_  
Welche zwei Personen erschienen bei der Verklärung und redeten mit Jesus?

- ⬜ Abraham und Isaak
- ⬜ David und Salomo
- ✅ **Mose und Elia** ← _als richtig markiert_
- ⬜ Noah und Daniel

**Aktuell EN** · _Matthew 17:3_  
What affliction did the lunatic child have whom the disciples could not cure?

- ⬜ He was blind from his mother's womb and begged
- ⬜ He was sick of the palsy and lay bedridden
- ✅ **He was lunatick, sore vexed, and fell oft into fire and water** ← _als richtig markiert_
- ⬜ He was a leper dwelling in the caves of the mountains

> 📖 **Beleg:** DE [x] "Mose und Elia"; EN: "What affliction did the lunatic child have..." [x] "He was lunatick, sore vexed..."; KJV 17:3 "there appeared unto them Moses and Elias talking with him"

> ✏️ **Korrekturvorschlag:** EN: "Which two persons appeared and talked with Jesus at the transfiguration?", Optionen: Abraham and Isaac / David and Solomon / [x] Moses and Elias / Noah and Daniel.

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach dem Leiden des mondsüchtigen Knaben (17:15), die Stelle ist aber 17:3. Korrektur: EN-Frage zu Mose und Elias, mit 'Moses and Elias' an Index 2 wie in DE.</sub>

---

#### `mt_105` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt etwas völlig anderes als DE. DE fragt, womit Jesus sich vergleicht (verworfener Stein/Eckstein), EN, was die Weingärtner mit dem Sohn taten. Zudem ist in EN die falsche Option 1 ("They fled ... into the desert") markiert; richtig wäre Option 2. Die Antwort auf die EN-Frage steht außerdem in V. 39, nicht in 21:42-44.

**Aktuell DE** · _Matthäus 21:42-44_  
Womit vergleicht Sich Jesus am Schluss des Gleichnisses von den Weingärtnern?

- ⬜ Mit der Rebe am Weinstock, die reiche Frucht bringt und immer bei ihm bleibt
- ✅ **Mit dem Stein, den die Bauleute verworfen haben und der zum Eckstein geworden ist** ← _als richtig markiert_
- ⬜ Mit dem Zaun um den Weinberg, der alle Feinde fernhält und die Reben schützt
- ⬜ Mit dem treuen Knecht auf dem Feld, der den Herrn erwartet und wachsam bleibt

**Aktuell EN** · _Matthew 21:42-44_  
What did the wicked husbandmen do when the lord sent his son to receive the fruits?

- ⬜ They received him with honour and delivered the fruits to him
- ✅ **They fled out of the vineyard into the desert wilderness** ← _als richtig markiert_
- ⬜ They caught him, and cast him out, and slew him
- ⬜ They set him upon the judgment seat as their lawful master

> 📖 **Beleg:** DE: "Womit vergleicht Sich Jesus ... ?" [x] Stein/Eckstein; EN: "What did the wicked husbandmen do when the lord sent his son..." [x] 1: "They fled out of the vineyard into the desert wilderness"; KJV 21:42 "The stone which the builders rejected..."

> ✏️ **Korrekturvorschlag:** EN an DE angleichen: "To what did Jesus liken himself at the end of the parable of the husbandmen?", richtig an Index 1: "The stone which the builders rejected, the same is become the head of the corner". Dazu passende Distraktoren (vine branch / hedge / faithful servant).

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt etwas anderes (was mit dem Sohn geschah, V. 39 und damit außerhalb von 21:42-44), und markiert ist zudem das falsche 'They fled...'. Nach dem Text wäre Option 2 richtig. Korrektur: EN an die DE-Frage angleichen (Stein/Eckstein an Index 1).</sub>

---

#### `mt_110` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Jesu Frage über David (Mt 22:42-45), DE nach dem zweiten Gebot (Nächstenliebe). Die Stelle 22:39-40 deckt die EN-Frage nicht ab. Außerdem ist in EN "Why did David build an altar upon the threshingfloor?" markiert; richtig wäre Option 1 "If David then call him Lord, how is he his son?".

**Aktuell DE** · _Matthäus 22:39-40_  
Welches zweite Gebot ist dem ersten Gebot der Gottesliebe gleichgestellt?

- ⬜ Du sollst Vater und Mutter ehren, damit du lange lebst
- ⬜ Du sollst nicht stehlen und nicht falsch Zeugnis reden
- ✅ **Du sollst deinen Nächsten lieben wie dich selbst** ← _als richtig markiert_
- ⬜ Du sollst den Zehnten geben von allen deinen Einkünften

**Aktuell EN** · _Matthew 22:39-40_  
With which question concerning David did Jesus silence the Pharisees in Matthew 22:42-45?

- ⬜ Why did David eat the shewbread in the house of God?
- ⬜ If David then call him Lord, how is he his son?
- ✅ **Why did David build an altar upon the threshingfloor?** ← _als richtig markiert_
- ⬜ How did David slay the Philistine without sword or spear?

> 📖 **Beleg:** DE: "Welches zweite Gebot ..." [x] Nächster wie dich selbst; EN: "With which question concerning David..." [x] 2: "Why did David build an altar upon the threshingfloor?"; KJV 22:39 "Thou shalt love thy neighbour as thyself"

> ✏️ **Korrekturvorschlag:** EN: "Which second commandment is like unto the first?", Index 2 = "Thou shalt love thy neighbour as thyself"; Distraktoren: Honour thy father and mother / Thou shalt not steal nor bear false witness / Bring all the tithes.

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach Jesu Frage über David (22:42-45), was außerhalb der Stelle 22:39-40 liegt. Markiert ist zudem das falsche 'altar upon the threshingfloor', richtig wäre Index 1. Korrektur: EN an DE angleichen (zweites Gebot, 'love thy neighbour as thyself' an Index 2).</sub>

---

### 📄 `42_lukas.json` (3)

#### `lk_024` · Mehrere richtig

🔴 **hoch** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Distraktor 2 nennt 'Matthäus' als Zöllner. Matthäus ist nach Mt 9,9 (vgl. Mk 2,14) derselbe Zöllner, den Jesus an der Zollstätte mit 'Folge mir nach!' berief, also Levi. Die Option ist deshalb nicht eindeutig falsch. Dazu kommt: Distraktor 3 nennt Barabbas einen 'Zöllner im Hafen', was sachlich irreführt.

**Aktuell DE** · _Lukas 5:27-28_  
Welchen Zöllner rief Jesus mit den Worten „Folge mir nach!“?

- ✅ **Levi, den Zöllner an der Zollstätte** ← _als richtig markiert_
- ⬜ Zachäus, den Oberzöllner an der Straße nach Jericho
- ⬜ Matthäus aus Nain, den Zöllner an der Stadtmauer
- ⬜ Barabbas aus der Gegend, den Zöllner im Hafen

> 📖 **Beleg:** [ ] 2: Matthäus aus Nain, den Zöllner an der Stadtmauer / Lk 5:27 'einen Zöllner namens Levi beim Zollhaus sitzen'

> ✏️ **Korrekturvorschlag:** Distraktoren an EN angleichen: '2: Simon, ein vornehmer und reicher Pharisäer', '3: Nikodemus, ein Oberster des Hohen Rates'

<sub>🔎 Gegenprüfung: Trifft zu. Nach Mt 9,9 ruft Jesus Matthäus an der Zollstätte mit 'Folge mir nach!', und die Frage schränkt das nicht auf Lukas ein. Matthäus/Levi ist also eine echte Doppellösung; die erfundenen Zusätze 'aus Nain'/'an der Stadtmauer' heben das nur halb auf. Der Teil zu Barabbas ist dagegen kein Mangel: Ein Distraktor darf sachlich falsch sein. Korrektur: DE 2/3 an EN angleichen ('Simon, ein vornehmer und reicher Pharisäer' / 'Nikodemus, ein Oberster des Hohen Rates').</sub>

---

#### `lk_042` · Mehrere richtig

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Laut Lk 9:7-8 sagten 'etliche', Johannes sei auferstanden, andere aber, Elia sei erschienen. Damit ist Option 0 (Elia) ebenso ein Gerücht wie die markierte Antwort. Die EN-Frage ('Who was it said by some that Jesus was') lässt beide Optionen zu. Außerdem stimmt die DE-Frage nicht mit Lukas überein: Herodes hielt Jesus dort gerade nicht für Johannes ('Johannes habe ich enthauptet; wer ist aber der …?').

**Aktuell DE** · _Lukas 9:7-9_  
Für wen hielt Herodes Antipas nach den Gerüchten Jesus?

- ⬜ Dass er der wiedergekommene Elia sei, der das Volk Israel sammeln solle
- ⬜ Dass er der König der Juden sei, der Rom bekämpfen werde
- ✅ **Dass Johannes der Täufer von den Toten auferstanden sei** ← _als richtig markiert_
- ⬜ Dass er der Hohepriester des neuen Bundes sei und im Tempel diene

**Aktuell EN** · _Luke 9:7-9_  
Who was it said by some that Jesus was, causing Herod the tetrarch perplexity?

- ⬜ That Elias had appeared again to gather the people of Israel
- ⬜ That he was the king of the Jews who would fight against Rome
- ✅ **That John the Baptist was risen from the dead** ← _als richtig markiert_
- ⬜ That he was the high priest of the new covenant in the temple

> 📖 **Beleg:** DE-TEXT V.7-9: 'weil von etlichen gesagt wurde, Johannes sei von den Toten auferstanden, von etlichen aber, Elia sei erschienen … Johannes habe ich enthauptet; wer ist aber der …'

> ✏️ **Korrekturvorschlag:** Frage: 'Welches Gerücht über Jesus brachte Herodes Antipas laut einigen besonders in Verlegenheit, sodass er sagte: Johannes habe ich enthauptet?' Besser noch Option 0 durch eine Aussage ersetzen, die im Text nicht vorkommt, z. B. 'Dass er der verheißene Hohepriester aus Aarons Haus sei'. EN entsprechend: 'That he was a priest of the house of Aaron'.

<sub>🔎 Gegenprüfung: Der Befund stimmt. Nach Lk 9:7-8 sagten 'etliche', Johannes sei auferstanden, andere aber, Elia sei erschienen. Damit ist Option 0 (Elia) ebenfalls ein im Text genanntes Gerücht. Der Zusatz 'das Volk Israel sammeln' ändert daran wenig. Die DE-Frage 'Für wen hielt Herodes … Jesus?' widerspricht außerdem V.9, denn Herodes fragt dort ja gerade, wer das ist. Korrektur: Option 0 durch ein Gerücht ersetzen, das im Text nicht vorkommt, und die DE-Frage umformulieren, z. B. 'Welches Gerücht beantwortete Herodes mit den Worten: Johannes habe ich enthauptet?'</sub>

---

#### `lk_071` · Inhaltlicher Fehler

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage will wissen, wie der Hirte auf den Fund reagiert. Die DE-Optionen handeln aber von Freude im Himmel und von Belohnungen. Die markierte Antwort 'Mehr Freude über einen bußfertigen Sünder' ist die Anwendung aus V.7 und nicht die Reaktion des Hirten (V.5-6: Er legt es auf die Schulter und freut sich). Die EN-Optionen passen dagegen zur Frage. DE und EN weichen also voneinander ab.

**Aktuell DE** · _Lukas 15:3-7_  
Wie reagiert der Hirte im Gleichnis bei dem Fund des verlorenen Schafes?

- ⬜ Große Ehre für Gerechte, die das Gesetz halten
- ⬜ Reiche Belohnung für treue Knechte im Himmel
- ⬜ Hohen Lohn bei der Auferstehung der Gerechten
- ✅ **Mehr Freude über einen bußfertigen Sünder** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT V.5: 'Und wenn er es gefunden hat, nimmt er es auf seine Schulter mit Freuden'

> ✏️ **Korrekturvorschlag:** DE-Optionen an EN anpassen: 0 'Er trieb es mit Schlägen zurück in den Pferch', 1 'Er verkaufte es auf dem Markt', 2 'Er sperrte es dreißig Tage ein', 3 [x] 'Er legte es mit Freuden auf seine Schultern'

<sub>🔎 Gegenprüfung: Der Befund stimmt. Die DE-Frage fragt nach der Reaktion des Hirten (V.5: Er legt das Schaf mit Freuden auf seine Schulter). Die markierte DE-Antwort ist aber die Anwendung aus V.7 und damit für die gestellte Frage sachlich falsch. Die DE-Distraktoren passen ebenfalls nicht zur Frage. EN ist in sich stimmig. Die DE-Optionen sollten an EN angeglichen werden.</sub>

---

### 📄 `43_johannes.json` (1)

#### `joh_101` · Mehrere richtig

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Der EN-Distraktor 'lake of Gennesaret' ist derselbe See wie der See von Tiberias. Damit sind zwei Optionen richtig. In DE steht an dieser Stelle 'Totes Meer'.

**Aktuell EN** · _John 21:1-6_  
At what sea did Jesus show himself again unto the disciples when they were fishing?

- ⬜ At the lake of Gennesaret
- ✅ **At the sea of Tiberias** ← _als richtig markiert_
- ⬜ At the Salt Sea in the plain
- ⬜ At the river of Jordan

> 📖 **Beleg:** EN: [ ] 'At the lake of Gennesaret' / [x] 'At the sea of Tiberias'

> ✏️ **Korrekturvorschlag:** Option 0 ersetzen durch 'At the Salt Sea' / 'At the Dead Sea' oder 'At the Great Sea'.

<sub>🔎 Gegenprüfung: Bestätigt: 'Lake of Gennesaret' (Lk 5:1) und 'Sea of Tiberias' bezeichnen denselben See, damit sind zwei Optionen richtig. Option 0 ersetzen, z. B. durch 'At the Dead Sea'. Option 2 ist schon 'Salt Sea', daher besser 'Great Sea' oder 'Red Sea' wählen.</sub>

---

### 📄 `44_apostelgeschichte.json` (64)

#### `apg_007` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'beside themselves in trance' als richtig. Laut KJV ist 'full of new wine' richtig (Index 1). Im ganzen EN-Teil der Apostelgeschichte wurden die Lösungsindizes offenbar aus DE übernommen, obwohl die EN-Optionen anders angeordnet sind.

**Aktuell EN** · _Acts 2:13_  
What mocking word did others speak when the disciples spake with other tongues?

- ⬜ These men are drunken with wine from Rome
- ⬜ These men are full of new wine
- ⬜ These men have eaten the strange bread
- ✅ **These men are beside themselves in trance** ← _als richtig markiert_

> 📖 **Beleg:** KJV 2:13: 'These men are full of new wine.'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [1] setzen ('These men are full of new wine').

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 'beside themselves in trance', KJV 2:13 'full of new wine' = Index 1. Die Quelldatei en/44 hat correctAnswers [3], identisch mit DE. Das bestätigt, dass die DE-Indizes übernommen wurden. Korrektur: EN [1].</sub>

---

#### `apg_008` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert Isaiah als richtig. Petrus zitiert aber Joel (EN Index 1).

**Aktuell EN** · _Acts 2:16-21_  
From which prophet did Peter quote on the day of Pentecost concerning the pouring out of the Spirit?

- ✅ **The prophet Isaiah** ← _als richtig markiert_
- ⬜ The prophet Joel
- ⬜ The prophet Ezekiel
- ⬜ The prophet Daniel

> 📖 **Beleg:** KJV 2:16: 'spoken by the prophet Joel'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [1] setzen ('The prophet Joel').

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=0 Isaiah, KJV 2:16 Joel = Index 1. Korrektur: EN [1].</sub>

---

#### `apg_009` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN stellt eine andere Frage als DE (Antwort des Petrus statt: wie viele Seelen hinzugetan wurden). Diese Antwort steht nicht in Apg 2:41, sondern in 2:38. Zudem ist die falsche Option markiert ('Fast forty days'), richtig wäre Index 3 ('Repent ...').

**Aktuell DE** · _Apostelgeschichte 2:41_  
Wie viele Seelen schlossen sich nach der Predigt des Petrus der Gemeinde an?

- ⬜ Etwa eintausend Menschen
- ✅ **Etwa dreitausend Seelen** ← _als richtig markiert_
- ⬜ Etwa fünftausend Gläubige
- ⬜ Etwa siebenhundert Männer

**Aktuell EN** · _Acts 2:41_  
What did Peter answer the people when they were pricked in their heart?

- ⬜ Bring your tithes and gifts unto the temple treasury
- ✅ **Fast forty days in sackcloth and mourn before God** ← _als richtig markiert_
- ⬜ Depart out of Jerusalem into the hills of Judaea
- ⬜ Repent, and be baptized every one of you in Jesus' name

> 📖 **Beleg:** DE: 'Wie viele Seelen ...' / EN: 'What did Peter answer ...' [x] 'Fast forty days in sackcloth'

> ✏️ **Korrekturvorschlag:** EN an DE angleichen: 'How many souls were added unto them that same day?' mit [x] 'About three thousand souls'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach der Antwort des Petrus (2:38), die Stelle 2:41 nennt aber dreitausend Seelen. Markiert ist 'Fast forty days' (Index 1), das ist falsch. Angleichung an DE wie vorgeschlagen.</sub>

---

#### `apg_010` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'Kept their goods in secret chests' als richtig. Richtig ist Index 0.

**Aktuell EN** · _Acts 2:44-45_  
How did the early church at Jerusalem deal with their possessions and goods?

- ⬜ Sold their possessions, and parted them to all men
- ⬜ Delivered all their gold and silver unto the priests
- ✅ **Kept their goods in secret chests in their own houses** ← _als richtig markiert_
- ⬜ Paid great tribute money unto the Roman governor

> 📖 **Beleg:** KJV 2:45: 'sold their possessions and goods, and parted them to all men'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=2 'secret chests', richtig ist Index 0 nach KJV 2:45. Korrektur: EN [0].</sub>

---

#### `apg_011` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'At the Valley gate' als richtig. Richtig ist 'the gate Beautiful' (Index 2).

**Aktuell EN** · _Acts 3:1-2_  
At which gate of the temple was the man lame from his mother's womb laid daily?

- ⬜ At the Water gate
- ⬜ At the Sheep gate
- ⬜ At the gate Beautiful
- ✅ **At the Valley gate** ← _als richtig markiert_

> 📖 **Beleg:** KJV 3:2: 'the gate of the temple which is called Beautiful'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [2] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 'Valley gate', KJV 3:2 'Beautiful' = Index 2. Korrektur: EN [2].</sub>

---

#### `apg_015` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der aufgebrachten Partei (Apg 4:1-2), DE nach Petrus' Bezeichnung für Jesus (Fürst des Lebens). Außerdem ist 'Herodians' markiert, laut Text waren es die Sadduzäer (Index 1).

**Aktuell DE** · _Apostelgeschichte 3:13-15_  
Wie bezeichnete Petrus den Herrn Jesus Christus vor den Versammelten im Tempel?

- ⬜ Den Erben der Königreiche
- ⬜ Den Gelehrten der Tora
- ⬜ Den Schöpfer der Welt
- ✅ **Den Fürsten des Lebens** ← _als richtig markiert_

**Aktuell EN** · _Acts 3:13-15_  
Which religious party in Jerusalem was grieved that the apostles preached through Jesus the resurrection?

- ⬜ The party of the Pharisees
- ⬜ The Sadducees
- ⬜ The sect of the Essenes
- ✅ **The party of the Herodians** ← _als richtig markiert_

> 📖 **Beleg:** DE: 'Den Fürsten des Lebens' / EN [x] 'The party of the Herodians'; KJV 3:15 'killed the Prince of life'

> ✏️ **Korrekturvorschlag:** EN: 'By what title did Peter call Jesus whom they had killed?' – [x] 'The Prince of life'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach dem Inhalt von 4:1-2, die Stelle ist aber 3:13-15. Markiert ist 'Herodians' (Index 3), richtig wären die Sadducees (Index 1). Angleichung an DE ('Prince of life', KJV 3:15).</sub>

---

#### `apg_017` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Apg 4:13 (ungelehrte Leute), DE nach der Zahl von fünftausend Männern. Zudem ist 'rich scribes of the temple' markiert, richtig wäre Index 0.

**Aktuell DE** · _Apostelgeschichte 4:4_  
Wie groß war die Zahl der gläubig gewordenen Männer nach der Rede im Tempel?

- ⬜ Etwa dreitausend Männer
- ✅ **Etwa fünftausend Männer** ← _als richtig markiert_
- ⬜ Etwa zehntausend Männer
- ⬜ Etwa zweitausend Männer

**Aktuell EN** · _Acts 4:4_  
What did the rulers of the council perceive concerning Peter and John when they saw their boldness?

- ⬜ That they were unlearned and ignorant men
- ✅ **That they were rich scribes of the temple** ← _als richtig markiert_
- ⬜ That they were soldiers of the king's guard
- ⬜ That they were foreign doctors from Babylon

> 📖 **Beleg:** DE: 'Etwa fünftausend Männer' / EN [x] 'That they were rich scribes of the temple'

> ✏️ **Korrekturvorschlag:** EN: 'What was the number of the men that believed?' – [x] 'About five thousand'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 4:13, die Stelle ist 4:4. Markiert ist 'rich scribes' (Index 1), richtig wäre 'unlearned and ignorant men' (Index 0).</sub>

---

#### `apg_019` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Antwort von Petrus und Johannes (Apg 4:19), DE nach dem Eckstein (4:11). Zudem ist 'appeal unto the Roman governor' markiert, richtig wäre Index 1.

**Aktuell DE** · _Apostelgeschichte 4:11_  
Welcher Begriff bezeichnet nach Psalm 118 den von den Bauleuten verworfenen Stein?

- ⬜ Er ist zum Stolperstein geworden
- ⬜ Er ist zum Gedenkstein geworden
- ⬜ Er ist zum Grundstein der Mauer geworden
- ✅ **Er ist zum Eckstein geworden** ← _als richtig markiert_

**Aktuell EN** · _Acts 4:11_  
What did Peter and John answer when commanded not to speak at all in the name of Jesus?

- ⬜ We will hold our peace until we depart unto the Gentiles
- ⬜ Whether it be right in the sight of God to hearken unto you, judge ye
- ⬜ We will ask the high priest to examine our doctrine in full
- ✅ **We will appeal unto the Roman governor for our protection** ← _als richtig markiert_

> 📖 **Beleg:** DE: 'Er ist zum Eckstein geworden' / EN [x] 'We will appeal unto the Roman governor'

> ✏️ **Korrekturvorschlag:** EN: 'What is the stone set at nought of the builders become?' – [x] 'The head of the corner'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 4:19, die Stelle ist 4:11. Markiert ist 'appeal unto the Roman governor' (Index 3), richtig wäre Index 1. Angleichung an DE ('head of the corner').</sub>

---

#### `apg_023` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'speak a word of blessing' als richtig. Richtig ist der Schatten des Petrus (Index 1).

**Aktuell EN** · _Acts 5:15-16_  
What miraculous benefit did the sick in Jerusalem hope for from Peter as he passed by?

- ⬜ That they might touch the hem of his garment in faith
- ⬜ At the least the shadow of Peter passing by might overshadow them
- ⬜ That he might anoint their foreheads with holy temple oil
- ✅ **That he might speak a word of blessing over their heads** ← _als richtig markiert_

> 📖 **Beleg:** KJV 5:15: 'at the least the shadow of Peter passing by might overshadow some of them'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [1] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 'word of blessing', richtig ist Index 1 (der Schatten, KJV 5:15). Korrektur: EN [1].</sub>

---

#### `apg_025` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Grundsatz der Apostel (Apg 5:29), DE nach Gamaliel. Zudem ist 'obey all the ordinances of the king' markiert, richtig wäre Index 0.

**Aktuell DE** · _Apostelgeschichte 5:34-39_  
Welcher berühmte Gesetzeslehrer riet dem Hohen Rat zur Besonnenheit?

- ⬜ Esra, der Schriftgelehrte und Priester
- ✅ **Gamaliel, ein Pharisäer und Gesetzeslehrer** ← _als richtig markiert_
- ⬜ Kaiphas, der Hohepriester und Schwiegersohn Hannas
- ⬜ Nikodemus, der Pharisäer und Ratsherr

**Aktuell EN** · _Acts 5:34-39_  
What famous principle did Peter and the other apostles proclaim before the council?

- ⬜ We ought to obey God rather than men
- ✅ **We must obey all the ordinances of the king** ← _als richtig markiert_
- ⬜ The law of the fathers must be kept above all
- ⬜ Peace with all rulers is our holy calling

> 📖 **Beleg:** DE: 'Gamaliel, ein Pharisäer' / EN [x] 'We must obey all the ordinances of the king'

> ✏️ **Korrekturvorschlag:** EN: 'Which doctor of the law counselled the council to refrain from these men?' – [x] 'Gamaliel, a Pharisee'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 5:29, die Stelle ist 5:34-39. Markiert ist 'ordinances of the king' (Index 1), richtig wäre Index 0. Angleichung an DE (Gamaliel).</sub>

---

#### `apg_026` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'forbidden to enter the inner courts' als richtig. Richtig ist Index 0 (Witwen übersehen).

**Aktuell EN** · _Acts 6:1-2_  
Why did a murmuring of the Grecians against the Hebrews arise in the early church?

- ⬜ Because their widows were neglected in the daily ministration
- ⬜ Because their young men were not chosen to preach the word
- ✅ **Because they were forbidden to enter the inner courts of Zion** ← _als richtig markiert_
- ⬜ Because they paid greater tribute money than the native Jews

> 📖 **Beleg:** KJV 6:1: 'because their widows were neglected in the daily ministration'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=2, richtig ist Index 0 (KJV 6:1, die Witwen wurden übersehen). Korrektur: EN [0].</sub>

---

#### `apg_030` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Apg 7:2 (wem Gott erschien), DE nach Stephanus' Angesicht (6:15). Zudem ist 'Unto Isaac' markiert, richtig wäre Abraham (Index 0).

**Aktuell DE** · _Apostelgeschichte 6:15_  
Wie erschien das Angesicht des Stephanus vor dem versammelten Hohen Rat?

- ⬜ Wie eine sonnige Flamme
- ⬜ Wie ein dunkles Gewölk
- ✅ **Wie das Angesicht eines Engels** ← _als richtig markiert_
- ⬜ Wie ein schreckliches Antlitz

**Aktuell EN** · _Acts 6:15_  
In Stephen's defense, unto whom did the God of glory appear in Mesopotamia?

- ⬜ Unto our father Abraham
- ⬜ Unto Noah the righteous
- ✅ **Unto Isaac on the mount** ← _als richtig markiert_
- ⬜ Unto Jacob at Bethel

> 📖 **Beleg:** DE: 'Wie das Angesicht eines Engels' / EN [x] 'Unto Isaac on the mount'

> ✏️ **Korrekturvorschlag:** EN: 'How did Stephen's face appear unto the council?' – [x] 'As it had been the face of an angel'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 7:2, die Stelle ist 6:15. Markiert ist 'Unto Isaac' (Index 2), richtig wäre Abraham (Index 0).</sub>

---

#### `apg_031` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Verheißung (Apg 7:5), DE nach dem Ort der Erscheinung (Mesopotamien, 7:2). Zudem ist 'Twelve palaces' markiert, das ist falsch.

**Aktuell DE** · _Apostelgeschichte 7:2_  
An welchem Ort erschien Gott dem Erzvater Abraham vor der Siedlung in Haran?

- ⬜ In Ägypten, ehe er in Kanaan wohnte
- ⬜ In Kanaan, ehe er nach Ägypten zog
- ⬜ In Beerscheba, ehe er in Gerar wohnte
- ✅ **In Mesopotamien, ehe er in Haran wohnte** ← _als richtig markiert_

**Aktuell EN** · _Acts 7:2_  
What did God promise to give unto Abraham for a possession, when as yet he had no child?

- ⬜ He promised that he would give it to him for a possession
- ⬜ All the silver and gold of the kings of Mesopotamia
- ⬜ A kingdom in the wilderness of Sinai for all his days
- ✅ **Twelve palaces of stone and cedar in the land of Canaan** ← _als richtig markiert_

> 📖 **Beleg:** DE [x] 'In Mesopotamien' / EN [x] 'Twelve palaces of stone and cedar'

> ✏️ **Korrekturvorschlag:** EN: 'Where did the God of glory appear unto Abraham before he dwelt in Charran?' – [x] 'In Mesopotamia'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 7:5, die Stelle ist 7:2. Markiert ist 'Twelve palaces' (Index 3), das ist falsch. Für die EN-Frage wäre Index 0 richtig. Angleichung an DE (Mesopotamia).</sub>

---

#### `apg_034` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Seelenzahl nach Ägypten (Apg 7:14), DE nach Stephanus' Vision (7:55-56). Zudem ist 'An hundred and twenty souls' markiert, laut KJV 7:14 sind es 'threescore and fifteen' (Index 0).

**Aktuell DE** · _Apostelgeschichte 7:55-56_  
Welche Erscheinung sah Stephanus unmittelbar vor seiner Steinigung?

- ⬜ Ein Heer feuriger Engel, das die Steiniger umringte
- ⬜ Einen Donner aus dem Himmel, der die Menge erschütterte
- ✅ **Den Himmel offen und den Menschensohn zur Rechten Gottes stehen** ← _als richtig markiert_
- ⬜ Das Bild des alten Tempels, wie er einst unter Salomo stand

**Aktuell EN** · _Acts 7:55-56_  
How many souls did Joseph call into Egypt when he sent for his father Jacob?

- ⬜ Threescore and fifteen souls
- ⬜ Seventy souls of Israel
- ✅ **An hundred and twenty souls** ← _als richtig markiert_
- ⬜ Fifty and five persons

> 📖 **Beleg:** DE [x] 'Den Himmel offen und den Menschensohn' / EN [x] 'An hundred and twenty souls'

> ✏️ **Korrekturvorschlag:** EN: 'What did Stephen see when he looked up stedfastly into heaven?' – [x] 'The heavens opened, and the Son of man standing on the right hand of God'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 7:14, die Stelle ist 7:55-56. Markiert ist 'An hundred and twenty' (Index 2), KJV 7:14 sagt 'threescore and fifteen' = Index 0.</sub>

---

#### `apg_035` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Moses' Bildung (Apg 7:22), DE nach Saulus bei den Kleidern (7:58). Zudem ist 'building of temples and pyramids' markiert, richtig wäre Index 1.

**Aktuell DE** · _Apostelgeschichte 7:58_  
Welcher junge Mann wachte bei der Steinigung des Stephanus über die Kleider?

- ⬜ Markus
- ⬜ Silas
- ⬜ Titus
- ✅ **Saulus** ← _als richtig markiert_

**Aktuell EN** · _Acts 7:58_  
In what was Moses learned in Egypt according to Stephen's speech?

- ⬜ In the warfare of the kings of Canaan and Syria
- ⬜ In all the wisdom of the Egyptians, mighty in words and deeds
- ⬜ In the trade of the merchants of Tyre and Sidon
- ✅ **In the building of temples and great pyramids of stone** ← _als richtig markiert_

> 📖 **Beleg:** DE [x] 'Saulus' / EN [x] 'In the building of temples and great pyramids of stone'

> ✏️ **Korrekturvorschlag:** EN: 'At whose feet did the witnesses lay down their clothes?' – [x] 'Saul'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 7:22, die Stelle ist 7:58. Markiert ist 'temples and pyramids' (Index 3), richtig wäre Index 1.</sub>

---

#### `apg_038` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Weg (Apg 8:26), DE nach dem Amt des Äthiopiers. Zudem ist 'Jerusalem to Jericho' markiert, richtig wäre 'unto Gaza' (Index 0).

**Aktuell DE** · _Apostelgeschichte 8:27_  
Welches Amt bekleidete der Mann aus Äthiopien am Hof der Königin Kandake?

- ⬜ Er war der Heerführer der Königin und befehligte ihre Truppen
- ⬜ Er war ein Priester im Tempel und diente dort am Altar
- ✅ **Er war der Schatzmeister der Königin Kandake** ← _als richtig markiert_
- ⬜ Er war der Statthalter einer Stadt am Nil und sprach Recht

**Aktuell EN** · _Acts 8:27_  
Unto what way was Philip commanded by the angel of the Lord to go toward the south?

- ⬜ The way from Jerusalem unto Gaza, which is desert
- ⬜ The highway from Damascus unto the coast of Joppa
- ✅ **The road that goeth down from Jerusalem to Jericho** ← _als richtig markiert_
- ⬜ The path through Samaria unto the sea of Galilee

> 📖 **Beleg:** DE [x] 'Schatzmeister der Königin Kandake' / EN [x] 'The road that goeth down from Jerusalem to Jericho'

> ✏️ **Korrekturvorschlag:** EN: 'What office did the eunuch hold under Candace?' – [x] 'He had the charge of all her treasure'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 8:26, die Stelle ist 8:27. Markiert ist 'Jerusalem to Jericho' (Index 2), richtig wäre Gaza (Index 0).</sub>

---

#### `apg_039` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'The prophet Daniel' als richtig. Der Kämmerer las Jesaja ('Esaias', Index 1).

**Aktuell EN** · _Acts 8:28-35_  
What scripture was the Ethiopian eunuch reading in his chariot?

- ⬜ The book of Psalms
- ⬜ The prophet Esaias
- ⬜ The law of Moses
- ✅ **The prophet Daniel** ← _als richtig markiert_

> 📖 **Beleg:** KJV 8:28: 'read Esaias the prophet'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [1] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 Daniel, KJV 8:28 'Esaias' = Index 1. Korrektur: EN [1].</sub>

---

#### `apg_041` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt, wo Philippus gefunden wurde (Apg 8:40), DE nach der Stadt der Bekehrung (Damaskus). Zudem ist 'At Caesarea' markiert, laut 8:40 wurde Philippus in Azotus gefunden.

**Aktuell DE** · _Apostelgeschichte 9:3-4_  
Nahe welcher Stadt erstrahlte das Himmelslicht bei der Bekehrung des Saulus?

- ⬜ Bei Jerusalem
- ✅ **Bei Damaskus** ← _als richtig markiert_
- ⬜ Bei Antiochia
- ⬜ Bei Cäsarea

**Aktuell EN** · _Acts 9:3-4_  
Where was Philip found after the Spirit of the Lord caught him away?

- ⬜ At Azotus
- ✅ **At Caesarea** ← _als richtig markiert_
- ⬜ At Joppa
- ⬜ At Damascus

> 📖 **Beleg:** DE [x] 'Bei Damaskus' / EN [x] 'At Caesarea'

> ✏️ **Korrekturvorschlag:** EN: 'Near what city did a light from heaven shine round about Saul?' – [x] 'Damascus'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 8:40, die Stelle ist 9:3-4. Markiert ist 'At Caesarea' (Index 1), laut 8:40 wäre es Azotus (Index 0).</sub>

---

#### `apg_042` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Reiseziel (9:3), DE nach drei Tagen Blindheit (9:9). Zudem ist 'Unto Antioch' markiert, richtig wäre Damaskus (Index 0).

**Aktuell DE** · _Apostelgeschichte 9:9_  
Wie viele Tage blieb Saulus nach der Himmelserscheinung blind und ohne Speise?

- ⬜ Sieben Tage lang
- ⬜ Vierzig Tage lang
- ✅ **Drei Tage lang** ← _als richtig markiert_
- ⬜ Zehn Tage lang

**Aktuell EN** · _Acts 9:9_  
Unto what city was Saul journeying when a light from heaven shined round about him?

- ⬜ Unto Damascus
- ⬜ Unto Jerusalem
- ✅ **Unto Antioch** ← _als richtig markiert_
- ⬜ Unto Tarsus

> 📖 **Beleg:** DE [x] 'Drei Tage lang' / EN [x] 'Unto Antioch'

> ✏️ **Korrekturvorschlag:** EN: 'How many days was Saul without sight, neither eating nor drinking?' – [x] 'Three days'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 9:3, die Stelle ist 9:9. Markiert ist 'Antioch' (Index 2), richtig wäre Damaskus (Index 0).</sub>

---

#### `apg_043` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Himmelsstimme (9:4), DE nach Hananias. Zudem ist 'depart into the wilderness' markiert, richtig wäre Index 0.

**Aktuell DE** · _Apostelgeschichte 9:10-17_  
Welcher Jünger in Damaskus wurde von Gott gesandt, um Saulus Hände aufzulegen?

- ⬜ Der Apostel Petrus aus Jerusalem
- ⬜ Barnabas, ein Levit aus Zypern
- ⬜ Philippus, der Evangelist aus Cäsarea
- ✅ **Hananias, ein Jünger in Damaskus** ← _als richtig markiert_

**Aktuell EN** · _Acts 9:10-17_  
What did the voice from heaven say unto Saul as he fell to the earth?

- ⬜ Saul, Saul, why persecutest thou me?
- ⬜ Saul, Saul, return unto the high priest
- ⬜ Saul, Saul, why dost thou break the law?
- ✅ **Saul, Saul, depart into the wilderness** ← _als richtig markiert_

> 📖 **Beleg:** DE [x] 'Hananias, ein Jünger in Damaskus' / EN [x] 'Saul, Saul, depart into the wilderness'

> ✏️ **Korrekturvorschlag:** EN: 'Which disciple at Damascus was sent to lay hands on Saul?' – [x] 'Ananias'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 9:4, die Stelle ist 9:10-17. Markiert ist 'depart into the wilderness' (Index 3), richtig wäre Index 0.</sub>

---

#### `apg_044` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Hananias (9:10-17), DE nach der Flucht im Korb (9:23-25). Zudem ist 'Barnabas' markiert, richtig wäre Ananias (Index 1).

**Aktuell DE** · _Apostelgeschichte 9:23-25_  
Wie entkam Saulus den nach seinem Leben trachtenden Juden in Damaskus?

- ✅ **In einem Korb ließen ihn die Jünger an der Stadtmauer hinab** ← _als richtig markiert_
- ⬜ Verkleidet als römischer Soldat durch das Haupttor
- ⬜ Durch ein geheimes Tor im Süden der Stadt
- ⬜ Unter dem Schutz der römischen Wachen

**Aktuell EN** · _Acts 9:23-25_  
Which disciple at Damascus was sent of the Lord to lay hands on Saul that he might receive sight?

- ✅ **Barnabas** ← _als richtig markiert_
- ⬜ Ananias
- ⬜ Agabus
- ⬜ Silas

> 📖 **Beleg:** DE [x] 'In einem Korb ...' / EN [x] 'Barnabas'

> ✏️ **Korrekturvorschlag:** EN: 'How did Saul escape the Jews at Damascus?' – [x] 'The disciples let him down by the wall in a basket'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach Ananias, die Stelle ist 9:23-25. Markiert ist Barnabas (Index 0), richtig wäre Ananias (Index 1).</sub>

---

#### `apg_047` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'A ladder set upon earth' (Jakobs Traum) als richtig. Richtig ist das Tuch mit allerlei Tieren (Index 0).

**Aktuell EN** · _Acts 10:9-16_  
What vision did Peter see upon the housetop about the sixth hour in Joppa?

- ⬜ A great sheet let down from heaven with all manner of beasts
- ⬜ A burning bush that was not consumed by the flame of fire
- ⬜ A golden candlestick with seven lamps burning before God
- ✅ **A ladder set upon earth, reaching unto the gate of heaven** ← _als richtig markiert_

> 📖 **Beleg:** KJV 10:11: 'as it had been a great sheet knit at the four corners'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 'ladder', richtig ist Index 0 (sheet, KJV 10:11). Korrektur: EN [0].</sub>

---

#### `apg_055` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem von Herodes getöteten Apostel (12:2), DE nach Saulus als Begleiter des Barnabas (11:25-26). Zudem ist 'Philip of Bethsaida' markiert, richtig wäre James (Index 0).

**Aktuell DE** · _Apostelgeschichte 11:25-26_  
Welcher Apostel begleitete Barnabas bei der Stärkung der Gemeinde in Antiochia?

- ⬜ Petrus
- ⬜ Johannes
- ⬜ Jakobus
- ✅ **Saulus** ← _als richtig markiert_

**Aktuell EN** · _Acts 11:25-26_  
Which apostle did Herod the king kill with the sword?

- ⬜ James the brother of John
- ⬜ Peter the apostle
- ⬜ Andrew the brother of Simon
- ✅ **Philip of Bethsaida** ← _als richtig markiert_

> 📖 **Beleg:** DE [x] 'Saulus' / EN [x] 'Philip of Bethsaida'

> ✏️ **Korrekturvorschlag:** EN: 'Whom did Barnabas seek at Tarsus and bring unto Antioch?' – [x] 'Saul'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 12:2, die Stelle ist 11:25-26. Markiert ist 'Philip of Bethsaida' (Index 3), richtig wäre James (Index 0).</sub>

---

#### `apg_056` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Fest der Festnahme des Petrus (12:3), DE nach der Hinrichtung des Jakobus (12:1-2). Zudem ist 'Pentecost' markiert, laut 12:3 war es 'the days of unleavened bread' (Index 1).

**Aktuell DE** · _Apostelgeschichte 12:1-2_  
Welcher Apostel wurde von König Herodes Agrippa I. mit dem Schwert hingerichtet?

- ✅ **Jakobus, der Bruder des Johannes** ← _als richtig markiert_
- ⬜ Petrus, der Fischer aus Bethsaida
- ⬜ Andreas, der Bruder des Simon Petrus
- ⬜ Matthäus, der ehemalige Zöllner

**Aktuell EN** · _Acts 12:1-2_  
At what feast was Peter apprehended and put into prison by Herod?

- ✅ **The feast of Pentecost** ← _als richtig markiert_
- ⬜ The days of unleavened bread
- ⬜ The feast of tabernacles
- ⬜ The feast of dedication

> 📖 **Beleg:** DE [x] 'Jakobus, der Bruder des Johannes' / EN [x] 'The feast of Pentecost'

> ✏️ **Korrekturvorschlag:** EN: 'Which apostle did Herod kill with the sword?' – [x] 'James the brother of John'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 12:3, die Stelle ist 12:1-2. Markiert ist Pentecost (Index 0), richtig wäre 'days of unleavened bread' (Index 1).</sub>

---

#### `apg_057` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'Two quaternions' als richtig. Laut KJV sind es vier (Index 0). Damit widerspricht EN auch der DE-Lösung.

**Aktuell EN** · _Acts 12:4_  
Unto how many quaternions of soldiers was Peter delivered to be kept in prison?

- ⬜ Four quaternions of soldiers
- ✅ **Two quaternions of soldiers** ← _als richtig markiert_
- ⬜ Six quaternions of soldiers
- ⬜ Eight quaternions of soldiers

> 📖 **Beleg:** KJV 12:4: 'delivered him to four quaternions of soldiers'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=1 'Two quaternions', KJV 12:4 sagt 'four' = Index 0. Korrektur: EN [0].</sub>

---

#### `apg_058` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'Lydia' als richtig. Richtig ist Rhoda (Index 0).

**Aktuell EN** · _Acts 12:13-14_  
What damsel came to hearken when Peter knocked at the door of the gate of Mary's house?

- ⬜ Rhoda
- ⬜ Tabitha
- ✅ **Lydia** ← _als richtig markiert_
- ⬜ Priscilla

> 📖 **Beleg:** KJV 12:13: 'a damsel came to hearken, named Rhoda'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=2 Lydia, KJV 12:13 sagt Rhoda = Index 0. Korrektur: EN [0].</sub>

---

#### `apg_061` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Zauberer in Paphos (13:6), DE nach der Insel Zypern (13:4). Zudem ist 'Simon' markiert, richtig wäre Barjesus (Index 0).

**Aktuell DE** · _Apostelgeschichte 13:4-5_  
Auf welcher Insel begann die erste Missionsreise von Barnabas und Saulus?

- ⬜ Auf Kreta
- ✅ **Auf Zypern** ← _als richtig markiert_
- ⬜ Auf Malta
- ⬜ Auf Rhodos

**Aktuell EN** · _Acts 13:4-5_  
What was the name of the sorcerer, a false prophet, at Paphos in Cyprus?

- ⬜ Barjesus
- ✅ **Simon** ← _als richtig markiert_
- ⬜ Alexander
- ⬜ Demetrius

> 📖 **Beleg:** DE [x] 'Auf Zypern' / EN [x] 'Simon'

> ✏️ **Korrekturvorschlag:** EN: 'Unto what island did Barnabas and Saul sail from Seleucia?' – [x] 'Cyprus'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 13:6, die Stelle ist 13:4-5. Markiert ist Simon (Index 1), richtig wäre Barjesus (Index 0). Angleichung an DE (Cyprus).</sub>

---

#### `apg_062` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Urteil über Elymas, DE nach dessen Namen. Zudem ist 'cast into the sea with a millstone' markiert, richtig wäre Index 0 (blind sein).

**Aktuell DE** · _Apostelgeschichte 13:8-11_  
Welcher Zauberer und falsche Prophet wurde auf Zypern mit Blindheit geschlagen?

- ⬜ Simon, der Zauberer
- ⬜ Barjesus, der Pharisäer
- ✅ **Elymas, der Zauberer** ← _als richtig markiert_
- ⬜ Alexander, der Schmied

**Aktuell EN** · _Acts 13:8-11_  
What judgment did Paul pronounce upon Elymas the sorcerer for seeking to turn away the deputy?

- ⬜ Thou shalt be blind, not seeing the sun for a season
- ⬜ Thou shalt fall down dead before all the people here
- ✅ **Thou shalt be cast into the sea with a great millstone** ← _als richtig markiert_
- ⬜ Thou shalt wander as a leper in the land of the Gentiles

> 📖 **Beleg:** EN [x] 'Thou shalt be cast into the sea with a great millstone'; KJV 13:11 'thou shalt be blind, not seeing the sun for a season'

> ✏️ **Korrekturvorschlag:** EN an DE angleichen ('Which sorcerer was smitten with blindness at Paphos?' – [x] 'Elymas the sorcerer'), mindestens aber correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach dem Urteil über Elymas statt nach seinem Namen. Markiert ist 'millstone' (Index 2), richtig ist Index 0 (KJV 13:11, blind). Mindestens EN [0] setzen.</sub>

---

#### `apg_065` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'They took up stones to cast at Paul' als richtig. Richtig ist Index 0 ('They were glad ...').

**Aktuell EN** · _Acts 13:46-48_  
How did the Gentiles at Antioch in Pisidia receive Paul's word when the Jews contradicted?

- ⬜ They were glad, and as many as were ordained to eternal life believed
- ✅ **They took up stones to cast at Paul and Barnabas in the synagogue** ← _als richtig markiert_
- ⬜ They brought gifts of gold and silver to offer unto the apostles
- ⬜ They appealed unto the Roman governor to banish them from the city

> 📖 **Beleg:** KJV 13:48: 'they were glad, and glorified the word of the Lord: and as many as were ordained to eternal life believed'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=1 'took up stones', richtig ist Index 0 (KJV 13:48). Korrektur: EN [0].</sub>

---

#### `apg_067` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'Saturn; Vulcan' als richtig. Richtig ist 'Jupiter; Mercurius' (Index 0).

**Aktuell EN** · _Acts 14:11-13_  
What names of heathen gods did the people of Lystra give unto Barnabas and Paul?

- ⬜ They called Barnabas, Jupiter; and Paul, Mercurius
- ⬜ They called Barnabas, Apollo; and Paul, Hercules
- ⬜ They called Barnabas, Mars; and Paul, Neptune
- ✅ **They called Barnabas, Saturn; and Paul, Vulcan** ← _als richtig markiert_

> 📖 **Beleg:** KJV 14:12: 'they called Barnabas, Jupiter; and Paul, Mercurius'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 'Saturn; Vulcan', richtig ist Index 0 (KJV 14:12). Korrektur: EN [0].</sub>

---

#### `apg_069` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'They appointed governors from among the Romans' als richtig. Richtig ist Index 0 (Älteste).

**Aktuell EN** · _Acts 14:23_  
What did Paul and Barnabas ordain in every church as they confirmed the souls of the disciples?

- ⬜ They ordained them elders in every church
- ✅ **They appointed governors from among the Romans** ← _als richtig markiert_
- ⬜ They built sanctuaries of stone in every city
- ⬜ They collected tithes for the temple in Zion

> 📖 **Beleg:** KJV 14:23: 'when they had ordained them elders in every church'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=1 'governors', richtig ist Index 0 (elders, KJV 14:23). Korrektur: EN [0].</sub>

---

#### `apg_071` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'Gentiles must not eat of any fruit' als richtig. Richtig ist Index 0 (Beschneidung). Die Frage ist auch enger gefasst als in DE (Lehre in Antiochia statt Streitfrage des Konzils), inhaltlich aber verwandt.

**Aktuell EN** · _Acts 15:1-6_  
What doctrine taught by certain men from Judaea caused dissension at Antioch?

- ⬜ Except ye be circumcised after the manner of Moses, ye cannot be saved
- ⬜ That the resurrection was past already and none should rise again
- ⬜ That all believers must pay tribute money unto the high priest
- ✅ **That Gentiles must not eat of any fruit grown in the land of Israel** ← _als richtig markiert_

> 📖 **Beleg:** KJV 15:1: 'Except ye be circumcised after the manner of Moses, ye cannot be saved.'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 'fruit', richtig ist Index 0 (KJV 15:1). Korrektur: EN [0].</sub>

---

#### `apg_073` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'swearing oaths, wearing gold, paying taxes, and wine' als richtig. Richtig ist Index 0.

**Aktuell EN** · _Acts 15:28-29_  
What four things did the council at Jerusalem write that the Gentiles should abstain from?

- ⬜ From meats offered to idols, blood, things strangled, and fornication
- ✅ **From swearing oaths, wearing gold, paying taxes, and wine** ← _als richtig markiert_
- ⬜ From temple worship, fasting in secret, trade, and warfare
- ⬜ From reading foreign books, cutting the hair, swine's flesh, and oil

> 📖 **Beleg:** KJV 15:29: 'abstain from meats offered to idols, and from blood, and from things strangled, and from fornication'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=1, richtig ist Index 0 (KJV 15:29). Korrektur: EN [0].</sub>

---

#### `apg_077` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Inhalt der Vision, DE nach dem Ort (Troas). Zudem ist 'An angel commanding him to return unto Jerusalem' markiert, richtig wäre Index 0 (Mann aus Mazedonien).

**Aktuell DE** · _Apostelgeschichte 16:8-10_  
In welcher Stadt sah Paulus in der Nacht die Vision eines um Hilfe rufenden Mannes?

- ⬜ In Philippi
- ✅ **In Troas** ← _als richtig markiert_
- ⬜ In Athen
- ⬜ In Korinth

**Aktuell EN** · _Acts 16:8-10_  
What vision appeared unto Paul in the night at Troas concerning his journey?

- ⬜ A man of Macedonia, saying, Come over into Macedonia, and help us
- ✅ **An angel commanding him to return straightway unto Jerusalem** ← _als richtig markiert_
- ⬜ A pillar of fire guiding the ship across the Great Sea to Rome
- ⬜ A prophet holding two chains of iron and prophesying afflictions

> 📖 **Beleg:** DE [x] 'In Troas' / EN [x] 'An angel commanding him to return straightway unto Jerusalem'

> ✏️ **Korrekturvorschlag:** EN: 'In what city did Paul see the vision of the man of Macedonia?' – [x] 'At Troas'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach dem Inhalt der Vision statt nach dem Ort. Markiert ist der Engel (Index 1), richtig wäre 'man of Macedonia' (Index 0).</sub>

---

#### `apg_082` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'the disputations of the philosophers' als richtig. Richtig ist Index 0 (Götzendienst).

**Aktuell EN** · _Acts 17:16_  
Why was Paul's spirit stirred in him when he was waiting at Athens?

- ⬜ When he saw the city wholly given to idolatry
- ⬜ When he saw the poverty and affliction of the poor
- ✅ **When he heard the disputations of the philosophers** ← _als richtig markiert_
- ⬜ When he beheld the great temple of the heathen gods

> 📖 **Beleg:** KJV 17:16: 'when he saw the city wholly given to idolatry'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=2 'philosophers', richtig ist Index 0 (KJV 17:16 idolatry). Korrektur: EN [0].</sub>

---

#### `apg_083` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'the inner court of the philosophers' als richtig. Richtig ist der Areopag (Index 2).

**Aktuell EN** · _Acts 17:19-22_  
Unto what place in Athens was Paul brought to declare his doctrine?

- ⬜ Unto the palace of the Roman governor
- ⬜ Unto the council hall in the marketplace
- ⬜ Unto the Areopagus (Mars' hill)
- ✅ **Unto the inner court of the philosophers** ← _als richtig markiert_

> 📖 **Beleg:** KJV 17:19: 'brought him unto Areopagus'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [2] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 'inner court', richtig ist Index 2 (Areopagus, KJV 17:19). Korrektur: EN [2].</sub>

---

#### `apg_087` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Handwerk (18:3), DE nach der Dauer in Korinth (18:11). Zudem ist 'carvers of olive wood' markiert, richtig wäre Index 1 (Zeltmacher).

**Aktuell DE** · _Apostelgeschichte 18:11_  
Wie lange wirkte Paulus lehrend und predigend in der Stadt Korinth?

- ⬜ Zwei Jahre und drei Monate
- ⬜ Sechs Monate und zwei Wochen
- ⬜ Drei Jahre und einen Monat
- ✅ **Ein Jahr und sechs Monate** ← _als richtig markiert_

**Aktuell EN** · _Acts 18:11_  
What craft did Paul, Aquila, and Priscilla practice together in Corinth?

- ⬜ They were sellers of purple fabric
- ⬜ By their occupation they were tentmakers
- ⬜ They were fishermen upon the sea
- ✅ **They were carvers of olive wood** ← _als richtig markiert_

> 📖 **Beleg:** DE [x] 'Ein Jahr und sechs Monate' / EN [x] 'They were carvers of olive wood'

> ✏️ **Korrekturvorschlag:** EN: 'How long did Paul continue at Corinth teaching the word of God?' – [x] 'A year and six months'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 18:3, die Stelle ist 18:11. Markiert ist 'carvers of olive wood' (Index 3), richtig wäre 'tentmakers' (Index 1).</sub>

---

#### `apg_089` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Apollos (18:24), DE nach Krispus (18:8). Zudem ist 'Barnabas the Levite' markiert, richtig wäre Apollos (Index 0).

**Aktuell DE** · _Apostelgeschichte 18:8_  
Welcher jüdische Synagogenvorsteher in Korinth kam mit seinem Haus zum Glauben?

- ⬜ Jairus, der Vorsteher in Kapernaum
- ✅ **Krispus, der Vorsteher der Synagoge** ← _als richtig markiert_
- ⬜ Nikodemus, ein Oberster der Juden
- ⬜ Gaius, der Gastgeber des Paulus

**Aktuell EN** · _Acts 18:8_  
What eloquent Jew of Alexandria, mighty in the scriptures, came to Ephesus?

- ⬜ Apollos of Alexandria
- ✅ **Barnabas the Levite** ← _als richtig markiert_
- ⬜ Tychicus of Asia
- ⬜ Epaphras of Colosse

> 📖 **Beleg:** DE [x] 'Krispus, der Vorsteher der Synagoge' / EN [x] 'Barnabas the Levite'

> ✏️ **Korrekturvorschlag:** EN: 'Which chief ruler of the synagogue at Corinth believed on the Lord with all his house?' – [x] 'Crispus'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach Apollos, die Stelle ist 18:8 (Krispus). Markiert ist Barnabas (Index 1), richtig wäre Apollos (Index 0).</sub>

---

#### `apg_090` · DE/EN weicht ab

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Taufe, die Apollos kannte, DE nach seiner Identität. Zudem ist 'The baptism of the temple priests' markiert, richtig wäre Index 1 (Taufe des Johannes).

**Aktuell DE** · _Apostelgeschichte 18:24-26_  
Welcher schriftgelehrte Jude aus Alexandrien wurde in Ephesus unterwiesen?

- ⬜ Barnabas aus Zypern
- ⬜ Nikolaus aus Antiochia
- ✅ **Apollos, ein Alexandriner** ← _als richtig markiert_
- ⬜ Stephanus aus Jerusalem

**Aktuell EN** · _Acts 18:24-26_  
What baptism only did Apollos know before Aquila and Priscilla expounded unto him the way more perfectly?

- ⬜ The baptism of Moses in the cloud
- ⬜ The baptism of John only
- ✅ **The baptism of the temple priests** ← _als richtig markiert_
- ⬜ The baptism of fire on Pentecost

> 📖 **Beleg:** DE [x] 'Apollos, ein Alexandriner' / EN [x] 'The baptism of the temple priests'

> ✏️ **Korrekturvorschlag:** EN: 'What Jew born at Alexandria, mighty in the scriptures, came to Ephesus?' – [x] 'Apollos'.

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach der Taufe, DE nach der Identität des Apollos. Markiert ist 'temple priests' (Index 2), richtig wäre 'baptism of John' (Index 1, KJV 18:25).</sub>

---

#### `apg_091` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN markiert 'They sought to buy the gift of the Spirit' als richtig. Richtig ist Index 0.

**Aktuell EN** · _Acts 19:1-3_  
What deficiency did Paul find in certain disciples at Ephesus concerning the Holy Ghost?

- ⬜ We have not so much as heard whether there be any Holy Ghost
- ⬜ They refused to speak with other tongues in the congregation
- ⬜ They had departed from the faith and turned back to idols
- ✅ **They sought to buy the gift of the Spirit with gold and silver** ← _als richtig markiert_

> 📖 **Beleg:** KJV 19:2: 'We have not so much as heard whether there be any Holy Ghost.'

> ✏️ **Korrekturvorschlag:** EN correctAnswers auf [0] setzen.

<sub>🔎 Gegenprüfung: Bestätigt: EN [x]=3 'buy the gift', richtig ist Index 0 (KJV 19:2). Korrektur: EN [0].</sub>

---

#### `apg_092` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt etwas anderes als DE (wessen Schule statt wie lange), und die als richtig markierte EN-Option 0 (Gamaliel) ist falsch. Richtig wäre Option 1 (Tyrannus).

**Aktuell EN** · _Acts 19:9-10_  
In whose school did Paul dispute daily for the space of two years at Ephesus?

- ✅ **In the school of Gamaliel the doctor** ← _als richtig markiert_
- ⬜ In the school of one Tyrannus
- ⬜ In the synagogue of the libertines
- ⬜ In the court of the governor

> 📖 **Beleg:** KJV 19:9: "disputing daily in the school of one Tyrannus"; EN [x] 0: "In the school of Gamaliel the doctor"

> ✏️ **Korrekturvorschlag:** EN an DE angleichen: "How long did Paul dispute daily in the school of one Tyrannus at Ephesus?" mit den Optionen "The space of two years" (richtig, Index 0) / "three years" / "one year" / "six months"

<sub>🔎 Gegenprüfung: Bestätigt (auch in en/44_apostelgeschichte.json correctAnswers=[0]): EN markiert Gamaliel, laut KJV 19:9 war es die Schule des Tyrannus. Außerdem fragt EN 'wessen Schule', DE 'wie lange'. Am einfachsten passt man EN an DE an (zwei Jahre, Index 0).</sub>

---

#### `apg_093` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach den besonderen Wundern durch Paulus (Apg 19:11-12), nicht nach den Söhnen des Skevas, und das passt nicht zur Stelle 19:13-16. Markiert ist "multiplied bread and fishes", das ist falsch. Inhaltlich richtig wäre Option 0.

**Aktuell EN** · _Acts 19:13-16_  
What special miracles did God work by the hands of Paul at Ephesus?

- ⬜ From his body were brought handkerchiefs or aprons, and the diseases departed
- ✅ **He multiplied bread and fishes for all the believers that were gathered** ← _als richtig markiert_
- ⬜ He caused the temple of Diana to fall down to the ground by his word
- ⬜ He made the water of the harbor to turn into sweet wine for three days

> 📖 **Beleg:** EN [x] 1: "He multiplied bread and fishes for all the believers"; KJV 19:16: "they fled out of that house naked and wounded"

> ✏️ **Korrekturvorschlag:** EN an DE angleichen: "What befell the seven sons of Sceva when they adjured the evil spirit?" mit der richtigen Option an Index 1: "The evil spirit overcame them, and they fled naked and wounded"

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 19:11-12 (Wunder), die Stelle ist aber 19:13-16. Markiert ist 'multiplied bread and fishes', das ist falsch. EN-Frage zu den Söhnen des Skevas umschreiben, richtige Option an Index 1.</sub>

---

#### `apg_094` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach den Söhnen des Skevas (19:13-16) statt nach dem Wert der Zauberbücher (19:19). Markiert ist "struck blind", das ist falsch. Inhaltlich richtig wäre Option 0.

**Aktuell EN** · _Acts 19:18-19_  
What happened to the seven sons of Sceva, vagabond Jews, when they adjured an evil spirit?

- ⬜ The man in whom the evil spirit was leaped on them, and overcame them
- ⬜ The evil spirit departed out of the man and entered into a herd of swine
- ✅ **They were struck blind and wandered through the city seeking a guide** ← _als richtig markiert_
- ⬜ They were cast into prison by the magistrates for disturbing the peace

> 📖 **Beleg:** EN [x] 2: "They were struck blind and wandered through the city"; KJV 19:19: "fifty thousand pieces of silver"

> ✏️ **Korrekturvorschlag:** EN: "What was the price of the books of curious arts burned at Ephesus?" mit "Fifty thousand pieces of silver" an Index 2

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach Skevas (19:13-16) statt nach dem Wert der Bücher (19:19). Markiert ist 'struck blind', das ist falsch. EN neu fassen mit 'fifty thousand pieces of silver' an Index 2.</sub>

---

#### `apg_095` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach den Zauberbüchern (19:19) statt nach dem Silberschmied (19:24). Markiert ist "delivered them unto the elders", das ist falsch. Inhaltlich richtig wäre Option 1.

**Aktuell EN** · _Acts 19:24-27_  
What did many that used curious arts do with their books at Ephesus after the word grew?

- ⬜ They sold them unto the merchants of Rome for much gold
- ⬜ Brought their books together, and burned them before all men
- ⬜ They hid them in secret caves in the mountains of Asia
- ✅ **They delivered them unto the elders of the church to keep** ← _als richtig markiert_

> 📖 **Beleg:** EN [x] 3: "They delivered them unto the elders of the church to keep"; KJV 19:19: "brought their books together, and burned them"

> ✏️ **Korrekturvorschlag:** EN: "What silversmith stirred up the uproar against Paul at Ephesus?" mit "Demetrius, a silversmith" an Index 3

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach den Zauberbüchern (19:19), die Stelle ist aber 19:24-27. Die markierte Option 3 ist falsch. EN zu Demetrius umschreiben, an Index 3.</sub>

---

#### `apg_096` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Silberschmied (Apg 19) statt nach Eutychus (20:7-9). Markiert ist "Alexander the coppersmith", das ist falsch. Inhaltlich richtig wäre Option 1 (Demetrius).

**Aktuell EN** · _Acts 20:7-9_  
What silversmith made silver shrines for Diana and stirred up an uproar against Paul?

- ✅ **Alexander the coppersmith** ← _als richtig markiert_
- ⬜ Demetrius, a silversmith
- ⬜ Sceva, a chief of the priests
- ⬜ Hermogenes of Asia

> 📖 **Beleg:** EN [x] 0: "Alexander the coppersmith"; KJV 19:24: "Demetrius, a silversmith"

> ✏️ **Korrekturvorschlag:** EN: "What young man fell down from a window while Paul preached at Troas?" mit "Eutychus" an Index 0

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach dem Silberschmied (Kap. 19), Stelle ist 20:7-9. Markiert ist 'Alexander the coppersmith', richtig wäre Demetrius. EN zu Eutychus umschreiben, an Index 0.</sub>

---

#### `apg_107` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 3 (Caiaphas), das ist falsch. Richtig ist Option 0 (Gamaliel). Das passt auch nicht zur DE-Lösung (Index 3 = Gamaliel).

**Aktuell EN** · _Acts 22:3_  
At whose feet was Paul brought up in Jerusalem and taught according to the law?

- ⬜ At the feet of Gamaliel
- ⬜ At the feet of Annas the priest
- ⬜ At the feet of Nicodemus
- ✅ **At the feet of Caiaphas** ← _als richtig markiert_

> 📖 **Beleg:** KJV 22:3: "brought up in this city at the feet of Gamaliel"; EN [x] 3: "At the feet of Caiaphas"

> ✏️ **Korrekturvorschlag:** EN-Optionen so umstellen, dass "At the feet of Gamaliel" an Index 3 steht (z. B. 0: Caiaphas, 3: Gamaliel)

<sub>🔎 Gegenprüfung: Bestätigt (EN correctAnswers=[3] = Caiaphas). KJV 22:3 sagt Gamaliel, in EN an Index 0. Gamaliel an Index 3 setzen.</sub>

---

#### `apg_110` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 2 (Berufung vor dem Hohen Rat), das ist falsch. Richtig ist Option 0 (römisches Bürgerrecht, wörtlich KJV 22:25).

**Aktuell EN** · _Acts 22:25-29_  
What privilege did Paul claim when the chief captain commanded him to be examined by scourging?

- ⬜ Is it lawful for you to scourge a man that is a Roman, and uncondemned?
- ⬜ I am a priest of the order of Aaron and may not be touched by Gentiles
- ✅ **I have an appeal before the high council of the elders in Jerusalem** ← _als richtig markiert_
- ⬜ I am protected by the imperial decree of the Roman senate in Asia

> 📖 **Beleg:** KJV 22:25: "Is it lawful for you to scourge a man that is a Roman, and uncondemned?"; EN [x] 2: "I have an appeal before the high council"

> ✏️ **Korrekturvorschlag:** Die richtige EN-Option an Index 2 setzen (passend zu DE "Das römische Bürgerrecht")

<sub>🔎 Gegenprüfung: Bestätigt: EN markiert Index 2 ('appeal before the high council'), richtig ist Index 0 (wörtlich KJV 22:25). Die richtige Option an Index 2 setzen.</sub>

---

#### `apg_111` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 3 (Sceva), das ist falsch. Richtig ist Option 0 (Ananias).

**Aktuell EN** · _Acts 23:1-3_  
Which high priest commanded them that stood by Paul to smite him on the mouth?

- ⬜ Ananias the high priest
- ⬜ Caiaphas the high priest
- ⬜ Annas the high priest
- ✅ **Sceva the chief priest** ← _als richtig markiert_

> 📖 **Beleg:** KJV 23:2: "the high priest Ananias commanded them that stood by him to smite him on the mouth"; EN [x] 3: "Sceva the chief priest"

> ✏️ **Korrekturvorschlag:** "Ananias the high priest" an Index 3 setzen (passend zu DE), Sceva auf Index 0

<sub>🔎 Gegenprüfung: Bestätigt: EN markiert Sceva, laut KJV 23:2 war es Ananias (EN Index 0). Die Optionen tauschen.</sub>

---

#### `apg_114` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 2 (100 Reiter), das ist falsch. Richtig ist Option 0 (470 insgesamt: 200 Soldaten, 70 Reiter, 200 Lanzenträger).

**Aktuell EN** · _Acts 23:23-24_  
How many soldiers, horsemen, and spearmen were prepared to bring Paul safe unto Felix?

- ⬜ Four hundred and seventy soldiers in all
- ⬜ Two hundred soldiers under two centurions
- ✅ **One hundred horsemen from the palace guard** ← _als richtig markiert_
- ⬜ Three hundred men of the Roman garrison

> 📖 **Beleg:** KJV 23:23: "two hundred soldiers ... horsemen threescore and ten, and spearmen two hundred"; EN [x] 2: "One hundred horsemen from the palace guard"

> ✏️ **Korrekturvorschlag:** EN-Optionen an DE angleichen: Index 2 = "Four hundred and seventy (200 soldiers, 70 horsemen, 200 spearmen)"

<sub>🔎 Gegenprüfung: Bestätigt: EN markiert 'One hundred horsemen', richtig ist Index 0 (470, KJV 23:23). Die richtige Option an Index 2 setzen.</sub>

---

#### `apg_117` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Felix' Reaktion auf die Rede über Gerechtigkeit (24:25) statt nach Tertullus' Vorwurf (24:5). Markiert ist "commanded that Paul should be released", das ist falsch. Inhaltlich richtig wäre Option 0 ("Felix trembled").

**Aktuell EN** · _Acts 24:5-6_  
As Paul reasoned of righteousness, temperance, and judgment to come, what was Felix's reaction?

- ⬜ Felix trembled, and answered, Go thy way for this time
- ✅ **Felix commanded that Paul should be released from bonds** ← _als richtig markiert_
- ⬜ Felix laughed him to scorn and mocked his words in open court
- ⬜ Felix straightway believed and was baptized with his household

> 📖 **Beleg:** EN [x] 1: "Felix commanded that Paul should be released from bonds"; KJV 24:5: "a ringleader of the sect of the Nazarenes"

> ✏️ **Korrekturvorschlag:** EN: "What chief accusation did Tertullus bring against Paul before Felix?" mit "A ringleader of the sect of the Nazarenes" an Index 1

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 24:25 statt nach 24:5. Markiert ist 'released from bonds', das ist falsch, denn laut 24:25 zitterte Felix (Option 0). EN zum Vorwurf des Tertullus umschreiben, an Index 1.</sub>

---

#### `apg_118` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach 24:27 (warum Felix Paulus gebunden zurückließ) statt nach dem Aufschub in 24:22. Markiert ist "the emperor commanded", das ist falsch. Inhaltlich richtig wäre Option 0.

**Aktuell EN** · _Acts 24:22-23_  
Why did Felix leave Paul bound when Porcius Festus came into his room two years later?

- ⬜ Willing to shew the Jews a pleasure, Felix left Paul bound
- ⬜ Because he found him guilty of death by the imperial law
- ✅ **Because the emperor commanded that he be sent bound to Rome** ← _als richtig markiert_
- ⬜ Because Paul had refused to pay the tribute money demanded

> 📖 **Beleg:** EN [x] 2: "Because the emperor commanded that he be sent bound to Rome"; KJV 24:22: "he deferred them, and said, When Lysias the chief captain shall come down"

> ✏️ **Korrekturvorschlag:** EN: "What did Felix do after hearing Paul's defence?" mit "He deferred them until Lysias the chief captain should come down" an Index 2

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 24:27, die Stelle ist 24:22-23. Markiert ist 'the emperor commanded', das ist falsch, richtig wäre Option 0. EN zum Aufschub bis Lysias umschreiben, an Index 2.</sub>

---

#### `apg_119` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Berufung des Paulus vor Festus (25:9-11) statt nach Drusilla (24:24). Markiert ist "I appeal unto the governor", das ist falsch. Inhaltlich richtig wäre Option 0 ("unto Caesar").

**Aktuell EN** · _Acts 24:24_  
What appeal did Paul make when Festus asked if he would go up to Jerusalem to be judged?

- ⬜ I appeal unto Caesar
- ⬜ I appeal unto the council
- ⬜ I appeal unto king Agrippa
- ✅ **I appeal unto the governor** ← _als richtig markiert_

> 📖 **Beleg:** EN [x] 3: "I appeal unto the governor"; KJV 25:11: "I appeal unto Cæsar"; KJV 24:24: "his wife Drusilla, which was a Jewess"

> ✏️ **Korrekturvorschlag:** EN: "What was the name of Felix's wife, a Jewess, who heard Paul?" mit "Drusilla" an Index 3

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach der Berufung (25:11), die Stelle ist 24:24. Markiert ist 'unto the governor', das ist falsch. EN zu Drusilla umschreiben, an Index 3.</sub>

---

#### `apg_121` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Geste des Paulus vor Agrippa (26:1) statt nach dem Ansinnen der Hohenpriester (25:3). Markiert ist "lifted up both his hands", das ist falsch. Inhaltlich richtig wäre Option 0.

**Aktuell EN** · _Acts 25:1-3_  
What did Paul stretch forth when he answered for himself before king Agrippa?

- ⬜ Paul stretched forth the hand
- ✅ **He lifted up both his hands** ← _als richtig markiert_
- ⬜ He bowed his head to the earth
- ⬜ He held forth his holy chains

> 📖 **Beleg:** EN [x] 1: "He lifted up both his hands"; KJV 25:3: "that he would send for him to Jerusalem"

> ✏️ **Korrekturvorschlag:** EN: "Whither did the chief priests desire Festus to send for Paul?" mit "To Jerusalem" an Index 1

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 26:1, die Stelle ist 25:1-3. Markiert ist 'lifted up both his hands', das ist falsch, laut KJV 26:1 'stretched forth the hand' (Option 0). EN neu fassen mit 'To Jerusalem' an Index 1.</sub>

---

#### `apg_122` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Sekte der Pharisäer (26:5) statt nach der Berufung auf den Kaiser (25:11). Markiert ist "Essenes", das ist falsch. Inhaltlich richtig wäre Option 0.

**Aktuell EN** · _Acts 25:10-11_  
After what straitest sect of the Jews' religion did Paul live from his youth?

- ⬜ After the most straitest sect of our religion I lived a Pharisee
- ⬜ After the doctrine of the Sadducees which deny the resurrection
- ✅ **After the strict company of the Essenes dwelling in the desert** ← _als richtig markiert_
- ⬜ After the party of the Herodians which favor the king's house

> 📖 **Beleg:** EN [x] 2: "After the strict company of the Essenes"; KJV 25:11: "I appeal unto Cæsar"

> ✏️ **Korrekturvorschlag:** EN: "What right did Paul claim before Festus?" mit "He appealed unto Caesar" an Index 2

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 26:5, die Stelle ist 25:10-11. Markiert ist 'Essenes', das ist falsch, richtig wäre Option 0 (Pharisee). EN zur Berufung auf den Kaiser umschreiben, an Index 2.</sub>

---

#### `apg_123` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Agrippas Antwort an Festus statt nach dem König. Markiert ist "Send him straightway unto Caesar", das ist falsch. Richtig ist Option 0 ("I would also hear the man myself", KJV 25:22).

**Aktuell EN** · _Acts 25:13-22_  
What did Agrippa say unto Festus after Festus related the cause of Paul?

- ⬜ I would also hear the man myself
- ⬜ Let him be delivered unto the Jews
- ⬜ Let him be released from all bonds
- ✅ **Send him straightway unto Caesar** ← _als richtig markiert_

> 📖 **Beleg:** KJV 25:22: "Then Agrippa said unto Festus, I would also hear the man myself"; EN [x] 3: "Send him straightway unto Caesar"

> ✏️ **Korrekturvorschlag:** EN: "Which king came unto Caesarea and desired to hear Paul?" mit "King Agrippa" an Index 3

<sub>🔎 Gegenprüfung: Bestätigt: EN markiert 'Send him straightway unto Caesar', laut KJV 25:22 ist richtig 'I would also hear the man myself' (Index 0). EN an DE angleichen (König Agrippa an Index 3).</sub>

---

#### `apg_125` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach 26:9-11 (Verfolgung durch Saulus) statt nach dem Urteil des Festus (25:12). Markiert ist "high priest promised me great riches", das ist falsch. Inhaltlich richtig wäre Option 0.

**Aktuell EN** · _Acts 25:12_  
Why did Paul say he thought with himself that he ought to do many things contrary to Jesus of Nazareth?

- ⬜ Being exceedingly mad against them, I persecuted them even unto strange cities
- ✅ **Because the high priest promised me great riches and honor in Jerusalem** ← _als richtig markiert_
- ⬜ Because I desired to be made a ruler and chief judge in the council
- ⬜ Because I feared that the Romans would take away our place and nation

> 📖 **Beleg:** EN [x] 1: "Because the high priest promised me great riches and honor"; KJV 25:12: "Hast thou appealed unto Cæsar? unto Cæsar shalt thou go."

> ✏️ **Korrekturvorschlag:** EN: "What did Festus answer after Paul appealed unto Caesar?" mit "Hast thou appealed unto Caesar? unto Caesar shalt thou go" an Index 1

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach 26:9-11, die Stelle ist 25:12. Markiert ist 'high priest promised me great riches', das ist erfunden, Option 0 wäre richtig. EN zum Urteil des Festus umschreiben, an Index 1.</sub>

---

#### `apg_126` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Licht auf dem Weg nach Damaskus (26:13) statt nach der Partei der Pharisäer (26:5). Markiert ist "A burning star falling", das ist falsch. Inhaltlich richtig wäre Option 0.

**Aktuell EN** · _Acts 26:4-5_  
What light did Paul see at midday on the way to Damascus, above the brightness of the sun?

- ⬜ A light from heaven, above the brightness of the sun, shining round about
- ⬜ A pillar of fire descending from the top of the mountains round about
- ✅ **A burning star falling from heaven into the midst of the way before him** ← _als richtig markiert_
- ⬜ A golden chariot with holy angels surrounded with bright burning flames

> 📖 **Beleg:** EN [x] 2: "A burning star falling from heaven"; KJV 26:5: "after the most straitest sect of our religion I lived a Pharisee"

> ✏️ **Korrekturvorschlag:** EN: "Of what sect of the Jews' religion was Paul before his conversion?" mit "The Pharisees" an Index 2

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach dem Licht (26:13), die Stelle ist 26:4-5. Markiert ist 'burning star', das ist falsch, Option 0 wäre richtig. EN zur Partei der Pharisäer umschreiben, an Index 2.</sub>

---

#### `apg_129` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Agrippas Ausspruch, DE nach der Antwort des Paulus. Markiert ist "Thou art worthy of death", das ist falsch. Richtig wäre Option 0 ("Almost thou persuadest me").

**Aktuell EN** · _Acts 26:28-29_  
What famous answer did King Agrippa give unto Paul after hearing his testimony?

- ⬜ Almost thou persuadest me to be a Christian
- ✅ **Thou art worthy of death according to our law** ← _als richtig markiert_
- ⬜ Go thy way, and preach this doctrine in Rome
- ⬜ I will give thee great gold and set thee free

> 📖 **Beleg:** KJV 26:28: "Almost thou persuadest me to be a Christian"; EN [x] 1: "Thou art worthy of death according to our law"

> ✏️ **Korrekturvorschlag:** EN: "What did Paul answer when Agrippa said, Almost thou persuadest me to be a Christian?" mit "I would to God that all ... were such as I am, except these bonds" an Index 1

<sub>🔎 Gegenprüfung: Bestätigt: EN fragt nach Agrippas Ausspruch und markiert 'worthy of death', das ist falsch, laut KJV 26:28 'Almost thou persuadest me' (Index 0). EN an DE angleichen (Paulus' Antwort 26:29, an Index 1).</sub>

---

#### `apg_130` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 2 ("delivered unto the high priest"), das ist falsch. Richtig ist Option 0 (wörtlich KJV 26:32).

**Aktuell EN** · _Acts 26:31-32_  
What did Agrippa say unto Festus concerning Paul's appeal?

- ⬜ This man might have been set at liberty, if he had not appealed unto Caesar
- ⬜ This man is guilty of death and worthy of bonds according to the law
- ✅ **This man must be delivered unto the high priest to be judged in Zion** ← _als richtig markiert_
- ⬜ This man shall be banished into the wilderness of Syria for evermore

> 📖 **Beleg:** KJV 26:32: "This man might have been set at liberty, if he had not appealed unto Cæsar"; EN [x] 2: "This man must be delivered unto the high priest"

> ✏️ **Korrekturvorschlag:** Die richtige Option an Index 2 setzen (passend zu DE) oder die Markierung auf Index 0 setzen und DE entsprechend angleichen

<sub>🔎 Gegenprüfung: Bestätigt: EN markiert Index 2 ('delivered unto the high priest'), richtig ist Index 0 (KJV 26:32). Die richtige Option an Index 2 setzen, dann stimmt sie mit DE überein.</sub>

---

#### `apg_134` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 2 ("Twelve legions of angels"), das ist falsch. Richtig ist Option 0 (KJV 27:24).

**Aktuell EN** · _Acts 27:22-25_  
What comfort did the angel of God declare unto Paul during the tempest at sea?

- ⬜ Fear not, Paul; thou must be brought before Caesar: and, lo, God hath given thee all
- ⬜ The ship shall come safe into the fair havens without any loss of its lading
- ✅ **Twelve legions of angels shall guide the vessel into the harbor of Crete** ← _als richtig markiert_
- ⬜ Thou shalt return unto Jerusalem and testify before the council once again

> 📖 **Beleg:** KJV 27:24: "Fear not, Paul; thou must be brought before Cæsar: and, lo, God hath given thee all them that sail with thee"; EN [x] 2: "Twelve legions of angels shall guide the vessel"

> ✏️ **Korrekturvorschlag:** Index 2 = "Fear not, Paul ... God hath given thee all them that sail with thee" (passend zu DE "Keiner von ihnen werde umkommen")

<sub>🔎 Gegenprüfung: Bestätigt: EN markiert 'Twelve legions of angels', das ist falsch, richtig ist Index 0 (KJV 27:24). Die richtige Option an Index 2 setzen.</sub>

---

#### `apg_135` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 3 ("Seventy and two souls"), das ist falsch. Richtig ist Option 0 (276).

**Aktuell EN** · _Acts 27:37-44_  
How many souls were in the ship in all, which were all brought safe to land on boards?

- ⬜ Two hundred threescore and sixteen souls
- ⬜ One hundred and forty and four souls
- ⬜ Three hundred and twelve persons in all
- ✅ **Seventy and two souls upon the vessel** ← _als richtig markiert_

> 📖 **Beleg:** KJV 27:37: "two hundred threescore and sixteen souls"; EN [x] 3: "Seventy and two souls upon the vessel"

> ✏️ **Korrekturvorschlag:** "Two hundred threescore and sixteen souls" an Index 3 setzen (passend zu DE)

<sub>🔎 Gegenprüfung: Bestätigt: EN markiert 'Seventy and two souls', laut KJV 27:37 waren es 276 (Index 0). 'Two hundred threescore and sixteen' an Index 3 setzen.</sub>

---

#### `apg_136` · Falsche Lösung

🔴 **hoch** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** In beiden Sprachen ist Zypern als richtig markiert. Laut Text hieß die Insel Melite/Melita, das ist Option 3.

**Aktuell DE** · _Apostelgeschichte 28:1_  
Auf welcher Insel strandete die Schiffsmannschaft nach dem Schiffbruch?

- ✅ **Auf Zypern** ← _als richtig markiert_
- ⬜ Auf Kreta
- ⬜ Auf Rhodos
- ⬜ Auf Melite

**Aktuell EN** · _Acts 28:1_  
What was the name of the island upon which the shipwrecked company escaped safe?

- ✅ **The island of Cyprus** ← _als richtig markiert_
- ⬜ The island of Crete
- ⬜ The island of Rhodes
- ⬜ The island called Melita

> 📖 **Beleg:** DE-TEXT 28:1: "dass die Insel Melite hieß"; KJV: "the island was called Melita"; [x] 0: "Auf Zypern" / "The island of Cyprus"

> ✏️ **Korrekturvorschlag:** Die richtige Antwort auf Index 3 setzen ("Auf Melite" / "The island called Melita")

<sub>🔎 Gegenprüfung: Bestätigt (DE und EN correctAnswers=[0] = Zypern). Laut DE-TEXT und KJV 28:1 hieß die Insel Melite/Melita (Index 3). In beiden Sprachen correctAnswers auf [3] setzen.</sub>

---

#### `apg_139` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 3 ("six months"), das ist falsch. Richtig ist Option 0 (zwei Jahre).

**Aktuell EN** · _Acts 28:30-31_  
How long did Paul dwell in his own hired house at Rome, preaching the kingdom of God?

- ⬜ Paul dwelt two whole years in Rome
- ⬜ Paul dwelt three years in the city
- ⬜ Paul remained for the space of a year
- ✅ **Paul tarried six months in his bonds** ← _als richtig markiert_

> 📖 **Beleg:** KJV 28:30: "Paul dwelt two whole years in his own hired house"; EN [x] 3: "Paul tarried six months in his bonds"

> ✏️ **Korrekturvorschlag:** "Paul dwelt two whole years in Rome" an Index 3 setzen (passend zu DE)

<sub>🔎 Gegenprüfung: Bestätigt: EN markiert 'six months', laut KJV 28:30 'two whole years' (Index 0). Die richtige Option an Index 3 setzen.</sub>

---

#### `apg_142` · Falsche Lösung

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Markiert ist EN Option 1 (John), das ist falsch. Laut 3:6 sprach Petrus (EN Option 0).

**Aktuell EN** · _Acts 3:6_  
Who said unto the lame man at the temple gate: 'Silver and gold have I none' (Acts 3:6)?

- ⬜ Peter
- ✅ **John** ← _als richtig markiert_
- ⬜ Paul
- ⬜ Philip

> 📖 **Beleg:** KJV 3:6: "Then Peter said, Silver and gold have I none"; EN [x] 1: "John"

> ✏️ **Korrekturvorschlag:** EN-Optionen an DE angleichen: 0: Stephen, 1: Peter (richtig), 2: Barnabas, 3: Philip

<sub>🔎 Gegenprüfung: Bestätigt (EN correctAnswers=[1] = John). Laut KJV 3:6 sprach Petrus. Die EN-Optionen an DE angleichen (Peter an Index 1).</sub>

---

### 📄 `46_1_korinther.json` (2)

#### `1kor_014` · Falsche Lösung

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die Frage lautet 'Wodurch wird das Bauwerk geprüft?'. Markiert ist aber 'Vergängliches Holz, Heu und Stroh', also ein Baumaterial. Laut Text prüft das Feuer jedes Werk. Keine der DE-Optionen ist richtig. EN fragt korrekt und markiert 'revealed by fire'.

**Aktuell DE** · _1. Korinther 3:12-15_  
Wodurch wird das Bauwerk eines jeden Arbeiters am Tage des Gerichts geprüft werden?

- ⬜ Gold, Silber und kostbare Steine
- ⬜ Marmor, Granit und gebrannte Ziegel
- ✅ **Vergängliches Holz, Heu und Stroh** ← _als richtig markiert_
- ⬜ Kupfer, gehärtetes Eisen und Bronze

> 📖 **Beleg:** V.13: 'weil es durchs Feuer offenbar wird ... wird das Feuer erproben'

> ✏️ **Korrekturvorschlag:** Richtige Option 2 ersetzen durch 'Durch das Feuer am Tag des Herrn'. Die Distraktoren an EN angleichen (römischer Richter, Abstimmung der Brüder, Abwägen weltlicher Reichtümer).

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage fragt 'Wodurch wird geprüft?', alle DE-Optionen sind aber Baumaterialien, und markiert ist 'Holz, Heu und Stroh'. Laut V.13 prüft das Feuer. Keine DE-Option ist richtig. Korrektur: Option 2 'Durch das Feuer, das jedes Werk erprobt', die Distraktoren an EN angleichen.</sub>

---

#### `1kor_063` · Inhaltlicher Fehler

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage lautet 'Was geschieht mit den prophetischen Gaben und dem Sprachenreden in der Vollendung?'. Die Optionen sind aber Substantive ('Das prophetische Weissagen', 'Die Gabe der Zungenrede' …), und die markierte Antwort 'Die Liebe vergeht nimmer' passt nicht zur Frage. Die Frage ist so nicht sinnvoll zu beantworten. EN fragt dagegen korrekt, welche Tugend nie aufhört.

**Aktuell DE** · _1. Korinther 13:8-10_  
Was geschieht mit den prophetischen Gaben und dem Sprachenreden in der Vollendung?

- ⬜ Das prophetische Weissagen
- ⬜ Die Gabe der Zungenrede
- ⬜ Die menschliche Erkenntnis
- ✅ **Die Liebe vergeht nimmer** ← _als richtig markiert_

> 📖 **Beleg:** V.8: 'Die Liebe hört niemals auf, wo doch die Prophezeiungen abgetan werden'

> ✏️ **Korrekturvorschlag:** DE-Frage: 'Was hört niemals auf, auch wenn Weissagungen abgetan werden und das Sprachenreden aufhört?'

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage fragt, was mit Prophetie und Sprachenrede geschieht. Die Optionen sind Substantive, die markierte Antwort 'Die Liebe vergeht nimmer' beantwortet die Frage nicht. Nach V.8 würden diese Gaben aufhören, und diese Antwort fehlt. Die DE-Frage wie in EN umformulieren: 'Was hört niemals auf, auch wenn Weissagungen abgetan werden?'</sub>

---

### 📄 `49_epheser.json` (1)

#### `eph_028` · Mehrere richtig

🔴 **hoch** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Gefragt ist, gegen wen die Gläubigen NICHT kämpfen. Im DE sind die Distraktoren genau das, wogegen sie laut Text kämpfen (finstere Mächte, böse Herrscher, böse Geister), also klar falsch. Im EN stimmen zwei Distraktoren aber ebenfalls: 'carnal magistrates' sind Fleisch und Blut, also auch nicht der Gegner, und gegen 'heavenly angels' (Gottes Engel) kämpfen Gläubige auch nicht. Damit hat die EN-Frage drei richtige Antworten und weicht inhaltlich von DE ab.

**Aktuell EN** · _Ephesians 6:12_  
Against whom do believers wrestle not (Ephesians 6:12)?

- ✅ **Against flesh and blood** ← _als richtig markiert_
- ⬜ Against dark principalities
- ⬜ Against carnal magistrates
- ⬜ Against heavenly angels

> 📖 **Beleg:** KJV: 'For we wrestle not against flesh and blood, but against principalities, against powers, against the rulers of the darkness of this world, against spiritual wickedness in high places.' EN-Optionen: '2: Against carnal magistrates', '3: Against heavenly angels'

> ✏️ **Korrekturvorschlag:** EN-Distraktoren an DE angleichen: '1: Against principalities and powers', '2: Against the rulers of the darkness of this world', '3: Against spiritual wickedness in high places'

<sub>🔎 Gegenprüfung: Der Befund stimmt. EN-Option 2 'carnal magistrates' sind Menschen, also 'flesh and blood', und damit nach dem Vers ebenfalls nicht der Gegner. Option 3 'heavenly angels' meint ohne 'wicked' Gottes Engel, gegen die auch nicht gekämpft wird. Sie ist zumindest mehrdeutig, weil der Vers von 'spiritual wickedness in high places' spricht. Die EN-Frage hat also mehr als eine vertretbare Antwort. Die DE-Version ist korrekt. Korrektur: '1: Against principalities and powers', '2: Against the rulers of the darkness of this world', '3: Against spiritual wickedness in high places'.</sub>

---

### 📄 `66_offenbarung.json` (1)

#### `off_094` · Inhaltlicher Fehler

🔴 **hoch** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die deutsche Frage fragt nach dem Namen des Reiters, die Optionen nennen aber Pferd und Gewand. Keine Option nennt einen Namen ("Treu und Wahrhaftig" / "Das Wort Gottes"). Außerdem verrät die Frage mit "weißen Pferd" schon die Lösung. EN fragt richtig nach Pferd und Gewand.

**Aktuell DE** · _Offenbarung 19:11-13_  
Welchen Namen trägt der siegreiche Reiter auf dem weißen Pferd?

- ⬜ Ein schwarzes Pferd; Gewand in Purpur und Gold gehüllt
- ⬜ Ein feuerrotes Pferd; Gewand mit Löwenfell geschmückt
- ✅ **Ein weißes Pferd; Gewand in reines Blut getaucht** ← _als richtig markiert_
- ⬜ Ein grünes Pferd; Gewand aus glänzendem Silberstoff

> 📖 **Beleg:** DE: "Welchen Namen trägt der siegreiche Reiter auf dem weißen Pferd?" – Optionen: "Ein weißes Pferd; Gewand in reines Blut getaucht"; EN: "What horse and vesture did the Faithful and True have?"

> ✏️ **Korrekturvorschlag:** DE-Frage: "Auf welchem Pferd reitet der Treue und Wahrhaftige, und wie ist sein Gewand beschaffen?"; Option 2: "Ein weißes Pferd; Gewand in Blut getaucht" ("reines" streichen)

<sub>🔎 Gegenprüfung: Bestätigt: Die DE-Frage fragt nach einem Namen, alle Optionen nennen aber Pferd und Gewand. Außerdem verrät 'weißen Pferd' die Lösung. 'reines Blut' steht nicht in 19:13. Korrektur wie vorgeschlagen: 'Auf welchem Pferd reitet der Treue und Wahrhaftige, und wie ist sein Gewand beschaffen?' und Option 2 'Ein weißes Pferd; Gewand in Blut getaucht'.</sub>

---


<a id="mittlere-fehler"></a>

## 🟠 Mittlere Fehler (120)

_DE und EN inhaltlich verschieden, Faktenfehler in Frage oder Distraktor, falsche Bibelstelle._

### 📄 `01_1_mose.json` (17)

#### `1mose_114` · Bibelstelle

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die DE-Stelle 1. Mose 32:31 enthält im hinterlegten Text nicht die Benennung von Pniel und deren Begründung, sondern nur den Sonnenaufgang und das Hinken. Der hinterlegte DE-Text zählt 1. Mose 32 wie die KJV; Benennung und Begründung stehen dort in 32:30.

**Aktuell DE** · _1. Mose 32:31_  
Wie nannte Jakob den Ort des nächtlichen Kampfes und was war seine Begründung?

- ⬜ Bethel; „Hier ist nichts anderes als ein Haus Gottes und die offene Pforte des Himmels!“
- ⬜ Mahanaim; „Dies ist das Heerlager Gottes, dessen Engel mir auf dem Wege begegnet sind!“
- ✅ **Pniel; „Denn ich habe Gott von Angesicht zu Angesicht gesehen, und meine Seele ist errettet worden!“** ← _als richtig markiert_
- ⬜ Mizpa; „Der HERR sei Wächter zwischen mir und dir, wenn wir voneinander geschieden sind!“

> 📖 **Beleg:** DE-TEXT (1. Mose 32:31): "Und die Sonne ging ihm auf, als er an Pniel vorüberzog; und er hinkte wegen seiner Hüfte." / Nachschlagen 32:30 DE: "Jakob aber nannte den Ort Pniel; denn er sprach: Ich habe Älohim von Angesicht zu Angesicht gesehen…"

> ✏️ **Korrekturvorschlag:** DE-bibleReference auf „1. Mose 32:30“ ändern. Weil der hinterlegte DE-Text in Kap. 32 KJV-Verszahlen nutzt, auch 1mose_110 bis 1mose_113 prüfen (DE-Stellen derzeit um +1 verschoben).

<sub>🔎 Gegenprüfung: Bestätigt per Nachschlagen: Im hinterlegten DE-Text steht in 32:30 die Benennung Pniel samt Begründung, in 32:31 nur Sonnenaufgang und Hinken. Die DE-Stelle sollte auf 1. Mose 32:30 geändert werden. Der DE-Text nutzt in Kap. 32 die KJV-Verszahlen. Daher sind auch 1mose_111 (DE 32:10-11, besser 32:9-10 bzw. 32:10) und 1mose_113 (DE 32:28-29, besser 32:27-28) an EN anzugleichen.</sub>

---

#### `1mose_134` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach Jakobs Worten, als er den Trost seiner Kinder ablehnte (V. 35). EN fragt nach seiner Reaktion auf das blutige Gewand. Die EN-Lösung enthält „rent his clothes“, das steht in V. 34 und nicht in der angegebenen Stelle 37:35. Das KJV-Zitat ist gekürzt („unto my son“ fehlt). Alle Distraktoren unterscheiden sich zwischen DE und EN.

**Aktuell DE** · _1. Mose 37:35_  
Welche drastischen Worte benutzte der trauernde Jakob, als er sich weigerte, von seinen Söhnen und Töchtern getröstet zu werden?

- ⬜ „Gott hat mich verlassen; mein Leben hat keinen Sinn mehr!“
- ⬜ „Bringt mir den Kopf des Tieres, das meinen geliebten Jüngling zerrissen hat!“
- ✅ **„Ich höre nicht auf zu trauern, bis ich zu meinem Sohn hinabfahre ins Totenreich!“** ← _als richtig markiert_
- ⬜ „Ich werde fasten und beten, bis Gott mir Joseph wiedergibt!“

**Aktuell EN** · _Genesis 37:35_  
How did heartbroken Jacob respond to the presentation of Joseph's bloody coat?

- ⬜ He offered a solemn burnt sacrifice and fell silent before the elders
- ⬜ He called for armed servants to pursue the wild beasts in the mountains
- ✅ **He rent his clothes and vowed: "I will go down into the grave mourning"** ← _als richtig markiert_
- ⬜ He departed into the wilderness of Paran to mourn forty days alone

> 📖 **Beleg:** EN: "How did heartbroken Jacob respond to the presentation of Joseph's bloody coat?" [x] "He rent his clothes and vowed: 'I will go down into the grave mourning'" – KJV 37:35: "For I will go down into the grave unto my son mourning."

> ✏️ **Korrekturvorschlag:** EN-Frage: "With what words did mourning Jacob refuse to be comforted by his sons and daughters?"; Lösung: "\"I will go down into the grave unto my son mourning\""; Distraktoren als Übersetzung der DE-Optionen 0, 1 und 3.

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt nach der Reaktion auf das Gewand, DE nach den Worten beim abgelehnten Trost. „rent his clothes“ steht in V. 34, nicht in 37:35. Im Zitat fehlt „unto my son“. Alle Distraktoren weichen ab.</sub>

---

#### `1mose_139` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** DE-Distraktor 0 enthält die richtigen Zwillingsnamen in englischer Schreibweise (Pharez und Zarah = Perez und Serach). Nur der Zusatz über Aarons Priestertum macht die Option falsch. Das ist verwirrend. In EN fragt man nur nach den Namen. Die EN-Distraktoren sind andere: EN0 Er/Onan, EN2 Manasse/Ephraim, dagegen DE0 Pharez/Zarah, DE2 Er/Onan.

**Aktuell DE** · _1. Mose 38:29-30_  
Wie hießen die Zwillinge, die Tamar gebar, und welche theologische Bedeutung hat der Erstgeborene in Bezug auf den Messias?

- ⬜ Pharez und Zarah; Serach wurde der Stammvater des Priestertums Aarons
- ⬜ Esau und Jakob; Esau trat sein Erstgeburtsrecht an Perez im Mutterleib ab
- ⬜ Er und Onan; sie wurden wiedergeboren, um den göttlichen Fluch zu tilgen
- ✅ **Perez und Serach; Perez wurde der Stammvater des königlichen Hauses Juda** ← _als richtig markiert_

**Aktuell EN** · _Genesis 38:29-30_  
What were the names of the twin sons Tamar bare unto Judah?

- ⬜ Er and Onan, who were restored to life in Judah
- ⬜ Esau and Jacob, born together in the same tent
- ⬜ Manasseh and Ephraim, adopted into the patriarchs
- ✅ **Pharez and Zarah, of whom Pharez became forefather of David** ← _als richtig markiert_

> 📖 **Beleg:** DE 0: „Pharez und Zarah; Serach wurde der Stammvater des Priestertums Aarons“ / EN 0: "Er and Onan, who were restored to life in Judah"

> ✏️ **Korrekturvorschlag:** DE 0 ersetzen durch „Manasse und Ephraim; sie wurden von den Erzvätern adoptiert“ (entspricht EN 2), DE 2 = „Er und Onan; sie wurden wieder zum Leben erweckt“. EN-Frage um den Teil zur Bedeutung des Erstgeborenen ergänzen.

<sub>🔎 Gegenprüfung: Bestätigt. DE 0 nennt die richtigen Zwillinge in KJV-Schreibweise (Pharez/Zarah) und ist nur wegen des Zusatzes falsch. Das ist verwirrend, weil DE-Spieler die richtigen Namen doppelt sehen. Die EN-Distraktoren sind anders verteilt (EN0 Er/Onan, EN2 Manasse/Ephraim). Zusätzlich: Die DE-Frage nach der „theologischen Bedeutung“ geht über 38:29-30 hinaus.</sub>

---

#### `1mose_163` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nur nach Josephs Gefühlsreaktion (Lösung: Sein Herz wühlte sich auf). EN fragt, was Joseph sagte und was er danach tat (Lösung: "God be gracious unto thee…"). Frage, Lösung und alle Distraktoren unterscheiden sich inhaltlich.

**Aktuell DE** · _1. Mose 43:29-30_  
Wie reagierte Joseph emotional, als er seinen leiblichen Bruder Benjamin erblickte?

- ⬜ Er umarmte ihn sofort stürmisch vor allen Ägyptern und rief seinen Namen
- ⬜ Er blieb völlig kalt und distanziert, um keinen Verdacht zu erregen
- ⬜ Er fragte ihn streng aus, ob der Vater noch am Leben sei
- ✅ **Sein Herz wühlte sich auf gegen seinen Bruder** ← _als richtig markiert_

**Aktuell EN** · _Genesis 43:29-30_  
What did Joseph say when he saw his mother's son Benjamin, and what did he do immediately after?

- ⬜ "Welcome to Egypt"; he ordered his chariot to show him royal palaces
- ⬜ "Behold my beloved brother"; he embraced him before all servants with tears
- ⬜ "Art thou indeed the youngest?"; he commanded a golden garment for him
- ✅ **"God be gracious unto thee, my son"; he sought where to weep, into his chamber** ← _als richtig markiert_

> 📖 **Beleg:** DE: „Wie reagierte Joseph emotional…“ [x] „Sein Herz wühlte sich auf gegen seinen Bruder“ / EN: "What did Joseph say … and what did he do immediately after?" [x] "\"God be gracious unto thee, my son\"; he sought where to weep"

> ✏️ **Korrekturvorschlag:** Eine der beiden Fassungen angleichen, z. B. DE: „Was sagte Joseph, als er Benjamin sah, und was tat er unmittelbar danach?“ mit Lösung „»Gott sei dir gnädig, mein Sohn!«; er suchte einen Ort zum Weinen und ging in sein Gemach“ und den übersetzten EN-Distraktoren.

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nur nach der Gefühlsreaktion („Herz wühlte sich auf“), EN nach Worten und Handlung („God be gracious…; sought where to weep“). Frage, Lösung und Distraktoren sind verschieden. Beide Fassungen sind für sich textgemäß, müssen aber angeglichen werden.</sub>

---

#### `1mose_165` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach der Sitzordnung. EN fragt, warum die Brüder staunten. Die Distraktoren 0, 2 und 3 haben in DE und EN völlig anderen Inhalt (DE: Losverfahren, Wert der Geschenke, Söhne Leas/der Mägde; EN: Goldgefäße aus einem Baal-Tempel, hebräische Lieder, Opferfleisch).

**Aktuell DE** · _1. Mose 43:33_  
In welcher verblüffenden Reihenfolge mussten sich die Brüder vor Joseph zum Essen setzen?

- ⬜ In einer völlig zufälligen Reihenfolge, die der Verwalter ausloste
- ✅ **Der Erstgeborene zu oberst und der Jüngste zu unterst nach ihrem Alter** ← _als richtig markiert_
- ⬜ Nach dem Wert der Geschenke, die sie aus Kanaan mitgebracht hatten
- ⬜ Die Söhne Leas saßen rechts, die Söhne der Mägde links

**Aktuell EN** · _Genesis 43:33_  
Why were Joseph's brethren astonished when they sat down to dine before him?

- ⬜ They were served with gold vessels stolen from temple of Baal in Canaan
- ✅ **They sat the firstborn according to birthright, youngest according to youth** ← _als richtig markiert_
- ⬜ They heard the servants sing ancient Hebrew songs taught in Beersheba
- ⬜ They were offered sacrificial meat consecrated to Egyptian holy gods

> 📖 **Beleg:** DE: „In welcher verblüffenden Reihenfolge mussten sich die Brüder … setzen?“ / EN: "Why were Joseph's brethren astonished when they sat down to dine before him?"

> ✏️ **Korrekturvorschlag:** EN-Frage: "In what astonishing order were the brethren seated before Joseph?"; Distraktoren: "In a random order determined by lot by the steward", "According to the value of the presents they had brought from Canaan", "The sons of Leah on the right, the sons of the handmaids on the left"

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach der Sitzordnung, EN nach dem Grund des Staunens. Die Distraktoren 0, 2 und 3 sind völlig verschieden. Die Lösung 1 entspricht sich inhaltlich.</sub>

---

#### `1mose_167` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt, welcher Gegenstand in Benjamins Sack versteckt wurde. EN fragt nach der „final test“-Anordnung. Die Distraktoren sind völlig verschieden (DE: Zepter, Amtsgewand, Siegelkette; EN: Osiris-Götzenbild in Rubens Sack, Dokumente in Judas Sack, Wegnahme der Waffen).

**Aktuell DE** · _1. Mose 44:1-2_  
Welchen Gegenstand ließ Joseph im Sack des jüngsten Bruders Benjamin verstecken?

- ⬜ Das goldene Zepter des Pharao
- ⬜ Ein wertvolles ägyptisches Amts-Leibgewand
- ⬜ Eine goldene Siegelkette
- ✅ **Seinen Becher, den silbernen Becher** ← _als richtig markiert_

**Aktuell EN** · _Genesis 44:1-2_  
What final test did Joseph command his house steward to arrange in the sacks of his brethren?

- ⬜ To place a golden idol of Osiris in Reuben's sack to accuse him of theft
- ⬜ To hide royal palace documents in Judah's sack to charge him with treason
- ⬜ To take all their weapons secretly by night and leave them defenceless
- ✅ **To put my cup, the silver cup, in the sack's mouth of the youngest** ← _als richtig markiert_

> 📖 **Beleg:** DE: „Welchen Gegenstand ließ Joseph im Sack des jüngsten Bruders Benjamin verstecken?“ / EN: "What final test did Joseph command his house steward to arrange in the sacks of his brethren?"

> ✏️ **Korrekturvorschlag:** EN: "What object did Joseph cause to be hidden in the sack of the youngest, Benjamin?" mit 0 "Pharaoh's golden sceptre", 1 "A precious Egyptian robe of office", 2 "A golden signet chain", 3 [x] "My cup, the silver cup"

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach dem Gegenstand, EN nach der „final test“-Anordnung. Alle Distraktoren sind verschieden. Die Lösungen stimmen inhaltlich überein (silberner Becher).</sub>

---

#### `1mose_169` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** DE-Distraktor 3 gibt V. 16 sinngemäß richtig wieder ("wie sollen wir uns rechtfertigen? Gott hat die Missetat … gefunden"). Distraktor 0 kommt dem ebenfalls sehr nahe. Damit ist die Frage mehrdeutig. In EN sind die Distraktoren klar falsch und andere als in DE.

**Aktuell DE** · _1. Mose 44:16_  
Mit welchen theologischen Worten gestand Juda Joseph die ausweglose Lage der Brüder ein?

- ⬜ „Gott hat unsere geheime Schuld aufgedeckt; nimm nun unser ganzes Leben als Strafe!“
- ✅ **„Gott hat die Missetat deiner Knechte gefunden! Siehe, wir sind unseres Herrn Knechte...“** ← _als richtig markiert_
- ⬜ „Der Herr hat das Unrecht unserer Väter heimgesucht; wir beugen uns dem Urteil deines Hauses!“
- ⬜ „Wir vermögen uns nicht zu rechtfertigen, denn der Höchste hat unser Vergehen offenbart!“

> 📖 **Beleg:** DE 3: „Wir vermögen uns nicht zu rechtfertigen, denn der Höchste hat unser Vergehen offenbart!“ – DE-TEXT: „wie sollen wir uns rechtfertigen? Älohim hat die Missetat deiner Knechte gefunden!“

> ✏️ **Korrekturvorschlag:** DE-Distraktoren an EN angleichen, z. B. 0: „Die ägyptischen Wachen haben uns fälschlich beschuldigt! Wir sind ehrliche Händler!“, 2: „Nimm unsere Kamele und unser Silber, aber lass uns in Frieden nach Kanaan ziehen!“, 3: „Unser Vater Jakob ist ein heiliger Prophet; tastet seine geliebten Kinder nicht an!“

<sub>🔎 Gegenprüfung: Bestätigt. DE 3 ist eine fast wörtliche Umschreibung von V. 16 („wie sollen wir uns rechtfertigen? Älohim hat die Missetat … gefunden“). DE 0 kommt dem ebenfalls nahe. Bei einer Zitatfrage ist das mehrdeutig. Die EN-Distraktoren sind eindeutig falsch und inhaltlich anders. Die DE-Distraktoren sollten an EN angeglichen werden.</sub>

---

#### `1mose_193` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Urteil über Ruben, DE nach dem Grund für den Verlust der Erstgeburt. EN-Distraktor 2 ist ein angebliches Zitat über Königsherrschaft bis Schilo. Es passt nicht zur Frage (es betrifft Juda) und entspricht nicht DE-Option 2 (Weigerung, für Benjamin zu bürgen).

**Aktuell DE** · _1. Mose 49:3-4_  
Warum verlor Ruben, der Erstgeborene, sein Vorrecht auf die Erstgeburt laut Jakobs Urteil?

- ⬜ Weil er Joseph damals heimlich an fremde Händler verkauft hatte
- ✅ **Weil er wie kochendes Wasser war und seines Vaters Bett bestieg** ← _als richtig markiert_
- ⬜ Weil er sich weigerte, die Bürgschaft für Benjamin zu übernehmen
- ⬜ Weil er vor den Feinden geflohen war und feige gewirkt hatte

**Aktuell EN** · _Genesis 49:3-4_  
What solemn sentence did Jacob pronounce over his firstborn son Reuben?

- ⬜ Because he secretly sold Joseph of old unto travelling merchants
- ✅ **Because he was unstable as water and went up to his father's bed** ← _als richtig markiert_
- ⬜ "Thou shalt reign as king over all thy brethren until Shiloh cometh"
- ⬜ Because he fled before his enemies and acted in cowardice

> 📖 **Beleg:** DE 2: „Weil er sich weigerte, die Bürgschaft für Benjamin zu übernehmen“ / EN 2: "\"Thou shalt reign as king over all thy brethren until Shiloh cometh\""

> ✏️ **Korrekturvorschlag:** EN-Frage: "Why did Reuben, the firstborn, lose the excellency of his birthright according to Jacob?"; EN 2: "Because he refused to be surety for Benjamin"

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Frage („What solemn sentence…“) passt nicht zu den „Because…“-Optionen. EN 2 ist ein Juda/Schilo-Zitat und entspricht nicht DE 2 (Bürgschaft für Benjamin). Die EN-Frage sollte an DE angeglichen und EN 2 übersetzt werden.</sub>

---

#### `1mose_225` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Die Frage setzt einen Grund voraus, den der Bibeltext nicht nennt. 1. Mose 50:4 sagt nur, dass Joseph mit dem Haus des Pharao redete. Von Trauerkleidung oder ungeschorenem Haar ist keine Rede. Die markierte Lösung ist eine Auslegung (Rückschluss aus 41:14 / Est 4:2), wird aber als Bibelfakt abgefragt.

**Aktuell DE** · _1. Mose 50:4_  
Warum bat Joseph das Haus des Pharao und nicht den Pharao selbst um Erlaubnis zur Reise nach Kanaan?

- ⬜ Weil der Pharao schwer krank war und niemanden empfing
- ✅ **Weil er sich in Trauerkleidung befand und sich das Haar nicht schor** ← _als richtig markiert_
- ⬜ Weil Joseph die ägyptische Sprache verlernt hatte
- ⬜ Weil er Angst hatte, der Pharao würde ihn wegen Hochverrats verhaften lassen

**Aktuell EN** · _Genesis 50:4_  
Why did Joseph speak unto the house of Pharaoh rather than to Pharaoh himself to ask leave?

- ⬜ Because Pharaoh was sick and unable to receive visitors
- ✅ **Because he was in mourning apparel and unshaven for his father** ← _als richtig markiert_
- ⬜ Because Joseph had forgotten the court language of Egypt
- ⬜ Because he feared Pharaoh would arrest him for treason

> 📖 **Beleg:** DE-TEXT 50:4: „redete Joseph mit dem Hause des Pharao und sprach: Habe ich Gnade gefunden in euren Augen, so redet doch vor Pharaos Ohren“ – kein Grund genannt

> ✏️ **Korrekturvorschlag:** Frage umformulieren, z. B. „Über wen ließ Joseph den Pharao um Erlaubnis bitten, seinen Vater in Kanaan zu begraben?“ mit Lösung „Über das Haus des Pharao (dessen Hofleute)“, oder die Lösung ausdrücklich als Auslegung kennzeichnen.

<sub>🔎 Gegenprüfung: Bestätigt. 50:4 nennt keinen Grund, warum Joseph über das Haus des Pharao ging. Die Lösung „Trauerkleidung/ungeschoren“ ist eine verbreitete Auslegung (vgl. 41:14, Est 4:2), wird aber als Bibelfakt abgefragt. Frage umformulieren oder die Lösung als Auslegung kennzeichnen.</sub>

---

#### `1mose_264` · Bibelstelle

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Weder 1. Mose 15:12 noch das ganze Kapitel 15 nennt einen Ort für den Bundesschluss zwischen den Stücken. "Mamre (Hebron)" ist nur aus 13:18 und 14:13 erschlossen. Mit der angegebenen Stelle lässt sich die Frage nicht beantworten, und die Lösung wird als gesicherte Tatsache dargestellt.

**Aktuell DE** · _1. Mose 15:12_  
Wo fand der schauerliche Bundesschluss zwischen den Stücken statt, bei dem Abram in einen tiefen Schlaf und dichte Finsternis fiel?

- ✅ **Bei den Eichen von Mamre (Hebron)** ← _als richtig markiert_
- ⬜ In Haran in Mesopotamien
- ⬜ In Jerusalem (Salem)
- ⬜ In Gerar im Land der Philister

**Aktuell EN** · _Genesis 15:12_  
Where did the covenant between the pieces take place, when deep sleep and horror of darkness fell upon Abram?

- ✅ **At the plain of Mamre (in Hebron)** ← _als richtig markiert_
- ⬜ At Haran in northern Mesopotamia
- ⬜ At the city of Jerusalem (Salem)
- ⬜ At Gerar in land of the Philistines

> 📖 **Beleg:** DE-TEXT 15:12: "Da nun die Sonne anfing sich zu neigen, fiel ein tiefer Schlaf auf Abram ..." (keine Ortsangabe)

> ✏️ **Korrekturvorschlag:** Frage umformulieren, z. B.: "Wo wohnte Abram (vgl. 1. Mose 13:18; 14:13), bevor Gott mit ihm den Bund zwischen den Stücken schloss?" und bibleReference auf "1. Mose 13:18; 14:13" setzen. Alternativ etwas fragen, das in 15:12 steht (tiefer Schlaf bei Sonnenuntergang).

<sub>🔎 Gegenprüfung: Bestätigt. Kapitel 15 nennt keinen Ort. Mamre ist nur aus dem Kontext erschlossen (13:18; 14:13; vgl. 18:1). Die Antwort ist plausibel, wird aber als Tatsache aus 15:12 ausgegeben. Frage auf den Wohnort Abrams (13:18) umstellen oder etwas fragen, das in 15:12 steht.</sub>

---

#### `1mose_276` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die Distraktoren 2 und 3 haben in DE und EN einen anderen Inhalt. Außerdem passt die Erklärung (stellvertretendes Sühnopfer) nicht zur markierten Lösung (Dornenkrone).

**Aktuell DE** · _1. Mose 22:13_  
Nach christlicher (typologischer) Auslegung – Der Widder, den Abraham stellvertretend für Isaak opferte, war „mit seinen Hörnern im Gestrüpp verwickelt“. Welches neutestamentliche Schattenbild deutet sich hier an?

- ✅ **Die Dornenkrone auf dem Haupt Jesu Christi bei Seiner Kreuzigung** ← _als richtig markiert_
- ⬜ Der Hirtenstab, mit dem Mose später das Rote Meer teilte
- ⬜ Die zukünftige Posaune (Schofar) beim Gericht am Sinai
- ⬜ Das unlösbare Joch des mosaischen Gesetzes

**Aktuell EN** · _Genesis 22:13_  
According to Christian typological interpretation, what New Testament figure is foreshadowed by the ram caught in the thicket?

- ✅ **The crown of thorns placed upon Christ's head at His crucifixion** ← _als richtig markiert_
- ⬜ The shepherd's rod with which Moses parted the waters of Red Sea
- ⬜ The golden crown worn by the kings of Judah when going to battle
- ⬜ The brazen serpent lifted up upon a pole in the barren wilderness

> 📖 **Beleg:** DE 2: "Die zukünftige Posaune (Schofar) beim Gericht am Sinai" / EN 2: "The golden crown worn by the kings of Judah"; DE 3: "Das unlösbare Joch des mosaischen Gesetzes" / EN 3: "The brazen serpent lifted up upon a pole"

> ✏️ **Korrekturvorschlag:** EN 2: "The trumpet (shofar) sounding at the judgment on Sinai"; EN 3: "The unbearable yoke of the Mosaic law". Die Erklärung um den Bezug Dornen/Dornenkrone ergänzen (vgl. 1. Mose 3:18; Johannes 19:2).

<sub>🔎 Gegenprüfung: Bestätigt. In Distraktor 2 und 3 steht in DE Schofar/Joch, in EN goldene Krone/eherne Schlange. Auch der Einwand zur Erklärung trifft zu: Sie begründet die Stellvertretung, nicht den Bezug Gestrüpp/Dornenkrone. Erklärung um Dornen ergänzen (1. Mose 3:18; Joh 19:2).</sub>

---

#### `1mose_277` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die Distraktoren 0, 2 und 3 haben in DE und EN völlig verschiedenen Inhalt.

**Aktuell DE** · _1. Mose 40:21-22_  
Nach christlicher (typologischer) Auslegung – Josephs zwei Mitgefangene im Gefängnis des Pharao (der Mundschenk und der Bäcker) erleben zwei völlig unterschiedliche Schicksale (1. Mose 40). Welches Golgatha-Schattenbild verbirgt sich hier?

- ⬜ Die beiden Könige Saul und David: Der Ungehorsame wird vom Königtum verworfen, während der Treue auf den Thron gelangt
- ✅ **Die beiden Schächer (Verbrecher) am Kreuz neben Jesus: Einer wird begnadigt und gerettet, der andere verurteilt und gerichtet** ← _als richtig markiert_
- ⬜ Die zwei Bundestafeln vom Sinai: Das geschriebene Gesetz, das den Sünder verdammt, und das Opferblut, das Gnade spendet
- ⬜ Das Volk Israel und die heidnischen Nationen: Die Unbußfertigen verfallen dem Gericht, während die Erwählten Gnade finden

**Aktuell EN** · _Genesis 40:21-22_  
According to Christian typological interpretation, what scene is foreshadowed by the butler and the baker in prison?

- ⬜ The two disciples walking together on the dusty road to Emmaus
- ✅ **The two thieves crucified with Christ: one pardoned, the other dying** ← _als richtig markiert_
- ⬜ Moses and Aaron standing before Pharaoh demanding Israel's freedom
- ⬜ Peter and John healing the lame man at the beautiful temple gate

> 📖 **Beleg:** DE 0: "Die beiden Könige Saul und David ..." / EN 0: "The two disciples walking ... to Emmaus"; DE 2: "Die zwei Bundestafeln vom Sinai ..." / EN 2: "Moses and Aaron standing before Pharaoh"; DE 3: "Das Volk Israel und die heidnischen Nationen ..." / EN 3: "Peter and John healing the lame man"

> ✏️ **Korrekturvorschlag:** EN-Distraktoren aus DE übersetzen, z. B. EN 0: "The two kings Saul and David: the disobedient rejected, the faithful enthroned"; EN 2: "The two tables of the law: the written law condemning, the blood granting grace"; EN 3: "Israel and the Gentile nations: the impenitent judged, the elect finding grace".

<sub>🔎 Gegenprüfung: Bestätigt. Die Distraktoren 0, 2 und 3 sind in DE (Saul/David, Bundestafeln, Israel/Nationen) und EN (Emmaus, Mose/Aaron, Petrus/Johannes) inhaltlich verschieden. Die Lösung 1 stimmt überein.</sub>

---

#### `1mose_282` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die Fragen unterscheiden sich: DE fragt auch, warum das Tier zerteilt wurde, EN nur, warum Gott allein hindurchging. Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt.

**Aktuell DE** · _1. Mose 15:9-18_  
Nach christlicher (typologischer) Auslegung – Warum musste das Opfertier beim Bundesschluss Abrahams exakt in zwei Hälften zerteilt werden, und was bedeutete das feurige Hindurchfahren Gottes?

- ⬜ Das Zerteilen diente allein dem rascheren Verbrennen auf dem Altar
- ⬜ Abraham musste hindurchgehen, um seine absolute Sündlosigkeit zu beweisen
- ✅ **Gott schritt allein hindurch und übernahm bürgend die volle Bundesverpflichtung** ← _als richtig markiert_
- ⬜ Das Zerteilen stellte die künftige Spaltung der zwölf Stämme Israels dar

**Aktuell EN** · _Genesis 15:9-18_  
According to Christian typological interpretation, why did God alone pass between the divided pieces in Genesis 15?

- ⬜ Abram had fallen asleep and forgotten the solemn covenant ritual
- ⬜ Because human beings were forbidden to walk upon blood of sacrifice
- ✅ **To show that God alone bound Himself unilaterally to fulfill covenant** ← _als richtig markiert_
- ⬜ To prove that Abram's seed would never suffer any earthly hardship

> 📖 **Beleg:** DE 0: "Das Zerteilen diente allein dem rascheren Verbrennen" / EN 0: "Abram had fallen asleep and forgotten the solemn covenant ritual"; DE 1: "Abraham musste hindurchgehen, um seine absolute Sündlosigkeit zu beweisen" / EN 1: "human beings were forbidden to walk upon blood"; DE 3: "künftige Spaltung der zwölf Stämme" / EN 3: "Abram's seed would never suffer any earthly hardship"

> ✏️ **Korrekturvorschlag:** EN-Frage und EN-Distraktoren an DE angleichen, z. B. EN 0: "The dividing served only to burn the pieces faster upon the altar"; EN 1: "Abram had to pass through to prove his complete sinlessness"; EN 3: "The dividing pictured the future split of the twelve tribes".

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt zusätzlich nach dem Sinn des Zerteilens, EN nur nach Gottes alleinigem Hindurchgehen. Die Distraktoren 0, 1 und 3 weichen inhaltlich voneinander ab. EN-Frage und EN-Distraktoren an DE angleichen.</sub>

---

#### `1mose_283` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die Distraktoren 0, 1 und 2 haben in DE und EN völlig verschiedenen Inhalt.

**Aktuell DE** · _1. Mose 41:40-44_  
Nach christlicher (typologischer) Auslegung – Inwiefern ist Josephs Erhöhung vom tiefsten Kerker direkt auf den Thron als Vizekönig von Ägypten (1. Mose 41) ein Vorbild (Typus) auf Jesus Christus?

- ⬜ Joseph stürzte den Pharao vom Thron und regierte als weltlicher Monarch
- ⬜ Joseph heiratete die heidnischen Götzenpriesterinnen gegen Gottes Willen
- ⬜ Joseph eroberte den Thron mit einem gewaltigen hebräischen Söldnerheer
- ✅ **Nach tiefster Erniedrigung wurde er erhöht und über das ganze Reich gesetzt** ← _als richtig markiert_

**Aktuell EN** · _Genesis 41:40-44_  
According to Christian typological interpretation, how does Joseph's exaltation from prison foreshadow Jesus Christ?

- ⬜ Joseph established an earthly dynasty of Hebrew kings over Egypt
- ⬜ He built magnificent granaries which typified the temple of God
- ⬜ He used his power to punish all pagan priests throughout the land
- ✅ **His humiliation in prison followed by exaltation typifieth Christ** ← _als richtig markiert_

> 📖 **Beleg:** DE 0: "Joseph stürzte den Pharao vom Thron" / EN 0: "Joseph established an earthly dynasty of Hebrew kings"; DE 1: "heiratete die heidnischen Götzenpriesterinnen" / EN 1: "He built magnificent granaries which typified the temple"; DE 2: "eroberte den Thron mit einem ... Söldnerheer" / EN 2: "He used his power to punish all pagan priests"

> ✏️ **Korrekturvorschlag:** EN-Distraktoren aus DE übersetzen: "Joseph overthrew Pharaoh and reigned as a worldly monarch"; "Joseph married heathen priestesses against God's will"; "Joseph seized the throne with a mighty army of Hebrew mercenaries".

<sub>🔎 Gegenprüfung: Bestätigt. Die Distraktoren 0, 1 und 2 sind in DE und EN inhaltlich verschieden (Sturz des Pharao/Götzenpriesterinnen/Söldnerheer gegenüber Dynastie/Kornspeicher/Bestrafung der Priester). Die Lösung 3 stimmt überein.</sub>

---

#### `1mose_284` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die richtige Antwort hat in DE und EN einen anderen Inhalt. DE: Der höchste Segen wird durch Gnade verliehen, nicht nach dem Fleisch. EN: das Kreuz Christi. Auch die Distraktoren 1 bis 3 sagen in DE und EN völlig Verschiedenes (DE: Versehen, ägyptischer Ritus, gleiches Erbteil; EN: Verwerfung der Patriarchen, Priesterritual, körperliche Schwäche).

**Aktuell DE** · _1. Mose 48:13-19_  
Nach christlicher (typologischer) Auslegung – Welches messianische Geheimnis offenbart das „kreuzweise Auflegen“ der Hände Jakobs bei der Segnung von Josephs Söhnen Ephraim und Manasseh?

- ✅ **Dass der höchste Segen nicht nach dem Fleisch, sondern durch Gnade verliehen wird** ← _als richtig markiert_
- ⬜ Jakob war altersschwach und beging ein Versehen, das er später bereute
- ⬜ Das Kreuzen der Arme war ein altägyptischer Ritus zur Abwehr böser Geister
- ⬜ Es sollte verdeutlichen, dass beide Brüder exakt denselben Erbteil bekamen

**Aktuell EN** · _Genesis 48:13-19_  
According to Christian typological interpretation, what mystery is revealed by Jacob crossing his hands to bless Ephraim?

- ✅ **The cross of Christ, through which blessing passeth by sovereign grace** ← _als richtig markiert_
- ⬜ The rejection of all Hebrew patriarchs in favour of Egyptian lords
- ⬜ A royal priestly ritual that could only be performed by the aged
- ⬜ A sign of physical weakness because Jacob could not lift his arms

> 📖 **Beleg:** DE [x] 0: "Dass der höchste Segen nicht nach dem Fleisch, sondern durch Gnade verliehen wird" vs. EN [x] 0: "The cross of Christ, through which blessing passeth by sovereign grace"

> ✏️ **Korrekturvorschlag:** EN-Lösung angleichen: "That the highest blessing is bestowed not after the flesh but by grace". EN-Distraktoren 1 bis 3 aus DE übersetzen, z. B.: "Jacob was feeble with age and made a mistake he later regretted" usw.

<sub>🔎 Gegenprüfung: Bestätigt. DE-Lösung: Gnade statt Fleisch. EN-Lösung: Kreuz Christi. Die Distraktoren 1 bis 3 sind inhaltlich völlig verschieden. EN-Lösung und EN-Distraktoren aus DE übersetzen.</sub>

---

#### `1mose_285` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt. Zusätzlich in DE: "jerusalemer" muss groß geschrieben werden ("Jerusalemer").

**Aktuell DE** · _1. Mose 41:45_  
Nach christlicher (typologischer) Auslegung – Wie spiegelt die Ehe Josephs mit der ägyptischen Priestertochter Asnath während seiner Verwerfung durch seine Brüder das Heilszeitalter wider?

- ⬜ Joseph verwarf den Glauben seiner Väter und übernahm die Religion Ägyptens
- ✅ **Während Seiner Verwerfung gewinnt der Messias eine Braut aus den Heidenvölkern** ← _als richtig markiert_
- ⬜ Die Verbindung zeigte, dass Israel seine Eigenart völlig aufgeben sollte
- ⬜ Asnath wurde zur Hohepriesterin des jerusalemer Heiligtums ernannt

**Aktuell EN** · _Genesis 41:45_  
According to Christian typological interpretation, how does Joseph's marriage to Asenath foreshadow Christ and the church?

- ⬜ It showed that Hebrew patriarchs should take wives of the heathen
- ✅ **Christ taketh a Gentile bride during His rejection by His brethren** ← _als richtig markiert_
- ⬜ Asenath was a prophetess who converted Pharaoh to worship of God
- ⬜ It symbolized the political union of Egyptian and Hebrew nations

> 📖 **Beleg:** DE 0: "Joseph verwarf den Glauben seiner Väter" / EN 0: "Hebrew patriarchs should take wives of the heathen"; DE 2: "Israel seine Eigenart völlig aufgeben sollte" / EN 2: "Asenath was a prophetess who converted Pharaoh"; DE 3: "Asnath wurde zur Hohepriesterin des jerusalemer Heiligtums ernannt" / EN 3: "political union of Egyptian and Hebrew nations"

> ✏️ **Korrekturvorschlag:** EN-Distraktoren aus DE übersetzen (z. B. EN 3: "Asenath was appointed high priestess of the sanctuary at Jerusalem"); in DE "des Jerusalemer Heiligtums" schreiben.

<sub>🔎 Gegenprüfung: Bestätigt. Die Distraktoren 0, 2 und 3 sind in DE und EN verschieden. Die Kleinschreibung 'jerusalemer' ist ebenfalls falsch: Ableitungen von Ortsnamen auf -er werden großgeschrieben ('des Jerusalemer Heiligtums').</sub>

---

#### `1mose_286` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Alle drei Distraktoren (0, 1, 3) haben in DE und EN einen anderen Inhalt.

**Aktuell DE** · _1. Mose 3:21_  
Nach christlicher (typologischer) Auslegung – Als Gott Adam und Eva «Röcke von Fellen» machte, um ihre Blöße dauerhaft zu bedecken: Welches geistliche Fundament der Sühne wird hier gelegt?

- ⬜ Der gefallene Mensch sollte lernen, sich durch mühsame Handarbeit aus Wolle und Flachs selbst zu schützen
- ⬜ Die rauhen Tierhäute sollten die Menschen täglich an die Härte und Entbehrung der verfluchten Erde gemahnen
- ✅ **Die Vergebung und Bedeckung der Schuld erfordert das Sterben eines unschuldigen Stellvertreters (Blutverguss)** ← _als richtig markiert_
- ⬜ Gott veranschaulichte damit, dass Vergängliches abgelegt werden muss, um ewige Reinheit im Geist zu empfangen

**Aktuell EN** · _Genesis 3:21_  
According to Christian typological interpretation, what was foreshadowed when God made coats of skins for Adam and Eve?

- ⬜ That man should henceforth live solely by hunting wild woodland beasts
- ⬜ That human clothing must always be fashioned from pure white sheep
- ✅ **A spotless sacrifice had to die and shed blood to cover man's guilt** ← _als richtig markiert_
- ⬜ That human works of righteousness are sufficient to please the LORD

> 📖 **Beleg:** DE 0: "sich durch mühsame Handarbeit aus Wolle und Flachs selbst zu schützen" / EN 0: "live solely by hunting wild woodland beasts"; DE 1: "Tierhäute sollten ... an die Härte ... der verfluchten Erde gemahnen" / EN 1: "clothing must always be fashioned from pure white sheep"; DE 3: "Vergängliches abgelegt werden muss" / EN 3: "human works of righteousness are sufficient"

> ✏️ **Korrekturvorschlag:** EN-Distraktoren an DE angleichen, z. B. EN 0: "Fallen man should learn to clothe himself by toil with wool and flax"; EN 1: "The rough skins should daily remind men of the hardship of the cursed ground"; EN 3: "God showed that perishable things must be put off to receive eternal purity".

<sub>🔎 Gegenprüfung: Bestätigt. Die Distraktoren 0, 1 und 3 sind in DE (Wolle/Flachs, Härte der Erde, Vergängliches ablegen) und EN (Jagd, weiße Schafe, Werkgerechtigkeit) inhaltlich verschieden.</sub>

---

### 📄 `02_2_mose.json` (8)

#### `ex_018` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die Verwandtschaft ist vertauscht. Jethro war der Schwiegervater des Mose, nicht umgekehrt. Die deutsche Frage nennt Mose Jethros "Schwiegervater". Die EN-Fassung enthält den Fehler nicht.

**Aktuell DE** · _2. Mose 18:21-22_  
Welchen praktischen Rat gab Jethro seinem Schwiegervater Mose zur Bewältigung der Rechtsprechung?

- ⬜ Er sollte alle Rechtsfälle allein bis zum Abend hin entscheiden
- ⬜ Er sollte das Richten den hebräischen Priestern ganz übergeben
- ⬜ Er sollte das Volk ohne Richter alle Streitigkeiten tragen lassen
- ✅ **Er sollte Fürsten über tausend, hundert, fünfzig und zehn einsetzen** ← _als richtig markiert_

> 📖 **Beleg:** DE: "Welchen praktischen Rat gab Jethro seinem Schwiegervater Mose ..."; 2. Mose 18:1: "Jethro, der Priester in Midian, Moses Schwiegervater"

> ✏️ **Korrekturvorschlag:** "Welchen praktischen Rat gab Jethro, der Schwiegervater des Mose, ihm zur Bewältigung der Rechtsprechung?" (oder: "... seinem Schwiegersohn Mose ...")

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage vertauscht die Verwandtschaft: Jethro war der Schwiegervater des Mose (2. Mose 18:1). Die Lösung ist davon nicht betroffen, der Fragetext enthält aber einen sachlichen Fehler, deshalb mittel statt hoch. Korrektur: 'Welchen praktischen Rat gab Jethro seinem Schwiegersohn Mose ...'.</sub>

---

#### `ex_106` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN-Distraktor 2 ('Where shall we find good water to drink?') ist inhaltlich ein anderer Ausruf als DE 2 ('Wann erreichen wir die Oasen?'). Er liegt außerdem sehr nah an der richtigen Antwort 'What shall we drink?'.

**Aktuell DE** · _2. Mose 15:24_  
Welche klagende Frage rief das durstige Volk in Mara gegen Mose aus?

- ⬜ »Warum führtest du uns hierher?«
- ⬜ »Gibt es keine Gräber in Ägypten?«
- ⬜ »Wann erreichen wir die Oasen?«
- ✅ **»Was sollen wir trinken?«** ← _als richtig markiert_

**Aktuell EN** · _Exodus 15:24_  
What complaining question did the thirsty people murmur against Moses at Marah?

- ⬜ "Why hast thou brought us into this place?"
- ⬜ "Were there no graves for us in Egypt?"
- ⬜ "Where shall we find good water to drink?"
- ✅ **"What shall we drink?"** ← _als richtig markiert_

> 📖 **Beleg:** DE 2: "»Wann erreichen wir die Oasen?«" / EN 2: "\"Where shall we find good water to drink?\""

> ✏️ **Korrekturvorschlag:** EN 2: '"When shall we reach the oases?"'

<sub>🔎 Gegenprüfung: Bestätigt. EN 2 'Where shall we find good water to drink?' hat einen anderen Inhalt als DE 2 und ist zudem fast gleichbedeutend mit der richtigen Antwort 'What shall we drink?'. Dadurch wird die EN-Frage mehrdeutig, deshalb severity mittel. EN 2 z. B. in '"When shall we reach the oases?"' ändern.</sub>

---

#### `ex_184` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die richtige DE-Antwort lautet 'Der Betroffene musste unweigerlich sterben'. 'Der Betroffene' meint normalerweise das Opfer. Laut Text muss aber der Täter (Menschenräuber) sterben. Auch die Frage ist sprachlich falsch: 'traf einen Menschenraub, der eine Person entführte' statt 'einen Menschenräuber'.

**Aktuell DE** · _2. Mose 21:16_  
Welches Gericht traf einen Menschenraub, der eine Person entführte und verkaufte?

- ⬜ Er musste das dreifache Lösegeld erstatten
- ✅ **Der Betroffene musste unweigerlich sterben** ← _als richtig markiert_
- ⬜ Er wurde für sieben Jahre Knecht im Land
- ⬜ Er wurde in eine Zufluchtsstadt verbannt

> 📖 **Beleg:** DE-TEXT 21:16: "Wer einen Menschen stiehlt und ihn verkauft ... der soll des Todes sterben."

> ✏️ **Korrekturvorschlag:** Frage: 'Welches Gericht traf einen Menschenräuber, der eine Person entführte und verkaufte?'; Option 1: 'Der Menschenräuber musste unweigerlich sterben'.

<sub>🔎 Gegenprüfung: Bestätigt. Die Frage schreibt 'Menschenraub' statt 'Menschenräuber'. 'Der Betroffene' in der Lösung ist missverständlich, weil man dabei an das Opfer denkt. Laut 21:16 muss der Täter sterben. Korrektur wie vorgeschlagen, z. B. 'Er (der Menschenräuber) musste unweigerlich sterben'.</sub>

---

#### `ex_204` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Die Frage ist mehrdeutig. Mose teilte das Blut in zwei Hälften: Die eine sprengte er auf den Altar (V. 6). Die andere füllte er in Becken und sprengte sie später auf das Volk (V. 8). Damit treffen Option 0 (Altar) und Option 2 (in Schalen gefüllt) teilweise ebenfalls zu.

**Aktuell DE** · _2. Mose 24:6-8_  
Was tat Mose mit der Hälfte des Opferblutes beim feierlichen Bundesschluss?

- ⬜ Er goss es vollständig am Altar aus
- ✅ **Er besprengte damit das Volk Israel** ← _als richtig markiert_
- ⬜ Er füllte es in die goldenen Schalen
- ⬜ Er salbte damit die Stirn der Priester

**Aktuell EN** · _Exodus 24:6-8_  
What did Moses do with half of the sacrificial blood at the ratification of the covenant?

- ⬜ He poured it out entirely at the base of the mountain altar
- ✅ **He sprinkled it on the people, saying, Behold the blood** ← _als richtig markiert_
- ⬜ He filled the golden bowls of the sanctuary with it
- ⬜ He anointed the foreheads of Aaron and all his sons

> 📖 **Beleg:** DE-TEXT: "nahm die Hälfte des Blutes und tat es in Becken; aber die andere Hälfte des Blutes sprengte er auf den Altar"; DE 2: "Er füllte es in die goldenen Schalen"

> ✏️ **Korrekturvorschlag:** Frage präzisieren: "Was tat Mose schließlich mit der in Becken aufgefangenen Hälfte des Blutes?" / EN: "What did Moses finally do with the half of the blood he had put in basons?". Option 2 ersetzen, z. B. "Er goss es in den Fluss".

<sub>🔎 Gegenprüfung: Zutreffend. 24:6 nennt zwei Hälften: Eine kam in Becken, die andere wurde auf den Altar gesprengt. 'Die Hälfte' ist daher mehrdeutig, und DE/EN 2 ('in die goldenen Schalen gefüllt') beschreibt im Kern V.6 (Becken, nicht ausdrücklich golden). Option 0 ('vollständig ausgegossen') ist eher klar falsch. Die vorgeschlagene Präzisierung ist sinnvoll.</sub>

---

#### `ex_225` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach dem Material des Gitters (27:4). EN fragt, was unter der Einfassung des Altars angebracht war (Lage, 27:5). Auch die Distraktoren sind andere: DE vergoldetes Holz, Silber, Eisen; EN Steine, Goldplatte, Silberbecken. Die EN-Frage wird außerdem von der angegebenen Stelle 27:4 nicht gedeckt.

**Aktuell DE** · _2. Mose 27:4_  
Woraus bestand das Gitternetz, das unter dem Rand des Brandopferaltars angebracht war?

- ⬜ Aus vergoldetem Akazienholz mit Ringen
- ⬜ Aus gegossenem Silber aus den Spenden
- ✅ **Aus einem Netzgitter von reinem Erz** ← _als richtig markiert_
- ⬜ Aus geflochtenem Eisen der Handwerker

**Aktuell EN** · _Exodus 27:4_  
What was placed under the compass of the altar beneath, even to the midst of the altar?

- ⬜ A thick layer of stones gathered from the brook
- ⬜ A solid golden plate to catch the fallen coals
- ✅ **A grate of network of brass with four rings** ← _als richtig markiert_
- ⬜ A silver basin designed to hold the ashes safe

> 📖 **Beleg:** DE: "Woraus bestand das Gitternetz, das unter dem Rand ... angebracht war?"; EN: "What was placed under the compass of the altar beneath, even to the midst of the altar?"

> ✏️ **Korrekturvorschlag:** EN angleichen: "Of what was the grate of network made that was put under the compass of the altar?". Distraktoren: "Of shittim wood overlaid with gold", "Of cast silver from the offerings", "Of wrought iron".

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Frage fragt nach der Lage (27:5, nicht in der Stelle 27:4 enthalten), die DE-Frage nach dem Material, und alle Distraktoren unterscheiden sich. Die Lösung (ehernes Gitter) ist zwar in beiden gleich, trotzdem müssen Frage und Distraktoren angeglichen werden.</sub>

---

#### `ex_289` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** DE fragt nach der alleräußersten Decke, Lösung: Seehundsfelle. Die EN-Lösung nennt zwei Decken (rote Widderfelle und Dachsfelle), passt also nicht zur Frage nach „the outermost covering“ und weicht von der DE-Lösung ab. Auch alle EN-Distraktoren haben einen anderen Inhalt als die DE-Distraktoren.

**Aktuell DE** · _2. Mose 36:19_  
Woraus bestand die alleräußerste Schutzdecke, die über das Zelt der Stiftshütte gelegt wurde?

- ⬜ Aus einer feinen Decke aus gewobenem Byssusleinen
- ⬜ Aus einer dicken Schicht von gezwirntem Ziegenhaar
- ✅ **Aus einer wetterfesten Decke von dunklen Seehundsfellen** ← _als richtig markiert_
- ⬜ Aus einer Decke von rot gefärbten Schafswollfäden

**Aktuell EN** · _Exodus 36:19_  
Of what skins was the outermost covering made above the tent of the tabernacle?

- ⬜ A vast canopy of white bleached lambskins sewn with wire
- ⬜ A heavy covering woven of thick camel fleece and sheepskins
- ✅ **A covering of rams' skins dyed red, and badgers' skins above that** ← _als richtig markiert_
- ⬜ An oiled leather covering stripped from desert cattle

> 📖 **Beleg:** DE 2 [x]: "Aus einer wetterfesten Decke von dunklen Seehundsfellen"; EN 2 [x]: "A covering of rams' skins dyed red, and badgers' skins above that"

> ✏️ **Korrekturvorschlag:** EN 2: "A covering of badgers' skins above that". EN-Distraktoren an DE angleichen (fine twined linen / goats' hair / wool dyed red).

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Lösung nennt beide Decken aus 36:19, gefragt ist aber nur 'the outermost covering'. Sie weicht damit von DE (nur Seehundsfelle) ab, und alle Distraktoren unterscheiden sich.</sub>

---

#### `ex_303` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Distraktor 1 bezeichnet Eleasar als den erstgeborenen Sohn Aarons. Erstgeborener war Nadab (2. Mose 6:23; 4. Mose 3:2), Eleasar war der dritte Sohn. Der Spieler lernt hier eine falsche Tatsache.

**Aktuell DE** · _2. Mose 38:21_  
Welcher Priester leitete die genaue Berechnung und Inventur des Materials der Stiftshütte?

- ✅ **Ithamar der Sohn des Priesters Aaron** ← _als richtig markiert_
- ⬜ Eleasar der erstgeborene Sohn Aarons
- ⬜ Pinchas der Eiferer aus dem Hause Levis
- ⬜ Abihu der zweite Sohn des Priesters Aaron

**Aktuell EN** · _Exodus 38:21_  
Which priest was in charge of the inventory and counting of the materials of the tabernacle?

- ✅ **Ithamar, son to Aaron the priest, by Moses' command** ← _als richtig markiert_
- ⬜ Eleazar the firstborn son of Aaron the high priest
- ⬜ Phinehas the zealous servant of the house of Levi
- ⬜ Abihu the second son of Aaron who served at altar

> 📖 **Beleg:** DE 1: "Eleasar der erstgeborene Sohn Aarons"; EN 1: "Eleazar the firstborn son of Aaron the high priest"

> ✏️ **Korrekturvorschlag:** DE 1: "Eleasar der dritte Sohn Aarons" / EN 1: "Eleazar the third son of Aaron the high priest".

<sub>🔎 Gegenprüfung: Bestätigt. Eleasar war der dritte Sohn, Nadab der Erstgeborene (2. Mose 6:23; 4. Mose 3:2). Der Distraktor vermittelt damit eine falsche Tatsache.</sub>

---

#### `ex_316` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt, was mit Aaron und seinen Söhnen nach dem Waschen geschah (Lösung: bekleidet und gesalbt). EN fragt nach dem Zweck der Salbung (Lösung: ewiges Priestertum). Frage, Lösung und Distraktoren unterscheiden sich inhaltlich.

**Aktuell DE** · _2. Mose 40:13-15_  
Was geschah mit Aaron und seinen Söhnen, als sie am Eingang des Zeltes gewaschen wurden?

- ⬜ Sie wurden zu Richtern des Volkes gewählt
- ✅ **Sie wurden bekleidet und gesalbt zum Dienst** ← _als richtig markiert_
- ⬜ Sie wurden in das Land Midian gesandt
- ⬜ Sie legten ein Fastengelübde ab

**Aktuell EN** · _Exodus 40:13-15_  
What was the purpose of anointing Aaron and his sons with the holy oil?

- ⬜ To exempt them from all physical labor throughout life
- ✅ **Their anointing shall surely be an everlasting priesthood** ← _als richtig markiert_
- ⬜ To make them the military rulers of the twelve tribes
- ⬜ To grant them ownership of the tabernacle vessels

> 📖 **Beleg:** DE: "Was geschah mit Aaron und seinen Söhnen, als sie ... gewaschen wurden?" [x] "Sie wurden bekleidet und gesalbt zum Dienst"; EN: "What was the purpose of anointing Aaron and his sons...?" [x] "Their anointing shall surely be an everlasting priesthood"

> ✏️ **Korrekturvorschlag:** Eine Fassung an die andere angleichen, z. B. DE: "Welchem Zweck diente die Salbung Aarons und seiner Söhne?" – "Sie sollte ihnen ein ewiges Priestertum verschaffen". Die Distraktoren entsprechend übersetzen.

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach dem Vorgang (bekleidet/gesalbt), EN nach dem Zweck (ewiges Priestertum). Frage, Lösung und Distraktoren unterscheiden sich vollständig.</sub>

---

### 📄 `03_3_mose.json` (4)

#### `lev_006` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Die DE-Frage spricht von einem „sozial Armen“. In 3. Mose 1:14 geht es aber allgemein um ein Brandopfer aus Geflügel, ohne Bezug auf Armut (der steht erst in 5:7 bzw. 12:8). Die EN-Frage enthält diese Einschränkung nicht. Auch die Distraktoren 1 bis 3 haben im DE und im EN einen anderen Inhalt.

**Aktuell DE** · _3. Mose 1:14_  
Welche Vögel durfte ein sozial Armer als vollwertiges Brandopfer dem HERRN darbringen?

- ✅ **Turteltauben oder junge Felsentauben** ← _als richtig markiert_
- ⬜ Junge Tauben oder frische Wachteln
- ⬜ Junge Hühner oder kleine Turteltauben
- ⬜ Sperlinge oder wild gefangene Raben

**Aktuell EN** · _Leviticus 1:14_  
Which fowls was a man permitted to bring for a burnt offering unto the LORD?

- ✅ **Turtledoves, or young pigeons** ← _als richtig markiert_
- ⬜ Sparrows, or wild fowls of the hills
- ⬜ Quails, or partridges from the fields
- ⬜ Swallows, or white birds of the brook

> 📖 **Beleg:** DE: "Welche Vögel durfte ein sozial Armer als vollwertiges Brandopfer ... darbringen?"; DE-TEXT: "Soll aber seine Brandopfergabe ... aus Geflügel bestehen"; DE 1: "Junge Tauben oder frische Wachteln" vs EN 1: "Sparrows, or wild fowls"

> ✏️ **Korrekturvorschlag:** DE: "Welche Vögel durften als Brandopfer aus Geflügel dem HERRN dargebracht werden?". DE-Distraktoren an EN angleichen (Sperlinge/Wildvögel, Wachteln/Rebhühner, Schwalben/weiße Bachvögel).

<sub>🔎 Gegenprüfung: Bestätigt und verschärft. 'sozial Armer' steht nicht in 1:14, und die Distraktoren weichen von EN ab. Zusätzlich enthalten DE 1 ('Junge Tauben oder frische Wachteln') und DE 2 ('Junge Hühner oder kleine Turteltauben') jeweils eine laut Text richtige Vogelart, sind also teilweise richtig. Deshalb mittel. Die DE-Distraktoren sollten wie vorgeschlagen an EN angeglichen werden.</sub>

---

#### `lev_031` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Lösung hängt 'and not a sweet savour' an. Das steht nicht in 3. Mose 5:11 und widerspricht 3. Mose 4:31, wo das Fett des Sündopfers ausdrücklich 'for a sweet savour unto the LORD' verbrannt wird. Die Option liest sich wie ein KJV-Zitat, ist aber an dieser Stelle sachlich falsch.

**Aktuell EN** · _Leviticus 5:11_  
Why was the poor man commanded to put NO oil and NO frankincense upon his flour offering?

- ⬜ Because fine olive oil was too costly for his family
- ✅ **For it is a sin offering, and not a sweet savour** ← _als richtig markiert_
- ⬜ Because frankincense was reserved solely for the princes
- ⬜ Because mourning rites forbade the use of sweet spices

> 📖 **Beleg:** EN [x] 1: 'For it is a sin offering, and not a sweet savour' – KJV 5:11: '...for it is a sin offering.'

> ✏️ **Korrekturvorschlag:** 'For it is a sin offering' (ohne den Zusatz 'and not a sweet savour')

<sub>🔎 Gegenprüfung: Bestätigt. KJV 5:11 endet mit 'for it is a sin offering'. Den Zusatz 'and not a sweet savour' gibt es nicht. Er steht sogar im Gegensatz zu 4:31, wo es heißt 'for a sweet savour unto the LORD'. Da er als Zitat formuliert ist, ist er sachlich irreführend. Korrektur: 'For it is a sin offering'.</sub>

---

#### `lev_142` · Sprachfehler

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Durch die doppelte Verneinung bedeutet die EN-Frage das Gegenteil ('forbidden NOT to marry' = 'verpflichtet zu heiraten'). Damit passt sie nicht mehr zur DE-Frage und zur Lösung.

**Aktuell EN** · _Leviticus 21:7_  
Which woman was a common priest strictly forbidden NOT to marry according to the law?

- ✅ **A whore, or profane, or a woman put away by husband** ← _als richtig markiert_
- ⬜ A maiden born of the daughters of the house of Levi
- ⬜ A widow whose deceased husband was an anointed priest
- ⬜ A young virgin chosen from the twelve tribes of Israel

> 📖 **Beleg:** EN: 'Which woman was a common priest strictly forbidden NOT to marry according to the law?'

> ✏️ **Korrekturvorschlag:** 'Which woman was a common priest strictly forbidden to marry according to the law?'

<sub>🔎 Gegenprüfung: Bestätigt. 'forbidden NOT to marry' ist eine doppelte Verneinung und heißt sinngemäß 'musste heiraten'. Das widerspricht der Lösung und der DE-Frage. 'NOT' streichen.</sub>

---

#### `lev_154` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Die DE-Lösung nennt 'Myrthen'. Myrten kommen in 3. Mose 23:40 nicht vor (sie stehen erst in Neh 8:15); der Text nennt Früchte schöner Bäume, Palmzweige, Zweige dichtbelaubter Bäume und Bachweiden. Ein EN-Distraktor führt Myrte dagegen als falsch auf, damit ist DE/EN widersprüchlich. Außerdem behauptet die DE-Frage, die Zweige seien 'zum Flechten der Laubhütten' verwendet worden. Laut 23:40 nimmt man sie aber, um sich vor dem HERRN zu freuen; EN fragt hier richtig. Rechtschreibung: 'Myrten' statt 'Myrthen'.

**Aktuell DE** · _3. Mose 23:40_  
Welches Holz und welche Zweige wurden zum Flechten der Laubhütten verwendet?

- ✅ **Schönheitsbäume, Palmen, Bachweiden und Myrthen** ← _als richtig markiert_
- ⬜ Nur dicke Aststücke von den stolzen Zedern
- ⬜ Ausschließlich Akazienholz aus der Wüste
- ⬜ Trockenes Stroh und Schilfrohr vom Meere

**Aktuell EN** · _Leviticus 23:40_  
What boughs and branches were Israel commanded to take on the first day to rejoice before the LORD?

- ✅ **Boughs of goodly trees, palm branches, and willows** ← _als richtig markiert_
- ⬜ Branches of cedar wood, olive boughs, and hyssop
- ⬜ Oak leaves, cypress twigs, and fragrant myrtle
- ⬜ Pomegranate boughs, fig tree leaves, and vines

> 📖 **Beleg:** DE [x] 0: 'Schönheitsbäume, Palmen, Bachweiden und Myrthen'; EN Distraktor 2: 'Oak leaves, cypress twigs, and fragrant myrtle'; DE-TEXT: 'Früchte ... von schönen Bäumen, Palmenzweige und Zweige von dichtbelaubten Bäumen und Bachweiden, und sieben Tage lang fröhlich sein'

> ✏️ **Korrekturvorschlag:** DE-Frage: 'Was sollten die Israeliten am ersten Tag des Laubhüttenfestes nehmen, um sich vor dem HERRN zu freuen?' Option 0: 'Früchte schöner Bäume, Palmzweige, Zweige dichtbelaubter Bäume und Bachweiden'

<sub>🔎 Gegenprüfung: Bestätigt. 23:40 nennt keine Myrten. Die Gleichsetzung der 'dichtbelaubten Bäume' mit Myrten ist rabbinische Tradition und kein Bibeltext. Im EN-Paket gilt Myrte als falscher Distraktor, DE und EN widersprechen sich also. 'zum Flechten der Laubhütten' steht so nicht im Vers (Zweck: fröhlich sein vor JHWH). Außerdem steht 'Schönheitsbäume' nicht im Text, und 'Myrthen' ist falsch geschrieben. Die vorgeschlagene Korrektur passt.</sub>

---

### 📄 `04_4_mose.json` (5)

#### `num_026` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die DE-Frage fragt, womit die GERÄTE des Schaubrottischs abgedeckt wurden. Laut Text wurde das blaue Tuch aber unter die Geräte auf den Tisch gebreitet. Über die Geräte kam ein scharlachrotes Tuch und darüber Seehundsfelle (V. 8). Die EN-Frage ('first spread over the table') ist dagegen korrekt.

**Aktuell DE** · _4. Mose 4:7_  
Womit wurden die Geräte des Tischs der Schaubrote beim Transport abgedeckt?

- ⬜ Mit einer Decke aus rotem Widderfell
- ✅ **Mit einem Tuch aus blauem Purpur** ← _als richtig markiert_
- ⬜ Mit einem feinen Leinentuch aus Byssus
- ⬜ Mit einer Decke aus schwarzen Ziegenhaaren

> 📖 **Beleg:** 4. Mose 4:7-8: "über den Schaubrottisch sollen sie ein Tuch von blauem Purpur breiten und darauf setzen die Schüsseln ... Und sie sollen ein Tuch von scharlachroter Karmesinfarbe darüber breiten"

> ✏️ **Korrekturvorschlag:** DE-Frage: "Was wurde beim Aufbruch zuerst über den Schaubrottisch gebreitet?"

<sub>🔎 Gegenprüfung: Bestätigt. Laut 4. Mose 4:7-8 kommt das blaue Tuch unter die Geräte auf den Tisch. Über die Geräte kommen ein scharlachrotes Tuch und Seehundsfelle. Die DE-Frage fragt nach der Abdeckung der Geräte, deshalb ist die markierte Antwort 'blauer Purpur' falsch. EN ('first spread over the table') ist korrekt. Korrektur: "Was wurde beim Aufbruch zuerst über den Schaubrottisch gebreitet?"</sub>

---

#### `num_082` · Sprachfehler

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Hier steht 'Gebot' (Befehl) statt 'Gebet'. Das verändert den Sinn: Mose betet für Mirjam, er erteilt kein Gebot.

**Aktuell DE** · _4. Mose 12:13_  
Welches kurze, ergreifende Gebot rief Mose vor Gott für seine aussätzige Schwester aus?

- ⬜ Vergib ihr diese große Sünde um des Bundes willen
- ✅ **„O Gott, heile sie doch!“ rief Mose zum HERRN** ← _als richtig markiert_
- ⬜ Erlasse ihr die Strafe des Aussatzes am Altar
- ⬜ Lass sie nicht vor den Augen des Volkes sterben

> 📖 **Beleg:** DE: "Welches kurze, ergreifende Gebot rief Mose vor Gott ..."; 4. Mose 12:13: "Mose aber schrie zu JHWH und sprach: Ach Äl, heile sie doch!"

> ✏️ **Korrekturvorschlag:** "Welches kurze, ergreifende Gebet rief Mose zu Gott für seine aussätzige Schwester?"

<sub>🔎 Gegenprüfung: Bestätigt. 'Gebot' ist ein Tippfehler für 'Gebet' und verändert den Sinn. 12:13 ist ein Ausruf an Gott, kein Gebot. EN sagt korrekt 'prayer'. Korrektur: "Welches kurze, ergreifende Gebet rief Mose zu Gott für seine aussätzige Schwester?"</sub>

---

#### `num_085` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die DE-Frage nennt die Antwort schon selbst ('Aus welchem Ort in der Wüste Paran ...'). Die richtige Option lautet 'Aus der Wüste Paran', die Frage ist also ohne Wissen lösbar. Die EN-Frage verrät die Antwort nicht.

**Aktuell DE** · _4. Mose 13:2-3_  
Aus welchem Ort in der Wüste Paran wurden die zwölf Kundschafter zur Auskundschaftung ausgesandt?

- ✅ **Aus der Wüste Paran auf Gottes Befehl hin** ← _als richtig markiert_
- ⬜ Aus der Oase Elim mit ihren Palmenbäumen
- ⬜ Aus dem Lager Tabera nach dem großen Feuer
- ⬜ Aus dem Passahlager am Fuß des Sinai

> 📖 **Beleg:** DE: "Aus welchem Ort in der Wüste Paran wurden die zwölf Kundschafter ... ausgesandt?" / [x] "Aus der Wüste Paran auf Gottes Befehl hin"

> ✏️ **Korrekturvorschlag:** "Von wo aus sandte Mose die zwölf Kundschafter nach Kanaan aus?"

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage nennt 'Wüste Paran' schon, und die richtige Option lautet 'Aus der Wüste Paran'. Die Frage ist also ohne Wissen lösbar. Außerdem ist die Wüste kein 'Ort in der Wüste Paran'. EN verrät die Antwort nicht. Vorgeschlagene Umformulierung passt.</sub>

---

#### `num_146` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Lösung spricht vom „ersten König der Moabiter“. Gemeint ist laut Text aber der frühere bzw. vorige König von Moab (KJV: „the former king of Moab“) und nicht der erste König Moabs überhaupt. Zudem fragt die DE-Frage nach einem „Volk“, die Antwort nennt aber einen König. In EN heißt es richtig „From which ruler“.

**Aktuell DE** · _4. Mose 21:26_  
Welchem Volk hatte Sihon, der König der Amoriter, zuvor das Erdland bis zum Arnon entrissen?

- ⬜ Dem kriegerischen Stamm der Philister im Westen
- ✅ **Dem ersten König der Moabiter im Ostjordanland** ← _als richtig markiert_
- ⬜ Den Edomitern aus den Bergen des Seir-Gebirges
- ⬜ Den Ammonitern aus den nördlichen Grenzzonen

> 📖 **Beleg:** DE 1: „Dem ersten König der Moabiter im Ostjordanland“ / KJV: „who had fought against the former king of Moab“

> ✏️ **Korrekturvorschlag:** Frage: „Welchem Herrscher hatte Sihon … zuvor das Erdland bis zum Arnon entrissen?“; Option 1: „Dem früheren König der Moabiter“

<sub>🔎 Gegenprüfung: Bestätigt. Laut Text („gegen den König der Moabiter“, KJV „former king of Moab“) war es der damalige bzw. vorige König Moabs, nicht der „erste“. Außerdem fragt DE nach einem „Volk“, die Lösung nennt aber einen König, und die Distraktoren nennen Völker. Vorschlag: „Welchem Herrscher …?“ und als Lösung „Dem früheren König der Moabiter“.</sub>

---

#### `num_152` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Die DE-Lösung nennt als Grund für Gottes Zorn, dass Bileams Herz auf den Lohn aus war. Das steht nicht in 4. Mose 22:22 (dort steht nur „darüber, dass er ging“), es ist eine Auslegung nach 2. Petrus 2:15. Die EN-Lösung sagt etwas anderes: „because he went, and the angel of the LORD stood in his way“. DE und EN stimmen also inhaltlich nicht überein, und die DE-Lösung geht über den Bibeltext hinaus.

**Aktuell DE** · _4. Mose 22:22_  
Warum entbrannte der Zorn Gottes, als Bileam am Morgen mit den Fürsten Moabs ritt?

- ⬜ Weil er vergessen hatte, sein Sündopfer zu bringen
- ⬜ Weil er seine Eselin mit einer Peitsche schlug
- ⬜ Weil er ohne Waffen auf dem Weg ritt
- ✅ **Weil er ging und sein Herz auf den Lohn aus war** ← _als richtig markiert_

**Aktuell EN** · _Numbers 22:22_  
Why was God's anger kindled when Balaam rose up in the morning and went with the princes?

- ⬜ Because he forgot to offer his morning sacrifice on the road
- ⬜ Because he smote his ass with an unrighteous heavy whip
- ⬜ Because he journeyed without carrying protective armor
- ✅ **Because he went, and the angel of the LORD stood in his way** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT: „Aber der Zorn Älohims entbrannte darüber, daß er ging.“ / DE 3: „Weil er ging und sein Herz auf den Lohn aus war“ / EN 3: „Because he went, and the angel of the LORD stood in his way“

> ✏️ **Korrekturvorschlag:** DE 3: „Weil er mit den Fürsten Moabs hinging“; EN 3: „Because he went with the princes of Moab“

<sub>🔎 Gegenprüfung: Bestätigt. 4. Mose 22:22 nennt nur „darüber, daß er ging“. „sein Herz auf den Lohn aus war“ ist eine Auslegung (2. Petr 2:15, Jud 11) und steht nicht im Vers. In EN ist „the angel ... stood in his way“ die Folge des Zorns, nicht sein Grund. DE und EN weichen also inhaltlich voneinander ab. Der Korrekturvorschlag („Weil er (mit den Fürsten Moabs) hinging“ / „Because he went“) ist sinnvoll.</sub>

---

### 📄 `05_5_mose.json` (5)

#### `dtn_053` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die Distraktoren 0, 2 und 3 haben verschiedenen Inhalt. DE: ebenes Wüstenland mit Brunnen und Palmen, Handelsland mit Palästen und Goldminen, bewaldetes Bergland voller Weinberge und Zedern. EN: Sanddünen, ebenes Land ohne Berge, isoliertes Land mit Wüstenölen. DE-Option 3 ist zudem teilweise wahr, denn das Land hat laut V. 8 Weinstöcke.

**Aktuell DE** · _5. Mose 8:7-9_  
Wie beschrieb Mose das gute Erdland, in das der HERR sie führen wollte?

- ⬜ Ein ebenes Wüstenland mit tiefen Brunnen und Oasenpalmen
- ✅ **Ein Erdland von Bächen, Quellen, Weizen, Feigen und Erz** ← _als richtig markiert_
- ⬜ Ein Handelsland mit prächtigen Palästen und Goldminen
- ⬜ Ein bewaldetes Bergland voller Weinberge und Zedernholz

**Aktuell EN** · _Deuteronomy 8:7-9_  
How is the good land of Canaan described with respect to its natural resources and wealth?

- ⬜ As a dry land of golden sand dunes and burning desert heat
- ✅ **A land of brooks, wheat, vines, iron, and brass in the hills** ← _als richtig markiert_
- ⬜ As a level country possessing neither mountains nor valleys
- ⬜ As an isolated land yielding only desert oils and dry herbs

> 📖 **Beleg:** DE-Option 3: 'Ein bewaldetes Bergland voller Weinberge und Zedernholz' / EN-Option 3: 'As an isolated land yielding only desert oils and dry herbs'

> ✏️ **Korrekturvorschlag:** Die Distraktoren in beiden Sprachen gleich fassen; in DE-Option 3 die 'Weinberge' durch etwas eindeutig Falsches ersetzen (z. B. 'ein bewaldetes Bergland voller Zedern ohne Ackerland').

<sub>🔎 Gegenprüfung: Bestätigt. Die Distraktoren 0, 2 und 3 unterscheiden sich. Relevanter ist DE-Option 3 ('Bergland voller Weinberge'): V. 7-8 nennen Berge und Weinstöcke, der Distraktor ist also teilweise wahr. Ihn durch etwas eindeutig Falsches ersetzen.</sub>

---

#### `dtn_072` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage fragt, worin sich Kanaan von Ägypten unterschied. Die Antwort 'Mit einem Gemüsegarten, den man mit dem Fuß wässert' beschreibt aber Ägypten und passt grammatisch nicht zur Frage. Die EN-Frage fragt korrekt, womit Ägypten verglichen wird. Die Distraktoren stimmen nicht überein: DE-Option 1 ist eine Oase, EN-Option 1 eine 'barren wilderness'; DE-Optionen 2 und 3 entsprechen EN-Optionen 3 und 2 (vertauscht). Außerdem steht 'dörren' statt 'dürren'.

**Aktuell DE** · _5. Mose 11:10_  
Worin unterschied sich das Erdland Kanaan vom Erdlande Ägypten bei der Bewässerung?

- ✅ **Mit einem Gemüsegarten, den man mit dem Fuß wässert** ← _als richtig markiert_
- ⬜ Mit einer fruchtbaren Oase inmitten von dichten Dattelpalmen
- ⬜ Mit einer dörren Wüste ohne jeglichen Regen im ganzen Jahr
- ⬜ Mit einem felsigen Gebirge ohne Weideplätze für Herden

**Aktuell EN** · _Deuteronomy 11:10_  
To what did Moses compare the land of Egypt in contrast to the promised land?

- ✅ **As a garden of herbs where thou wateredst the seed with thy foot** ← _als richtig markiert_
- ⬜ As a barren wilderness where no green tree can bring forth fruit
- ⬜ As a rocky mountain range where sheep find no green pastures
- ⬜ As a burning sandy plain where rain never descends from heaven

> 📖 **Beleg:** DE-TEXT: 'ist nicht wie das Erdland Mizraim ... das du mit deinem Fuß wässertest wie einen Grüngarten' / DE-Option 2: 'Mit einer dörren Wüste'

> ✏️ **Korrekturvorschlag:** DE-Frage: 'Womit verglich Mose das Erdland Ägypten im Gegensatz zum verheißenen Land?'; Antwort: 'Mit einem Gemüsegarten, den man mit dem Fuß bewässerte'; die Distraktoren an EN angleichen; 'dürren' statt 'dörren'.

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage ('Worin unterschied sich Kanaan…') passt nicht zur Antwort ('Mit einem Gemüsegarten…'), die Ägypten beschreibt. Die Zuordnung der Distraktoren stimmt (DE1 Oase / EN1 barren wilderness; DE2 ≈ EN3; DE3 ≈ EN2). Der Tippfehler 'dörren' statt 'dürren' liegt vor.</sub>

---

#### `dtn_073` · Sprachfehler

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die DE-Frage fragt 'Worauf richten sich die Augen des HERRN', die richtige Antwort gibt aber einen Zeitraum an ('Vom Anfang des Jahres bis zum Ende'). Frage und Antwort passen nicht zusammen, denn nach dieser Frage wäre 'auf das Land' die Antwort. Die EN-Frage fragt korrekt 'How constantly'. Kleinere Abweichung: DE-Option 0 nennt Salböl, EN-Option 0 Räucherwerk (incense).

**Aktuell DE** · _5. Mose 11:12_  
Worauf richten sich die Augen des HERRN im verheißenen Land Kanaan beständig?

- ⬜ Auf das Salböl auf dem Haupt des Hohepriesters im Hof
- ✅ **Vom Anfang des Jahres bis zum Ende des Jahres darauf** ← _als richtig markiert_
- ⬜ Auf die festen Mauern der Städte des Stammes Juda
- ⬜ Ausschließlich während der drei großen Wallfahrtsfeste

> 📖 **Beleg:** DE-TEXT: 'auf welches die Augen des JHWH ... immerdar gerichtet sind, von Anfang bis Ende des Jahres'

> ✏️ **Korrekturvorschlag:** DE-Frage: 'Wie beständig ruhen die Augen des HERRN auf dem verheißenen Land Kanaan?'

<sub>🔎 Gegenprüfung: Bestätigt. 'Worauf richten sich die Augen…' verlangt einen Gegenstand, die Lösung ist aber eine Zeitangabe. Distraktor 3 ist eine Zeitangabe, die Distraktoren 0 und 2 sind Gegenstände; Frage und Optionen sind uneinheitlich. Vorschlag: 'Wie beständig/Wann ruhen die Augen des HERRN auf dem Land?' Die Abweichung Salböl/Räucherwerk ist nebensächlich.</sub>

---

#### `dtn_075` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** EN stellt die umgekehrte Frage. DE fragt nach der Folge des Götzendienstes (Antwort: Der Himmel wird verschlossen), EN nach der Ursache des verschlossenen Himmels (Antwort: anderen Göttern dienen). Alle Distraktoren unterscheiden sich inhaltlich.

**Aktuell DE** · _5. Mose 11:16-17_  
Was drohte dem Volk, wenn es fremden Göttern diente, bezüglich des Erdlandes?

- ⬜ Die Feinde würden alle Weinberge und Fruchtbäume niederbrennen
- ⬜ Fremde Herrscher würden sofort alle Städte und Brunnen besetzen
- ⬜ Eine schwere Plage giftiger Schlangen würde das Lager befallen
- ✅ **Der Himmel verschließt sich und das Erdland gibt keinen Ertrag** ← _als richtig markiert_

**Aktuell EN** · _Deuteronomy 11:16-17_  
What would cause the LORD's wrath to shut up heaven so that there be NO rain?

- ⬜ If the tribal rulers disputed about the borders of the inheritance
- ⬜ If the people neglected to pay the daily tithe unto the Levites
- ⬜ If the armed men refused to cross the Jordan into battle
- ✅ **If your heart be deceived, and ye turn aside and serve other gods** ← _als richtig markiert_

> 📖 **Beleg:** DE: 'Was drohte dem Volk, wenn es fremden Göttern diente' / EN: 'What would cause the LORD's wrath to shut up heaven'

> ✏️ **Korrekturvorschlag:** EN: 'What would befall the land if Israel turned aside and served other gods?'; Antwort: 'He shall shut up the heaven, that there be no rain, and the land yield not her fruit'; die Distraktoren an DE angleichen.

<sub>🔎 Gegenprüfung: Bestätigt. EN fragt umgekehrt nach der Ursache, DE nach der Folge. Beide sind in sich korrekt und textgemäß, aber nicht parallel. Alle Distraktoren unterscheiden sich. Eine Sprache an die andere angleichen.</sub>

---

#### `dtn_136` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach "zwei weiteren Gründen" und nennt als Lösung Weinberg und Verlobte. Der Text 20:6-8 nennt aber drei weitere Gründe; Vers 8 nennt den Furchtsamen. Die EN-Lösung nennt alle drei ("or fainthearted"). DE und EN haben damit eine unterschiedliche Lösung, und die DE-Frage ist sachlich unvollständig.

**Aktuell DE** · _5. Mose 20:6-8_  
Welche zwei weiteren Gründe befreiten einen Mann rechtmäßig vom Kriegsdienst?

- ✅ **Ein neuer Weinberg ohne Ernte und eine Verlobte** ← _als richtig markiert_
- ⬜ Ein hoher Viehbestand oder Altersschwäche
- ⬜ Das Amt des Richters oder der Priesterdienst
- ⬜ Ein fehlendes Pferd oder mangelnder Helm

**Aktuell EN** · _Deuteronomy 20:6-8_  
What additional reasons exempted an Israelite man from going into battle?

- ✅ **Planted a vineyard and not eaten of it, betrothed a wife, or fainthearted** ← _als richtig markiert_
- ⬜ Owning many herds of cattle, or suffering from the feebleness of age
- ⬜ Holding the office of judge, or serving in the active Levitical choir
- ⬜ Lacking a swift chariot horse, or having no helmet of protective brass

> 📖 **Beleg:** DE: "Welche zwei weiteren Gründe…" / [x] "Ein neuer Weinberg ohne Ernte und eine Verlobte"; EN: [x] "Planted a vineyard…, betrothed a wife, or fainthearted"; DE-TEXT v8: "Wer sich fürchtet und ein verzagtes Herz hat…"

> ✏️ **Korrekturvorschlag:** DE-Frage: "Welche weiteren Gründe befreiten einen Mann vom Kriegsdienst?". DE-Lösung: "Ein neuer Weinberg ohne Ernte, eine Verlobte oder ein verzagtes Herz". Alternativ die Stelle auf 5. Mose 20:6-7 einschränken und "or fainthearted" aus EN streichen.

<sub>🔎 Gegenprüfung: Bestätigt. Die angegebene Stelle 20:6-8 nennt in Vers 8 einen dritten Grund, den Furchtsamen. EN nennt alle drei, DE fragt nach 'zwei' Gründen und nennt nur Weinberg und Verlobte. Die Lösungen in DE und EN unterscheiden sich also. Behebung: DE um 'oder ein verzagtes Herz' ergänzen und 'zwei' streichen, oder die Stelle auf 20:6-7 kürzen und EN anpassen.</sub>

---

### 📄 `06_josua.json` (2)

#### `jos_013` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Auch Distraktor 3 (das rote Seil einholen bzw. entfernen) hebt den Schutz auf. Nach 2,18 ist die Zusage an das geknüpfte rote Seil gebunden. Die Frage ist mehrdeutig, solange sie sich nicht ausdrücklich auf V. 19 beschränkt.

**Aktuell DE** · _Josua 2:19_  
Unter welcher Bedingung sollte der Schutz für die Hausgenossen Rahabs NICHT mehr gelten?

- ⬜ Wenn sie vergessen würde, das Schild am Tor aufzuhängen
- ⬜ Wenn ihre Verwandten kein Schutzgeld an die Priester zahlten
- ✅ **Wenn jemand das Haus auf die Straße hinaus verließ** ← _als richtig markiert_
- ⬜ Wenn sie das rote Seil während der Belagerung einholte

**Aktuell EN** · _Joshua 2:19_  
Under what condition would the pledge of protection for Rahab's household NOT apply?

- ⬜ If she failed to set out the sign of peace on the gate
- ⬜ If her brethren refused to pay a ransom of gold coins
- ✅ **If any person went out of the doors of the house into the street** ← _als richtig markiert_
- ⬜ If she took down the scarlet cord during the seven days

> 📖 **Beleg:** 2:18: "wenn wir kommen ins Land und du nicht dies rote Seil in das Fenster knüpfst"

> ✏️ **Korrekturvorschlag:** Distraktor 3 durch eine eindeutig falsche Bedingung ersetzen, z. B. „Wenn sie ihr Haus vor der Eroberung verkauft hätte“ / „If she had sold her house before the city was taken“. Alternativ die Frage präzisieren: „Was galt laut 2,19 für jeden, der das Haus verließ?“

<sub>🔎 Gegenprüfung: Bestätigt. Nach 2,18 ist der Schutz an das geknüpfte rote Seil gebunden, nach 2,20 zusätzlich an das Schweigen. Das Einholen des Seils während der Belagerung würde die Zusage also ebenfalls aufheben, und Distraktor 3 ist vertretbar richtig. Die Frage nennt zwar 2,19, ihr Wortlaut ist aber allgemein. Distraktor ersetzen oder die Frage auf V. 19 präzisieren.</sub>

---

#### `jos_087` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Option 2 hat in DE und EN verschiedenen Inhalt: DE „Die Hälfte aller Erträge der Weinberge“, EN „The tenth part ...“. Die EN-Fassung (Zehnter) ist außerdem biblisch richtig, denn nach 4. Mose 18,21.24 ist der Zehnte das Erbteil der Leviten. Damit ist der englische Distraktor teilweise korrekt.

**Aktuell DE** · _Josua 13:14_  
Was diente dem Stamm Levi stattdessen als sein zugewiesener Anteil im Lande Kanaan?

- ✅ **Die Feueropfer des HERRN sind ihr Erbteil** ← _als richtig markiert_
- ⬜ Die Goldvorräte aus den Beuten der Siege
- ⬜ Die Hälfte aller Erträge der Weinberge
- ⬜ Die Erstlinge aller Beutetiere aus den Kriegszügen

**Aktuell EN** · _Joshua 13:14_  
What served instead as the inheritance of the tribe of Levi among the children of Israel?

- ✅ **The sacrifices of the LORD God made by fire are their inheritance** ← _als richtig markiert_
- ⬜ The treasures of gold and silver taken from all smitten kings
- ⬜ The tenth part of all the fruit of the oliveyards and vineyards
- ⬜ The firstlings of all cattle taken as spoil throughout the war

> 📖 **Beleg:** EN: "The tenth part of all the fruit of the oliveyards and vineyards" vs. DE: "Die Hälfte aller Erträge der Weinberge"

> ✏️ **Korrekturvorschlag:** EN-Option 2 an DE angleichen: "The half of all the increase of the vineyards"

<sub>🔎 Gegenprüfung: Bestätigt. Option 2 sagt in DE „Hälfte der Weinberge“, in EN „Zehnter“, der Inhalt ist also verschieden. Die EN-Fassung ist zudem nach 4. Mose 18,21.24 (der Zehnte als Erbteil der Leviten) vertretbar richtig. Damit gibt es in EN zwei mögliche richtige Antworten. EN an DE angleichen, wie vorgeschlagen.</sub>

---

### 📄 `07_richter.json` (6)

#### `ri_004` · KJV-Wortlaut

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die richtige EN-Option übernimmt den KJV-Wortlaut, ändert aber die Verwandtschaft: Die KJV sagt „father in law“ (Schwiegervater), die Option „brother in law“. Damit gibt sie das deutsche „Schwager“ wieder und nicht den hinterlegten KJV-Text.

**Aktuell EN** · _Judges 1:16_  
Which people went up with the children of Judah out of the city of palm trees?

- ⬜ The Amalekites from the southern desert
- ⬜ The Gibeonites from the cities of league
- ✅ **The children of the Kenite, Moses' brother in law** ← _als richtig markiert_
- ⬜ The Edomites from the mountains of the south

> 📖 **Beleg:** EN [x]: "The children of the Kenite, Moses' brother in law"; KJV: "the children of the Kenite, Moses’ father in law"

> ✏️ **Korrekturvorschlag:** "The children of the Kenite, Moses' father in law"

<sub>🔎 Gegenprüfung: Bestätigt. KJV 1:16 hat „Moses' father in law“, die EN-Option „brother in law“ übernimmt Luthers „Schwager“. Weil die Option ansonsten den KJV-Wortlaut zitiert, ist das eine sachliche Abweichung vom KJV-Text. Korrektur: „father in law“.</sub>

---

#### `ri_054` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN stellt eine andere Frage (Gideons Antwort) als DE (welches Angebot er ablehnte). Die Distraktoren haben einen anderen Inhalt: DE 1 Hohepriesteramt, 2 Hälfte der Ländereien, 3 Palast in Sichem; EN 1 nahm die Krone unter Bedingung an, 2 setzte Jether ein, 3 verwies an die Priester.

**Aktuell DE** · _Richter 8:22-23_  
Welches Angebot der Herrschaft lehnte Gideon nach dem Sieg über Midian standhaft ab?

- ✅ **Die erbliche Königsherrschaft über Israel** ← _als richtig markiert_
- ⬜ Das Amt des Hohepriesters am Stiftszelt
- ⬜ Die Hälfte aller Ländereien im Ostjordanland
- ⬜ Den Bau eines eigenen Palastes in Sichem

**Aktuell EN** · _Judges 8:22-23_  
What answer did Gideon give when the men of Israel said unto him: Rule thou over us, both thou and thy son?

- ✅ **I will not rule over you, neither my son: the LORD shall rule** ← _als richtig markiert_
- ⬜ He accepted the crown upon condition of yearly tribute
- ⬜ He appointed his eldest son Jether to be the prince
- ⬜ He deferred the question unto the priests at Shiloh

> 📖 **Beleg:** DE: "Welches Angebot der Herrschaft lehnte Gideon … ab?" vs. EN: "What answer did Gideon give when the men of Israel said …"

> ✏️ **Korrekturvorschlag:** EN: "What offer of rule did Gideon refuse after the victory over Midian?" 0 [x]: "To rule over Israel, both he, his son, and his son's son", 1: "The office of high priest at the tabernacle", 2: "Half of all the lands beyond Jordan", 3: "A palace of his own built in Shechem".

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach dem abgelehnten Angebot, EN nach Gideons Antwort. Die Lösung entspricht sich ungefähr, die Distraktoren haben aber einen ganz anderen Inhalt. Im Vorschlag sollte die richtige Option knapp bleiben, z. B. „Hereditary rule over Israel, he, his son and his son's son“.</sub>

---

#### `ri_055` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE und EN fragen verschiedene Dinge: DE fragt nach dem Material des Ephods (goldene Stirnbänder), EN nach dem angefertigten Gegenstand (Ephod). Deshalb haben alle Optionen einen anderen Inhalt, DE nennt Materialien, EN Gegenstände.

**Aktuell DE** · _Richter 8:24-27_  
Woraus fertigte Gideon ein Priestergewand (Ephod), das später zum Fall für sein Haus wurde?

- ⬜ Aus edlem Purpurstoff aus den Beuten
- ✅ **Aus den goldenen Stirnbändern der Beute** ← _als richtig markiert_
- ⬜ Aus Silberlingen der Fürsten von Sukkoth
- ⬜ Aus den Rüstungen der geschlagenen Könige

**Aktuell EN** · _Judges 8:24-27_  
What object did Gideon fashion out of the golden earrings of the prey, which became a snare unto his house?

- ⬜ A golden calf after the pattern of the idol at Sinai
- ✅ **Gideon made an ephod thereof, and put it in Ophrah** ← _als richtig markiert_
- ⬜ A golden chariot to ride before the host of Israel
- ⬜ A great altar plated with the beaten gold of Midian

> 📖 **Beleg:** DE: "Woraus fertigte Gideon ein Priestergewand (Ephod) …" [x] "Aus den goldenen Stirnbändern der Beute"; EN: "What object did Gideon fashion out of the golden earrings …" [x] "Gideon made an ephod thereof"

> ✏️ **Korrekturvorschlag:** EN an DE angleichen: "Out of what did Gideon make an ephod which became a snare unto his house?" 0: "Of purple raiment taken from the spoil", 1 [x]: "Of the golden earrings of the prey", 2: "Of pieces of silver from the princes of Succoth", 3: "Of the armour of the slain kings".

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach dem Material (Stirnbänder), EN nach dem Gegenstand (Ephod). Lösung und Distraktoren sind inhaltlich nicht gleichwertig. Der Vorschlag passt zu KJV 8:24-27.</sub>

---

#### `ri_070` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt etwas völlig anderes als DE: DE fragt, wo sich die Ammoniter lagerten (Gilead, Ri 10,17), EN fragt nach dem Kriegsvorwand des Ammoniterkönigs (Arnon bis Jabbok). Das steht in Ri 11,13 und nicht in der angegebenen Stelle Judges 10:17. Auch die Optionen haben einen anderen Inhalt.

**Aktuell DE** · _Richter 10:17_  
An welchem Ort versammelten sich die Söhne Ammons zum Krieg gegen das beunruhigte Israel?

- ✅ **Im Lande Gilead lagerten die Ammoniter** ← _als richtig markiert_
- ⬜ In der Wüste Kadesch an den Grenzen
- ⬜ Vor den Toren der Stadt Jericho im Tal
- ⬜ Auf den Hügeln der Stadt Sichem im Binnenland

**Aktuell EN** · _Judges 10:17_  
What historical plea did the king of the Ammonites falsely claim as his pretext for war?

- ✅ **Because Israel took away my land from Arnon even unto Jabbok** ← _als richtig markiert_
- ⬜ Because Israel had broken the treaty made with king Balak
- ⬜ Because Israel refused to pay tribute for crossing the river
- ⬜ Because Israel had polluted the high sanctuary of Chemosh

> 📖 **Beleg:** DE: "An welchem Ort versammelten sich die Söhne Ammons …" [x] "Im Lande Gilead"; EN: "What historical plea did the king of the Ammonites falsely claim …" [x] "from Arnon even unto Jabbok"; KJV 10:17: "encamped in Gilead"

> ✏️ **Korrekturvorschlag:** EN: "Where did the children of Ammon gather together and encamp against Israel?" 0 [x]: "They encamped in the land of Gilead", 1: "In the wilderness of Kadesh on the borders", 2: "Before the gates of Jericho in the valley", 3: "Upon the hills of Shechem in the inland".

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Frage gibt den Inhalt von Ri 11,13 wieder, nicht von der angegebenen Stelle 10,17, und passt nicht zu DE. Innerhalb von EN ist die Lösung aber biblisch richtig, und „falsely claim“ ist eine Deutung. Deshalb eher mittel als hoch. Vorschlag zur Angleichung übernehmen.</sub>

---

#### `ri_104` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Frage verlegt das Scheren der Locken nach Gaza. Laut Text geschah das im Haus Delilas (im Tal Sorek, 16:4.19). Erst danach wurde Simson nach Gaza hinabgeführt.

**Aktuell EN** · _Judges 16:21_  
What cruelty did the Philistines inflict upon Samson after his locks were shorn at Gaza?

- ⬜ They cut off his right hand and banished him to the desert
- ⬜ They exposed him upon the battlements of Gaza without food
- ✅ **They put out his eyes, bound him with brass, and made him grind** ← _als richtig markiert_
- ⬜ They sold him as an oarsman upon the Phoenician galleys

> 📖 **Beleg:** EN: 'after his locks were shorn at Gaza'; KJV 16:21: 'put out his eyes, and brought him down to Gaza'

> ✏️ **Korrekturvorschlag:** EN: 'What cruelty did the Philistines inflict upon Samson after his locks were shorn by Delilah?'

<sub>🔎 Gegenprüfung: Bestätigt. Nach 16:4.19 schor man die Locken bei Delila im Tal Sorek. Erst nach 16:21 wurde Simson nach Gaza hinabgeführt, die EN-Prämisse 'shorn at Gaza' ist also falsch. Korrektur: 'after his locks were shorn by Delilah'. Zusätzlich: Die DE-Frage nimmt mit 'überwältigt und geblendet' die Lösung ('stachen ihm die Augen aus') vorweg. Besser: 'Was taten die Philister mit Simson, nachdem ihm Delila die Locken hatte abscheren lassen?'</sub>

---

#### `ri_135` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE und EN stellen unterschiedliche Fragen. DE fragt nach der Anzahl der Jungfrauen (Optionen sind Zahlen). EN fragt, WIE die 400 Frauen beschafft wurden, und nennt die Zahl schon in der Frage. Alle Distraktoren unterscheiden sich daher inhaltlich.

**Aktuell DE** · _Richter 21:12_  
Wie viele jungfräuliche Mädchen wurden aus Jabes-Gilead für die überlebenden Benjaminiten gewonnen?

- ⬜ Genau zweihundert Mädchen aus der Stadt
- ✅ **Genau vierhundert junge Jungfrauen** ← _als richtig markiert_
- ⬜ Genau sechshundert Mädchen für alle Männer
- ⬜ Genau achthundert Mädchen aus den Familien

**Aktuell EN** · _Judges 21:12_  
How did the congregation obtain four hundred wives for the surviving men of Benjamin?

- ⬜ They bought captive maidens from the merchants of Midian
- ✅ **They smote Jabesh-gilead and preserved four hundred young virgins** ← _als richtig markiert_
- ⬜ They invited four hundred maidens from the coasts of Moab
- ⬜ They took four hundred handmaids from the Levite suburbs

> 📖 **Beleg:** DE: 'Wie viele jungfräuliche Mädchen wurden aus Jabes-Gilead ... gewonnen?' / EN: 'How did the congregation obtain four hundred wives ...?'

> ✏️ **Korrekturvorschlag:** EN angleichen: 'How many young virgins were found among the inhabitants of Jabesh-gilead for the surviving men of Benjamin?' mit Optionen 'Two hundred' / 'Four hundred young virgins' [x] / 'Six hundred' / 'Eight hundred'.

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach der Zahl (zweihundert/vierhundert/...), EN nach der Art der Beschaffung und nennt die Zahl 400 schon in der Frage. Beide Sprachfassungen sind nicht gleichwertig. Die vorgeschlagene EN-Angleichung an KJV 21:12 ('four hundred young virgins') passt.</sub>

---

### 📄 `08_rut.json` (1)

#### `rut_015` · Sonstiges

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die Erklärung gehört zur vorherigen Frage rut_014 (Epha, Rut 2:17), steht aber bei rut_015 (Boas als nächster Erbe, Rut 2:20). Der Spieler bekommt dadurch eine Erklärung, die nichts mit der Frage zu tun hat. rut_014 hat keine Erklärung.

**Aktuell DE** · _Rut 2:20_  
Welche Bedeutung hatte Boas für die Familie Naemis nach den Worten der Schwiegermutter?

- ⬜ Er war der oberste Richter der Stadt
- ⬜ Er war der Verwalter der Kornhäuser
- ✅ **Der Mann gehört zu unseren nächsten Erben** ← _als richtig markiert_
- ⬜ Er war der Hauptmann des Heeres Judas

**Aktuell EN** · _Ruth 2:20_  
What significance did Boaz have for Naomi's family according to Naomi's words?

- ⬜ He was the chief magistrate sitting in the city gate
- ⬜ He was the royal overseer of the storehouses of Judah
- ✅ **The man is near of kin unto us, one of our next kinsmen** ← _als richtig markiert_
- ⬜ He was the captain of the armed host of Beth-lehem

> 📖 **Beleg:** rut_015 explanation: 'Ein Epha war ein altes biblisches Hohlmaß für Getreide ... (Rut 2:17).' / EN: 'An ephah was an ancient biblical dry measure ...'

> ✏️ **Korrekturvorschlag:** Erklärung (DE und EN) zu rut_014 verschieben. Bei rut_015 eine passende Erklärung setzen oder leer lassen, z. B. 'Als naher Verwandter (Löser/Erbe) hatte Boas das Recht und die Pflicht, das Erbe der Familie Elimelechs einzulösen (Rut 2:20; 3:12).'

<sub>🔎 Gegenprüfung: Bestätigt. Die DE- und EN-Erklärung zu rut_015 behandeln das Epha (Rut 2:17) und gehören damit zu rut_014, das im Paket keine Erklärung hat. Erklärung zu rut_014 verschieben und bei rut_015 eine passende Erklärung zum Löser/Erben setzen oder das Feld leer lassen.</sub>

---

### 📄 `09_1_samuel.json` (1)

#### `1sam_066` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach der Stadt (Lösung: Bethlehem), EN fragt nach der Person (Lösung: Isai/Jesse). Auch die Optionen sind in EN Personen (Ahimelech, Caleb, Abner), in DE Städte. DE und EN fragen also nach Verschiedenem.

**Aktuell DE** · _1. Samuel 16:1_  
In welcher judäischen Stadt sollte Samuel einen der Söhne Isais zum neuen König salben?

- ⬜ In der Priesterstadt Nob nahe den Hügeln
- ⬜ In der Festung Hebron auf dem Gebirge
- ✅ **In der Stadt Bethlehem im Lande Juda** ← _als richtig markiert_
- ⬜ In der Stadt Gibea im Stamme Benjamin

**Aktuell EN** · _1 Samuel 16:1_  
Unto whom in Beth-lehem did the LORD send Samuel to anoint a new king?

- ⬜ Unto Ahimelech the priest in the city of Nob
- ⬜ Unto Caleb the prince in the fortress of Hebron
- ✅ **Unto Jesse the Beth-lehemite, among whose sons was a king** ← _als richtig markiert_
- ⬜ Unto Abner the captain in the city of Gibeah

> 📖 **Beleg:** DE: "In welcher judäischen Stadt sollte Samuel ... salben?" / EN: "Unto whom in Beth-lehem did the LORD send Samuel...?" – [x] "Unto Jesse the Beth-lehemite"

> ✏️ **Korrekturvorschlag:** Entweder EN: "Unto which city of Judah did the LORD send Samuel to anoint one of Jesse's sons?" mit den Optionen Nob / Hebron / Beth-lehem / Gibeah, oder DE: "Zu wem in Bethlehem sandte der HERR Samuel...?" mit Lösung "Zu Isai, dem Bethlehemiter"

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach der Stadt (Bethlehem, Distraktoren sind Städte), EN nach der Person (Jesse, Distraktoren sind Personen). Beide Fassungen sind für sich korrekt, fragen aber nach Verschiedenem. Eine Seite angleichen. Am textnächsten ist die Person ("zu dem Bethlehemiter Isai").</sub>

---

### 📄 `11_1_koenige.json` (2)

#### `1kön_010` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Der Vers nennt neben 'dem Strom' (Euphrat) auch die Grenze Ägyptens als Grenze von Salomos Herrschaft. Der EN-Distraktor 'Unto the border of Egypt' zitiert damit wörtlich eine richtige Aussage des Verses. Die DE-Fassung derselben Option sagt etwas anderes ('Strome Ägyptens' statt 'Grenze Ägyptens'). Außerdem nennt der Vers den Strom als Ausgangspunkt ('von dem Strom an'), nicht als Endpunkt ('bis zum').

**Aktuell DE** · _1. Könige 4:21_  
Bis zu welchem großen Strom reichte der Herrschaftsbereich Salomos?

- ✅ **Bis zum großen Strom Euphrat im Osten** ← _als richtig markiert_
- ⬜ Bis zum Strome Ägyptens im fernen Süden
- ⬜ Bis zum Fluss Jordan in den weiten Tälern
- ⬜ Bis zum Bachtal Kison nahe dem Berge Karmel

**Aktuell EN** · _1 Kings 4:21_  
Unto which great river did the dominion of king Solomon reach?

- ✅ **Unto the great river Euphrates in the east** ← _als richtig markiert_
- ⬜ Unto the border of Egypt in the distant south
- ⬜ Unto the river Jordan in the pleasant valleys
- ⬜ Unto the brook Kishon beside the mount Carmel

> 📖 **Beleg:** KJV: 'from the river unto the land of the Philistines, and unto the border of Egypt' / EN-Option 1: 'Unto the border of Egypt in the distant south' / DE-Option 1: 'Bis zum Strome Ägyptens'

> ✏️ **Korrekturvorschlag:** Option 1 in beiden Sprachen durch einen klar falschen Fluss ersetzen, z. B. 'Bis zum Strom Nil in Ägypten' / 'Unto the river Nile in Egypt'. Die Frage könnte lauten: 'Von welchem großen Strom an erstreckte sich Salomos Herrschaft?'

<sub>🔎 Gegenprüfung: Bestätigt. 'Unto the border of Egypt' ist wörtlich eine Grenze aus dem Vers. Ein EN-Spieler kann diese Option daher als richtig ansehen, auch wenn nach einem 'river' gefragt wird. DE weicht ab ('Strome Ägyptens'). Laut 1 Kön 8:65 ist auch der 'Bach Ägyptens' eine Grenze. Außerdem ist der Strom im Vers der Ausgangspunkt ('von dem Strom an'). Korrektur: Die Frage umformulieren ('Von welchem großen Strom an …?') und Option 1 in beiden Sprachen durch einen eindeutig falschen Fluss ersetzen, der nicht Ägypten heißt, z. B. Nil/Nile oder Tigris.</sub>

---

#### `1kön_012` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Option 3 ist in DE und EN verschieden: DE 'Mandelbaumholz', EN 'Almug trees'. Dazu ist der EN-Distraktor teilweise richtig. Nach 1. Könige 10:11-12 brachten Hirams Schiffe Almugholz aus Ophir, und Salomo machte daraus Pfeiler für das Haus des HERRN. Englische Spieler können die Frage dadurch als mehrdeutig verstehen.

**Aktuell DE** · _1. Könige 5:6-9_  
Welches Bauholz lieferte König Hiram von Tyrus Salomo für das Haus des HERRN?

- ⬜ Eichenholz und Akazienholz aus Basan
- ⬜ Olivenholz und Feigenholz aus den Bergen
- ✅ **Zedernholz und Tannenholz vom Libanon** ← _als richtig markiert_
- ⬜ Mandelbaumholz und Zypressen aus Ophir

**Aktuell EN** · _1 Kings 5:6-9_  
What timber did Hiram king of Tyre furnish unto Solomon for the house of the LORD?

- ⬜ Oak trees and shittim wood from Bashan
- ⬜ Olive trees and fig timber from the hills
- ✅ **Cedar trees and fir trees out of Lebanon** ← _als richtig markiert_
- ⬜ Almug trees and cypress timber from Ophir

> 📖 **Beleg:** EN: 'Almug trees and cypress timber from Ophir' / DE: 'Mandelbaumholz und Zypressen aus Ophir' / KJV 1 Kön 10:11-12: 'brought in from Ophir great plenty of almug trees … made of the almug trees pillars for the house of the LORD'

> ✏️ **Korrekturvorschlag:** EN-Option 3 an DE angleichen und klar falsch machen, z. B. 'Almond wood and cypress from Ophir'

<sub>🔎 Gegenprüfung: Bestätigt. Die Distraktoren unterscheiden sich: DE 'Mandelbaumholz', EN 'Almug trees … from Ophir'. Der EN-Distraktor ist zudem teilweise vertretbar: Nach 1 Kön 10:11-12 brachten Hirams Schiffe Almugholz aus Ophir, und daraus wurden Pfeiler für das Haus des HERRN gemacht. In 2 Chr 2:8 erbittet Salomo von Hiram sogar 'algum trees'. Korrektur: Option 3 in beiden Sprachen angleichen und eindeutig falsch machen, ohne Almug und Ophir, z. B. DE 'Mandelbaumholz und Zypressen aus Ägypten' / EN 'Almond wood and cypress out of Egypt'.</sub>

---

### 📄 `12_2_koenige.json` (2)

#### `2kön_027` · Sprachfehler

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die richtige EN-Antwort ist grammatisch kaputt: 'The shadow brought the shadow' ergibt keinen Sinn. Im KJV ist 'he' (der HERR) das Subjekt.

**Aktuell EN** · _2 Kings 20:8-11_  
What wondrous sign did God give Hezekiah for his healing upon the dial of Ahaz?

- ⬜ The light of the sun was darkened over all Jerusalem
- ⬜ A double rainbow was seen in heaven above the temple
- ✅ **The shadow brought the shadow ten degrees backward** ← _als richtig markiert_
- ⬜ A mighty voice of thunder sounded in the clear noon sky

> 📖 **Beleg:** EN [x] 2: "The shadow brought the shadow ten degrees backward" / KJV 20:11: "and he brought the shadow ten degrees backward"

> ✏️ **Korrekturvorschlag:** "He brought the shadow ten degrees backward on the dial of Ahaz" oder "The shadow went back ten degrees"

<sub>🔎 Gegenprüfung: Bestätigt. EN [x] 2 lautet wörtlich 'The shadow brought the shadow ten degrees backward' und ist damit sinnlos. Laut KJV 20:11 ist der HERR das Subjekt ('he brought the shadow ten degrees backward'). Weil es die richtige Antwort ist, bleibt mittel angemessen. Vorschlag: 'He brought the shadow ten degrees backward on the dial of Ahaz'.</sub>

---

#### `2kön_069` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die als richtig markierte Antwort macht Elisa (Subjekt der Frage) zum Schützen. Laut Text schoss aber König Joas den Pfeil; Elisa befahl nur 'Schieß!' (V.15-16: Elisa legte seine Hände auf die Hände des Königs). Die Antwort schreibt den Schuss also der falschen Person zu.

**Aktuell DE** · _2. Könige 13:17-19_  
Welches prophetische Zeichen gab der sterbende Elisa dem König Joas von Israel?

- ⬜ Er salbte sein Schwert mit heiligem Öl aus dem Tempel
- ⬜ Er ließ ihn einen ehernen Bogen vor den Ältesten spannen
- ⬜ Er teilte einen Pfeil in drei Teile vor seinen Augen
- ✅ **Er schoss den Heilspfeil und ließ ihn die Pfeile auf die Erde schlagen** ← _als richtig markiert_

**Aktuell EN** · _2 Kings 13:17-19_  
What prophetic sign did dying Elisha give unto king Joash of Israel?

- ⬜ He anointed his royal sword with holy oil from the altar
- ⬜ He caused him to draw a bow of brass before all the elders
- ⬜ He brake an arrow in three parts before his face in the chamber
- ✅ **He shot the arrow of deliverance, and bade him smite upon the ground** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT 13:17: "Und Elisa sprach: Schieß! Und er schoß." / KJV: "Then Elisha said, Shoot. And he shot."

> ✏️ **Korrekturvorschlag:** DE: "Er ließ ihn den Heilspfeil schießen und mit den Pfeilen auf die Erde schlagen" / EN: "He bade him shoot the arrow of deliverance, and smite upon the ground"

<sub>🔎 Gegenprüfung: Stimmt. Laut V.17 befiehlt Elisa 'Schieß!' und König Joas schießt. In V.18 schlägt der König auf die Erde. Die als richtig markierte DE-Antwort ('Er schoss den Heilspfeil...') und die EN-Antwort ('He shot the arrow...') schreiben den Schuss mit dem Subjekt der Frage (Elisa) also falsch zu. Vorschlag: DE 'Er ließ ihn den Heilspfeil schießen und mit den Pfeilen auf die Erde schlagen', EN 'He bade him shoot the arrow of deliverance, and smite upon the ground'.</sub>

---

### 📄 `14_2_chronik.json` (2)

#### `2chr_032` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die Frage sagt, Josia sei Necho bei Karchemis entgegengetreten. Karchemis am Euphrat war aber Nechos Ziel. Josia stellte sich ihm laut Text in der Ebene bei Megiddo entgegen.

**Aktuell DE** · _2. Chronik 35:20-22_  
Welche Botschaft sandte Pharao Necho an Josia, als dieser ihm bei Karchemis entgegentrat?

- ⬜ Er wolle ganz Juda erobern und den Tempel niederbrennen
- ✅ **Gott habe ihm geboten zu eilen; Josia solle Gott nicht widerstehen** ← _als richtig markiert_
- ⬜ Er verlange zehntausend Zentner Silber als Tribut des Landes
- ⬜ Er bitte um ein militärisches Bündnis wider den König von Babel

**Aktuell EN** · _2 Chronicles 35:20-22_  
What message sent Pharaoh-necho to Josiah when he went out against him at Carchemish?

- ⬜ He intended to destroy all Judah and burn down temple
- ✅ **God commanded him to make haste; forbear to meddle with God** ← _als richtig markiert_
- ⬜ He demanded ten thousand talents of silver from land
- ⬜ He desired a league with Judah against the king of Babylon

> 📖 **Beleg:** V.20 "zog Necho ... herauf, zu streiten wider Karchemis am Euphrat. Und Josia zog aus, ihm entgegen"; V.22 "kam, mit ihm zu streiten auf der Ebene bei Megiddo"

> ✏️ **Korrekturvorschlag:** DE: "Welche Botschaft sandte Pharao Necho an Josia, als dieser ihm auf dem Zug gegen Karchemis entgegenzog?" / EN: "What message sent Pharaoh-necho to Josiah when he went out against him, as Necho came up to fight against Carchemish?"

<sub>🔎 Gegenprüfung: Bestätigt. Nach V.20 war Karchemis am Euphrat Nechos Kriegsziel. Josia stellte sich ihm laut V.22 in der Ebene bei Megiddo entgegen. „bei Karchemis entgegentrat“ / „at Carchemish“ ist also sachlich falsch. Korrektur wie vorgeschlagen, oder „... als Josia ihm auf dem Zug gegen Karchemis entgegenzog“.</sub>

---

#### `2chr_058` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die Frage fragt nach der Antwort, die Rehabeam dem Volk tatsächlich gab. Der Satz vom kleinen Finger steht aber nur im Rat der Jungen (V. 10). In seiner tatsächlichen Antwort (V. 14) sagt Rehabeam nur: Joch schwerer machen, Peitschen und Skorpione. Die markierte Lösung schreibt Rehabeam also Worte zu, die er laut Text nicht gesagt hat.

**Aktuell DE** · _2. Chronik 10:10-14_  
Welche hochmütige Antwort gab Rehabeam dem Volk auf Anraten der Jungen?

- ⬜ Mein Vater züchtigte mit Ruten; ich lasse euch frei!
- ⬜ Ich erlasse euch alle Dienste für zehntausend Krieger!
- ✅ **Mein kleiner Finger ist dicker als meines Vaters Lenden!** ← _als richtig markiert_
- ⬜ Wer sich mir widersetzt, dessen Sippe wird verbannt!

**Aktuell EN** · _2 Chronicles 10:10-14_  
What haughty answer did Rehoboam give unto the people after the counsel of young men?

- ⬜ My father chastised you with rods; I release you today!
- ⬜ I remit all heavy burdens if ye give me ten thousand men!
- ✅ **My little finger shall be thicker than my father's loins!** ← _als richtig markiert_
- ⬜ Whosoever murmurs against me shall be banished from land!

> 📖 **Beleg:** V.10 (Rat der Jungen): "Mein kleinster Finger soll dicker sein den meines Vaters Lenden"; V.14 (Rehabeams Antwort): "Hat mein Vater euer Joch schwer gemacht, so will ich noch mehr dazu machen: mein Vater hat euch mit Peitschen gezüchtigt, ich aber mit Skorpionen."

> ✏️ **Korrekturvorschlag:** Lösung ändern zu: "Mein Vater hat euch mit Peitschen gezüchtigt, ich aber mit Skorpionen!" / EN: "My father chastised you with whips, but I will chastise you with scorpions!". Alternativ die Frage umformulieren: "Welche Worte rieten die Jungen Rehabeam, dem Volk zu sagen?"

<sub>🔎 Gegenprüfung: Bestätigt. Der Satz vom kleinen Finger steht nur im Rat der Jungen (V.10). In Rehabeams tatsächlicher Antwort (V.14, KJV und Luther gleich) kommt er nicht vor, dort stehen nur das schwerere Joch und Peitschen/Skorpione. Die Frage fragt ausdrücklich, welche Antwort er „gab“. Korrektur: Lösung auf „Mein Vater hat euch mit Peitschen gezüchtigt, ich aber mit Skorpionen!“ / „My father chastised you with whips, but I will chastise you with scorpions!“ ändern. Alternativ die Frage auf den Rat der Jungen umformulieren.</sub>

---

### 📄 `17_esther.json` (1)

#### `est_022` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Lösung sagt, der König habe Mardochai den Siegelring UND Hamans Haus übergeben. Laut Est 8:1-2 gab der König Hamans Haus aber Esther, und Esther setzte Mardochai darüber. Die EN-Lösung nennt nur den Ring, DE und EN sagen also inhaltlich Verschiedenes.

**Aktuell DE** · _Esther 8:2_  
Was übergab König Ahasveros an Mardochai nach dem Tode Hamans?

- ⬜ Die goldene Krone, die zuvor die Königin Vasthi getragen hatte
- ✅ **Seinen Siegelring, den er Haman abgenommen hatte, und Hamans Haus** ← _als richtig markiert_
- ⬜ Ein kaiserliches Heer von zehntausend persischen Reitern zu Ross
- ⬜ Die uneingeschränkte Herrschaft über ganz Babylon und Medien

**Aktuell EN** · _Esther 8:2_  
What did king Ahasuerus bestow upon Mordecai following the execution of Haman?

- ⬜ The crown royal which had aforetime been worn by queen Vashti
- ✅ **The king took off his ring, which he had taken from Haman, and gave it** ← _als richtig markiert_
- ⬜ An imperial garrison of ten thousand horsemen out of the provinces
- ⬜ Absolute rule over the dominions of Babylon, Media, and Syria

> 📖 **Beleg:** DE-TEXT 8:2: "Und der König tat ab von seinem Fingerreif ... und gab ihn Mardochai. Und Esther setzte Mardochai über das Haus Hamans."

> ✏️ **Korrekturvorschlag:** DE-Option 1: "Seinen Siegelring, den er Haman abgenommen hatte" (ohne "und Hamans Haus") oder: "Seinen Siegelring; und Esther setzte ihn über Hamans Haus"; EN entsprechend: "The king took off his ring, which he had taken from Haman, and gave it unto Mordecai".

<sub>🔎 Gegenprüfung: Bestätigt. Laut Est 8:2 gab der König Mardochai nur den Ring, und Esther setzte ihn über Hamans Haus. Das Haus selbst hatte der König in 8:1 Esther gegeben. Die DE-Lösung schreibt dem König also eine Handlung zu, die er nicht vorgenommen hat, und weicht damit inhaltlich von EN ab. Korrektur DE-Option 1: "Seinen Siegelring, den er Haman abgenommen hatte". EN kann bleiben oder auf "... and gave it unto Mordecai" ergänzt werden.</sub>

---

### 📄 `18_hiob.json` (1)

#### `hi_012` · Bibelstelle

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die richtige Antwort verbindet Hiob 16,2 (leidige/miserable Tröster) mit 'unnütze Ärzte / physicians of no value'. Dieser zweite Teil steht aber in Hiob 13,4 und nicht in der angegebenen Stelle 16,2. Außerdem weicht 'mühselige Tröster' vom hinterlegten Luthertext ('leidige Tröster') ab. Inhaltlich ist die Frage fast gleich wie hi_072 (ebenfalls 16,2).

**Aktuell DE** · _Hiob 16:2_  
Wie bezeichnete Hiob seine drei Freunde angesichts ihrer harten Zurechtweisungen?

- ⬜ Als treue Ratgeber und erleuchtete Propheten des HERRN
- ✅ **Als mühselige Tröster und unnütze Ärzte allezumal** ← _als richtig markiert_
- ⬜ Als gerechte Richter über die Verfehlungen seines Hauses
- ⬜ Als barmherzige Hirten auf den öden Bergen der Wüste

**Aktuell EN** · _Job 16:2_  
How did Job describe his three friends in the midst of their continuous rebukes?

- ⬜ As faithful counselors and enlightened prophets of God
- ✅ **As miserable comforters and physicians of no value** ← _als richtig markiert_
- ⬜ As righteous judges over the secret trespass of house
- ⬜ As merciful shepherds upon the mountains of the wilderness

> 📖 **Beleg:** DE-TEXT (Hiob 16:2): 'Ihr seid allzumal leidige Tröster!' / KJV: 'miserable comforters are ye all.' – Option: 'Als mühselige Tröster und unnütze Ärzte allezumal' / 'As miserable comforters and physicians of no value'

> ✏️ **Korrekturvorschlag:** bibleReference auf 'Hiob 13:4; 16:2' (EN: Job 13:4; 16:2) erweitern und DE-Option als 'Als leidige Tröster und unnütze Ärzte allzumal' formulieren. Alternativ den Ärzte-Teil streichen und die Frage zusammen mit hi_072 auf Dubletten prüfen.

<sub>🔎 Gegenprüfung: Trifft zu. 'unnütze Ärzte / physicians of no value' steht in Hiob 13,4 (DE: 'seid alle unnütze Ärzte'; KJV: 'ye are all physicians of no value'), nicht in 16,2. Die Lösung ordnet der angegebenen Stelle also fremden Inhalt zu. Der hinterlegte Luther-1912-Text hat in 16,2 'leidige Tröster', nicht 'mühselige'. Die Frage überschneidet sich stark mit hi_072 (16,2, 'leidige Tröster'). Korrektur: Referenz 'Hiob 13:4; 16:2' / 'Job 13:4; 16:2' und DE 'Als leidige Tröster und unnütze Ärzte allzumal'. Alternativ den Ärzte-Teil streichen und wegen der Dublette mit hi_072 die Frage umformulieren oder ersetzen.</sub>

---

### 📄 `19_psalmen.json` (2)

#### `ps_091` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Der Distraktor "Untadelig" ist ein Synonym der Lösung "Vollkommen" (hebr. tamim). Andere Übersetzungen geben die Stelle mit "untadelig" wieder, die Frage ist daher mehrdeutig. In EN steht an Index 1 inhaltlich etwas anderes ("unsearchable").

**Aktuell DE** · _Psalmen 18:30_  
Wie nennt Psalm 18:30 die Wege Gottes?

- ✅ **Vollkommen** ← _als richtig markiert_
- ⬜ Untadelig
- ⬜ Wunderbar
- ⬜ Verborgen

> 📖 **Beleg:** DE-TEXT: "Gottes Wege sind vollkommen"; EN-Option 1: "As for God, his way is unsearchable"

> ✏️ **Korrekturvorschlag:** DE-Option 1 durch "Unerforschlich" ersetzen (passend zu EN "unsearchable").

<sub>🔎 Gegenprüfung: Zutreffend. 'Untadelig' und 'vollkommen' geben beide hebr. tamim wieder, das Wort wird je nach Übersetzung mal so, mal so übertragen. Als Distraktor ist es daher mehrdeutig. EN-Index 1 heißt 'unsearchable'. DE-Option 1 durch 'Unerforschlich' zu ersetzen, löst das Problem und gleicht DE an EN an.</sub>

---

#### `ps_106` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Der Distraktor "Die Gnade des HERRN" ist fast gleichbedeutend mit der Lösung "Die Güte des HERRN" (hebr. chesed). Viele gängige Übersetzungen (z. B. Schlachter, Elberfelder) haben in Ps 63:4 "deine Gnade ist besser als Leben". Die Frage ist dadurch mehrdeutig.

**Aktuell DE** · _Psalmen 63:3_  
Was ist nach Psalm 63:3 besser als Leben?

- ⬜ Die Treue des HERRN
- ⬜ Die Gnade des HERRN
- ⬜ Die Weisheit des HERRN
- ✅ **Die Güte des HERRN** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT: "Denn deine Güte ist besser denn Leben"; KJV: "thy lovingkindness is better than life"

> ✏️ **Korrekturvorschlag:** Distraktor 1 klar unterscheidbar machen, z. B. "Die Macht des HERRN" oder "Der Ruhm des HERRN".

<sub>🔎 Gegenprüfung: Zutreffend. Gnade und Güte geben beide hebr. chesed wieder. Elberfelder und Schlachter übersetzen Ps 63:4 mit 'deine Gnade ist besser als Leben'. Wer nicht Luther 1912 im Kopf hat, kann Option 1 mit gutem Grund wählen. 'Treue' liegt ebenfalls nah, ist aber eher vertretbar. Distraktor 1 sollte ersetzt werden, z. B. durch 'Die Macht des HERRN' oder 'Die Ehre des HERRN'. EN ist nicht betroffen.</sub>

---

### 📄 `20_sprueche.json` (3)

#### `spr_034` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** In DE ist 'Perlen' die richtige Antwort (Luther), in EN steht 'pearls' aber als falscher Distraktor (Index 3), und richtig sind 'rubies' (KJV). Dieselbe Aussage ist damit je nach Sprache richtig oder falsch. Der DE-Distraktor 'Edelsteinen' liegt außerdem nah an KJV 'rubies'.

**Aktuell DE** · _Sprüche 31:10_  
Wem gleicht nach Sprüche 31:10 eine tugendsame Frau an Wert?

- ⬜ Silber, sie ist viel edler als dieses
- ⬜ Gold, sie ist viel edler als dieses
- ✅ **Perlen, sie ist viel edler als diese** ← _als richtig markiert_
- ⬜ Edelsteinen, sie ist viel edler als diese

**Aktuell EN** · _Proverbs 31:10_  
Above what is the price of a virtuous woman according to Proverbs 31:10?

- ⬜ Above refined silver
- ⬜ Above fine gold of Ophir
- ✅ **Her price is far above rubies** ← _als richtig markiert_
- ⬜ Above all precious pearls

> 📖 **Beleg:** DE [x] 2: 'Perlen, sie ist viel edler als diese' / EN [ ] 3: 'Above all precious pearls' / KJV: 'her price is far above rubies'

> ✏️ **Korrekturvorschlag:** EN-Option 3 ersetzen, z. B. 'Above the treasures of kings'. DE-Option 3 ersetzen, z. B. 'Elfenbein, sie ist viel edler als dieses'.

<sub>🔎 Gegenprüfung: Bestätigt. In DE ist 'Perlen' richtig (Luther), in EN ist 'pearls' ein falscher Distraktor (KJV: rubies). Innerhalb jeder Sprache stimmt die Lösung, über beide Sprachen hinweg widerspricht sich die Frage aber, zumal das hebräische peninim umstritten ist (Perlen, Korallen, Rubine). Auch 'Edelsteinen' liegt nah an 'rubies'. Beide Optionen 3 sollten ersetzt werden.</sub>

---

#### `spr_062` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Der DE-Distraktor 0 'Es macht den Leib gesund' gibt genau den Sinn der KJV-Lösung wieder ('doeth good like a medicine'), ebenso viele deutsche Übersetzungen ('bringt gute Besserung'). Die DE-Lösung (Luther: 'macht das Leben lustig') und die EN-Lösung unterscheiden sich inhaltlich, und in DE wird die EN-Lösung als falsch gewertet.

**Aktuell DE** · _Sprüche 17:22_  
Was bewirkt nach Sprüche 17:22 ein fröhliches Herz?

- ⬜ Es macht den Leib gesund
- ⬜ Es macht die Augen hell
- ✅ **Es macht das Leben lustig** ← _als richtig markiert_
- ⬜ Es macht den Geist stark

**Aktuell EN** · _Proverbs 17:22_  
What doth a merry heart do according to Proverbs 17:22?

- ⬜ It maketh the body strong
- ⬜ It maketh the eyes clear
- ✅ **A merry heart doeth good like a medicine** ← _als richtig markiert_
- ⬜ It maketh the spirit bold

> 📖 **Beleg:** DE [ ] 0: 'Es macht den Leib gesund' / EN [x] 2: 'A merry heart doeth good like a medicine' / KJV: 'A merry heart doeth good like a medicine'

> ✏️ **Korrekturvorschlag:** DE-Option 0 ersetzen, z. B. 'Es macht den Menschen reich'. EN-Option 0 parallel dazu: 'It maketh a man rich'.

<sub>🔎 Gegenprüfung: Bestätigt. DE-Option 0 'macht den Leib gesund' trifft den Sinn von KJV und anderen deutschen Übersetzungen (z. B. 'ist gute Medizin'). Ein kundiger Spieler kann sie als richtig ansehen. EN-Option 0 'maketh the body strong' liegt ebenfalls nah an 'doeth good like a medicine'. Beide Optionen 0 sollten ersetzt werden, z. B. durch 'macht den Menschen reich' bzw. 'It maketh a man rich'.</sub>

---

#### `spr_090` · Sprachfehler

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die DE-Lösung lautet 'Um Armut noch Reichtum ...'. Das ist grammatisch falsch und verkehrt den Sinn: Agur bittet gerade weder um Armut noch um Reichtum.

**Aktuell DE** · _Sprüche 30:7-9_  
Worum bittet Agur den HERRN nach Sprüche 30:8?

- ⬜ Um Reichtum und Ehre, damit er den HERRN verherrliche
- ⬜ Um langes Leben und Weisheit, damit er das Volk führe
- ✅ **Um Armut noch Reichtum, nur um sein bescheiden Teil Speise** ← _als richtig markiert_
- ⬜ Um Sieg über die Feinde und Frieden im Land

> 📖 **Beleg:** DE [x] 2: 'Um Armut noch Reichtum, nur um sein bescheiden Teil Speise' / DE-TEXT: 'Armut und Reichtum gib mir nicht, laß mich aber mein bescheiden Teil Speise dahinnehmen'

> ✏️ **Korrekturvorschlag:** 'Weder um Armut noch um Reichtum, sondern um sein bescheiden Teil Speise'.

<sub>🔎 Gegenprüfung: Bestätigt. 'Um Armut noch Reichtum' ist ungrammatisch (das 'weder' fehlt) und liest sich wie eine Bitte um Armut, verkehrt also den Sinn. Vorschlag: 'Weder um Armut noch um Reichtum, sondern um sein bescheiden Teil Speise'. Inhaltlich vollständiger wäre auch 'Abgötterei und Lüge fern; weder Armut noch Reichtum'.</sub>

---

### 📄 `21_prediger.json` (2)

#### `pred_004` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Distraktor 2 'Dieselbe Schande und dieselbe Vergessenheit' ist zur Hälfte richtig: V. 16 sagt ausdrücklich, dass der Weise ebenso vergessen wird wie der Narr. Das schwächt die Eindeutigkeit der Frage.

**Aktuell DE** · _Prediger 2:14-16_  
Was trifft nach Prediger 2:14-16 den Weisen wie den Toren?

- ✅ **Es geht dem einen wie dem andern: der Tod** ← _als richtig markiert_
- ⬜ Dasselbe hohe Alter und dieselbe Armut im Tod
- ⬜ Dieselbe Schande und dieselbe Vergessenheit
- ⬜ Dieselbe schwere Krankheit und dasselbe Leid

**Aktuell EN** · _Ecclesiastes 2:14-16_  
What happeneth to the wise man even as to the fool in Ecclesiastes 2:14-16?

- ✅ **One event happeneth to them all: they die** ← _als richtig markiert_
- ⬜ The same great age and the same poverty in their death
- ⬜ The same open reproach and the same quick forgetting
- ⬜ The same grievous sickness and the same heavy affliction

> 📖 **Beleg:** DE-TEXT V.16: 'Denn man gedenkt des Weisen nicht immerdar, ebenso wenig wie des Narren, und die künftigen Tage vergessen alles' / EN 2: 'The same open reproach and the same quick forgetting'

> ✏️ **Korrekturvorschlag:** Option 2 ändern, z. B. DE 'Dieselbe Schande und dieselbe Gefangenschaft' und EN 'The same open reproach and the same captivity'.

<sub>🔎 Gegenprüfung: Bestätigt. V.16 sagt ausdrücklich, dass der Weise wie der Narr vergessen wird ('die künftigen Tage vergessen alles' bzw. 'shall all be forgotten'). Die Hälfte von Distraktor 2 stimmt also, in DE und in EN. Die vorgeschlagene Änderung zu 'Gefangenschaft' bzw. 'captivity' ist geeignet.</sub>

---

#### `pred_022` · Mehrere richtig

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Distraktoren 1 (Heuschrecke als Last, V. 5) und 3 (Sonne, Licht, Mond und Sterne verfinstert, V. 2) sind selbst Bilder für das Alter in Prediger 12. Beide stehen innerhalb der angegebenen bibleReference 12:2-5, Option 0 steht in 12:6. Wer die Verszahlen nicht kennt, kann die Frage nicht eindeutig beantworten. Die DE-Distraktoren sind dagegen erfunden, DE und EN unterscheiden sich also.

**Aktuell EN** · _Ecclesiastes 12:2-5_  
How doth Ecclesiastes 12:3 describe old age in figurative language?

- ⬜ The golden bowl is shattered and the cistern wheel is broken in twain
- ⬜ The grasshopper is a heavy burden and all the desire of life faileth
- ✅ **The keepers of the house shall tremble, and the strong men shall bow** ← _als richtig markiert_
- ⬜ The sun, the light, the moon, and the stars are darkened in the heavens

> 📖 **Beleg:** KJV 12:2 'While the sun, or the light, or the moon, or the stars, be not darkened' / 12:5 'the grasshopper shall be a burden, and desire shall fail'

> ✏️ **Korrekturvorschlag:** EN-Distraktoren an DE angleichen: 'The trees wither and the fruit falleth from the bough' / 'The ship sinketh and the sails are rent in the storm' / 'The mountains sink down and the valleys are filled up'.

<sub>🔎 Gegenprüfung: Bestätigt. Die Frage nennt zwar ausdrücklich 12:3, aber die EN-Distraktoren 0 (V.6), 1 (V.5) und 3 (V.2) sind ebenfalls Altersbilder aus Pred 12, und 1 und 3 liegen in der bibleReference 12:2-5. Lösbar ist die Frage nur über die Verszahl. Die DE-Distraktoren sind dagegen erfunden, DE und EN sind also ungleich schwer. Angleichen an DE ist sinnvoll.</sub>

---

### 📄 `23_jesaja.json` (5)

#### `jes_022` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Der DE-Distraktor 2 ('ihr Armen, kommt und kauft Brot ohne Geld') steht inhaltlich fast wörtlich in Jes 55:1 ('die ihr nicht Geld habt, kommet her, kaufet und esset; kauft ohne Geld'). Er ist also eher richtig als falsch. Der EN-Distraktor 2 ('ye wealthy, buy ... with money') ist ein anderer, eindeutig falscher Inhalt. Auch die Optionen 1 und 3 weichen zwischen DE und EN ab.

**Aktuell DE** · _Jesaja 55:1-3_  
Welche Einladung ergeht in Jesaja 55:1?

- ✅ **Auf, ihr Durstigen, kommt her zum Wasser** ← _als richtig markiert_
- ⬜ Wohlan, alle, die ihr hungrig seid, kommt zu meinem Mahl
- ⬜ Auf, ihr Armen, kommt und kauft Brot ohne Geld
- ⬜ Wohlan, alle, die ihr müde seid, kommt zum Berg

**Aktuell EN** · _Isaiah 55:1-3_  
What gracious invitation is proclaimed in Isaiah 55:1?

- ✅ **Ho, every one that thirsteth, come ye to the waters** ← _als richtig markiert_
- ⬜ Come, all ye that hunger, feast at the king's table
- ⬜ Arise, all ye wealthy, buy wine and milk with money
- ⬜ Come, all ye weary, bring your offerings to the altar

> 📖 **Beleg:** DE 2: 'Auf, ihr Armen, kommt und kauft Brot ohne Geld' / DE-TEXT: 'die ihr nicht Geld habt, kommet her, kaufet und esset; kommt her und kauft ohne Geld'

> ✏️ **Korrekturvorschlag:** DE-Option 2: 'Auf, ihr Reichen, kauft Wein und Milch mit Geld' (passend zu EN 2)

<sub>🔎 Gegenprüfung: Bestätigt. 55:1 lautet: 'die ihr nicht Geld habt, kommet her, kaufet ... kauft ohne Geld'. DE 2 ('ihr Armen, kommt und kauft Brot ohne Geld') ist inhaltlich korrekt, nur 'Brot' statt 'Wein und Milch'. EN 2 ('ye wealthy ... with money') ist dagegen falsch. Auch DE 1/3 und EN 1/3 weichen voneinander ab. DE 2 an EN 2 angleichen.</sub>

---

#### `jes_065` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Lösung zitiert nicht Jes 15:5, sondern vermischt sie mit Jes 16:11 (dort brummt bei Luther der 'Bauch' wie eine Harfe). In 15:5 heißt es nur 'Mein Herz schreit über Moab'. Die EN-Lösung ('His heart crieth out') ist dagegen richtig, deshalb weichen DE und EN voneinander ab.

**Aktuell DE** · _Jesaja 15:5_  
Wie reagiert der Prophet selbst auf den Untergang Moabs (Jesaja 15:5)?

- ⬜ Sein Herz freut sich über den Fall Moabs
- ⬜ Sein Herz ruft zu Moab um Umkehr zum HERRN
- ✅ **Sein Herz brummt über Moab wie eine Harfe** ← _als richtig markiert_
- ⬜ Sein Herz verflucht Moab für alle Zeiten

> 📖 **Beleg:** DE-Option: 'Sein Herz brummt über Moab wie eine Harfe' / DE-TEXT 15:5: 'Mein Herz schreit über Moab'

> ✏️ **Korrekturvorschlag:** Option 2: 'Sein Herz schreit über Moab'

<sub>🔎 Gegenprüfung: Bestätigt. In Luther 15:5 steht 'Mein Herz schreit über Moab'. 'Brummt wie eine Harfe' stammt aus 16:11. Die DE-Lösung gibt also den falschen Vers wieder und passt nicht zur EN-Lösung. Korrektur: 'Sein Herz schreit über Moab'.</sub>

---

#### `jes_072` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Kusch ist Äthiopien (Luther: 'Mohrenland'). Deshalb sagt der DE-Distraktor 0 ('Land Äthiopiens im Süden von Ägypten') praktisch dasselbe wie die Lösung ('Land jenseits der Wasser von Kusch'). Der EN-Distraktor 0 nennt dagegen Edom, hat also einen anderen Inhalt.

**Aktuell DE** · _Jesaja 18:1_  
Welchem Land gilt das Wehe in Jesaja 18:1?

- ⬜ Dem Land Äthiopiens im Süden von Ägypten
- ✅ **Dem Land jenseits der Wasser von Kusch** ← _als richtig markiert_
- ⬜ Dem Land der Chaldäer im Osten des Euphrat
- ⬜ Dem Land Tarsis im Westen am Meer

**Aktuell EN** · _Isaiah 18:1_  
Unto which land is the woe pronounced in Isaiah 18:1?

- ⬜ Unto the land of Edom bordering upon the desert
- ✅ **Unto the land beyond the rivers of Ethiopia** ← _als richtig markiert_
- ⬜ Unto the land of Chaldea east of the river Euphrates
- ⬜ Unto the land of Tarshish across the western sea

> 📖 **Beleg:** DE 0: 'Dem Land Äthiopiens im Süden von Ägypten' / DE-TEXT: 'jenseits der Wasser des Mohrenlandes'; EN 0: 'the land of Edom'

> ✏️ **Korrekturvorschlag:** DE-Option 0 an EN angleichen: 'Dem Land Edom am Rand der Wüste'

<sub>🔎 Gegenprüfung: Bestätigt. Luther schreibt 'Mohrenland' (= Kusch/Äthiopien), und Kap. 18 richtet sich nach gängiger Deutung an Kusch selbst. DE-Option 0 ('Land Äthiopiens südlich Ägyptens') ist damit faktisch auch richtig. Im EN steht als Option 0 Edom, was eindeutig falsch ist. DE 0 an EN 0 angleichen (Edom).</sub>

---

#### `jes_112` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Distraktor 3 ('wie ein Brunnen, der den Durstigen tränkt' / 'A living spring of fresh water') entspricht fast genau dem Bild aus 32:2 ('wie die Wasserbäche am dürren Ort' / 'as rivers of water in a dry place'). Das Bild ist also ebenfalls richtig.

**Aktuell DE** · _Jesaja 32:1-2_  
Was verheißt Jesaja 32:1-2 für die Herrschaft des gerechten Königs?

- ⬜ Jeder wird wie ein Schutz vor Feinden sein, ein Schild in der Schlacht
- ⬜ Jeder wird wie eine Burg sein, die Zuflucht vor dem Krieg gibt
- ✅ **Jeder wird wie ein Bergungsort vor Wind und Sturm sein** ← _als richtig markiert_
- ⬜ Jeder wird wie ein Brunnen sein, der den Durstigen tränkt

**Aktuell EN** · _Isaiah 32:1-2_  
What shall a man be under the reign of a righteous king (Isaiah 32:2)?

- ⬜ A buckler against all the arrows of the ungodly heathen
- ⬜ A strong tower of stone giving refuge from armed hosts
- ✅ **As an hiding place from wind, a covert from tempest** ← _als richtig markiert_
- ⬜ A living spring of fresh water in the midst of cities

> 📖 **Beleg:** DE-TEXT 32:2: 'wie die Wasserbäche am dürren Ort'; KJV: 'as rivers of water in a dry place'

> ✏️ **Korrekturvorschlag:** Option 3 ersetzen, z. B. 'Jeder wird wie ein Richter sein, der die Schuldigen straft' / 'A judge that punisheth the guilty'

<sub>🔎 Gegenprüfung: Bestätigt. 32:2 nennt ausdrücklich 'wie die Wasserbäche am dürren Ort' bzw. 'as rivers of water in a dry place'. Das Brunnen- bzw. Quellbild in Option 3 ist darum ebenfalls richtig. Option 3 ersetzen.</sub>

---

#### `jes_148` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Der DE-Distraktor 0 trifft weitgehend zu: Babel hat keinen Thron mehr (v1), muss Mühle drehen, also Magdarbeit tun (v2), und durchs Wasser waten, was auf Verschleppung deutet (v2). Damit ist die Frage mehrdeutig. Der EN-Distraktor 0 ('besieged for seven years and pay heavy tribute') hat einen anderen Inhalt.

**Aktuell DE** · _Jesaja 47:1-3_  
Was kündigt Jesaja 47:1-3 der Tochter Babel an?

- ⬜ Sie wird verbannt, von ihrem Thron gestürzt und muss in der Fremde dienen
- ⬜ Sie wird verschont, aber ihre Kinder werden den Feinden preisgegeben
- ⬜ Sie wird belagert, bleibt aber auf dem Thron und herrscht lange weiter
- ✅ **Sie muss vom Thron in den Staub, soll Mühle drehen und ihre Schande wird aufgedeckt** ← _als richtig markiert_

> 📖 **Beleg:** DE 0: 'Sie wird verbannt, von ihrem Thron gestürzt und muss in der Fremde dienen' / DE-TEXT: 'hat keinen Stuhl mehr ... Nimm die Mühle und mahle Mehl'

> ✏️ **Korrekturvorschlag:** DE-Option 0: 'Sie wird sieben Jahre belagert und muss schweren Tribut zahlen'

<sub>🔎 Gegenprüfung: Weitgehend bestätigt. Laut V.1 hat Babel 'keinen Stuhl mehr' (Thronsturz), die Mühle steht für Magdarbeit, 'wate durchs Wasser' deutet auf Wegführung. DE 0 trifft also großenteils zu. EN 0 (sieben Jahre Belagerung, Tribut) ist dagegen falsch, die Fassungen weichen ab. DE 0 an EN 0 angleichen.</sub>

---

### 📄 `24_jeremia.json` (4)

#### `jer_017` · Mehrere richtig

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN-Option 2 'dry cistern of the watchmen' beschreibt fast die richtige Grube: Sie lag im 'court of the prison' (Wachhof) und hatte kein Wasser. Die Option ist also nahezu richtig. DE-Option 2 lautet ganz anders ('Kerker im Tempel').

**Aktuell EN** · _Jeremiah 38:4-6_  
Whither did the princes cast Jeremiah in Jeremiah 38:6?

- ⬜ Into the prison house of king Zedekiah
- ⬜ Into the pit of lions in royal court
- ⬜ Into the dry cistern of the watchmen
- ✅ **Into the dungeon of Malchiah in mire** ← _als richtig markiert_

> 📖 **Beleg:** KJV 38:6: 'the dungeon of Malchiah … that was in the court of the prison … in the dungeon there was no water, but mire'

> ✏️ **Korrekturvorschlag:** EN-Option 2 an DE angleichen: 'Into a prison chamber within the temple'.

<sub>🔎 Gegenprüfung: Bestätigt. Die Grube Malchias lag 'am Vorhof des Gefängnisses' bzw. 'in the court of the prison' (Wachhof) und hatte kein Wasser. 'The dry cistern of the watchmen' beschreibt also nahezu genau dieselbe Grube. DE 2 ('Kerker im Tempel') ist dagegen klar falsch. EN 2 angleichen: 'Into a prison chamber within the temple'.</sub>

---

#### `jer_048` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Distraktor 2 ist im Kontext weitgehend richtig. Die Götzen sind mit Silber und Gold überzogen (10,4; 'überzogene Säulen' 10,5) und können 'weder helfen noch Schaden tun' (10,5), sind also unnütz und kraftlos. Auch EN-Option 2 ('Overlaid with silver and gold, yet utterly without breath') ist biblisch korrekt (10,4.14).

**Aktuell DE** · _Jeremia 10:5_  
Wie verspottet Jeremia 10:5 die Götzenbilder?

- ✅ **Sie können nicht reden und müssen getragen werden, denn sie können nicht gehen** ← _als richtig markiert_
- ⬜ Sie sind zu klein und können dem Volk nicht helfen und es nicht schützen
- ⬜ Sie sind aus Gold und Silber gemacht, aber sie sind völlig unnütz und kraftlos
- ⬜ Sie haben keinen Namen und werden von niemandem verehrt oder gefürchtet

**Aktuell EN** · _Jeremiah 10:5_  
How doth Jeremiah 10:5 deride the wooden idols?

- ✅ **Upright as palm tree, but speak not: must needs be borne** ← _als richtig markiert_
- ⬜ Too small to defend their worshippers in the day of wrath
- ⬜ Overlaid with silver and gold, yet utterly without breath
- ⬜ Nameless and despised by all the nations of the heathen

> 📖 **Beleg:** DE-TEXT: 'Es sind ja nichts als überzogene Säulen … denn sie können weder helfen noch Schaden tun.'

> ✏️ **Korrekturvorschlag:** Option 2 klar falsch formulieren, z. B. DE 'Sie sind aus Stein gehauen und sprechen zu ihren Priestern' / EN 'Hewn out of stone, and they speak unto their priests'.

<sub>🔎 Gegenprüfung: Bestätigt. 10,4 ('schmückt es mit Silber und Gold') und 10,5 ('können weder helfen noch Schaden tun') machen DE-Option 2 im Kern zutreffend. Nur 'aus Gold und Silber gemacht' ist ungenau, denn sie sind überzogen. EN 2 ('Overlaid with silver and gold, yet utterly without breath') ist durch 10,4 und 10,14 sogar wörtlich belegt. Zwar fragt die Frage eng nach 10,5, trotzdem ist die Option biblisch richtig. Ersetzen.</sub>

---

#### `jer_059` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** 'Die teure Zeit' (Luthers Wort für Teuerung bzw. Hungersnot durch Dürre) und Distraktor 3 'Der große Hunger' meinen praktisch dasselbe. Die Frage ist dadurch mehrdeutig. Auch die übrigen Distraktoren passen nicht zu EN: 0 Pest/war, 2 Schwert/plague, 3 Hunger/tremor.

**Aktuell DE** · _Jeremia 14:1-3_  
Welche Not war der Anlass für Jeremias Gebet in Jeremia 14:1-3?

- ⬜ Eine schwere Pest
- ✅ **Die teure Zeit** ← _als richtig markiert_
- ⬜ Ein hartes Schwert
- ⬜ Der große Hunger

> 📖 **Beleg:** DE-TEXT: 'von der teuren Zeit … finden sie kein Wasser'; KJV: 'concerning the dearth'. DE-Option 3: 'Der große Hunger'

> ✏️ **Korrekturvorschlag:** Distraktoren an EN angleichen: 0 'Ein schwerer Krieg', 1 'Die teure Zeit (Dürre)', 2 'Eine tödliche Pest', 3 'Ein großes Erdbeben'.

<sub>🔎 Gegenprüfung: Bestätigt. 'Teure Zeit' heißt bei Luther Teuerung oder Mangel, KJV sagt 'dearth' (Dürre). 'Der große Hunger' ist davon kaum zu unterscheiden, vor allem weil 'teure Zeit' heute veraltet und unverständlich ist. Echte Mehrdeutigkeit, aber kein Sachfehler, daher eher mittel als hoch. Auch die Abweichung der EN-Distraktoren (war/plague/tremor) stimmt. Vorschlag: DE an EN angleichen (Krieg / Pest / Erdbeben) und die Lösung z. B. 'Die teure Zeit (Dürre)' nennen.</sub>

---

#### `jer_131` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Der DE-Distraktor 1 ist zur Hälfte richtig. Laut 42:16 soll der Hunger, vor dem sie sich fürchten, ihnen in Ägypten nachfolgen. Der Distraktor sagt, der Hunger, vor dem ihr flieht, bleibt. Damit enthält er eine Aussage, die tatsächlich im Vers steht.

**Aktuell DE** · _Jeremia 42:16_  
Was droht der HERR in Jeremia 42:16 denen, die nach Ägypten ziehen?

- ✅ **Das Schwert, vor dem ihr euch fürchtet, wird euch in Ägypten treffen** ← _als richtig markiert_
- ⬜ Eine große Dürre wird euch in Ägypten verzehren, und der Hunger, vor dem ihr flieht, bleibt
- ⬜ Die Sklaverei, aus der ich euch einst befreite, wird euch in Ägypten wieder treffen
- ⬜ Keine Strafe wird euch in Ägypten ereilen, denn dort seid ihr vor dem Schwert sicher

> 📖 **Beleg:** Distraktor: "... und der Hunger, vor dem ihr flieht, bleibt" / DE-TEXT: "und der Hunger, des ihr euch besorgt, soll stets hinter euch her sein in Ägypten"

> ✏️ **Korrekturvorschlag:** Distraktor 1 eindeutig falsch formulieren, z. B. "Eine große Dürre wird Ägypten treffen, doch ihr werdet dort satt werden und sicher wohnen"

<sub>🔎 Gegenprüfung: Trifft zu. 42:16 droht ausdrücklich auch den Hunger an, der ihnen in Ägypten nachfolgt, und den Tod dort ('sollt daselbst sterben'). Distraktor 1 ('Dürre verzehrt euch', 'der Hunger ... bleibt') liegt damit inhaltlich nahe an der Wahrheit und ist für Kenner mindestens zur Hälfte richtig. Die EN-Variante ('plague ... blot out your name') ist unproblematisch. Den DE-Distraktor 1 durch eine eindeutig falsche Aussage ersetzen.</sub>

---

### 📄 `26_hesekiel.json` (1)

#### `hes_045` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Distraktor 2 sagt inhaltlich fast dasselbe wie die richtige Antwort: Es dauert lange, und aus der Weissagung wird nichts. Auch 12:27 ('da ist noch lange hin ... auf die Zeit, die noch ferne ist') stützt ihn. Distraktor 1 enthält ebenfalls 'der Tag des HERRN ist ferne'. Die Frage ist dadurch mehrdeutig.

**Aktuell DE** · _Hesekiel 12:22-28_  
Welches Sprichwort weist der HERR in Hesekiel 12:22 zurück?

- ✅ **Es verzieht sich so lange, es wird nichts aus der Weissagung** ← _als richtig markiert_
- ⬜ Wie die Väter, so die Söhne, der Tag des HERRN ist ferne
- ⬜ Der Tag des HERRN ist fern, und seine Weissagung wird nicht erfüllt
- ⬜ Die Zeit ist erfüllt, und die Weissagung ist wahr geworden

> 📖 **Beleg:** Richtig: 'Es verzieht sich so lange, es wird nichts aus der Weissagung' / Distraktor 2: 'Der Tag des HERRN ist fern, und seine Weissagung wird nicht erfüllt' – DE-TEXT 12:22: 'Weil sich's so lange verzieht, so wird nun hinfort nichts aus der Weissagung'

> ✏️ **Korrekturvorschlag:** Distraktor 2 durch etwas klar anderes ersetzen, zum Beispiel 'Der Tempel des HERRN ist hier, uns kann nichts geschehen'. Distraktor 1 durch 'Die Väter haben Herlinge gegessen, aber den Kindern sind die Zähne stumpf geworden' ersetzen, passend zu EN.

<sub>🔎 Gegenprüfung: Trifft zu. Distraktor 2 ('Der Tag des HERRN ist fern, und seine Weissagung wird nicht erfüllt') umschreibt das Sprichwort aus 12:22 fast bedeutungsgleich und wird zusätzlich von 12:27 gestützt. Distraktor 1 enthält mit 'ferne' teilweise dieselbe Aussage. Die richtige Antwort ist zwar am Wortlaut erkennbar, die Frage bleibt aber mehrdeutig. Severity auf mittel gesenkt, weil Option 0 der Wortlaut ist. Der Vorschlag, die Distraktoren an EN anzugleichen (Herlinge 18:2 / Tempel des HERRN), ist sinnvoll.</sub>

---

### 📄 `28_hosea.json` (1)

#### `hos_035` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Hosea 12:4 erinnert nicht nur an den Kampf mit dem Engel. Es heißt dort auch: 'er hat ihn zu Beth-El gefunden'. Damit sind die Begegnungen in Bethel gemeint (1. Mose 28 mit der Himmelsleiter bzw. 1. Mose 35 mit dem Altar). Die Distraktoren, die von Bethel handeln, sind deshalb streng genommen auch vertretbar.

**Aktuell DE** · _Hosea 12:4-5_  
Woran erinnert Hosea 12:4 im Leben Jakobs?

- ⬜ Er baute einen Altar in Bethel und opferte dort dem HERRN
- ⬜ Er träumte von der Himmelsleiter und erkannte den HERRN
- ⬜ Er kaufte das Erstgeburtsrecht und gewann den Segen
- ✅ **Er kämpfte mit dem Engel und siegte, denn er weinte und bat ihn** ← _als richtig markiert_

**Aktuell EN** · _Hosea 12:4-5_  
What event in Jacob's life is recalled in Hosea 12:4?

- ⬜ He fled from the face of Esau and slept on a stone in Bethel
- ⬜ He served Laban fourteen years for Rachel and kept his sheep
- ⬜ He blessed the two sons of Joseph with his hands crossed over
- ✅ **Yea, he had power over the angel, and prevailed: he wept and prayed** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT 12:4: 'auch hat er ihn ja zu Beth-El gefunden' / KJV: 'he found him in Beth-el' / DE-Distraktoren 0 'Er baute einen Altar in Bethel', 1 'Er träumte von der Himmelsleiter' / EN-Distraktor 0 'slept on a stone in Bethel'

> ✏️ **Korrekturvorschlag:** Die Bethel-Distraktoren ersetzen, z. B. DE 0 'Er diente Laban vierzehn Jahre um Rahel', 1 'Er segnete die Söhne Josefs mit gekreuzten Händen'. Im EN den Distraktor 0 ebenso ersetzen, z. B. 'He bought the birthright of Esau for pottage'.

<sub>🔎 Gegenprüfung: Bestätigt. Hosea 12:4 sagt ausdrücklich 'auch hat er ihn ja zu Beth-El gefunden' bzw. 'he found him in Beth-el' und spielt damit auf 1. Mose 28 bzw. 35 an. DE-Distraktor 1 (Himmelsleiter, den HERRN erkannt) und DE 0 (Altar in Bethel, 1. Mose 35:7) sind deshalb vertretbar, ebenso EN 0 (slept on a stone in Bethel). Die Lösung bleibt die beste Antwort, weil sie wörtlich zitiert ist. Trotzdem ist die Frage mehrdeutig, die Bethel-Distraktoren sollten ersetzt werden. EN 1 und 2 (Laban, Josefs Söhne) sind bereits unproblematisch.</sub>

---

### 📄 `29_joel.json` (1)

#### `joe_001` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Die richtige Antwort gibt die Abfolge in Joel 1:4 falsch wieder. Die Heuschrecken fressen nur, was die Raupen (palmerworm) übrig lassen. Die Käfer (cankerworm) fressen erst nach den Heuschrecken und lassen ihnen also nichts übrig.

**Aktuell DE** · _Joel 1:4-7_  
Welches Unglück schildert Joel 1:4 als Bild für das kommende Gericht?

- ⬜ Eine Dürre, die alle Quellen versiegen lässt und das Land verbrennt
- ✅ **Eine Heuschreckenplage, die alles abfrisst, was Raupen und Käfer übrig ließen** ← _als richtig markiert_
- ⬜ Ein Erdbeben, das die Stadt zerstört und die Mauern einstürzen lässt
- ⬜ Eine Seuche, die Vieh und Menschen trifft und das Land entvölkert

**Aktuell EN** · _Joel 1:4-7_  
What devastation does Joel 1:4 portray as a figure of the coming judgment?

- ⬜ A grievous drought that dried up the rivers and burned the pleasant pastures
- ✅ **A plague of locusts that devoureth what the palmerworm and cankerworm left** ← _als richtig markiert_
- ⬜ A mighty earthquake that cast down all the fortified walls of the cities
- ⬜ A deadly pestilence that smote man and beast and left the land desolate

> 📖 **Beleg:** DE-TEXT: 'Was die Raupen lassen, das fressen die Heuschrecken; und was die Heuschrecken lassen, das fressen die Käfer' / DE-Option: 'die alles abfrisst, was Raupen und Käfer übrig ließen' / EN-Option: 'devoureth what the palmerworm and cankerworm left'

> ✏️ **Korrekturvorschlag:** DE: 'Eine Insektenplage: Was die Raupen lassen, fressen die Heuschrecken, was diese lassen, die Käfer und das Geschmeiß' / EN: 'A plague of insects: what the palmerworm left the locust ate, then the cankerworm and the caterpiller'

<sub>🔎 Gegenprüfung: Bestätigt. Laut Joel 1:4 (DE und KJV) fressen die Heuschrecken nur, was die Raupen (palmerworm) lassen, und die Käfer (cankerworm) fressen erst danach. 'was Raupen und Käfer übrig ließen' bzw. 'what the palmerworm and cankerworm left' ist also sachlich falsch. Korrektur z. B. DE: 'Eine Insektenplage: Was die Raupen lassen, fressen die Heuschrecken, den Rest Käfer und Geschmeiß'.</sub>

---

### 📄 `33_micha.json` (1)

#### `mi_018` · Sprachfehler

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** In der EN-Lösung steht 'statues of Omri' (Standbilder) statt 'statutes of Omri' (Satzungen). Damit ändert sich der Sinn: Aus den Satzungen Omris werden Götzenbilder, und die Lösung passt nicht mehr zu KJV und DE ('die Weise Omris').

**Aktuell EN** · _Micah 6:10-16_  
What sins are condemned by the LORD in Micah 6:10-16?

- ⬜ Heathen altars upon the mountains and idolatrous groves in the land
- ⬜ Neglect of the holy altar and profaning the appointed feast days
- ✅ **Treasures of wickedness, the scant measure, and keeping statues of Omri** ← _als richtig markiert_
- ⬜ Perverting judgment by false witness and taking gifts of bribery

> 📖 **Beleg:** EN: 'keeping statues of Omri' / KJV 6:16: 'For the statutes of Omri are kept'

> ✏️ **Korrekturvorschlag:** Treasures of wickedness, the scant measure, and keeping the statutes of Omri

<sub>🔎 Gegenprüfung: Bestätigt. EN-Lösung lautet 'keeping statues of Omri', KJV 6:16 hat 'the statutes of Omri are kept'. Der Tippfehler ändert den Sinn (Bilder statt Satzungen). Korrektur: 'Treasures of wickedness, the scant measure, and keeping the statutes of Omri'.</sub>

---

### 📄 `35_habakuk.json` (1)

#### `hab_015` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Distraktor 1 ('Weh ihm, denn was mit Gold und Silber überzogen ist, bietet keinen Schutz') ist inhaltlich ebenfalls richtig. Er beginnt mit dem richtigen 'Weh', und dass der Götze nicht hilft, sagt der unmittelbare Kontext ausdrücklich (2:18 'Was wird dann helfen das Bild'; 2:19 'Wie sollte es lehren?'). Er unterscheidet sich von der Lösung also nur im Wortlaut.

**Aktuell DE** · _Habakuk 2:19_  
Was sagt Habakuk 2:19 über den, der zum Holz spricht: Wache auf!?

- ⬜ Wohl ihm, denn was mit Gold und Silber überzogen ist, erhört sein Flehen
- ⬜ Weh ihm, denn was mit Gold und Silber überzogen ist, bietet keinen Schutz
- ✅ **Weh ihm, denn es ist mit Gold und Silber überzogen und ist kein Odem in ihm** ← _als richtig markiert_
- ⬜ Wohl ihm, denn was mit Gold und Silber überzogen ist, zeigt Gottes Nähe

**Aktuell EN** · _Habakkuk 2:19_  
What is said in Habakkuk 2:19 of him that saith to the wood, Awake?

- ⬜ Blessed is he, for that which is laid over with gold heareth his cry
- ⬜ Woe unto him, for that which is laid over with gold cannot deliver him
- ✅ **Woe unto him, for it is laid over with gold and there is no breath in it** ← _als richtig markiert_
- ⬜ Blessed is he, for that which is laid over with gold showeth God's presence

> 📖 **Beleg:** Hab 2:18 'Was wird dann helfen das Bild...' / 2:19 'Weh dem, der zum Holz spricht: Wache auf! ... Wie sollte es lehren?'

> ✏️ **Korrekturvorschlag:** Distraktor 1 eindeutig falsch machen, z. B. 'Wohl ihm, denn was mit Gold und Silber überzogen ist, bringt ihm Reichtum' / EN 'Blessed is he, for that which is laid over with gold bringeth him riches'

<sub>🔎 Gegenprüfung: Bestätigt. Distraktor 1 ('Weh ihm … bietet keinen Schutz' / 'Woe unto him … cannot deliver him') beginnt wie der Vers mit dem richtigen 'Weh'. Auch der Inhalt ist sachlich wahr: 2:18 fragt 'Was wird dann helfen das Bild', 2:19 'Wie sollte es lehren?'. Er steht zwar nicht wörtlich in 2:19, ist aber nicht eindeutig falsch. Distraktor auf 'Wohl ihm …' oder eine klar falsche Aussage umstellen.</sub>

---

### 📄 `36_zephanja.json` (3)

#### `zef_003` · KJV-Wortlaut

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Lösung kürzt das KJV-Zitat zu 'The LORD will not do evil'. Damit wird aus der gleichgültigen Aussage 'er tut weder Gutes noch Böses' eine fromme, inhaltlich richtige Aussage. Der Sinn kippt, und die Lösung weicht von DE ('weder Gutes noch Böses') ab.

**Aktuell EN** · _Zephaniah 1:12_  
Against whom is the search of Jerusalem with candles directed in Zephaniah 1:12?

- ⬜ Against the merchants at the gate that deal deceitfully and oppress the needy
- ⬜ Against the thieves in the night that break into houses and spoil the wealthy
- ⬜ Against the false priests that prophesy peace and sacrifice unto strange gods
- ✅ **Against them that are settled on their lees, that say: The LORD will not do evil** ← _als richtig markiert_

> 📖 **Beleg:** EN: 'that say: The LORD will not do evil' / KJV: 'The LORD will not do good, neither will he do evil.'

> ✏️ **Korrekturvorschlag:** Against them that are settled on their lees, that say: The LORD will not do good, neither will he do evil

<sub>🔎 Gegenprüfung: Bestätigt. KJV 1:12 lautet 'The LORD will not do good, neither will he do evil'. Die verkürzte EN-Lösung 'The LORD will not do evil' macht aus der gleichgültigen, gerügten Haltung eine fromme Aussage und weicht von DE ab. Die vorgeschlagene Korrektur ist richtig.</sub>

---

#### `zef_009` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt allgemein nach der Zusage ('ist bei dir, ein starker Heiland; er freut sich über dich'). EN fragt dagegen, wie sich der HERR über Zion freuen wird ('rejoice over her with joy, rest in love, and joy with singing'). Auch alle Distraktoren haben andere Inhalte (DE 0 'sendet dir einen Heiland … in der Ferne' vs. EN 0 'rule over her with an iron sceptre').

**Aktuell DE** · _Zephanja 3:17_  
Welche Zusage gibt Zephanja 3:17?

- ⬜ Der HERR sendet dir einen Heiland und wird in der Ferne bei dir sein
- ✅ **Der HERR, dein Gott, ist bei dir, ein starker Heiland; er freut sich über dich** ← _als richtig markiert_
- ⬜ Der HERR richtet dich noch einmal und freut sich an deinem Untergang
- ⬜ Der HERR vergisst dich nicht, sondern ruft dich in sein Haus zurück

**Aktuell EN** · _Zephaniah 3:17_  
How will the LORD rejoice over Zion according to Zephaniah 3:17?

- ⬜ He will rule over her with an iron sceptre and judge her with fury
- ✅ **He will rejoice over her with joy, rest in love, and joy with singing** ← _als richtig markiert_
- ⬜ He will build her strong walls and defend her against all adversaries
- ⬜ He will bring many nations to enrich her with all earthly treasures

> 📖 **Beleg:** DE: 'Welche Zusage gibt Zephanja 3:17?' / EN: 'How will the LORD rejoice over Zion according to Zephaniah 3:17?'

> ✏️ **Korrekturvorschlag:** EN: 'What promise is given in Zephaniah 3:17?' mit Lösung 'The LORD thy God in the midst of thee is mighty; he will save, he will rejoice over thee' und Distraktoren, die DE 0/2/3 entsprechen

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt allgemein nach der Zusage, EN fragt, wie sich der HERR über Zion freut. Alle Distraktoren sind inhaltlich verschieden. Beide Lösungen sind textgetreu, die Fassungen aber nicht parallel. EN an DE angleichen (oder umgekehrt), Lösung etwa 'The LORD thy God in the midst of thee is mighty; he will save, he will rejoice over thee'.</sub>

---

#### `zef_011` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE und EN stellen unterschiedliche Fragen mit unterschiedlichen Optionen. DE fragt, was der HERR zubereitet hat (Lösung: 'Ein Schlachtopfer, zu dem er seine Gäste geladen hat'). EN fragt, warum alle vor dem Herrn still sein sollen (Lösung: 'Because the day of the LORD is at hand and he hath prepared a sacrifice'). Die Distraktoren haben ganz andere Inhalte (DE 0 'Ein Brandopfer…' vs. EN 0 'Because the holy temple is filled…').

**Aktuell DE** · _Zephanja 1:7_  
Was hat der HERR nach Zephanja 1:7 zubereitet?

- ⬜ Ein Brandopfer, das er allein auf dem Altar verzehren will
- ⬜ Ein Gastmahl der Versöhnung, zu dem er alle Völker ruft
- ✅ **Ein Schlachtopfer, zu dem er seine Gäste geladen hat** ← _als richtig markiert_
- ⬜ Ein Festmahl, zu dem er die Armen des Landes geladen hat

**Aktuell EN** · _Zephaniah 1:7_  
Why should all hold their peace before the Lord GOD in Zephaniah 1:7?

- ⬜ Because the holy temple is filled with his glorious brightness and power
- ⬜ Because the judgment against the heathen hath already been accomplished
- ✅ **Because the day of the LORD is at hand and he hath prepared a sacrifice** ← _als richtig markiert_
- ⬜ Because his mighty angels keep watch upon the high walls of Jerusalem

> 📖 **Beleg:** DE: 'Was hat der HERR nach Zephanja 1:7 zubereitet?' / EN: 'Why should all hold their peace before the Lord GOD in Zephaniah 1:7?'

> ✏️ **Korrekturvorschlag:** EN an DE angleichen: 'What hath the LORD prepared according to Zephaniah 1:7?' mit 0 'A burnt offering which he alone will consume upon the altar', 1 'A feast of reconciliation unto which he calleth all nations', 2 'A sacrifice, and he hath bid his guests', 3 'A banquet unto which he hath bidden the poor of the land'

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt 'Was hat der HERR zubereitet?', EN fragt 'Why should all hold their peace…?'. Auch die Distraktoren sind inhaltlich verschieden. Beide Lösungen sind für sich korrekt, aber die Sprachfassungen sind nicht parallel. Die vorgeschlagene EN-Angleichung passt; Lösung nach KJV 'A sacrifice, and he hath bid his guests'.</sub>

---

### 📄 `38_sacharja.json` (1)

#### `sach_013` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE und EN stellen verschiedene Fragen. DE fragt nach der Größe des fliegenden Briefes (V. 2), EN fragt, was die Rolle bedeutet (V. 3). Alle Optionen haben in DE und EN einen völlig anderen Inhalt.

**Aktuell DE** · _Sacharja 5:1-4_  
Wie groß ist der fliegende Brief nach Sacharja 5:2?

- ⬜ Zehn Ellen lang und fünf Ellen breit
- ✅ **Zwanzig Ellen lang und zehn Ellen breit** ← _als richtig markiert_
- ⬜ Dreißig Ellen lang und zwanzig Ellen breit
- ⬜ Zwölf Ellen lang und sechs Ellen breit

**Aktuell EN** · _Zechariah 5:1-4_  
What does the flying roll represent in Zechariah 5:3?

- ⬜ The everlasting covenant of God with the righteous
- ✅ **The curse that goeth forth against thieves and swearers** ← _als richtig markiert_
- ⬜ The message of peace unto all the scattered nations
- ⬜ The solemn book of remembrance written before the Lord

> 📖 **Beleg:** DE: 'Wie groß ist der fliegende Brief nach Sacharja 5:2?' / EN: 'What does the flying roll represent in Zechariah 5:3?'

> ✏️ **Korrekturvorschlag:** Beide Fassungen angleichen, z. B. EN: 'How large was the flying roll according to Zechariah 5:2?' mit 'Twenty cubits long and ten cubits broad' als Lösung und den DE-Distraktoren entsprechenden Maßen.

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach den Maßen (V. 2, Lösung 20×10 Ellen), EN nach der Bedeutung (V. 3, Lösung 'curse … against thieves and swearers'). Beide Fassungen sind für sich korrekt, stellen aber völlig verschiedene Fragen. Eine Fassung an die andere angleichen.</sub>

---

### 📄 `39_maleachi.json` (1)

#### `mal_009` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE und EN stellen verschiedene Fragen. DE fragt nach der Verheißung für den vollen Zehnten (V. 10), EN fragt, worin das Volk Gott beraubt hat (V. 8). Lösungen und Distraktoren haben einen anderen Inhalt.

**Aktuell DE** · _Maleachi 3:8-10_  
Was verheißt der HERR denen, die den Zehnten ganz bringen (Maleachi 3:10)?

- ⬜ Er will die Feinde schlagen und dem Volk Sieg über alle Völker geben
- ✅ **Er will des Himmels Fenster auftun und Segen die Fülle herabschütten** ← _als richtig markiert_
- ⬜ Er will lange Leben geben und die Jahre der Frommen mehren
- ⬜ Er will Sünden vergeben und die Schuld von seinem Volk nehmen

**Aktuell EN** · _Malachi 3:8-10_  
Wherein had the people robbed God according to Malachi 3:8?

- ⬜ In their neglect of the daily morning and evening prayer in the temple
- ✅ **In tithes and offerings; they should bring all into the storehouse** ← _als richtig markiert_
- ⬜ In their refusal to fast and mourn in the fifth and seventh months
- ⬜ In selling the holy vessels of the sanctuary unto foreign merchants

> 📖 **Beleg:** DE: 'Was verheißt der HERR denen, die den Zehnten ganz bringen (Maleachi 3:10)?' / EN: 'Wherein had the people robbed God according to Malachi 3:8?'

> ✏️ **Korrekturvorschlag:** EN angleichen: 'What does the LORD promise them that bring all the tithes into the storehouse (Malachi 3:10)?' – Lösung: 'He will open the windows of heaven and pour out a blessing'.

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt nach der Verheißung in V. 10 (Himmelsfenster, Segen), EN danach, worin das Volk Gott beraubt hat (V. 8, 'tithes and offerings'). Beide Fassungen sind für sich korrekt, aber inhaltlich verschiedene Fragen. Angleichen.</sub>

---

### 📄 `40_matthaeus.json` (5)

#### `mt_039` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** EN-Distraktor 2 ist ein wörtliches KJV-Zitat des Hilferufs der Jünger aus der Parallelstelle Markus 4:38. Der DE-Distraktor 2 ist sinngemäß dieselbe Stelle. Da die DE-Frage Matthäus nicht ausdrücklich nennt, wirkt die Option für bibelkundige Spieler ebenfalls richtig.

**Aktuell DE** · _Matthäus 8:23-27_  
Mit welchem Rufen weckten die verängstigten Jünger Jesus im Seesturm?

- ⬜ Meister, wach auf und steuere das Schiff!
- ⬜ Herr, gebiete den Winden und den Wellen!
- ⬜ Lehrer, siehst du nicht, wie wir leiden!
- ✅ **Herr, rette uns, wir gehen zugrunde!** ← _als richtig markiert_

**Aktuell EN** · _Matthew 8:23-27_  
With what cry did the fearful disciples awake Jesus during the great tempest?

- ⬜ Master, awake and guide the ship through the storm!
- ⬜ Lord, rebuke the wind and the raging billows!
- ⬜ Master, carest thou not that we perish in the sea?
- ✅ **Lord, save us: we perish!** ← _als richtig markiert_

> 📖 **Beleg:** EN-Option 2: 'Master, carest thou not that we perish in the sea?' (vgl. Mk 4:38 KJV: 'Master, carest thou not that we perish?')

> ✏️ **Korrekturvorschlag:** Option 2 ersetzen, z. B. DE 'Herr, lass uns ans Ufer fahren!' / EN 'Lord, bring us unto the shore!'; zusätzlich in der DE-Frage 'nach Matthäus 8:25' ergänzen.

<sub>🔎 Gegenprüfung: Teilweise bestätigt. EN-Option 2 'Master, carest thou not that we perish…' ist fast wörtlich Mk 4:38 KJV, also der Hilferuf derselben Begebenheit. Bibelkundige Spieler können ihn deshalb für richtig halten, auch wenn die Stellenangabe Mt 8 nennt. DE-Option 2 ('Lehrer, siehst du nicht, wie wir leiden!') ist nur entfernt an Mk 4:38 angelehnt und weniger problematisch. Vorrangig den EN-Distraktor ersetzen.</sub>

---

#### `mt_045` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Frage ist zirkulär: Sie nimmt die Lösung vorweg ('when He took … by the hand') und fragt dann, was Jesus tat. Die Lösung lautet wieder 'He took her by the hand'. DE fragt dagegen offen, was Jesus tat, um das Mädchen aufzuerwecken. Außerdem haben die Distraktoren in DE und EN einen anderen Inhalt (DE 0 gesegnetes Wasser / EN 0 wept aloud usw.).

**Aktuell DE** · _Matthäus 9:23-25_  
Was tat Jesus, um die verstorbene Tochter des Vorstehers wieder zu wecken?

- ⬜ Er gab ihr gesegnetes Wasser zu trinken, und das Mädchen stand auf
- ✅ **Er nahm sie bei der Hand, und das Mädchen stand auf** ← _als richtig markiert_
- ⬜ Er betete drei Stunden an ihrem Bett, und das Mädchen stand auf
- ⬜ Er rief den Namen des Herrn über ihr aus, und das Mädchen stand auf

**Aktuell EN** · _Matthew 9:23-25_  
What did Jesus do when He took the ruler's dead daughter by the hand?

- ⬜ He wept aloud and the maid arose
- ✅ **He took her by the hand, and the maid arose** ← _als richtig markiert_
- ⬜ He called the priests to offer prayer
- ⬜ He commanded her to wash in the pool

> 📖 **Beleg:** EN: 'What did Jesus do when He took the ruler's dead daughter by the hand?' – Lösung: 'He took her by the hand, and the maid arose'

> ✏️ **Korrekturvorschlag:** EN: 'What did Jesus do to raise the ruler's dead daughter?' und die EN-Distraktoren an DE angleichen.

<sub>🔎 Gegenprüfung: Bestätigt. Die EN-Frage nimmt die Lösung vorweg ('when He took … by the hand') und ist dadurch zirkulär bzw. trivial. Auch die Distraktoren weichen von DE ab. EN-Frage neu formulieren: 'What did Jesus do to raise the ruler's daughter?'. Dazu die Distraktoren angleichen.</sub>

---

#### `mt_083` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Der Distraktor 0 (DE "nicht nüchtern geblieben", EN "had not fasted for three days") berührt V. 21 ("diese Art fährt nicht aus außer durch Gebet und Fasten"), der im hinterlegten Text steht. "Nüchtern" kann im Deutschen auch "fastend" bedeuten. Ein Spieler kann diese Option daher begründet für (mit)richtig halten.

**Aktuell DE** · _Matthäus 17:14-21_  
Warum konnten die Jünger den mondsüchtigen Knaben nicht heilen?

- ⬜ Weil sie nicht nüchtern geblieben waren
- ⬜ Weil der Vater zu wenig gebetet hatte
- ⬜ Weil die Schriftgelehrten spotteten
- ✅ **Weil sie zu wenig Glauben hatten** ← _als richtig markiert_

**Aktuell EN** · _Matthew 17:14-21_  
Why could the disciples not cast out the devil from the lunatic child?

- ⬜ Because they had not fasted for three days
- ⬜ Because the father of the child lacked prayer
- ⬜ Because the scribes stood mocking in the way
- ✅ **Because of your unbelief** ← _als richtig markiert_

> 📖 **Beleg:** DE-TEXT 17:21 "Aber diese Art fährt nicht aus, außer durch Gebet und Fasten."; DE [ ] 0: "Weil sie nicht nüchtern geblieben waren"

> ✏️ **Korrekturvorschlag:** Distraktor 0 ersetzen durch eine Option ohne Bezug zum Fasten, z. B. DE "Weil der Knabe zu jung war" / EN "Because the child was too young".

<sub>🔎 Gegenprüfung: Für EN bestätigt. V. 21 (im hinterlegten Text) nennt 'prayer and fasting', deshalb wirkt 'had not fasted' teilweise richtig. Daran ändert auch das erfundene 'three days' wenig. DE 'nicht nüchtern' bedeutet heute eher 'nicht nüchtern = betrunken' und ist weniger kritisch, bleibt aber mehrdeutig. Korrektur: Distraktor 0 in beiden Sprachen ohne Bezug zum Fasten formulieren.</sub>

---

#### `mt_129` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Der DE-Distraktor 2 "Lass diesen Kelch ohne Leiden vergehen" liegt sehr nahe an Jesu tatsächlichem Gebet (V. 39: "so gehe dieser Kelch an mir vorüber"). Er ist deshalb kaum eindeutig falsch. Die EN-Option 2 hat zudem einen ganz anderen Inhalt ("Let me return straightway unto the glory of the Father").

**Aktuell DE** · _Matthäus 26:36-44_  
Was betete Jesus im Seelenkampf in Gethsemane?

- ⬜ Sende Engel zum Schutz vor den Feinden
- ✅ **Nicht wie ich will, sondern wie du willst** ← _als richtig markiert_
- ⬜ Lass diesen Kelch ohne Leiden vergehen
- ⬜ Nimm mich sogleich zu dir in den Himmel

**Aktuell EN** · _Matthew 26:36-44_  
What did Jesus pray during His agony in the garden of Gethsemane?

- ⬜ Send legions of angels to defend me from all my foes
- ✅ **Nevertheless not as I will, but as thou wilt** ← _als richtig markiert_
- ⬜ Let me return straightway unto the glory of the Father
- ⬜ Take away the power of darkness from the earth at once

> 📖 **Beleg:** DE-TEXT 26:39 "Ist es möglich, so gehe dieser Kelch an mir vorüber; doch nicht, wie ich, sondern wie du willst!"; DE [ ] 2: "Lass diesen Kelch ohne Leiden vergehen"

> ✏️ **Korrekturvorschlag:** DE-Option 2 ersetzen durch einen klar falschen Satz, passend zu EN: "Lass mich sogleich zur Herrlichkeit des Vaters zurückkehren".

<sub>🔎 Gegenprüfung: Weitgehend bestätigt. 'Lass diesen Kelch ohne Leiden vergehen' paraphrasiert fast V. 39 ('so gehe dieser Kelch an mir vorüber') und ist daher nicht eindeutig falsch. EN-Option 2 ist dagegen unproblematisch. Korrektur: Nur DE-Option 2 durch einen klar falschen Satz ersetzen, z. B. 'Lass mich sogleich zur Herrlichkeit des Vaters zurückkehren'.</sub>

---

#### `mt_138` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** DE fragt allgemein nach dem "Ruf", den Jesus an die Frauen richtete. Jesus sagte aber laut V. 10 auch "Geht hin", deshalb ist der Distraktor "Gehet hin!" ebenfalls zutreffend. EN fragt eindeutiger nach dem Gruß ("salutation"). Außerdem sind die Optionen 0 und 3 zwischen DE und EN vertauscht: DE 0 "Fürchtet euch!" steht gegen EN 0 "Peace be unto you!", DE 3 "Friede sei!" gegen EN 3 "Fear not the rulers!".

**Aktuell DE** · _Matthäus 28:9-10_  
Welchen Ruf richtete der auferstandene Jesus an die Frauen auf dem Wege?

- ⬜ Fürchtet euch!
- ⬜ Gehet hin!
- ✅ **Freuet euch!** ← _als richtig markiert_
- ⬜ Friede sei!

**Aktuell EN** · _Matthew 28:9-10_  
With what salutation did the risen Jesus meet the women as they went to tell the disciples?

- ⬜ Peace be unto you!
- ⬜ Go into Galilee!
- ✅ **All hail!** ← _als richtig markiert_
- ⬜ Fear not the rulers!

> 📖 **Beleg:** DE-TEXT 28:10 "Fürchtet euch nicht! Geht hin, verkündiget meinen Brüdern"; DE [ ] 1: "Gehet hin!"

> ✏️ **Korrekturvorschlag:** DE-Frage präzisieren: "Mit welchem Gruß begegnete der auferstandene Jesus den Frauen auf dem Weg?". Den Distraktor "Gehet hin!" durch "Seid getrost!" ersetzen und die Optionen 0/3 in DE und EN gleich ordnen (z. B. 0 = "Friede sei mit euch!" / "Peace be unto you!").

<sub>🔎 Gegenprüfung: Für DE bestätigt. Jesus sagt in V. 10 tatsächlich 'Geht hin', deshalb ist 'Gehet hin!' bei der Frage nach dem 'Ruf' mitrichtig. EN fragt eindeutig nach der 'salutation' und ist in Ordnung. Dass die Distraktoren in DE und EN verschieden angeordnet sind, ist dagegen kein Fehler. Korrektur: DE-Frage auf den Gruß einschränken oder 'Gehet hin!' durch einen anderen Distraktor ersetzen.</sub>

---

### 📄 `41_markus.json` (2)

#### `mk_014` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die DE-Lösung ist eine Deutung ('bewusstes Verwerfen des Wirkens des Geistes'), die EN-Lösung gibt den Text wieder ('Because they said, He hath an unclean spirit'). Auch alle Distraktoren sind inhaltlich verschieden: DE 0 Gesetz Mose aufheben vs. EN Hände waschen, DE 1 Tempel entweihen vs. EN Passahopfer, DE 3 Bann der Schriftgelehrten vs. EN Beschneidungsbund.

**Aktuell DE** · _Markus 3:28-30_  
Warum hat die Lästerung gegen den Heiligen Geist keine Vergebung (Markus 3:28-30)?

- ⬜ Weil sie das Gesetz Moses aufhebt und die Gebote der Väter missachtet
- ⬜ Weil sie den Tempel entweiht und das Heiligtum Gottes beschmutzt
- ✅ **Weil sie ein bewusstes Verwerfen des Wirkens des Geistes Gottes ist** ← _als richtig markiert_
- ⬜ Weil die Schriftgelehrten sie nicht vergeben wollen und den Bann verhängen

**Aktuell EN** · _Mark 3:28-30_  
Why hath blasphemy against the Holy Ghost no forgiveness in Mark 3:29-30?

- ⬜ Because they refused to wash their hands before eating bread
- ⬜ Because they neglected the sacrifices of the feast of Passover
- ✅ **Because they said, He hath an unclean spirit** ← _als richtig markiert_
- ⬜ Because they brake the holy covenant of circumcision

> 📖 **Beleg:** DE [x] 2: 'Weil sie ein bewusstes Verwerfen des Wirkens des Geistes Gottes ist' / EN [x] 2: 'Because they said, He hath an unclean spirit'

> ✏️ **Korrekturvorschlag:** DE-Lösung textnah formulieren: 'Weil sie sagten: Er hat einen unreinen Geist' (oder EN an DE angleichen) und die Distraktoren in beiden Sprachen gleich gestalten

<sub>🔎 Gegenprüfung: Bestätigt. V.30 nennt den Grund ausdrücklich ('Denn sie sagten: Er hat einen unreinen Geist'). Die DE-Lösung ist eine theologische Deutung, die so nicht im Text steht, und weicht inhaltlich von der EN-Lösung ab. Alle Distraktoren unterscheiden sich ebenfalls. DE-Lösung textnah formulieren und die Distraktoren angleichen.</sub>

---

#### `mk_021` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Distraktor 3 'Auf den hohen Bergen' ist laut V. 5 ebenfalls richtig: Der Besessene war Nacht und Tag in den Gräbern und auf den Bergen. Vor allem das DE-Wort 'Aufenthalt' macht die Frage mehrdeutig.

**Aktuell DE** · _Markus 5:1-5_  
Wo hatte der Besessene im Gebiet der Gerasener seinen Aufenthalt?

- ⬜ In einer Felsenhöhle
- ✅ **In den Totengräbern** ← _als richtig markiert_
- ⬜ Im tiefen Waldgebüsch
- ⬜ Auf den hohen Bergen

**Aktuell EN** · _Mark 5:1-5_  
Where did the man with the unclean spirit dwell in the country of the Gadarenes?

- ⬜ In a rocky cavern
- ✅ **Among the tombs** ← _als richtig markiert_
- ⬜ In the deep forest
- ⬜ Upon the mountains

> 📖 **Beleg:** V.5: 'Und er war allezeit, Nacht und Tag, in den Gräbern und auf den Bergen' / KJV: 'he was in the mountains, and in the tombs'

> ✏️ **Korrekturvorschlag:** Frage auf V. 3 zuspitzen: 'Wo hatte der Besessene seine Wohnung?' / 'Where had the man his dwelling?' und Distraktor 3 ersetzen, z. B. 'In einem verlassenen Dorf' / 'In a deserted village'

<sub>🔎 Gegenprüfung: Bestätigt. V.5 (DE und KJV) nennt Gräber UND Berge als Aufenthalt, deshalb ist 'Auf den hohen Bergen' / 'Upon the mountains' ebenfalls textgedeckt. Das DE-Wort 'Aufenthalt' verschärft das; EN 'dwell' passt eher zu V.3 ('had his dwelling among the tombs'), ist aber auch nicht eindeutig. Korrektur: nach der Wohnung fragen (V.3) und Distraktor 3 ersetzen.</sub>

---

### 📄 `42_lukas.json` (3)

#### `lk_061` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach EINEM Unglück in Jerusalem (Lösung: Turm in Siloah). EN fragt nach ZWEI Unglücken (Turm UND die Galiläer, deren Blut Pilatus vermischte). Frage, Lösung und alle Distraktoren unterscheiden sich inhaltlich.

**Aktuell DE** · _Lukas 13:1-5_  
Welches Unglück in Jerusalem führte Jesus an, um zur Buße zu rufen?

- ⬜ Die Zerstörung der Tempelmauern
- ✅ **Der Einsturz des Turms in Siloah** ← _als richtig markiert_
- ⬜ Die Dürre in ganz Judäa
- ⬜ Die Seuche unter den Herden

**Aktuell EN** · _Luke 13:1-5_  
Which two calamities did Jesus mention as warnings unto all except they repent?

- ⬜ The famine in Samaria and the pestilence in the valley of Jordan
- ✅ **The fall of the tower in Siloam and the Galileans whose blood Pilate mingled** ← _als richtig markiert_
- ⬜ The burning of the temple gates and the earthquake in the wilderness
- ⬜ The destruction of Sodom and the drowning of Pharaoh's host in the sea

> 📖 **Beleg:** DE: 'Welches Unglück in Jerusalem …' / EN: 'Which two calamities did Jesus mention …' – [x] 'The fall of the tower in Siloam and the Galileans whose blood Pilate mingled'

> ✏️ **Korrekturvorschlag:** Beide Fassungen angleichen, z. B. DE 'Welche zwei Unglücke führte Jesus an, um zur Buße zu rufen?' – [x] 'Den Einsturz des Turms in Siloah und die Galiläer, deren Blut Pilatus mit ihren Opfern vermischte', die DE-Distraktoren an EN anpassen.

<sub>🔎 Gegenprüfung: Der Befund stimmt. DE fragt nach einem Unglück (Lösung: Turm in Siloah), EN nach zwei Unglücken (Turm und die Galiläer). Frage, Lösung und Distraktoren unterscheiden sich inhaltlich. Jede Fassung ist für sich korrekt, die beiden Sprachen prüfen aber verschiedenes Wissen. Sie sollten angeglichen werden.</sub>

---

#### `lk_098` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Der Denar war eine römische Silbermünze. Der Distraktor 'Eine silberne Münze' bzw. 'A piece of silver money' ist deshalb sachlich ebenfalls richtig, und die Frage wird mehrdeutig. Außerdem verschiedene Distraktoren bei Index 3: DE 'Drei Silberlinge', EN 'Thirty pieces of silver'.

**Aktuell DE** · _Lukas 20:20-26_  
Welche Münze ließ Sich Jesus zeigen bei der Fangfrage nach der Steuer?

- ⬜ Einen goldenen Schekel
- ⬜ Eine silberne Münze
- ✅ **Einen römischen Denar** ← _als richtig markiert_
- ⬜ Drei Silberlinge

**Aktuell EN** · _Luke 20:20-26_  
What coin did Jesus ask them to shew Him when they sought to entangle Him in talk?

- ⬜ A gold shekel of the temple
- ⬜ A piece of silver money
- ✅ **A Roman tribute penny** ← _als richtig markiert_
- ⬜ Thirty pieces of silver

> 📖 **Beleg:** DE-TEXT V.24: 'Zeigt mir einen Denar!'; KJV: 'Shew me a penny.'

> ✏️ **Korrekturvorschlag:** Option 1 ersetzen, z. B. 'Eine Kupfermünze (Lepton)' / 'A brass mite'. Index 3 angleichen, z. B. DE 'Dreißig Silberlinge'.

<sub>🔎 Gegenprüfung: Der Befund stimmt. Der Denar war eine Silbermünze, deshalb ist 'Eine silberne Münze' bzw. 'A piece of silver money' sachlich ebenfalls richtig. Option 1 sollte durch eine eindeutig falsche Münze ersetzt werden (z. B. Lepton/mite). Dass Index 3 abweicht (DE 'Drei Silberlinge', EN 'Thirty pieces of silver'), ist nur ein Nebenpunkt.</sub>

---

#### `lk_125` · Bibelstelle

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die Ordering-Frage zur ganzen Weihnachtsgeschichte verweist nur auf Lukas 1:38 (Marias Antwort an den Engel). Die Geburt und die Hirten stehen in Lukas 2, die Weisen und die Flucht nach Ägypten nur in Matthäus 2. Die Stelle deckt den abgefragten Inhalt also nicht ab. Die Reihenfolge selbst (correctAnswers [4,3,1,2,0]) stimmt.

**Aktuell DE** · _Lukas 1:38_  
Bringe diese Ereignisse der Weihnachtsgeschichte in die richtige Reihenfolge.

1. Josef flieht mit Maria und dem Kind nach Ägypten
2. Die Hirten finden das Kind in der Krippe
3. Die Weisen aus dem Morgenland beten das Kind an
4. Jesus wird zu Bethlehem in einer Krippe geboren
5. Der Engel kündigt Maria die Geburt des Heilands an

**Aktuell EN** · _Luke 1:38_  
Put these events of the nativity story in the correct chronological order.

1. Joseph fleeth with Mary and the young child into Egypt
2. The shepherds find the babe lying in a manger
3. The wise men from the east fall down and worship him
4. Jesus is born in Bethlehem and laid in a manger
5. The angel Gabriel announces the holy birth unto Mary

> 📖 **Beleg:** bibleReference 'Lukas 1:38' / DE-TEXT: 'Maria aber sprach: Siehe, ich bin die Magd des Herrn!'; Optionen: 'Josef flieht ... nach Ägypten', 'Die Weisen aus dem Morgenland beten das Kind an'

> ✏️ **Korrekturvorschlag:** bibleReference z. B. auf 'Lukas 1:26-2:20; Matthäus 2:1-15' (EN: 'Luke 1:26-2:20; Matthew 2:1-15') erweitern oder die Matthäus-Ereignisse durch Lukas-Ereignisse ersetzen (z. B. 'Jesus wird im Tempel dargestellt', Lk 2:22).

<sub>🔎 Gegenprüfung: Bestätigt. Die Stelle Lk 1:38 deckt nur die Ankündigung ab. Geburt und Hirten stehen in Lk 2:1-20, die Weisen und die Flucht nach Ägypten in Mt 2:1-15. correctAnswers [4,3,1,2,0] ist in DE und EN korrekt. Vorschlag: 'Lukas 1:26-2:20; Matthäus 2:1-15' bzw. 'Luke 1:26-2:20; Matthew 2:1-15'.</sub>

---

### 📄 `43_johannes.json` (1)

#### `joh_031` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt, warum die Brüder nicht an Jesus glaubten. Darauf gibt der Text keinen Grund an, und die Lösung ist zirkulär und auslegend ('rein menschlich dachten'). EN fragt etwas anderes: warum die Brüder ihn drängten, nach Judäa zu gehen. Die EN-Lösung zitiert V. 5 als Begründung.

**Aktuell DE** · _Johannes 7:3-5_  
Warum glaubten die leiblichen Brüder Jesu zunächst nicht an Ihn?

- ⬜ Weil sie das Gesetz verwarfen und die Gebote des Mose nicht achteten
- ⬜ Weil sie den Tempel mieden und in Nazareth bleiben wollten
- ⬜ Weil sie die Römer fürchteten und keine Unruhe im Haus wollten
- ✅ **Weil sie rein menschlich dachten und nicht an ihn glaubten** ← _als richtig markiert_

**Aktuell EN** · _John 7:3-5_  
Why did Jesus' brethren urge him to go into Judaea to show his works?

- ⬜ Because they rejected the law and kept not the commandments of Moses
- ⬜ Because they refrained from the temple and desired to stay in Nazareth
- ⬜ Because they feared the Romans and sought no disturbance in the city
- ✅ **Because neither did his brethren believe in him at that season** ← _als richtig markiert_

> 📖 **Beleg:** DE: 'Warum glaubten die leiblichen Brüder Jesu zunächst nicht an Ihn?' – 'Weil sie rein menschlich dachten und nicht an ihn glaubten' / EN: 'Why did Jesus' brethren urge him to go into Judaea to show his works?' / Text V.5: 'Denn auch seine Brüder glaubten nicht an ihn.'

> ✏️ **Korrekturvorschlag:** DE an EN angleichen: 'Welche Begründung gibt Johannes 7:5 dafür, dass Jesu Brüder ihn drängten, nach Judäa zu ziehen?' – Lösung: 'Denn auch seine Brüder glaubten nicht an ihn.'

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage fragt nach einem Grund, den der Text nicht nennt. Die Lösung ist zirkulär ('... und nicht an ihn glaubten') und auslegend. EN fragt etwas anderes, und dort passt V. 5 als 'For'-Begründung. Zusätzlich ergänzt die EN-Lösung 'at that season', das im KJV V. 5 nicht steht. Beide Sprachen angleichen.</sub>

---

### 📄 `44_apostelgeschichte.json` (13)

#### `apg_012` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Machtwort an den Lahmen, DE danach, was Petrus nicht besaß (Silber und Gold). Die EN-Lösung ist richtig, die Frage aber eine andere.

**Aktuell DE** · _Apostelgeschichte 3:6_  
Was besaß Petrus nach eigenen Worten nicht, als der Gelähmte ihn um Almosen bat?

- ✅ **Silber und Gold** ← _als richtig markiert_
- ⬜ Brot und Fisch
- ⬜ Mantel und Schuhe
- ⬜ Haus und Acker

**Aktuell EN** · _Acts 3:6_  
What word of power did Peter speak unto the lame man at the Beautiful gate?

- ✅ **In the name of Jesus Christ of Nazareth rise up and walk** ← _als richtig markiert_
- ⬜ Be made whole by the prayer of the twelve holy apostles
- ⬜ Wash in the pool of Siloam seven times and be cleansed
- ⬜ Receive thy sight and walk in the presence of all men

> 📖 **Beleg:** DE: 'Was besaß Petrus ... nicht' / EN: 'What word of power did Peter speak'

> ✏️ **Korrekturvorschlag:** EN: 'What did Peter say he had none of when the lame man asked alms?' – [x] 'Silver and gold', dazu passende Distraktoren.

<sub>🔎 Gegenprüfung: Bestätigt: Die EN-Frage weicht von DE ab. Die EN-Lösung ist nach KJV 3:6 richtig, daher bleibt es bei mittel.</sub>

---

#### `apg_016` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Zahl der Gläubigen (Apg 4:4), DE nach dem Grund der Festnahme (Auferstehungspredigt). Die Stelle 4:1-3 enthält die EN-Antwort nicht.

**Aktuell DE** · _Apostelgeschichte 4:1-3_  
Welcher Glaubensinhalt der Apostel veranlasste die Priester zur Festnahme?

- ✅ **Die Verkündigung der Auferstehung der Toten in Jesus** ← _als richtig markiert_
- ⬜ Die Verweigerung der Steuern, die der Kaiser von den Juden forderte
- ⬜ Der Abbruch des Heiligtums, den sie im Namen Jesu angekündigt hatten
- ⬜ Der Verkauf von Feldern, dessen Erlös sie dem Tempel vorenthielten

**Aktuell EN** · _Acts 4:1-3_  
How many in number were the men that believed the word preached by Peter?

- ✅ **About five thousand** ← _als richtig markiert_
- ⬜ About three thousand
- ⬜ About seven thousand
- ⬜ About twelve thousand

> 📖 **Beleg:** DE: 'Welcher Glaubensinhalt ... Festnahme?' / EN: 'How many in number were the men that believed'

> ✏️ **Korrekturvorschlag:** EN: 'What preaching of the apostles grieved the priests and Sadducees so that they laid hands on them?' – [x] 'They preached through Jesus the resurrection from the dead'.

<sub>🔎 Gegenprüfung: Die Abweichung trifft zu: EN fragt nach 4:4, die Stelle ist 4:1-3. Die EN-Lösung 'About five thousand' ist für 4:4 aber inhaltlich richtig. Deshalb auf mittel herabgestuft. Angleichung an DE wie vorgeschlagen.</sub>

---

#### `apg_020` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Erschütterung des Gebetsorts (Apg 4:31), DE nach der Bedeutung von 'Barnabas' (4:36). Die EN-Frage passt nicht zur Stelle 4:36-37.

**Aktuell DE** · _Apostelgeschichte 4:36-37_  
Was bedeutet der Beiname Barnabas, den die Apostel dem Leviten Josef gaben?

- ✅ **Sohn des Trostes** ← _als richtig markiert_
- ⬜ Sohn der Stärke
- ⬜ Mann des Friedens
- ⬜ Mann Gottes

**Aktuell EN** · _Acts 4:36-37_  
What happened to the place where the believers prayed after the apostles were let go?

- ✅ **The place was shaken where they were assembled together** ← _als richtig markiert_
- ⬜ A pillar of fire appeared above the roof of the chamber
- ⬜ A great company of angels descended upon the company
- ⬜ The doors of the chamber were opened by a mighty rushing wind

> 📖 **Beleg:** DE: 'Was bedeutet der Beiname Barnabas' / EN: 'What happened to the place where the believers prayed'

> ✏️ **Korrekturvorschlag:** EN: 'What is the name Barnabas, being interpreted?' – [x] 'The son of consolation'.

<sub>🔎 Gegenprüfung: Die Abweichung trifft zu: EN fragt nach 4:31, die Stelle ist 4:36-37. Die EN-Lösung 'The place was shaken' ist für 4:31 aber richtig. Auf mittel herabgestuft, Angleichung an DE ('The son of consolation').</sub>

---

#### `apg_021` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Joses/Barnabas (Apg 4:36-37), DE nach Hananias und Saphira (5:1-3).

**Aktuell DE** · _Apostelgeschichte 5:1-3_  
Welches Ehepaar belog den Heiligen Geist beim Verkauf ihres Ackerlandes?

- ⬜ Aquila und Priszilla
- ✅ **Hananias und Saphira** ← _als richtig markiert_
- ⬜ Zacharias und Elisabeth
- ⬜ Felix und Drusilla

**Aktuell EN** · _Acts 5:1-3_  
What Levite of Cyprus sold land and laid the money at the apostles' feet?

- ⬜ Stephen the deacon
- ✅ **Joses, surnamed Barnabas** ← _als richtig markiert_
- ⬜ Philip the evangelist
- ⬜ Mnason of the island

> 📖 **Beleg:** DE: 'Welches Ehepaar belog den Heiligen Geist' / EN: 'What Levite of Cyprus sold land'

> ✏️ **Korrekturvorschlag:** EN: 'Which husband and wife lied unto the Holy Ghost about the price of the land?' – [x] 'Ananias and Sapphira'.

<sub>🔎 Gegenprüfung: Die Abweichung trifft zu: EN behandelt 4:36-37, die Stelle ist 5:1-3. Die EN-Lösung Joses/Barnabas ist für 4:36-37 aber richtig. Auf mittel herabgestuft, Angleichung an DE (Ananias and Sapphira).</sub>

---

#### `apg_029` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Stephanus' Angesicht (Apg 6:15), DE nach dem Vorwurf der falschen Zeugen (6:13).

**Aktuell DE** · _Apostelgeschichte 6:11-13_  
Welcher Vorwurf wurde Stephanus von den aufgehetzten Zeugen gemacht?

- ⬜ Er habe den Tempelschatz gestohlen und die Opfergaben unterschlagen
- ✅ **Er rede Lästerworte gegen diese heilige Stätte und das Gesetz** ← _als richtig markiert_
- ⬜ Er habe sich mit den Römern verbündet und das Volk verraten
- ⬜ Er habe den Zehnten verweigert und die Feste des Gesetzes gebrochen

**Aktuell EN** · _Acts 6:11-13_  
What did the council behold concerning Stephen's face as they looked stedfastly on him?

- ⬜ His face was covered with a dark cloud of sorrow
- ✅ **They saw his face as it had been the face of an angel** ← _als richtig markiert_
- ⬜ His countenance was pale as ashes through great fear
- ⬜ His face shone with the brightness of the noon day sun

> 📖 **Beleg:** DE: 'Welcher Vorwurf wurde Stephanus ... gemacht?' / EN: 'What did the council behold concerning Stephen's face'

> ✏️ **Korrekturvorschlag:** EN: 'What did the false witnesses say against Stephen?' – [x] 'He ceaseth not to speak blasphemous words against this holy place, and the law'.

<sub>🔎 Gegenprüfung: Die Abweichung trifft zu: EN fragt nach 6:15, die Stelle ist 6:11-13. Die EN-Lösung 'face of an angel' ist für 6:15 aber richtig. Auf mittel herabgestuft. Die vorgeschlagene EN-Lösung passt zu KJV 6:13.</sub>

---

#### `apg_036` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Moses in Midian (Apg 7:30), DE nach Philippus in Samaria (8:5-6).

**Aktuell DE** · _Apostelgeschichte 8:5-6_  
Welcher Diakon verkündigte das Evangelium mit großem Erfolg in Samaria?

- ✅ **Philippus** ← _als richtig markiert_
- ⬜ Stephanus
- ⬜ Prochorus
- ⬜ Nikanor

**Aktuell EN** · _Acts 8:5-6_  
How long was Moses in the land of Madian before the angel appeared in the burning bush?

- ✅ **Forty years of time** ← _als richtig markiert_
- ⬜ Seven years of exile
- ⬜ Twenty years of time
- ⬜ Twelve years in Madian

> 📖 **Beleg:** DE [x] 'Philippus' / EN: 'How long was Moses in the land of Madian'

> ✏️ **Korrekturvorschlag:** EN: 'Which of the seven preached Christ in the city of Samaria?' – [x] 'Philip'.

<sub>🔎 Gegenprüfung: Die Abweichung trifft zu: EN fragt nach 7:30, die Stelle ist 8:5-6. Die EN-Lösung 'Forty years' ist für 7:30 aber richtig. Auf mittel herabgestuft, Angleichung an DE (Philip).</sub>

---

#### `apg_040` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach dem Glaubensbekenntnis (8:37), DE nach dem Anlass der Taufbitte (Wasser am Weg). Die EN-Lösung ist inhaltlich richtig, die Frage aber eine andere.

**Aktuell DE** · _Apostelgeschichte 8:36-38_  
Was veranlasste den Kämmerer aus Äthiopien zur Bitte um die Taufe am Wege?

- ✅ **Ein Wasser am Weg** ← _als richtig markiert_
- ⬜ Ein Brunnen in der Stadt
- ⬜ Der Fluss Jordan
- ⬜ Der Regen vom Himmel

**Aktuell EN** · _Acts 8:36-38_  
What confession of faith did the Ethiopian eunuch make before his baptism?

- ✅ **I believe that Jesus Christ is the Son of God** ← _als richtig markiert_
- ⬜ I believe that Moses is the prophet of the Most High
- ⬜ I believe that the temple in Jerusalem is the house of God
- ⬜ I believe that the kingdom of heaven is at hand on earth

> 📖 **Beleg:** DE [x] 'Ein Wasser am Weg' / EN [x] 'I believe that Jesus Christ is the Son of God'

> ✏️ **Korrekturvorschlag:** EN: 'What did the eunuch see by the way that moved him to ask for baptism?' – [x] 'A certain water'.

<sub>🔎 Gegenprüfung: Bestätigt: Die Fragen in DE und EN weichen voneinander ab. Die EN-Lösung ist nach KJV 8:37 richtig, die Stelle 8:36-38 deckt das ab. mittel bleibt angemessen.</sub>

---

#### `apg_045` · Sonstiges

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage nennt die Lösung in Klammern ('(Tabitha)') und verrät damit die Antwort.

**Aktuell DE** · _Apostelgeschichte 9:36-41_  
Welche gläubige Frau in Joppe (Tabitha) erweckte Petrus durch Gebet vom Tode?

- ⬜ Lydia, die Purpurhändlerin
- ✅ **Tabita, die Dorkas genannt wird** ← _als richtig markiert_
- ⬜ Rhode, die junge Magd im Hause
- ⬜ Drusilla, die Edelfrau aus Rom

> 📖 **Beleg:** 'Welche gläubige Frau in Joppe (Tabitha) erweckte Petrus durch Gebet vom Tode?'

> ✏️ **Korrekturvorschlag:** 'Welche gläubige Frau in Joppe, reich an guten Werken, erweckte Petrus durch Gebet vom Tode?'

<sub>🔎 Gegenprüfung: Bestätigt: '(Tabitha)' in der DE-Frage verrät die Lösung 'Tabita, die Dorkas genannt wird'. Die Umformulierung ist sinnvoll.</sub>

---

#### `apg_062` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Der Distraktor 'Barjesus' ist dieselbe Person wie Elymas (Apg 13:6-8). Damit ist er ebenfalls richtig, die Frage ist mehrdeutig. Zudem ist Barjesus kein Pharisäer, sondern ein jüdischer falscher Prophet.

**Aktuell DE** · _Apostelgeschichte 13:8-11_  
Welcher Zauberer und falsche Prophet wurde auf Zypern mit Blindheit geschlagen?

- ⬜ Simon, der Zauberer
- ⬜ Barjesus, der Pharisäer
- ✅ **Elymas, der Zauberer** ← _als richtig markiert_
- ⬜ Alexander, der Schmied

> 📖 **Beleg:** Apg 13:6: 'einen Zauberer, einen falschen Propheten, einen Juden namens Barjesus'; 13:8 'Elymas, der Zauberer'

> ✏️ **Korrekturvorschlag:** Option 1 ersetzen, z. B. durch 'Theudas, der Aufrührer' oder 'Demetrius, der Silberschmied'.

<sub>🔎 Gegenprüfung: Trifft im Kern zu: Barjesus und Elymas sind dieselbe Person (13:6-8). Der Zusatz 'der Pharisäer' ist allerdings falsch und macht die Option formal unrichtig. Das ist also eher eine Fangoption als eine zweite richtige Antwort, für Kundige aber mehrdeutig. Deshalb mittel statt hoch. Der Distraktor sollte ersetzt werden (z. B. 'Theudas' oder 'Demetrius, der Silberschmied').</sub>

---

#### `apg_080` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach der Antwort an den Kerkermeister (16:31), DE danach, was dessen Selbsttötung verhinderte (16:28). Die Stelle 16:27-28 enthält die EN-Antwort nicht.

**Aktuell DE** · _Apostelgeschichte 16:27-28_  
Was verhinderte die Selbsttötung des Kerkermeisters in der Nacht von Philippi?

- ✅ **Paulus rief laut: Tu dir nichts an, wir sind alle hier!** ← _als richtig markiert_
- ⬜ Das Eingreifen römischer Soldaten, die ihm das Schwert entrissen
- ⬜ Eine plötzliche Lähmung seiner Hand, die das Schwert fallen ließ
- ⬜ Der Hilferuf des Silas, der ihn aus dem Kerker zurückrief

**Aktuell EN** · _Acts 16:27-28_  
What did Paul and Silas answer the keeper of the prison when he cried, 'What must I do to be saved?'

- ✅ **Believe on the Lord Jesus Christ, and thou shalt be saved, and thy house** ← _als richtig markiert_
- ⬜ Offer up sacrifices according to the law of the fathers in the temple
- ⬜ Keep all the ordinances and commandments of the elders from thy youth
- ⬜ Fast forty days in sackcloth and ashes and distribute thy goods

> 📖 **Beleg:** DE [x] 'Paulus rief laut: Tu dir nichts an' / EN: 'What must I do to be saved?'

> ✏️ **Korrekturvorschlag:** EN: 'What stayed the keeper of the prison from killing himself?' – [x] 'Paul cried with a loud voice, Do thyself no harm: for we are all here'.

<sub>🔎 Gegenprüfung: Die Abweichung trifft zu: EN fragt nach 16:31, die Stelle ist 16:27-28. Die EN-Lösung 'Believe on the Lord Jesus Christ' ist für 16:31 aber richtig. Auf mittel herabgestuft, Angleichung an DE.</sub>

---

#### `apg_097` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach dem Stockwerk, EN fragt nach dem Namen des Jünglings. Die Lösungen haben einen anderen Inhalt (dritter Stock bzw. Eutychus).

**Aktuell DE** · _Apostelgeschichte 20:9-12_  
Aus welchem Stockwerk stürzte Eutychus hinab, ehe Paulus ihn ins Leben rief?

- ⬜ Aus dem zweiten Stock
- ✅ **Aus dem dritten Stock** ← _als richtig markiert_
- ⬜ Aus dem vierten Stock
- ⬜ Aus dem fünften Stock

**Aktuell EN** · _Acts 20:9-12_  
What young man fell down from the third loft and was taken up dead while Paul preached long at Troas?

- ⬜ Trophimus of Ephesus
- ✅ **Eutychus, being fallen asleep** ← _als richtig markiert_
- ⬜ Secundus of Thessalonica
- ⬜ Gaius of Derbe

> 📖 **Beleg:** DE: "Aus welchem Stockwerk stürzte Eutychus hinab"; EN: "What young man fell down from the third loft"

> ✏️ **Korrekturvorschlag:** EN: "From which loft did Eutychus fall down?" mit den Optionen "From the second loft" / "From the third loft" (richtig, Index 1) / "From the fourth loft" / "From the fifth loft"

<sub>🔎 Gegenprüfung: Bestätigt: DE fragt nach dem Stockwerk, EN nach dem Namen. Die EN-Lösung (Eutychus) ist für die EN-Frage zwar richtig, aber DE und EN passen nicht zusammen. Die vorgeschlagene EN-Fassung ist korrekt (KJV 20:9 'third loft').</sub>

---

#### `apg_120` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN fragt nach Agrippa und Bernice (25:13), DE fragt nach dem Zeitpunkt der Ablösung durch Festus (24:27). Die EN-Frage passt nicht zur angegebenen Stelle.

**Aktuell DE** · _Apostelgeschichte 24:27_  
Wann löste Porcius Festus den Felix als Statthalter ab?

- ✅ **Nach zwei Jahren** ← _als richtig markiert_
- ⬜ Nach drei Jahren
- ⬜ Nach einem Jahr
- ⬜ Nach fünf Jahren

**Aktuell EN** · _Acts 24:27_  
Which king and queen came unto Caesarea to salute Festus and hear Paul's cause?

- ✅ **King Agrippa and Bernice** ← _als richtig markiert_
- ⬜ King Herod and Herodias
- ⬜ King Aretas and his queen
- ⬜ King Antiochus and Berenice

> 📖 **Beleg:** EN: "Which king and queen came unto Caesarea to salute Festus"; KJV 24:27: "after two years Porcius Festus came into Felix' room"

> ✏️ **Korrekturvorschlag:** EN: "After how long did Porcius Festus come into Felix' room?" mit "After two years" an Index 0

<sub>🔎 Gegenprüfung: Bestätigt: Die EN-Lösung (Agrippa und Bernice, 25:13) ist für sich richtig, passt aber nicht zur Stelle 24:27 und nicht zur DE-Frage. EN an DE angleichen ('after two years', Index 0).</sub>

---

#### `apg_140` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt nach dem Propheten Jesaja (28:25), EN nach dem Schlusswort der Apostelgeschichte (28:31). Das liegt außerhalb der Stelle 28:25-28.

**Aktuell DE** · _Apostelgeschichte 28:25-28_  
Auf welchen alttestamentlichen Propheten berief sich Paulus beim Abschied?

- ✅ **Auf den Propheten Jesaja** ← _als richtig markiert_
- ⬜ Auf den Propheten Jeremia
- ⬜ Auf den Propheten Hesekiel
- ⬜ Auf den Propheten Daniel

**Aktuell EN** · _Acts 28:25-28_  
With what word did the book of Acts conclude concerning Paul's preaching in Rome?

- ✅ **Preaching the kingdom of God with all confidence, no man forbidding him** ← _als richtig markiert_
- ⬜ He was delivered unto the emperor Nero and suffered martyrdom by the sword
- ⬜ He departed into Spain and founded churches throughout all the Western lands
- ⬜ He wrote epistles unto all the seven churches of Asia before his departure

> 📖 **Beleg:** EN: "With what word did the book of Acts conclude..."; KJV 28:25: "Well spake the Holy Ghost by Esaias the prophet"

> ✏️ **Korrekturvorschlag:** EN: "Which prophet did Paul cite when the Jews at Rome departed?" mit "Esaias the prophet" an Index 0

<sub>🔎 Gegenprüfung: Bestätigt: Die EN-Lösung (28:31) ist für sich richtig, liegt aber außerhalb der Stelle 28:25-28 und weicht von der DE-Frage (Jesaja) ab. EN an DE angleichen (Esaias, Index 0).</sub>

---

### 📄 `45_roemer.json` (1)

#### `roem_069` · Mehrere richtig

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: war schon in `main`

**Problem:** Die Frage ist verneint ('Worin besteht das Reich Gottes NICHT?'). Die markierte Antwort ist aber positiv formuliert ('Nicht in Essen und Trinken, sondern in Gerechtigkeit …'). Distraktor 0 ('Beten und Fasten, Verzicht auf Speise und Trank') beschreibt ebenfalls etwas, worin das Reich laut V.17 nicht besteht. Die Logik der Frage ist widersprüchlich. Außerdem weichen die Distraktoren 2/3 inhaltlich ab: DE 'Glauben an Christus' bzw. 'Liebe zum Nächsten', EN 'outward precepts' bzw. 'philanthropy without faith'.

**Aktuell DE** · _Römer 14:17_  
Worin besteht das Reich Gottes nach den klaren Worten des Paulus nicht?

- ⬜ Im Beten und Fasten, im Verzicht auf Speise und Trank und in strenger Disziplin
- ✅ **Nicht in Essen und Trinken, sondern in Gerechtigkeit, Friede und Freude im Heiligen Geist** ← _als richtig markiert_
- ⬜ Im Glauben an Christus, im Hören auf sein Wort und im Gehorsam gegen seine Gebote
- ⬜ In der Liebe zum Nächsten, im Dienst an den Armen und im Teilen mit den Bedürftigen

**Aktuell EN** · _Romans 14:17_  
Wherein does the kingdom of God consist NOT according to Romans 14:17?

- ⬜ In fasting and bodily affliction, abstaining from meats and observing rigid rules
- ✅ **For the kingdom of God is not meat and drink; but righteousness, and peace, and joy in the Holy Ghost** ← _als richtig markiert_
- ⬜ In formal adherence to outward precepts and submitting unto bodily ordinances
- ⬜ In worldly philanthropy, distributing bread unto the poor without faith in Christ

> 📖 **Beleg:** V.17: 'Denn das Reich Gottes ist nicht Essen und Trinken, sondern Gerechtigkeit, Friede und Freude im Heiligen Geist'

> ✏️ **Korrekturvorschlag:** Frage positiv stellen: 'Worin besteht das Reich Gottes nach Römer 14,17?' (EN: 'Wherein doth the kingdom of God consist?'). Distraktoren in DE und EN angleichen.

<sub>🔎 Gegenprüfung: Bestätigt. Die Frage ist verneint, die markierte Antwort enthält aber zugleich die positive Aussage. Distraktor 0 (Fasten, Verzicht auf Speise und Trank) betrifft ebenfalls Speisefragen, die nach V.17 nicht das Reich ausmachen, und ist damit vertretbar richtig. Die Distraktoren 2/3 weichen in DE und EN inhaltlich ab. Die Frage positiv stellen und die Distraktoren angleichen.</sub>

---

### 📄 `46_1_korinther.json` (5)

#### `1kor_007` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Die Frage ist verneint ('worauf stützte sich die Verkündigung NICHT'). Die DE-Distraktoren 1 ('Gesetz der Väter und die Überlieferung der Ältesten') und 2 ('Auslegung der Gelehrten') nennen aber ebenfalls Dinge, auf die Paulus seine Predigt nicht stützte. Damit sind mehrere Optionen vertretbar richtig. Die EN-Distraktoren (Propheten, Zeichen des Geistes, Offenbarung Christi) sind dagegen sauber 'nicht falsch' und haben auch einen anderen Inhalt.

**Aktuell DE** · _1. Korinther 2:4-5_  
Worauf stützte sich die Verkündigung des Paulus bei den Korinthern nicht?

- ⬜ Auf den Beistand des Geistes und die Kraft der Zeichen
- ⬜ Auf das Gesetz der Väter und die Überlieferung der Ältesten
- ⬜ Auf die Heilige Schrift und die Auslegung der Gelehrten
- ✅ **Auf überredende Worte menschlicher Weisheit** ← _als richtig markiert_

> 📖 **Beleg:** V.4: 'nicht in überredenden Worten menschlicher Weisheit, sondern in Erweisung des Geistes und der Kraft'

> ✏️ **Korrekturvorschlag:** DE-Distraktoren an EN angleichen: 0 'Auf das Zeugnis der heiligen Propheten', 1 'Auf die mächtigen Zeichen des Geistes', 2 'Auf die Offenbarung Jesu Christi'.

<sub>🔎 Gegenprüfung: Bestätigt. Bei der verneinten Frage sind die DE-Distraktoren 1 (Gesetz der Väter/Überlieferung) und 2 (Auslegung der Gelehrten) ebenfalls Dinge, auf die Paulus sich laut Text nicht stützte. Nur Distraktor 0 ist laut V.4 sauber ein 'stützte sich darauf'. Die Distraktoren sollten Dinge sein, auf die er sich nachweislich stützte (Geist, Kraft), oder die Frage positiv gestellt werden.</sub>

---

#### `1kor_029` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt 'Wessen Glieder sind die Leiber der Gläubigen?', EN fragt 'Why must a believer flee fornication?'. Das sind unterschiedliche Fragen. Auch die Distraktoren weichen ab: DE 'gehören dem Staat/Vorfahren', EN 'imperial statutes/bodily strength/heathen mock'. Zudem steht 'flee fornication' in V.18 und liegt damit außerhalb der Stelle 6:15-17.

**Aktuell DE** · _1. Korinther 6:15-17_  
Wessen Glieder sind die Leiber der Gläubigen nach den Ausführungen im sechsten Kapitel?

- ⬜ Sie gehören dem Staat
- ✅ **Sie sind Glieder Christi** ← _als richtig markiert_
- ⬜ Sie sind Werkzeuge der Welt
- ⬜ Sie gehören den Vorfahren

**Aktuell EN** · _1 Corinthians 6:15-17_  
Why must a believer flee fornication according to 1 Corinthians 6:15?

- ⬜ Because civil imperial statutes forbid all unchaste deeds within the city
- ✅ **Your bodies are members of Christ, and must not be made members of an harlot** ← _als richtig markiert_
- ⬜ Because it consumeth bodily strength and shorteneth the days of a man's youth
- ⬜ Because heathen neighbours will mock the holy assemblies of the congregation

> 📖 **Beleg:** DE: 'Wessen Glieder sind die Leiber' / EN: 'Why must a believer flee fornication'

> ✏️ **Korrekturvorschlag:** EN: 'Whose members are the bodies of believers according to 1 Corinthians 6:15?' Distraktoren angleichen (the state, the world, the forefathers).

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt 'Wessen Glieder sind die Leiber?', EN fragt 'Why must a believer flee fornication?'. Das sind verschiedene Fragen, und auch die Distraktoren unterscheiden sich vollständig. 'Flee fornication' steht in V.18, außerhalb der Stelle 6:15-17. Den Bezug 'members of an harlot' liefert V.15 aber durchaus. EN an DE angleichen.</sub>

---

#### `1kor_030` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** DE fragt 'Wozu ist der Körper geweiht?', EN fragt 'Why are believers commanded to glorify God in their body?'. Alle Distraktoren unterscheiden sich inhaltlich: DE 'Wohnsitz der Seele/Haus irdischer Schätze/Stätte weltlicher Feste', EN 'formed of dust/human discipline meriteth/Roman senate'.

**Aktuell DE** · _1. Korinther 6:19-20_  
Wozu ist der leibliche Körper des Glaubenden nach den Schlussversen von Kapitel 6 geweiht?

- ⬜ Der Leib ist Wohnsitz der Seele, die nach dem Tod zu Gott zurückkehrt
- ⬜ Der Leib ist Haus irdischer Schätze, die man hier erwirbt
- ✅ **Der Leib ist ein Tempel des Heiligen Geistes in euch** ← _als richtig markiert_
- ⬜ Der Leib ist Stätte weltlicher Feste, an denen man sich freut

**Aktuell EN** · _1 Corinthians 6:19-20_  
Why are believers commanded to glorify God in their body and in their spirit?

- ⬜ Because the physical frame is formed of dust and perisheth forevermore
- ⬜ Because human discipline meriteth justification before the righteous God
- ✅ **The body is the temple of the Holy Ghost, and ye are bought with a price** ← _als richtig markiert_
- ⬜ Because bodily glory gaineth the favour and praise of the Roman senate

> 📖 **Beleg:** DE 0: 'Wohnsitz der Seele' / EN 0: 'formed of dust and perisheth'

> ✏️ **Korrekturvorschlag:** EN-Frage: 'What is the body of the believer according to 1 Corinthians 6:19?' Distraktoren 1:1 übertragen.

<sub>🔎 Gegenprüfung: Bestätigt. DE fragt 'Wozu ist der Körper geweiht?', EN fragt, warum man Gott im Leib verherrlichen soll. Alle Distraktoren sind inhaltlich verschieden.</sub>

---

#### `1kor_067` · Inhaltlicher Fehler

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage nennt die Bedingung nicht (kein Ausleger anwesend). Die Lösung 'Er soll still sein und in der Gemeinde schweigen' klingt dadurch wie ein generelles Schweigegebot für Zungenredner. Gefragt wird nach 'der Bedingung für das Zungenreden', und die wäre eigentlich: zwei oder drei, der Reihe nach, einer legt aus. EN nennt die Bedingung ausdrücklich.

**Aktuell DE** · _1. Korinther 14:27-28_  
Welche Bedingung gilt für das Zungenreden in der öffentlichen Versammlung?

- ⬜ Er soll lauter sprechen, damit jedermann ihn versteht
- ⬜ Er soll einen Priester holen, der die Feier leitet
- ⬜ Er soll vor die Türe treten und dort weiterbeten
- ✅ **Er soll still sein und in der Gemeinde schweigen** ← _als richtig markiert_

> 📖 **Beleg:** V.28: 'Ist aber kein Ausleger da, so schweige er in der Gemeinde'

> ✏️ **Korrekturvorschlag:** DE-Frage: 'Was soll der Zungenredner tun, wenn kein Ausleger in der Gemeinde da ist?'

<sub>🔎 Gegenprüfung: Bestätigt. Die DE-Frage fragt nach 'der Bedingung für das Zungenreden', antwortet aber mit dem Schweigegebot aus V.28, das nur gilt, wenn kein Ausleger da ist. Dadurch wird ein generelles Schweigegebot nahegelegt, was V.27 widerspricht. Das Subjekt 'Er' der Optionen hat in der DE-Frage zudem keinen Bezug. Die vorgeschlagene Umformulierung passt.</sub>

---

#### `1kor_078` · Mehrere richtig

🟠 **mittel** · Sprache: **DE** · Ursprung: war schon in `main`

**Problem:** Distraktor 3 'Dass sie ihn bald zurückschicken' ist laut V.11 inhaltlich ebenfalls ein Anliegen des Paulus: Sie sollen Timotheus in Frieden geleiten, damit er zu Paulus kommt. EN 3 fügt 'into the regions of Macedonia' hinzu und ist dadurch falsch, DE nicht.

**Aktuell DE** · _1. Korinther 16:10-11_  
Welches Anliegen betont Paulus bezüglich des bevorstehenden Besuchs von Timotheus?

- ⬜ Dass sie ihm viel Geld mitgeben
- ⬜ Dass sie ihn sofort als Richter einsetzen
- ✅ **Dass er ohne Furcht bei ihnen sei** ← _als richtig markiert_
- ⬜ Dass sie ihn bald zurückschicken

> 📖 **Beleg:** V.11: 'Geleitet ihn vielmehr in Frieden, damit er zu mir komme; denn ich erwarte ihn'

> ✏️ **Korrekturvorschlag:** DE 3: 'Dass sie ihn nach Mazedonien zurückschicken' bzw. 'Dass sie ihn bei sich festhalten'.

<sub>🔎 Gegenprüfung: Bestätigt. Nach V.11 ('Geleitet ihn in Frieden, damit er zu mir komme; denn ich erwarte ihn') ist 'Dass sie ihn bald zurückschicken' ebenfalls ein Anliegen des Paulus. Im EN-Distraktor macht der Zusatz 'into the regions of Macedonia' die Option falsch, im DE-Distraktor fehlt er. Den DE-Distraktor präzisieren, z. B. 'Dass sie ihn bei sich festhalten'.</sub>

---

### 📄 `47_2_korinther.json` (2)

#### `2kor_010, 2kor_011, 2kor_012, 2kor_013, 2kor_014, 2kor_019, 2kor_037, 2kor_040, 2kor_042, 2kor_045, 2kor_047, 2kor_048, 2kor_049, 2kor_051, 2kor_052, 2kor_053, 2kor_054, 2kor_055, 2kor_056, 2kor_057, 2kor_058, 2kor_059, 2kor_061` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: unbekannt

**Problem:** Systematisch in 2. Korinther: Die EN-Distraktoren haben oft einen anderen Inhalt als die DE-Distraktoren mit gleichem Index. Sie bleiben zwar falsch, sind aber keine Übersetzung der DE-Option. Lösung und Index stimmen jeweils.

> 📖 **Beleg:** 2kor_056: DE '1: In den ersten Himmel / 2: In den siebenten Himmel / 3: In den Wolkenhimmel' vs. EN '1: Unto the summit of Mount Sinai / 2: Unto the earthly temple of Jerusalem / 3: Unto the royal palace of Rome'; 2kor_045: DE '0: Zahlt eure Steuern treu an Rom' vs. EN '0: Thanks be unto the churches of Macedonia'; 2kor_053: DE '0: Sie stammen aus dem Haus Juda' vs. EN '0: Are they Romans? so am I.'

> ✏️ **Korrekturvorschlag:** EN-Distraktoren jeweils als sinngemäße Übersetzung der DE-Option mit gleichem Index formulieren, z. B. 2kor_056 EN: '1: Unto the first heaven', '2: Unto the seventh heaven', '3: Unto the heaven of the clouds'.

<sub>🔎 Gegenprüfung: Stichprobe bestätigt: 2kor_019, 2kor_042, 2kor_045, 2kor_053, 2kor_054 und 2kor_056 haben EN-Distraktoren mit anderem Inhalt als die DE-Option mit gleichem Index. In 2kor_042 etwa steht DE 1 'reichen' gegen EN 1 'proud' und DE 3 'stolzen' gegen EN 3 'envious'. Die Lösungen stimmen überall. Das Problem ist systematisch, beim Spielen aber unschädlich, deshalb höchstens 'mittel'. Zusätzlich zu 2kor_053: Der EN-Distraktor 2 'Are they Pharisees? so am I.' ist sachlich nicht falsch, denn Paulus war Pharisäer (Apg 23:6, Phil 3:5). Er sollte ohnehin durch eine Übersetzung der DE-Option ersetzt werden.</sub>

---

#### `2kor_060` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE+EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die DE-Frage ist schief gestellt: Sie fragt, welche Gesinnung Paulus NICHT sucht, alle Optionen haben aber die Form 'Nicht X, sondern Y'. Die EN-Frage fragt etwas anderes (Paulus' Haltung zu den Gütern der Korinther). Auch die Distraktoren sind inhaltlich andere: DE 'Nicht euer Heil, sondern Geld' / 'Nicht eure Reue, sondern Strafe' / 'Nicht euer Gebet, sondern Opfer', EN dagegen Land in Achaja, ein Thron, Purpurgewänder.

**Aktuell DE** · _2. Korinther 12:14-15_  
Welche Gesinnung sucht Paulus nicht bei der Gemeinde, wenn er zu ihnen kommt?

- ✅ **Nicht das Eure, sondern euch selbst** ← _als richtig markiert_
- ⬜ Nicht euer Heil, sondern Geld
- ⬜ Nicht eure Reue, sondern Strafe
- ⬜ Nicht euer Gebet, sondern Opfer

**Aktuell EN** · _2 Corinthians 12:14-15_  
What disposition does Paul declare regarding the goods of the Corinthians?

- ✅ **For I seek not yours, but you: and I will very gladly spend and be spent for you** ← _als richtig markiert_
- ⬜ Great store of silver and gold to purchase lands in the province of Achaia
- ⬜ An exalted throne in their assembly from which to govern the local elders
- ⬜ Costly gifts of fine linen and purple garments for his companions

> 📖 **Beleg:** DE: 'Welche Gesinnung sucht Paulus nicht bei der Gemeinde ...?' / EN: 'What disposition does Paul declare regarding the goods of the Corinthians?'; DE-TEXT 12:14: 'denn ich suche nicht das Eurige, sondern euch'

> ✏️ **Korrekturvorschlag:** DE: 'Was sucht Paulus bei der Gemeinde, wenn er zum dritten Mal zu ihr kommt?' EN: 'What does Paul seek of the Corinthians when he cometh the third time?' Dazu die EN-Distraktoren sinngemäß an DE angleichen, z. B. 'Not your salvation, but your money'.

<sub>🔎 Gegenprüfung: Der Befund stimmt. Die DE-Frage 'Welche Gesinnung sucht Paulus nicht' passt nicht zu den Antworten der Form 'Nicht X, sondern Y'. Die EN-Frage fragt etwas anderes, nämlich Paulus' Haltung zu den Gütern der Korinther. Auch die EN-Distraktoren (Land in Achaja, Thron, Purpur) sind keine Übersetzung der DE-Distraktoren. Lösung und Index sind in beiden Sprachen richtig, das Problem liegt bei der Formulierung und der Parallelität. Der Korrekturvorschlag ist sinnvoll.</sub>

---

### 📄 `58_hebraeer.json` (1)

#### `hebr_039` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Frage fragt, WAS veraltet und vergeht. Die richtige Antwort darauf wäre 'der erste Bund'. Die Optionen beschreiben aber, was mit dem alten Bund geschieht, und die Lösung wiederholt nur die Frage ('That which decayeth...'). DE fragt dagegen sauber 'Was geschieht mit dem Vorherigen'.

**Aktuell DE** · _Hebräer 8:13_  
Was geschieht mit dem Vorherigen, indem Gott einen neuen Bund nennt (Hebräer 8:13)?

- ⬜ Er wird mit frischem Blut der Kälber erneuert
- ⬜ Er bleibt für alle Heidenvölker ewig bestehen
- ⬜ Er wird in das weltliche Gesetzbuch übernommen
- ✅ **Er ist veraltet und wird bald verschwinden** ← _als richtig markiert_

**Aktuell EN** · _Hebrews 8:13_  
What decayeth and waxeth old in that He saith a new covenant (Hebrews 8:13)?

- ⬜ It is renewed continually with the blood of calves
- ⬜ It remaineth binding for ever upon all the Gentiles
- ⬜ It is received into the secular statute books of men
- ✅ **That which decayeth and waxeth old is ready to vanish** ← _als richtig markiert_

> 📖 **Beleg:** EN: "What decayeth and waxeth old in that He saith a new covenant" / KJV: "he hath made the first old. Now that which decayeth and waxeth old is ready to vanish away."

> ✏️ **Korrekturvorschlag:** EN-Frage: "What becometh of the first covenant, in that He saith, A new covenant (Hebrews 8:13)?"; Option 3: "It is made old, and is ready to vanish away"

<sub>🔎 Gegenprüfung: Trifft zu. Die EN-Frage fragt nach dem Subjekt (was veraltet), die richtige Antwort wäre aber 'the first covenant'. Option 3 wiederholt nur die Frageformulierung, und die Distraktoren ('It is ...') passen grammatisch nicht zur Frage. DE fragt dagegen korrekt nach dem Schicksal des vorherigen Bundes. Der Vorschlag ('What becometh of the first covenant ...' / 'It is made old, and is ready to vanish away') passt zu KJV 8:13.</sub>

---

### 📄 `59_jakobus.json` (1)

#### `jak_013` · DE/EN weicht ab

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** EN-Distraktor 2 (Quelle mit süßem und bitterem Wasser) unterscheidet sich inhaltlich von DE (Brunnen mit viel frischem Wasser). Außerdem greift er genau das Bild aus Jak 3:11 auf, das Jakobus im selben Kapitel tatsächlich auf die Zunge anwendet. Dadurch ist er irreführend nah an einer richtigen Antwort.

**Aktuell DE** · _Jakobus 3:5-6_  
Womit vergleicht Jakobus die Zunge in Jakobus 3:5-6?

- ⬜ Mit einem mächtigen Schwert, das einen Feind besiegt
- ✅ **Mit einem kleinen Feuer, das einen großen Wald anzündet** ← _als richtig markiert_
- ⬜ Mit einem tiefen Brunnen, der viel frisches Wasser birgt
- ⬜ Mit einer goldenen Krone, die dem Träger Ehre verleiht

**Aktuell EN** · _James 3:5-6_  
To what doth James compare the tongue in James 3:5-6?

- ⬜ To a mighty twoedged sword that slayeth every enemy
- ✅ **To a little fire that kindleth how great a matter** ← _als richtig markiert_
- ⬜ To a deep fountain yielding sweet and bitter water
- ⬜ To a golden crown that bestoweth honor on its head

> 📖 **Beleg:** DE 2: "Mit einem tiefen Brunnen, der viel frisches Wasser birgt" / EN 2: "To a deep fountain yielding sweet and bitter water"

> ✏️ **Korrekturvorschlag:** EN Option 2: "To a deep well holding much fresh water"

<sub>🔎 Gegenprüfung: Trifft zu. DE-Option 2 (Brunnen mit frischem Wasser) und EN-Option 2 (Quelle mit süßem und bitterem Wasser) sagen inhaltlich Verschiedenes. Das EN-Bild stammt aus Jak 3:11, wo Jakobus die Quelle tatsächlich als Vergleich für die Zunge (Segen und Fluch) heranzieht. Der Distraktor ist nur durch die Einschränkung auf 3:5-6 formal falsch und deshalb irreführend. Der Vorschlag 'To a deep well holding much fresh water' gleicht EN an DE an.</sub>

---

### 📄 `61_2_petrus.json` (1)

#### `2petr_013` · KJV-Wortlaut

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Lösung zitiert KJV verkürzt und dadurch sinnwidrig: Es fehlt 'a thousand years', sodass es heißt 'ein Tag ist wie tausend Jahre und wie ein Tag'. DE-Option 1 ist ebenfalls verkürzt ('tausend wie ein Tag').

**Aktuell EN** · _2 Peter 3:8_  
How is time accounted with the Lord in 2 Peter 3:8?

- ⬜ One year is as an hundred days, and an hundred days as a year
- ✅ **One day is with the Lord as a thousand years, and as one day** ← _als richtig markiert_
- ⬜ One month is as ten whole years, and ten years as a month
- ⬜ One hour is as an hundred years, and an hundred as an hour

> 📖 **Beleg:** EN 1: "One day is with the Lord as a thousand years, and as one day" / KJV: "one day is with the Lord as a thousand years, and a thousand years as one day"

> ✏️ **Korrekturvorschlag:** EN 1: "One day is with the Lord as a thousand years, and a thousand years as one day"; DE 1: "Ein Tag ist vor dem Herrn wie tausend Jahre und tausend Jahre wie ein Tag"

<sub>🔎 Gegenprüfung: Trifft zu und wiegt eher mittel als niedrig, weil der Text der richtigen Antwort selbst sinnwidrig ist ('as a thousand years, and as one day'). Nach KJV 3:8 lautet er: 'One day is with the Lord as a thousand years, and a thousand years as one day'. DE 'und tausend wie ein Tag' ist eine verständliche Ellipse (vgl. das parallele Muster in DE-Option 3) und nicht zwingend zu ändern. Eine Ergänzung wäre dennoch sauberer.</sub>

---

### 📄 `66_offenbarung.json` (2)

#### `off_070` · DE/EN weicht ab

🟠 **mittel** · Sprache: **DE** · Ursprung: durch die Überarbeitung entstanden

**Problem:** Die DE-Frage fragt, womit der Sitzende "gekrönt und bewaffnet" ist. Die Krone (goldene Krone) kommt aber in keiner Option vor, und die Antwort nennt nur die Sichel. Die Optionen stehen im Nominativ statt im Dativ. EN fragt nur, was er in der Hand hatte.

**Aktuell DE** · _Offenbarung 14:14_  
Womit ist Der sitzend auf der weißen Wolke gekrönt und bewaffnet?

- ⬜ Ein flammendes Richtschwert
- ⬜ Ein langes goldenes Zepter
- ✅ **Eine scharfe Sichel zur Ernte** ← _als richtig markiert_
- ⬜ Eine hell brennende Fackel

**Aktuell EN** · _Revelation 14:14_  
What had the Son of man upon the white cloud in His hand?

- ⬜ A flaming sword of vengeance
- ⬜ A golden sceptre of royalty
- ✅ **A sharp sickle in his hand** ← _als richtig markiert_
- ⬜ A burning lamp of judgment

> 📖 **Beleg:** DE: "Womit ist Der sitzend auf der weißen Wolke gekrönt und bewaffnet?" – "Eine scharfe Sichel zur Ernte"; KJV: "having on his head a golden crown, and in his hand a sharp sickle"

> ✏️ **Korrekturvorschlag:** "Was hält der, der auf der weißen Wolke sitzt, in seiner Hand?"

<sub>🔎 Gegenprüfung: Bestätigt: 'gekrönt und bewaffnet' passt nicht zu den Optionen, die nur Gegenstände in der Hand nennen (die goldene Krone fehlt). Zudem ist 'Der sitzend' ungrammatisch. Korrektur: 'Was hält der, der auf der weißen Wolke sitzt, in seiner Hand?'</sub>

---

#### `off_082` · KJV-Wortlaut

🟠 **mittel** · Sprache: **EN** · Ursprung: in der neuen EN-Fassung entstanden

**Problem:** Die EN-Lösung gibt den Namen auf der Stirn sinnentstellend verkürzt wieder: "Abominations" fehlt, so entsteht "Mother ... of Earth".

**Aktuell EN** · _Revelation 17:5_  
What name was written upon the forehead of the woman?

- ⬜ The beast out of the pit, mother of all wickedness on earth
- ⬜ The queen of heaven, mother of all false idols and temples
- ✅ **Mystery: Babylon the Great, Mother of Harlots and of Earth** ← _als richtig markiert_
- ⬜ The enemy of saints, mother of all deceit and transgression

> 📖 **Beleg:** EN: "Mystery: Babylon the Great, Mother of Harlots and of Earth"; KJV: "MYSTERY, BABYLON THE GREAT, THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE EARTH"

> ✏️ **Korrekturvorschlag:** "Mystery, Babylon the Great, the Mother of Harlots and Abominations of the Earth"

<sub>🔎 Gegenprüfung: Bestätigt: Der EN-Lösung fehlt 'Abominations', dadurch entsteht sinnentstellt 'Mother of Harlots and of Earth'. KJV 17:5: 'THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE EARTH'.</sub>

---


<a id="kleinere-fehler"></a>

## 🟡 Kleinere Fehler (597)

_Wortlaut, Sprache, frei erfundene EN-Distraktoren. Je Datei aufklappbar._

<details>
<summary><b>01_1_mose.json</b> – 41 kleinere Befunde</summary>

- **`1mose_003`** · EN · DE/EN weicht ab  
  Distraktor 2 lautet in DE „Den Mond“, in EN aber „The high firmament“. Das ist ein anderer Inhalt, und die Feste wurde zudem tatsächlich zum Scheiden geschaffen (am 2. Tag).  
  ✏️ _EN 2: "The moon"._
- **`1mose_012`** · DE · Sprachfehler  
  Tippfehler im Flussnamen: „Pharpbar“ statt „Pharpar“.  
  ✏️ _„Jordan, Euphrat, Tigris und Pharpar“._
- **`1mose_017`** · EN · KJV-Wortlaut  
  Die richtige EN-Option ist als Zitat gesetzt, ergänzt den KJV-Wortlaut aber sinnverändernd um „knowing all“. Laut KJV heißt es „knowing good and evil“. Die DE-Option enthält nur den ersten Satzteil.  
  ✏️ _EN 1: "Ye shall not surely die!" (entspricht DE) oder "Ye shall not surely die … ye shall be as gods, knowing good and evil"._
- **`1mose_030`** · EN · DE/EN weicht ab  
  Distraktor 3 unterscheidet sich zwischen DE und EN.  
  ✏️ _EN 3: "An everlasting northern light" (oder DE: „Ein leuchtender Stern“)._
- **`1mose_038`** · DE · Inhaltlicher Fehler  
  Gebrannt wurden laut Text die Ziegel, nicht der Asphalt. Die Formulierung „gebrannten Asphalt“ ist sachlich falsch.  
  ✏️ _DE 2: „Gebrannte Ziegel für Steine und Asphalt für Kalk“._
- **`1mose_061`** · DE · Sprachfehler  
  Grammatikfehler: „seines Söhnes“ statt „seines Sohnes“.  
  ✏️ _„… bezüglich seines Sohnes Isaak …“._
- **`1mose_062`** · DE · Sprachfehler  
  Grammatikfehler: „seines Söhnes“ statt „seines Sohnes“.  
  ✏️ _„… anstelle seines Sohnes Isaak?“._
- **`1mose_071`** · DE+EN · Inhaltlicher Fehler  
  Die richtige DE-Option nennt einen „Stirnreif“. Der Text spricht nur von einem goldenen Reif, und nach 1. Mose 24:47 wurde er an die Nase gelegt. „Stirnreif“ ist daher sachlich falsch und stimmt auch nicht mit EN „earring“ überein.  
  ✏️ _DE-Option 3: „Einen goldenen Reif (Nasenring) und zwei Armspangen“._
- **`1mose_076`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren haben in DE und EN völlig unterschiedliche Inhalte.  
  ✏️ _EN-Distraktoren an DE angleichen: 1 "That both sons would become glorious kings over all Egypt"; 2 "That they would share all land and inheritance in perfect unity"; 3 "That the firstborn alone would receive all blessings and privileges"._
- **`1mose_090`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN einen anderen Inhalt (Bündnis mit dem Pharao gegen Kanaan bzw. angeheuerte Hetiter-Krieger).  
  ✏️ _EN 3: "To ally himself at once with Pharaoh to make war upon Canaan" (oder DE an EN angleichen)._
- **`1mose_097`** · DE+EN · Bibelstelle  
  Die Frage verlangt alle vier ersten Söhne Leas. Die Stelle 29:35 nennt aber nur Juda; Ruben, Simeon und Levi stehen in 29:32-34.  
  ✏️ _bibleReference auf „1. Mose 29:32-35“ / „Genesis 29:32-35“ erweitern._
- **`1mose_109`** · EN · DE/EN weicht ab  
  Die EN-Distraktoren 0, 2 und 3 haben andere Inhalte als die DE-Optionen. EN-Option 3 („Both agreed upon the name Mizpah“) ist zudem teilweise zutreffend, denn derselbe Steinhaufen heißt laut 31:49 auch Mizpa. Das ist irreführend.  
  ✏️ _EN-Optionen an DE angleichen: 0 "Laban called it Mahanaim, but Jacob called it Peniel"; 2 "Laban called it Hebron, but Jacob called it Succoth"; 3 "Laban called it Beer-sheba, but Jacob called it Bethel"._
- **`1mose_110`** · DE · Bibelstelle  
  Im hinterlegten DE-Text steht die Begegnung mit den Engeln in 32:1 und die Benennung Mahanaim in 32:2. Die angegebene Stelle 32:2-3 lässt die Begegnung weg und enthält stattdessen die Boten an Esau.  
  ✏️ _DE-bibleReference auf „1. Mose 32:1-2“ ändern._
- **`1mose_112`** · DE · Bibelstelle  
  Der hinterlegte DE-Text nutzt in Kap. 32 die KJV-Verszahlen. Der eigentliche Ringkampf („rang ein Mann mit ihm, bis die Morgenröte anbrach“) steht in DE 32:24 und fehlt in der angegebenen Stelle 32:25-26.  
  ✏️ _DE-bibleReference auf „1. Mose 32:24-25“ ändern (gleich wie EN)._
- **`1mose_123`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 unterscheidet sich: DE „einen Monat kein Wort gesprochen und gemieden“, EN „einen Monat nicht mit ihm am Tisch gegessen“. Auch Distraktor 0 weicht ab: DE enthält „enterben“, EN nur das Verbannen von den Weiden.  
  ✏️ _EN 2: "They spake not a word unto Joseph for a month and shunned him"_
- **`1mose_125`** · EN · Sprachfehler  
  In der EN-Lösung fehlt der Artikel. „kept saying“ heißt im Englischen „sagte ständig“, gemeint ist aber nach KJV „observed the saying“ (bewahrte das Wort).  
  ✏️ _"The sun, moon, and eleven stars made obeisance; Jacob rebuked him but observed the saying"_
- **`1mose_127`** · EN · KJV-Wortlaut  
  Die EN-Lösung steht als KJV-Zitat in Anführungszeichen, ergänzt aber „unto us in the field“. Das steht nicht in KJV 37:19.  
  ✏️ _"Behold, this dreamer cometh."_
- **`1mose_132`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN anderen Inhalt (DE: heimliche Freude über die Beseitigung / EN: Verfolgung der Karawane zum Freikauf).  
  ✏️ _EN 3: "He secretly rejoiced that his father's favourite was removed"_
- **`1mose_133`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN anderen Inhalt (DE0 im Brunnen ertrunken / EN0 zerrissene Sandalen; DE2 kanaanitische Räuber / EN2 Midianiter mit dem Schwert; DE3 Gewand im Sand vergraben / EN3 zerbrochener Stab mit Blut).  
  ✏️ _EN-Distraktoren als Übersetzung der DE-Optionen: 0 "They claimed Joseph was drowned in a well", 2 "They told their father Canaanite robbers had slain him in the mountains", 3 "They buried the coat in the sand and said he had fled into the wilderness"_
- **`1mose_135`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind verschoben oder inhaltlich anders: DE1 Priesterfürst von On / EN1 Getreidehändler in Memphis; DE2 Baumeister der Getreidespeicher / EN2 Hohepriester von On; DE0 an den Mundschenken / EN0 an den Pharao selbst als Mundschenk.  
  ✏️ _EN 0 "Unto the chief butler at Pharaoh's court", EN 1 "Unto a priest of the city of On", EN 2 "Unto the chief builder of the royal granaries"_
- **`1mose_150`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN anderen Inhalt (DE: Name El-Saddai, Frau Sarai / EN: Name „Prince of Nile“, eine kanaanitische Frau).  
  ✏️ _EN 3: "Iron armour and the second chariot; he called him El-shaddai and gave him Sarai" (oder DE an EN angleichen)_
- **`1mose_157`** · DE+EN · Inhaltlicher Fehler  
  Die Lösung behauptet, Jakob habe (bitterlich) geweint. In 42:36-38 steht nichts von Weinen. Jakob klagt nur, man habe ihn seiner Kinder beraubt, und weigert sich.  
  ✏️ _DE: „Er klagte, sie hätten ihn seiner Kinder beraubt; Ruben bot seine beiden Söhne als Pfand an“ / EN: "He lamented that they had bereaved him of his children; Reuben offered his two sons as pledge"_
- **`1mose_166`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN anderen Inhalt (DE0 doppelte Portion + Trinken / EN0 dreimal so viel; DE1 goldene Schale / EN1 doppelt so viel; DE3 von Joseph gefüttert / EN3 auf Gold serviert). Außerdem fehlt in DE 2 ein Wort: „als allen“ statt „als ihnen allen“.  
  ✏️ _Distraktoren angleichen (z. B. DE 0 „dreimal so viel“, DE 1 „doppelt so viel“, DE 3 „auf reinem Gold serviert“); DE 2: „Dem Benjamin wurde fünfmal mehr aufgetragen als ihnen allen“_
- **`1mose_192`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 haben in DE und EN anderen Inhalt (DE1 Schwur, nie mehr zu streiten / EN1 Rückkehr nach Kanaan vor Pharaos Tod; DE3 Abschiedsopfer für den Pharao / EN3 Sündenbekenntnis).  
  ✏️ _EN 1: "That they might swear never again to strive among themselves"; EN 3: "That they might offer together a farewell sacrifice for Pharaoh"_
- **`1mose_195`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 sind in DE und EN völlig verschieden (DE: Städte erobern und Gold horten / Priesteramt / Erbe ohne Waffen; EN: Bergfestungen ohne Kampf / Schiffe von Tarsis / demütiger Hirtenstamm). Außerdem fehlt in der EN-Lösung der Teil „Hand auf dem Nacken der Feinde“.  
  ✏️ _EN-Distraktoren als Übersetzung der DE-Optionen formulieren; EN 3: "His brethren shall praise him, his hand shall be in the neck of his enemies, and his father's children shall bow down before him"_
- **`1mose_196`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren stehen unter anderen Indizes bzw. sind andere Tiere: DE1 Stier / EN1 Adler; DE2 Hirsch / EN2 Wildstier; DE3 Adler / EN3 Leopard.  
  ✏️ _EN 1: "With a strong bull goring his enemies", EN 2: "With a swift hart leaping upon the mountains", EN 3: "With a bold eagle circling high over Canaan"_
- **`1mose_197`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren unterscheiden sich in DE und EN (DE0 Zepter geht an Levi / EN0 im Kampf gegen die Philister zerbrochen; DE2 Ungehorsam des ersten Königs / EN2 an Joseph übergeben; DE3 an den Pharao / EN3 Salomos Tempelbau).  
  ✏️ _EN-Distraktoren an DE angleichen: 0 "The sceptre shall pass to Levi when the people reach the wilderness of Sinai", 2 "The sceptre shall be broken when Israel's first king disobeyeth God", 3 "The sceptre shall be given to Pharaoh as a sign of everlasting covenant"_
- **`1mose_198`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN anderen Inhalt (DE0 Füße in Olivenöl baden / EN0 Ölflüsse; DE1 Milch der Kühe / EN1 siebenfache Weizenernte; DE3 Ernte im Winter / EN3 Zedern-Kornspeicher).  
  ✏️ _EN-Distraktoren als Übersetzung der DE-Optionen formulieren (oder umgekehrt)._
- **`1mose_199`** · DE · Sprachfehler  
  Der DE-Fragesatz ist unvollständig: „Wie wird das physische Erscheinungsbild Judas … ?“ (es fehlt „beschrieben“).  
  ✏️ _„Wie wird das physische Erscheinungsbild Judas infolge dieses Überflusses beschrieben?“_
- **`1mose_221`** · EN · Sprachfehler  
  Die EN-Lösung bricht mitten im Satz ab („and was gathered“ ohne „unto his people“).  
  ✏️ _"He gathered up his feet into the bed, yielded up the ghost, and was gathered unto his people"_
- **`1mose_222`** · DE · Sprachfehler  
  Tempusfehler im DE-Distraktor: „rasiert“ statt „rasierte“.  
  ✏️ _„Er zerriß sein buntes Gewand und rasierte sich den Kopf vor Trauer“_
- **`1mose_229`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 unterscheidet sich (DE: Drohung mit dem Fluch Gottes / EN: Übergabe des Viehs). Die DE-Frage enthält außerdem den unpassenden Zusatz „(Todesurkunde / Testament)“: Eine Todesurkunde kommt im Text nicht vor.  
  ✏️ _DE-Frage: „Welche Botschaft ließen die Brüder Joseph ausrichten, um sein Herz gnädig zu stimmen?“; EN 2: "They threatened him with the curse of God if he harmed a hair of them"_
- **`1mose_231`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 haben in DE und EN anderen Inhalt (DE1 Zweifel an Liebe / EN1 lange Verzögerung; DE2 Fleisch und Blut schaden / EN2 Silber und Gold als Sühne). DE 2 ist außerdem grammatisch falsch: „meinen eigenen Fleisch und Blut“ statt „meinem“.  
  ✏️ _DE 2: „Sollte ich meinem eigenen Fleisch und Blut Schaden zufügen?“; EN 1: "Why do ye doubt my love and faithfulness?", EN 2: "Should I do harm unto mine own flesh and blood?"_
- **`1mose_232`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 sind in DE und EN völlig verschieden (DE: Bruderliebe / eigener Fleiß / Schicksal; EN: Erlass des Pharao / Götter Ägyptens / Brüder als Knechte).  
  ✏️ _EN-Distraktoren als Übersetzung der DE-Optionen formulieren (oder umgekehrt)._
- **`1mose_233`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 2 haben in DE und EN anderen Inhalt (DE0 Paläste und Diener / EN0 befestigte Städte in Gosen; DE2 Gosen verlassen und nach Kanaan zurück / EN2 Steuerbefreiung).  
  ✏️ _EN 0: "He gave them rich palaces in the royal city and many Egyptian servants"; EN 2: "He bade them leave Goshen at once and return to Canaan"_
- **`1mose_237`** · DE+EN · Inhaltlicher Fehler  
  Distraktor 2 bezeichnet Abraham als Josephs Großvater. Abraham ist Josephs Urgroßvater, sein Großvater ist Isaak (180 Jahre). Der Spieler lernt hier eine falsche Verwandtschaftsangabe.  
  ✏️ _„… genau wie sein Urgroßvater Abraham“ / "even as his great-grandfather Abraham"_
- **`1mose_256`** · DE · Sprachfehler  
  Genitiv fehlt: „im Süden Kanaan“ statt „im Süden Kanaans“.  
  ✏️ _„Welcher geschichtsträchtige Ort im Süden Kanaans …“_
- **`1mose_299`** · DE+EN · Sonstiges  
  Die Erklärung handelt von Abrahams Zehntabgabe und der Überlegenheit des melchisedekischen Priestertums. Gefragt wird aber nach Brot und Wein als Vorbild auf das Abendmahl. Die Erklärung stützt die markierte Lösung nicht.  
  ✏️ _Erklärung anpassen, z. B.: "Melchisedeks Brot und Wein werden typologisch als Vorbild auf das Mahl des Herrn gedeutet, und sein Priestertum auf das ewige Priestertum Christi [ref:Hebräer 7:1-3; Lukas 22:19-20]."_
- **`1mose_305`** · DE+EN · DE/EN weicht ab  
  In Distraktor 1 bringt die Taube in DE einen "grünen Palmzweig", in EN einen "olive branch". Beide Optionen sind falsch, haben aber unterschiedlichen Inhalt.  
  ✏️ _Beide Sprachen angleichen, z. B. DE: "Eine weiße Taube, die sofort mit einem Ölblatt im Schnabel zurückkehrte" (oder EN: "palm branch")._
- **`1mose_316`** · DE · Inhaltlicher Fehler  
  Distraktor 0 nennt die falsche Person: Gott erhörte bei Ismael nicht das Weinen "Hiobs", sondern Hagars bzw. des Knaben (EN richtig: "the lad"). Außerdem gibt die DE-Lösung ein Zitat mit erfundenem Zusatz "zum Freudentag" wieder. Das Zitat stammt aus 21:6, also außerhalb der angegebenen Stelle 21:1-3.  
  ✏️ _DE 0: "Ismael ('Gott erhört'), weil Gott die Stimme des Knaben in der Wüste erhört hatte"; DE 3: "Isaak ('Lachen'), denn Sara sprach: 'Gott hat mir ein Lachen bereitet!'"; bibleReference auf "1. Mose 21:1-6" erweitern._
- **`1mose_329`** · DE+EN · Bibelstelle  
  Die Reihenfolge ist richtig (Arche bauen, Flut, Ararat, Taube mit Ölblatt, Regenbogen). Die bibleReference 1. Mose 6:14-22 deckt aber nur den Bau der Arche ab, nicht Flut, Ararat, Taube und Regenbogen.  
  ✏️ _bibleReference auf "1. Mose 6:14 – 9:17" / "Genesis 6:14 – 9:17" erweitern._

</details>

<details>
<summary><b>02_2_mose.json</b> – 45 kleinere Befunde</summary>

- **`ex_020`** · DE · Inhaltlicher Fehler  
  Die Zählung der Gebote hängt von der Tradition ab. Nach lutherischer und katholischer Zählung, die im deutschen Raum verbreitet ist, ist das Elterngebot das 4. und das Sabbatgebot das 3. Gebot. "Fünftes Gebot" stimmt nur nach jüdischer/reformierter Zählung, die die Frage nicht nennt.  
  ✏️ _In der Frage die Zählweise angeben: "Welches Gebot (nach jüdischer/reformierter Zählung) ..." oder die Optionen nur inhaltlich formulieren, ohne Ordnungszahl._
- **`ex_025`** · DE · Sprachfehler  
  DE spricht von "den Tischen der Stiftshütte" (Plural). Es gab aber nur einen Schaubrottisch (2. Mose 25:23). EN sagt richtig "the table of shewbread".  
  ✏️ _"Aus welchem Holz sollten die Bundeslade und der Schaubrottisch der Stiftshütte angefertigt werden?"_
- **`ex_045`** · DE+EN · Inhaltlicher Fehler  
  'Urgroßsohn' ist kein deutsches Wort (gemeint ist Urenkel). Außerdem enthalten die Distraktoren falsche Verwandtschaftsangaben: Jizhar/Izhar ist nach 2. Mose 6:18 ein Sohn Kehats, nicht sein Bruder. Usiel ist ebenfalls ein Sohn Kehats, nicht 'der jüngste Sohn der Sippe Levis'. So lernt der Spieler falsche Genealogie.  
  ✏️ _DE 2: 'Amram, der Sohn Kehats'. DE/EN 1: 'Jizhar, der Sohn Kehats' / 'Izhar the son of Kohath'. DE 3: 'Usiel, der jüngste Sohn Kehats'._
- **`ex_048`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 hat in DE und EN einen anderen Inhalt (DE: Mose zum Priester; EN: Moses the judge).  
  ✏️ _EN 0: 'Aaron was made the captain of the host and Moses the priest'._
- **`ex_060`** · DE · Sprachfehler  
  In der richtigen Option steht 'Wundzeichen' (Zeichen einer Wunde) statt 'Wunderzeichen'. Derselbe Fehler steht in ex_042, Option 0 ('sichtbaren Wundzeichen').  
  ✏️ _'Dass dieses Wunderzeichen eindeutig der Finger Gottes sei'; in ex_042 ebenso 'Wegen des Fehlens von sichtbaren Wunderzeichen im Lager'._
- **`ex_060`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 hat in DE und EN einen anderen Inhalt (DE: Zaubersprüche vom Wind verweht; EN: magic spells were powerless). Die EN-Lösung steht zudem als Zitat in Anführungszeichen ('This wonder is the finger of God'), während die KJV 'This is the finger of God' lautet.  
  ✏️ _EN 1: '"This is the finger of God"'; EN 0: 'That their spells had been blown away by the wind'._
- **`ex_073`** · DE · Sprachfehler  
  Die DE-Frage ist sprachlich verunglückt und kaum verständlich ('Wie beschaffte sich die neunte Plage ... ihren Raum'). Die EN-Frage fragt dagegen klar, wie die Finsternis herbeigeführt wurde.  
  ✏️ _'Wie wurde die neunte Plage der Finsternis über Ägypten herbeigeführt?'_
- **`ex_096`** · DE · Sprachfehler  
  Rechtschreibfehler im Distraktor: 'Sternsbildes'.  
  ✏️ _'Das Leuchten eines Sternbildes am Himmel'_
- **`ex_172`** · DE · Sprachfehler  
  Das Adjektiv 'Sanftmütiges' ist mitten in der Phrase großgeschrieben.  
  ✏️ _'Ein stilles, sanftes Sausen'_
- **`ex_187`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren haben in EN einen anderen Inhalt als in DE (DE: zwei Ochsen ersetzen / gesamtes Vieh verlieren / sieben Jahre Verbannung; EN: 30 Schekel Strafe / doppelter Wert / fünf Widder als Schuldopfer).  
  ✏️ _EN-Distraktoren angleichen: 1 'The owner had to restore two oxen', 2 'The owner forfeited all his cattle', 3 'The owner was banished for seven years'._
- **`ex_189`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 nennt in DE und EN verschiedene Zahlen (DE: sechs Schafe; EN: three sheep).  
  ✏️ _Beide angleichen, z. B. EN 1: 'Six sheep as restitution'._
- **`ex_191`** · DE+EN · DE/EN weicht ab  
  Neben der vertauschten Lösung weichen auch die EN-Distraktoren inhaltlich von DE ab: DE 2 'drei Jahre in den Dienst des Vaters' vs. EN 2 'banished ... three years'; DE 3 'aus der Gemeinde ausgeschlossen' vs. EN 3 'offer a ram for a trespass offering'.  
  ✏️ _EN-Optionen an DE angleichen: 0 'He shall surely endow her to be his wife', 1 'He had to pay her father double silver', 2 'He had to serve her father three years', 3 'He was to be cut off from the congregation'._
- **`ex_192`** · DE+EN · DE/EN weicht ab  
  Die EN-Distraktoren 0 und 3 weichen von DE ab (DE 0 'sieben Jahre verbannt' vs. EN 'banished forever beyond the river'; DE 3 'am Heiligtum gereinigt' vs. EN 'secluded in her house').  
  ✏️ _EN 0: 'She was to be banished for seven years'; EN 3: 'She was to be cleansed at the sanctuary'._
- **`ex_193`** · DE+EN · DE/EN weicht ab  
  Die EN-Distraktoren 0, 1 und 3 haben einen anderen Inhalt als DE (DE: Ernteverlust / Absetzung der Richter / Aussatz; EN: Vieh und Weinberge / Dürre und Seuche / Namen ausgelöscht). Zudem nennt die DE-Frage auch die Fremdlinge. Die Drohung in V. 22-24 gilt aber nur für Witwen und Waisen; EN fragt hier richtig.  
  ✏️ _DE-Frage: 'Womit drohte Gott, falls Witwen und Waisen bedrückt würden?'; EN-Distraktoren an DE angleichen (loss of the yearly harvest / removal of all judges / an outbreak of leprosy)._
- **`ex_194`** · DE+EN · DE/EN weicht ab  
  Die EN-Distraktoren 0-2 weichen inhaltlich von DE ab (DE: nur Silber, kein Gold / Rückzahlung binnen drei Monaten / Bürge nötig; EN: zwei Älteste als Zeugen / höchstens dreißig Tage / kein Kleiderpfand).  
  ✏️ _EN-Distraktoren angleichen: 'Only silver and no gold might be lent' / 'The money had to be repaid within three months' / 'A surety had to be appointed'._
- **`ex_195`** · DE+EN · DE/EN weicht ab  
  Die EN-Distraktoren 1-3 haben einen anderen Inhalt als DE (DE: behalten / dem Priester zur Verwahrung geben / erst nach drei Tagen zurückgeben; EN: liegen lassen / in den eigenen Pferch treiben / dem Magistrat melden).  
  ✏️ _EN-Distraktoren angleichen: 'He might keep it for himself' / 'He was to give it to the priest for safekeeping' / 'He might return it only after three days'._
- **`ex_196`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 sind zwischen DE und EN vertauscht bzw. inhaltlich verschieden: DE 2 'an Fremdlinge verpachtet' vs. EN 2 'harvest given to the priests'; DE 3 'dem Heiligtum geschenkt' vs. EN 3 'leased to strangers'.  
  ✏️ _EN 2 = 'They were to be leased to strangers dwelling in the land', EN 3 = 'They were to be given to the sanctuary'._
- **`ex_197`** · DE+EN · DE/EN weicht ab  
  Die EN-Distraktoren 1 und 3 nennen andere Feste als DE (DE 1 'Freudenfest' vs. EN 'rejoicing of the law'; DE 3 'Erstlingsfest, Fastenfest, Neujahrsfest' vs. EN 'trumpets, fasting, year of jubilee').  
  ✏️ _EN 3: 'The feast of firstfruits, a feast of fasting, and the new year feast'; EN 1: 'The feast of sabbaths, circumcision, and a feast of joy'._
- **`ex_206`** · DE · Sprachfehler  
  Grammatikfehler bei der Adjektivendung.  
  ✏️ _"um die steinernen Tafeln zu empfangen"_
- **`ex_219`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 sind zwischen DE und EN vertauscht.  
  ✏️ _EN 1 und EN 2 tauschen._
- **`ex_220`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 nennen im EN andere Zahlen und Materialien als im DE.  
  ✏️ _EN angleichen: 0 "One single heavy socket of cast brass", 2 "Four sockets of silver at the corners of the wall", 3 "Six sockets of shittim wood overlaid with gold"._
- **`ex_221`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN angleichen: 0 "Palm branches and blossoming almonds", 1 "The twelve names of the tribes of Israel", 3 "The fiery tables of the law from Mount Sinai"._
- **`ex_222`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 stehen im DE und im EN in anderer Reihenfolge. Gleiche Indizes bezeichnen daher verschiedene Geräte.  
  ✏️ _EN-Reihenfolge an DE angleichen: 0 table of shewbread, 1 candlestick, 2 altar of incense._
- **`ex_223`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben im EN andere Maße als im DE.  
  ✏️ _EN 2: "..., two high"; EN 3: "Two hundred cubits long and an hundred cubits broad"._
- **`ex_224`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 stimmen zwischen DE und EN inhaltlich nicht überein.  
  ✏️ _EN angleichen: 0 "Of pure beaten gold", 2 "Of solid forged iron", 3 "Of shittim wood overlaid with silver"._
- **`ex_226`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 haben im EN einen anderen Inhalt bzw. eine andere Reihenfolge als im DE.  
  ✏️ _EN angleichen: 0 "Thick cloth of red and blue wool", 1 "Braided goats' hair from the flocks", 2 "Tanned leather of rams' skins"._
- **`ex_227`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN angleichen: 1 "Only of pure purple without linen", 2 "Of gold thread, silver thread and black wool", 3 "Of brown goats' hair and fine wool"._
- **`ex_239`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 hat im DE einen anderen Inhalt als im EN (Goldkette gegenüber Siegelring).  
  ✏️ _EN 1: "Putting a chain of pure gold about his neck"._
- **`ex_248`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 2 nennen im EN andere Zutaten als im DE (Myrrhe ↔ Weihrauch; Onycha fehlt im DE).  
  ✏️ _EN 0: "Olive oil, wild honey, beeswax, and myrrh"; EN 2: "Frankincense, stacte, galbanum, and salt water"._
- **`ex_256`** · DE+EN · Sprachfehler  
  Die DE-Frage fragt „Wie oft“ (Häufigkeit), die Optionen und die EN-Frage („When“) fragen aber nach dem Tag. Außerdem ist „laut der Zusage im Sabbatgebot“ unpassend: Der Vers ist eine Begründung, keine Zusage.  
  ✏️ _"An welchem Tag ruhte Gott nach dem Schöpfungswerk laut der Begründung des Sabbatgebots?"_
- **`ex_258`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN angleichen: 0 "Because the water in the camp had run out", 1 "Because they would no longer eat the manna", 2 "Because the Amalekites attacked the camp"._
- **`ex_260`** · DE · Inhaltlicher Fehler  
  Die DE-Frage sagt, das Volk habe das Kalb „am Altar“ erblickt. Der Ausruf fiel aber in V. 4, bevor Aaron in V. 5 den Altar baute. Die EN-Frage enthält diese Angabe nicht.  
  ✏️ _"Was rief das verführte Volk aus, als Aaron das gegossene Kalb gemacht hatte?"_
- **`ex_267`** · DE · Sprachfehler  
  Genusfehler: Erdbeben ist sächlich.  
  ✏️ _"Ein starkes Erdbeben erschütterte den Ort"_
- **`ex_283`** · DE+EN · DE/EN weicht ab  
  DE fragt nach den Gaben „zur Verschönerung der Heiligtumsgeräte“ (ein Zweck, den der Text nicht nennt). EN fragt nach den „golden gifts“. Die Distraktoren 1 bis 3 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _DE-Frage: "Welche goldenen Gaben brachten die willigen Männer und Frauen dem HERRN?". Die Distraktoren in beiden Sprachen angleichen._
- **`ex_284`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben im DE und im EN einen anderen Inhalt bzw. eine andere Reihenfolge.  
  ✏️ _EN angleichen: 0 "Only out of fear of punishment", 2 "A compulsory tax according to a table of laws", 3 "Compulsion by the elders of the tribes"._
- **`ex_285`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben im EN einen anderen Inhalt als im DE. EN 3 nennt mit „crimson, sky blue“ zudem teilweise richtige Farben.  
  ✏️ _EN angleichen: 0 "White, yellow, green, and dark black", 1 "Silver thread, gold thread, brown and grey", 3 "Plain linen without any dye"._
- **`ex_286`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN angleichen: 1 "Because Pharaoh forbade the export of more gold", 2 "Because Bezaleel laid down the work from overwork"._
- **`ex_288`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 3 haben im EN einen anderen Inhalt als im DE (unter anderem 15 Teppiche aus Widderfell gegenüber 7 Teppichen).  
  ✏️ _EN 3: "Fifteen curtains of red rams' skins"; EN 0: "Ten curtains of fine white linen"._
- **`ex_290`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 nennen im EN andere Maße als im DE. Außerdem fragt die DE-Frage nur „Wie lang“, obwohl die Optionen auch die Breite angeben.  
  ✏️ _DE-Frage: "Welche Maße hatte jedes Wandbrett?". EN-Distraktoren an DE angleichen._
- **`ex_298`** · DE+EN · DE/EN weicht ab  
  DE fragt „Wer“, Lösung: Bezaleel. EN fragt „How“, Lösung: „According to the work of the apothecary“, ohne Bezaleel zu nennen. Die EN-Distraktoren nennen dagegen Personen, was zur Wie-Frage nicht passt.  
  ✏️ _EN-Frage: "Who made the holy anointing oil and the pure incense?". EN 3: "Bezaleel, according to the work of the apothecary"._
- **`ex_299`** · DE · Sprachfehler  
  Falsche Präteritumform von „gießen“.  
  ✏️ _"Wie viele Ringe aus reinem Gold goss Bezaleel ..."_
- **`ex_314`** · DE+EN · Bibelstelle  
  Die markierte Lösung enthält „im zweiten Jahr“. Diese Angabe steht nicht in 2. Mose 40:2, sondern erst in 40:17.  
  ✏️ _bibleReference auf "2. Mose 40:2.17" bzw. "Exodus 40:2,17" erweitern._
- **`ex_317`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 1 sind zwischen DE und EN vertauscht.  
  ✏️ _EN 0 und EN 1 tauschen._
- **`ex_319`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN-Distraktoren an DE angleichen (oder umgekehrt)._
- **`ex_320`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN 2: "By the daily melting of the manna"; EN 3: "By the command of Joshua in the camp"._

</details>

<details>
<summary><b>03_3_mose.json</b> – 31 kleinere Befunde</summary>

- **`lev_002`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben im EN einen anderen Inhalt als im DE (unter anderem ist das dreijährige Tier einmal Distraktor 1 und einmal Distraktor 2).  
  ✏️ _EN angleichen: 1 "A young female breeding calf", 2 "A fatted beast of three years", 3 "A white firstborn calf"._
- **`lev_007`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN angleichen: 0 "It was burnt together with the flesh", 2 "It was buried in the court before the people", 3 "It was given to the poor of the camp"._
- **`lev_008`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 nennen im EN andere Zutaten als im DE.  
  ✏️ _EN-Distraktoren an DE angleichen (oder umgekehrt)._
- **`lev_010`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 stehen im DE und im EN in anderer Reihenfolge bzw. haben einen anderen Inhalt.  
  ✏️ _EN 1 und EN 2 tauschen; EN 3: "Unto the Levitical singers in the court"._
- **`lev_011`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 nennen im EN andere Stoffe als im DE.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`lev_012`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 nennen im EN andere Gewürze als im DE.  
  ✏️ _EN angleichen: 0 "Fragrant myrrh from the south", 1 "Sweet calamus from far countries", 3 "Ground cummin of the field"._
- **`lev_013`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 2 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN 0: "As finely ground white flour in a basket"; EN 2: "As unbaked grain bound in a sheaf"._
- **`lev_014`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`lev_015`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN 2: "Only mother beasts with their young"; EN 3: "Only firstborn males"._
- **`lev_016`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren haben im EN einen anderen Inhalt als im DE.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`lev_028`** · DE · Sprachfehler  
  Die DE-Frage fragt nach der 'Sünde', alle Optionen nennen aber Folgen bzw. Strafen. EN fragt korrekt nach der Konsequenz.  
  ✏️ _'Welche Folge hatte es, wenn jemand den Eidfluch hörte, aber als Zeuge schwieg?'_
- **`lev_059`** · EN · DE/EN weicht ab  
  EN fragt nur nach dem Tier für Aarons Sündopfer (Singular), die Lösung nennt aber zusätzlich den Widder zum Brandopfer. DE fragt korrekt nach Sünd- UND Brandopfer.  
  ✏️ _'What animals was Aaron commanded to take for his own sin offering and burnt offering?'_
- **`lev_064`** · DE · Sprachfehler  
  Rechtschreibfehler: 'Schachten' statt 'Schächten'.  
  ✏️ _'Sie verweigerten das Schächten des Widders'_
- **`lev_065`** · DE · Sprachfehler  
  Falsche Partizipform: 'befällt' statt 'befallen'.  
  ✏️ _'Sie wurden auf der Stelle vom Aussatz befallen'_
- **`lev_072`** · DE · Inhaltlicher Fehler  
  Die Frage spricht von 'landwirtschaftlichen Bestimmungen der Tora'. Es geht aber um Speisegesetze (rein/unrein), nicht um Landwirtschaft.  
  ✏️ _'Warum wurde das Schwein nach den Speisegesetzen als unrein erklärt?'_
- **`lev_084`** · DE · Mehrere richtig  
  Die angegebene Stelle umfasst V.5, nach dem der Priester bei unverändertem Befund abermals sieben Tage einschließt, insgesamt also 14 Tage. Der Distraktor 'Vierzehn Tage lang' kann deshalb als vertretbar gelten. Die Frage sollte ausdrücklich nach der ersten Einschließung fragen.  
  ✏️ _'Wie lange wurde ein Mann bei zweifelhaftem Aussatzverdacht zunächst (beim ersten Mal) eingeschlossen?' oder den Distraktor 'Vierzehn Tage' ersetzen, z. B. durch 'Zehn Tage lang'_
- **`lev_086`** · DE+EN · DE/EN weicht ab  
  Die drei Zeichen in der Lösung sind verschieden: DE nennt 'verhüllter Bart', EN statt der Lippenbedeckung den Ruf 'Unclean, unclean'. Zudem ist die EN-Frage grammatisch verunglückt ('What signs was the leper ... commanded to display').  
  ✏️ _EN-Frage: 'What signs was the leper in whom the plague is commanded to display?'; EN-Lösung: 'His clothes rent, his head bare, and a covering upon his upper lip'_
- **`lev_100`** · DE · Sprachfehler  
  Tippfehler: 'Viehstuhl' statt 'Viehstall'.  
  ✏️ _'Es durfte als Viehstall weitergenutzt werden'_
- **`lev_106`** · DE+EN · DE/EN weicht ab  
  DE fragt nach Tag und Bedingung, die Lösung lautet 'Einmal im Jahr am Versöhnungstag mit Rauchwerk'. EN fragt nur nach der Bedingung, die Lösung lautet 'Not at all times, but with a cloud of incense'. Die Lösungen sind inhaltlich nicht deckungsgleich. 'Einmal im Jahr' und das Räucherwerk stehen außerdem nicht in 16:2, sondern in 16:13 und 16:34.  
  ✏️ _bibleReference auf '3. Mose 16:2.13.34' erweitern oder die DE-Lösung an EN angleichen: 'Nicht zu jeder Zeit, sondern nur mit einer Räucherwolke über dem Sühnedeckel'_
- **`lev_137`** · DE · Sprachfehler  
  'fluchen' verlangt den Dativ: 'seinem Vater oder seiner Mutter fluchte', nicht den Akkusativ.  
  ✏️ _'Welche Strafe traf einen Sohn, der seinem Vater oder seiner Mutter fluchte?'_
- **`lev_155`** · DE+EN · DE/EN weicht ab  
  Distraktoren 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Angleichen, z. B. EN 2: "On the fifteenth day of the seventh month", EN 3: "On the last day of the month at the new moon"_
- **`lev_156`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren haben in DE und EN einen völlig anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE anpassen, z. B. "Oil of olives pressed with boiling", "Olive oil mingled with fine balm", "Oil of the first unripe olives of spring"_
- **`lev_157`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 sind zwischen DE und EN vertauscht (DE 1 = zehn, EN 1 = vierundzwanzig). Option 0 ist ebenfalls unterschiedlich ausgeschmückt.  
  ✏️ _Reihenfolge angleichen: EN 1 "Ten loaves according to the commandments", EN 2 "Twenty-four cakes for the priests"_
- **`lev_158`** · DE · Sprachfehler  
  Grammatikfehler im Distraktor 3.  
  ✏️ _"Er opferte ein unreines Tier am Altar"_
- **`lev_158`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE anpassen (Gold gestohlen / Sabbat gebrochen / unreines Tier geopfert)_
- **`lev_159`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE anpassen_
- **`lev_160`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt (andere Faktoren und Strafen).  
  ✏️ _EN: "Fivefold restitution for every damage", "Threefold payment unto the judge", "Lifelong bondage for the offender"_
- **`lev_161`** · DE · Sprachfehler  
  Grammatikfehler: Das Partizip lautet 'geerntet'.  
  ✏️ _"Es sollte doppelt besät und geerntet werden"_
- **`lev_161`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren haben in DE und EN einen völlig anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE anpassen (doppelt besät / an Fremde verpachtet / Ertrag gehört den Priestern)_
- **`lev_162`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE anpassen_
- **`lev_174`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN einen anderen Inhalt. Außerdem vermischt EN 1 die DE-Optionen 1 und 3.  
  ✏️ _EN 1: "It could be redeemed again after three years"; EN 3: "It could be redeemed for double the money"_

</details>

<details>
<summary><b>04_4_mose.json</b> – 35 kleinere Befunde</summary>

- **`num_001`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 nennt in DE und EN einen anderen Ort.  
  ✏️ _EN 3: "At Kadesh-barnea in the wilderness"_
- **`num_007`** · EN · DE/EN weicht ab  
  Der EN-Distraktor zu Gad nennt 45.600 statt der biblisch korrekten 45.650 (DE und KJV 1:25). Benjamin und Sebulon sind in EN nur gerundet angegeben.  
  ✏️ _EN 3: "The tribe of Gad numbering forty and five thousand six hundred and fifty"; EN 0/1 analog vollständig (35,400 / 57,400)_
- **`num_010`** · DE · Inhaltlicher Fehler  
  Distraktor 0 nennt Levi den 'erstgeborenen Stamm'. Das ist eine falsche Tatsachenbehauptung, denn der Erstgeborene war Ruben, und Ruben ist hier die richtige Antwort. Das führt den Spieler in die Irre. EN hat diese Angabe nicht.  
  ✏️ _DE 0: "Der Stamm Levi rings um das Zelt"_
- **`num_031`** · DE · Inhaltlicher Fehler  
  'Mahlopfer' bezeichnet üblicherweise das Friedens- bzw. Gemeinschaftsopfer. Das Eifersuchtsopfer ist aber ein Speisopfer (4. Mose 5:15.18).  
  ✏️ _"Woraus bestand das Speisopfer der Eifersucht, das ein Ehemann bei Verdacht darbrachte?"_
- **`num_034`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 nennt verschiedene Krankheiten: DE Blattern (Pocken), EN Aussatz.  
  ✏️ _DE 0: "Sie wurde augenblicklich vom Aussatz befallen" (oder EN an Blattern/boils anpassen)_
- **`num_035`** · DE+EN · DE/EN weicht ab  
  In Distraktor 0 ist die Richtung vertauscht: In DE zahlt die Frau dem Mann, in EN zahlt der Mann der Frau.  
  ✏️ _EN 0: "She had to pay a ransom unto her husband"_
- **`num_040`** · DE+EN · KJV-Wortlaut  
  Die richtige Option gibt den Aaronssegen als Zitat wieder, hängt aber einen Zusatz an, der nicht im Text steht: EN 'in all thy ways', DE 'in allen Dingen'.  
  ✏️ _EN: "The LORD bless thee, and keep thee"; DE: "Der HERR segne dich und behüte dich"_
- **`num_048`** · DE · Sprachfehler  
  Grammatikfehler bei der Adjektivflexion.  
  ✏️ _"Die reicheren Stämme brachten doppelt so viele Tiere"_
- **`num_054`** · DE · Sprachfehler  
  'Wessen' ist mitten im Satz fälschlich großgeschrieben. Es bezieht sich nicht auf Gott.  
  ✏️ _"An wessen Stelle nahm Gott den Stamm Levi aus der Mitte der Kinder Israels an?"_
- **`num_067`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 hat in DE und EN einen anderen Inhalt: Verwirrung vs. Blindheit.  
  ✏️ _EN 0: "The enemy hosts would instantly be smitten with confusion"_
- **`num_077`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 hat in DE und EN einen anderen Inhalt: Wasser vs. Staub.  
  ✏️ _Angleichen, z. B. DE 2: "Das übrige Fleisch verwandelte sich in bitteren Wüstenstaub"_
- **`num_086`** · DE+EN · Inhaltlicher Fehler  
  Die Frage nennt schon den Stamm Ephraim. Nur die richtige Option enthält Ephraim, die Distraktoren nennen Juda, Ruben und Ascher. Damit verrät die Frage die Antwort.  
  ✏️ _"Welchem Kundschafter gab Mose vor der Aussendung den Namen Josua?" (EN: "Which of the spies did Moses rename Jehoshua?")_
- **`num_090`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 2: "That the rivers were poisoned by enemies"; EN 3: "That there were neither vines nor fig trees"_
- **`num_099`** · DE · Inhaltlicher Fehler  
  Laut Text zogen die Israeliten auf die Höhe des Gebirges und wurden von dort bis Horma verfolgt. Sie rückten nicht 'nach Horma vor'. Die richtige Option nennt außerdem nur die Amalekiter, der Text nennt Amalekiter und Kanaaniter (so auch EN).  
  ✏️ _Frage: "Was widerfuhr den Israeliten, die trotz Moses Warnung eigenmächtig auf die Höhe des Gebirges zogen?"; Antwort: "Sie wurden von den Amalekitern und Kanaanitern geschlagen und bis Horma verfolgt"_
- **`num_100`** · DE+EN · DE/EN weicht ab  
  Die DE-Frage ist sehr allgemein ('Was sollte Israel darbringen ...'). Dabei wäre auch ein Brandopfer (Distraktor 2) eine Darbringung. Die EN-Frage fragt präzise nach dem begleitenden Opfer zu jedem Brand- oder Schlachtopfer.  
  ✏️ _DE: "Was sollte im Land Kanaan zu jedem Brand- oder Schlachtopfer zusätzlich dargebracht werden?"_
- **`num_105`** · DE · Sprachfehler  
  Distraktor 1 schreibt „Silber blech“ getrennt, richtig ist das zusammengesetzte Wort „Silberblech“.  
  ✏️ _„Kleine Schalen aus geprägtem Silberblech“_
- **`num_106`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 nennt in DE „zweihundert Männer“, in EN „two hundred and fifty companions“.  
  ✏️ _Angleichen, z. B. DE 3: „Nadab und Abihu mit zweihundertfünfzig Männern“_
- **`num_108`** · DE+EN · Inhaltlicher Fehler  
  Laut Frage ließ Mose Dathan und Abiram „vor das Zelt“ (EN: „to the tabernacle“) rufen. Der Text sagt nur, dass Mose sie rufen ließ, ein Zelt wird nicht erwähnt. Außerdem weicht Distraktor 2 ab: DE „baten das gesamte Volk um Beistand“, EN „appealed to the princes of the camp for armed help“.  
  ✏️ _DE: „Was antworteten Dathan und Abiram, als Mose sie rufen ließ?“; EN: „…when Moses sent to call them?“; EN 2: „They besought all the people for help“_
- **`num_116`** · EN · KJV-Wortlaut  
  Die EN-Lösung zitiert 17:12 wörtlich, hängt aber „before the LORD“ an. Das steht nicht in der KJV.  
  ✏️ _EN 3: „Behold, we die, we perish, we all perish.“_
- **`num_124`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren weichen inhaltlich voneinander ab. Am deutlichsten bei Option 2: DE nennt fünfzig Festungsstädte, EN einen doppelten Anteil aus Juda. Auch die Optionen 0 und 1 sind vertauscht bzw. abgewandelt (DE 0: Ackerland in Juda, EN 0: Weideland im Süden Judas; DE 1: Weideland am Jordan, EN 1: Festungsstädte am Jordan).  
  ✏️ _EN 2: „Fifty fenced cities with their suburbs“ (und EN 0/1 entsprechend der DE-Fassung angleichen)_
- **`num_134`** · DE · Sprachfehler  
  Distraktor 2 enthält das sinnlose Wort „Aussatzerwählung“. Gemeint ist, dass Mirjam in Hazeroth mit Aussatz geschlagen wurde (EN: „where she had been smitten with leprosy“).  
  ✏️ _„In Hazeroth, wo sie mit Aussatz geschlagen wurde“_
- **`num_139`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN völlig verschiedene Inhalte (DE 0: Wegezoll vom Silber, EN 0: Geschenke aus Getreide; DE 1: öffnete die Brunnen, EN 1: doppelte Bezahlung für Wasser; DE 3: Friedensbund, EN 3: nur Priester und Älteste durften durchziehen). Außerdem gibt die DE-Lösung die Antwort aus Vers 18 wieder, die EN-Lösung dagegen Vers 20.  
  ✏️ _Die Distraktoren angleichen, z. B. EN 0: „He demanded half of the captured silver as toll“, EN 1: „He opened the wells and kindly showed them the way“, EN 3: „He made an everlasting covenant of peace with Moses at the border“_
- **`num_141`** · DE · Sprachfehler  
  Distraktor 2 enthält „in Sakk“. Das ist ein Tippfehler, gemeint ist „im Sack“ bzw. „in Sacktuch“ (EN: „in sackcloth“).  
  ✏️ _„Sieben Tage im Sacktuch vor der Lade zu fasten“_
- **`num_145`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 bedeutet in DE und EN etwas anderes: DE „Kauf von Wasser und Getreide“, EN „das Lager um die Wasserquellen aufschlagen“.  
  ✏️ _EN 2: „A request to buy water and corn along the way“_
- **`num_155`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 hat in DE und EN einen anderen Inhalt: DE „Balak werde ein Bündnis mit Israel schließen“, EN „Balak plane heimlich, ihn zu vernichten“.  
  ✏️ _EN 1: „That Balak would make a league with Israel“_
- **`num_168`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 hat in DE und EN einen anderen Inhalt: DE „ein viertes Opfer“, EN „eine achte Reihe von Altären“.  
  ✏️ _EN 1: „He besought Balaam to offer a fourth time“_
- **`num_178`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 nennt in DE eine andere Zahl als in EN: DE 600.350, EN 603.550 (das ist die Zahl der ersten Zählung).  
  ✏️ _Angleichen, z. B. EN 0: „Six hundred thousand and three hundred and fifty“_
- **`num_187`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 nennt in DE den Berg Hermon, in EN den Berg Karmel.  
  ✏️ _EN 3: „Unto Mount Hermon in the north“_
- **`num_202`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 nennen in DE und EN verschiedene Zahlen: DE fünf bzw. zehn Farren, EN drei bzw. zwölf.  
  ✏️ _EN 2: „Exactly five bullocks for the princes of the tribes“; EN 3: „Exactly ten bullocks according to the law“_
- **`num_227`** · DE+EN · DE/EN weicht ab  
  Die EN-Distraktoren 0, 1 und 3 haben einen anderen Inhalt als die DE-Optionen mit gleichem Index. DE: Tribut, Hungersnot, Raub der Bundeslade. EN: treue Knechte, Verbündete, leichte Beute für Nomaden.  
  ✏️ _Die EN-Optionen an DE angleichen, z. B. 0: 'The enemies would lay heavy tribute upon them', 1: 'A grievous famine would come upon the land', 3: 'The ark of the covenant would be taken by enemies'._
- **`num_231`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren weichen ab. DE 0: Kaleb/Pinhas, DE 1: Mose/Aaron, DE 3: Fürsten von Juda und Benjamin. EN 0: Moses/Joshua, EN 1: Caleb/Phinehas, EN 3: Ithamar/Hobab.  
  ✏️ _EN-Optionen 0, 1 und 3 an DE angleichen: 0 'Caleb ... and Phinehas the priest', 1 'Moses the prophet and Aaron the high priest', 3 'The two princes of the tribes of Judah and Benjamin'._
- **`num_232`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind verschoben bzw. inhaltlich anders. DE: 0 Leviten mit der Lade, 1 siebzig Älteste, 2 Hauptleute. EN: 0 siebzig Älteste, 1 Hauptleute, 2 levitische Schreiber.  
  ✏️ _Die EN-Reihenfolge an DE angleichen: 0 'The Levites that bare the ark', 1 'The seventy elders', 2 'The captains over thousands'._
- **`num_236`** · DE · Sprachfehler  
  Rechtschreibfehler: 'Levitienstädte' statt 'Levitenstädte'.  
  ✏️ _'Wie viele der achtundvierzig Levitenstädte mussten als Freistädte dienen?'_
- **`num_241`** · DE+EN · DE/EN weicht ab  
  Die EN-Distraktoren 1 bis 3 haben einen anderen Inhalt als DE. DE: zu viele Levitenstädte, zu wenig Weideland, Kanaaniter räumen die Festungen nicht. EN: Verkauf an Fremde, Zehnten, Abwanderung. Auch die Fragen setzen unterschiedliche Schwerpunkte: Land (DE) gegenüber den Töchtern (EN).  
  ✏️ _Die EN-Optionen 1 bis 3 an DE angleichen, z. B. 1 'That the Levites claimed too many of their cities', 2 'That they had too little pasture for their cattle', 3 'That the Canaanites refused to leave their strongholds'._
- **`num_242`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 weicht ab: DE sagt, sie mussten an ihre nächsten Brüder verkaufen, EN 'to their cousins'. 'Cousins' liegt zudem nahe an der tatsächlichen Heirat mit den Vettern (V. 11) und kann verwirren.  
  ✏️ _EN-Option 3: 'They had to sell their inheritance unto their nearest brethren'_

</details>

<details>
<summary><b>05_5_mose.json</b> – 27 kleinere Befunde</summary>

- **`dtn_003`** · DE+EN · Sprachfehler  
  Die DE-Lösung 'Dass er die Mühe und Streitigkeiten nicht allein trug' heißt wörtlich, er habe sie nicht allein getragen. Gemeint ist aber, dass er sie nicht allein tragen KONNTE. Außerdem nennt DE-Option 1 Gold, EN-Option 1 Silber.  
  ✏️ _DE-Option 3: 'Dass er die Last und die Streitigkeiten nicht allein tragen konnte'; EN-Option 1 'gold' bzw. DE 'Silber' angleichen._
- **`dtn_014`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 weicht ab: DE nennt die Armen der Moabiter, EN 'poor wanderers of the desert'.  
  ✏️ _EN-Option 1: 'The spoil was left unto the poor of the Moabites'_
- **`dtn_027`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren unterscheiden sich inhaltlich. DE: Knechtschaft in Ägypten, Stiftshütte verbrannt, siebenjährige Dürre. EN: drei Jahre kein Regen, Stiftshütte ins Meer geworfen, Seuche über Priester und Älteste.  
  ✏️ _Die EN-Distraktoren an DE angleichen (0 'They would again be bondmen unto Pharaoh in Egypt', 1 'The tabernacle would be burnt by enemies', 2 'A seven-year drought would dry up all wells')._
- **`dtn_031`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 weicht ab: DE nennt das Gebot, den Leviten den Zehnten zu geben, EN die Ruhe für die dienenden Leviten.  
  ✏️ _EN-Option 1: 'The commandment to give the tithe unto the Levites'_
- **`dtn_036`** · DE · Sprachfehler  
  Das Adjektiv 'Bekannten' ist fälschlich großgeschrieben, dadurch wird der Satz holprig bzw. missverständlich.  
  ✏️ _'Welches grundlegende Bekenntnis richtete Mose mit dem bekannten „Höre, Israel“ an das Volk?'_
- **`dtn_039`** · DE · Sprachfehler  
  Grammatikfehler in DE-Option 0: 'in den Tälern Kanaanitern'.  
  ✏️ _'Vor den Giftnattern in den Tälern Kanaans'_
- **`dtn_041`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben verschiedenen Inhalt. DE 2: Richter und Älteste haben die Gebote beschlossen; EN 2: Nur Priester dürfen das Gesetz verstehen. DE 3: Priester am Horeb haben sie erfunden; EN 3: Das Halten der Gebote garantiert Reichtum.  
  ✏️ _Die EN-Optionen 2 und 3 an DE angleichen: 2 'That the judges and elders once decreed these statutes', 3 'That the priests at Horeb devised them for the service'._
- **`dtn_066`** · DE · Sprachfehler  
  Falscher Kasus in DE-Option 3: 'schrieben auf den Berg' statt 'auf dem Berg'.  
  ✏️ _'Die siebzig Ältesten schrieben sie auf dem Berg'_
- **`dtn_070`** · EN · KJV-Wortlaut  
  Die EN-Lösung ist als KJV-Zitat formuliert, fügt aber 'and knew their affliction' hinzu, was in 5. Mose 10:19 nicht steht. Außerdem weicht EN-Option 3 von DE-Option 3 ab: Fremde führten Mose durch die Wüste bzw. Fremde führten Israel aus Ägypten.  
  ✏️ _EN-Option 2: 'For ye were strangers in the land of Egypt'_
- **`dtn_074`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 unterscheiden sich inhaltlich. DE: ewiger Tau, Quellwasser aus der Tiefe, Frühlingsschauer an jedem Sabbat. EN: Sommertau und Winterfluten, Talschauer und Gewitter, Frost und Wüstenquellen.  
  ✏️ _Die EN-Distraktoren an DE angleichen (0 'An everlasting dew watering the harvest every night', 1 'Spring water flowing from the deep without clouds', 3 'Gentle spring showers upon every sabbath of the year')._
- **`dtn_082`** · DE+EN · Inhaltlicher Fehler  
  Die DE-Frage behauptet, das Blut sei laut Tora 'ausdrücklich heilig', das sagt 5. Mose 12:23 nicht. Der Vers verbietet das Bluttrinken, weil das Blut die Seele/das Leben ist. Die EN-Frage fragt korrekt nach dem Grund des Verbots. Die beiden Fragen weichen also voneinander ab.  
  ✏️ _DE-Frage: 'Warum durfte das Blut eines Tieres nach dem Gesetz nicht gegessen werden?'_
- **`dtn_091`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 hat einen anderen Inhalt: DE nennt die Erlaubnis des Königs von Moab, EN die Erlaubnis der Ältesten des Nachbarstammes.  
  ✏️ _EN-Option 2: 'Obtain permission from the king of Moab'_
- **`dtn_101`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN völlig anderen Inhalt. Beispiel Index 0: DE "Knecht nach drei Jahren freigelassen", EN "impoverished should become priests". Index 2: DE "Zinsen halbiert", EN "additional inheritance of land". Außerdem steht "guten" (Erdlande) nicht im Text.  
  ✏️ _Die EN-Distraktoren an DE angleichen, z. B. EN 0: "That every bondservant should be released after three years", EN 2: "That the usury on lent silver should be halved", EN 3: "That all tithes should go to the widows alone". DE-Lösung: "Es soll gar kein Armer unter dir sein im Lande"._
- **`dtn_102`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 sagt in DE und EN Gegensätzliches: DE "Saatgut vergeuden", EN "Hoarding the seed corn" (horten). Distraktor 3 nennt in DE heimliches Essen der Gartenfrüchte, in EN Ernten ohne Verzehnten.  
  ✏️ _EN 1: "Wasting the seed corn of the fields during the fallow year"; EN 3: "Secretly eating the fruits of his own garden"_
- **`dtn_113`** · DE · Sprachfehler  
  Die DE-Lösung ist grammatisch kaputt ("Ein Blinder, lahmender oder fehlerhafter Zustand"). "Blind" und "lahm" stehen außerdem nicht in 17:1, sondern in 15:21. Die EN-Lösung gibt korrekt "blemish/evilfavouredness" wieder.  
  ✏️ _"Irgendein Mangel oder sonst etwas Böses an dem Tier"_
- **`dtn_116`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 hat einen anderen Inhalt: DE nennt die Grenze des Nachbarstammes, EN den Heerführer an der Grenze. Distraktor 3 nennt in DE nur Moab, in EN "Moab or Edom".  
  ✏️ _EN 1: "Unto the border of the neighbouring tribe"; EN 3: "Unto the king of Moab for judgment"_
- **`dtn_123`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 hat einen anderen Inhalt: DE "Verweigern des Namens am achten Tag", EN "Refusing to circumcise". Auch Distraktor 0 weicht ab: DE "Tätowieren", EN "Inscribing… upon the foreheads".  
  ✏️ _DE 2: "Das Verweigern der Beschneidung am achten Tag" (oder EN entsprechend auf die Namensgebung ändern)_
- **`dtn_126`** · EN · KJV-Wortlaut  
  Die EN-Lösung ist ein verstümmeltes KJV-Zitat: "that hath not been spoken" ergibt keinen sinnvollen Satz und weicht vom KJV ab.  
  ✏️ _"If the thing follow not, nor come to pass, that is the thing which the LORD hath not spoken"_
- **`dtn_127`** · DE · Sprachfehler  
  Distraktor 2 enthält das Unwort "Wasserbrände". Die EN-Fassung hat "water trenches" (Wassergräben).  
  ✏️ _"Wassergräben entlang der Grenzen anlegen"_
- **`dtn_138`** · DE · Inhaltlicher Fehler  
  Die DE-Frage spricht von den "sieben" Völkern. Die angegebene Stelle 20:17 zählt aber nur sechs Völker auf; die sieben Völker stehen in 5. Mose 7:1. Außerdem ist "der sieben heidnischen Völker Kanaaniter" grammatisch falsch.  
  ✏️ _"Welches unerbittliche Gebot galt für die Städte der Völker Kanaans, die Gott Israel zum Erbe gab?"_
- **`dtn_139`** · DE · Sprachfehler  
  Grammatisch falsche Fügung "der heidnischen Völker Kanaaniter".  
  ✏️ _"…die vollkommene Ausrottung der heidnischen Völker Kanaans"_
- **`dtn_147`** · DE · Sprachfehler  
  Das Adjektiv "Nächstgelegenen" ist fälschlich großgeschrieben.  
  ✏️ _"Was taten die Ältesten der nächstgelegenen Stadt zum Zeichen ihrer Schuldlosigkeit?"_
- **`dtn_161`** · EN · KJV-Wortlaut  
  Das KJV-Zitat ist grammatisch falsch verkürzt: "at thine pleasure" statt "at thine own pleasure".  
  ✏️ _"Thou mayest eat grapes thy fill at thine own pleasure; but thou shalt not put any in thy vessel"_
- **`dtn_181`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat einen anderen Inhalt: DE "immerwährender Frieden / Israel gelobte Opfer", EN "perpetual victory in battle / Israel vowed to conquer Canaan". Distraktor 2 hat in DE "Reichtum", in EN "boundless gold" (unkritisch).  
  ✏️ _EN 3: "God promised Israel perpetual peace, and Israel vowed sacrifices"_
- **`dtn_194`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 weichen inhaltlich ab: DE 1 "Gedächtnis auslöschen", EN 1 "forget the language of thy fathers"; DE 3 "Fürsten blinde Augen", EN 3 "magistrates… delusions of peace". DE 3 kommt mit "blinde Augen" zudem der richtigen Antwort (Blindheit) gefährlich nahe.  
  ✏️ _DE 3: "Gott wird deine Fürsten mit trügerischem Friedenswahn täuschen" (passend zu EN); DE 1: "Gott lässt dich die Sprache deiner Väter vergessen"_
- **`dtn_229`** · DE+EN · DE/EN weicht ab  
  DE fragt nach Metall für „Riegel an den Toren“, EN dagegen nach Metall für „shoes“. Der hinterlegte DE-Text hat „Schuhwerk“, nicht „Riegel“. Frage und Lösung passen in DE also weder zum Grundtext noch zu EN. Außerdem steht in Distraktor 2 der Tippfehler „Ophis“ statt „Ophirs“.  
  ✏️ _DE: „Welche Metalle werden Asser im Segen Moses für sein Schuhwerk verheißen?“ – richtige Option: „Eisen und Erz (Kupfer) sei dein Schuhwerk“. Distraktor 2: „Pures Gold aus den Schätzen Ophirs“_
- **`dtn_230`** · DE+EN · Inhaltlicher Fehler  
  Der Segen Moses schließt nicht mit 33,27, sondern mit 33,29 („Wohl dir, Israel! ...“). Die Formulierung „schließt der Segen“ ist deshalb ungenau.  
  ✏️ _DE: „Welche trostreichen Worte über den ewigen Gott finden sich gegen Ende des Segens Moses?“ / EN: „What comforting words concerning the eternal God are found near the end of the blessing of Moses?“_

</details>

<details>
<summary><b>06_josua.json</b> – 11 kleinere Befunde</summary>

- **`jos_002`** · DE · Sprachfehler  
  In DE-Option 1 steht am Ende das überflüssige Wort „her“, der Satz ist dadurch grammatisch falsch.  
  ✏️ _„Das Ausrüsten des Heeres mit eisernen Rüstungen“_
- **`jos_008`** · DE · Sprachfehler  
  In DE-Option 3 steht am Ende das überflüssige Wort „her“.  
  ✏️ _„Vier Männer aus dem Stamm Ephraim“_
- **`jos_015`** · DE+EN · Inhaltlicher Fehler  
  Nach 3,1–3 zog das Volk zuerst von Sittim an den Jordan und lagerte dort drei Tage. Die Lade zog erst beim Aufbruch vom Lager am Jordan voran, nicht beim Aufbruch von Sittim.  
  ✏️ _DE: „Was zog dem Volk Israel beim Aufbruch vom Lager am Jordan voran?“ / EN: „What went before the people when they removed from their camp at Jordan?“_
- **`jos_059`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN verschiedenen Inhalt: DE „als das Land unter den Stämmen verteilt wurde“ (dieselbe Begründung wie in DE-Option 2), EN „when the tabernacle was set up in Shiloh“.  
  ✏️ _DE 3: „Nach vierzig Tagen, als die Stiftshütte in Silo aufgerichtet wurde“_
- **`jos_067`** · DE+EN · DE/EN weicht ab  
  Die richtige Option lokalisiert Makkeda unterschiedlich: DE „im Gebirge“, EN „in the lowlands“. Makkeda lag in der Niederung (Josua 15,33.41), die DE-Angabe ist also sachlich falsch. Der Bibeltext enthält die Ortsangabe gar nicht.  
  ✏️ _DE: „In der Höhle zu Makkeda“ / EN: „In a cave at Makkedah“ (Zusatz in beiden Sprachen streichen)_
- **`jos_077`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 hat in DE und EN verschiedenen Inhalt: DE Rückkehr nach Ägypten, EN Rückkehr über den Fluss.  
  ✏️ _EN 0: "The tribes returned again into Egypt"_
- **`jos_082`** · EN · KJV-Wortlaut  
  Die richtige EN-Option ist ein verstümmeltes KJV-Zitat: „The river Arnon, which is in the midst of the river“ ergibt keinen Sinn. Im KJV gehört „upon the bank of“ zu Aroer und „from the middle of the river“ ist eine eigene Angabe.  
  ✏️ _EN 3: "The river Arnon, upon whose bank Aroer lieth"_
- **`jos_102`** · DE · Inhaltlicher Fehler  
  Durch den Genitiv „des Bruders Kalebs“ wird Kenas zum Bruder Kalebs. Im hinterlegten Text (und in Ri 1,13 „Kalebs jüngerer Bruder“) ist Othniel der Bruder Kalebs (Nominativ).  
  ✏️ _"Othniel, der Sohn des Kenas, der Bruder Kalebs"_
- **`jos_115`** · EN · DE/EN weicht ab  
  Die Distraktoren haben in DE und EN eine andere Reihenfolge und einen anderen Inhalt pro Index: DE 1 Hebron, 2 Silo, 3 Bethel; EN 1 Bethel, 2 Shiloh, 3 Kirjath-arba (= Hebron).  
  ✏️ _EN 1: "The fortress city Kirjath-arba (Hebron) in the south"; EN 3: "The border city Bethel among the hills"._
- **`jos_121`** · EN · DE/EN weicht ab  
  Die EN-Distraktoren haben einen anderen Inhalt als die DE-Optionen mit gleichem Index: DE 1 = dreißig Städte, EN 1 = siebzig; DE 3 = siebzig Städte, EN 3 = vierundzwanzig.  
  ✏️ _EN 1: "Thirty cities throughout all the land"; EN 3: "Seventy cities after the number of the elders" (oder DE an EN angleichen)._
- **`jos_130`** · DE+EN · Sprachfehler  
  „Welcher Vater Abrahams“ setzt mehrere Väter Abrahams voraus. Die Frage enthält außerdem die Lösung schon („der Vater Abrahams“) und passt nicht zu den Distraktoren (Isaak, Jakob, Lot sind keine Väter Abrahams).  
  ✏️ _DE: "Welcher Vorfahr Israels wohnte nach Josuas Rede vorzeiten jenseit des Stroms und diente andern Göttern?" EN: "Which of Israel's fathers dwelt on the other side of the flood in old time and served other gods?"_

</details>

<details>
<summary><b>07_richter.json</b> – 12 kleinere Befunde</summary>

- **`ri_012`** · EN · DE/EN weicht ab  
  DE fragt nach der Anzahl der Philisterfürsten („Wie viele“), EN fragt, welche Herrscher übrig blieben. Die EN-Frage enthält außerdem die Angabe „in the south“, die nicht im Text steht.  
  ✏️ _EN: "How many lords of the Philistines were left in the land to prove Israel?"_
- **`ri_014`** · EN · DE/EN weicht ab  
  Die EN-Distraktoren haben an Index 1 und 2 einen anderen Inhalt als DE: DE 1 = Ehud, DE 2 = Schamgar; EN 1 = Shamgar, EN 2 = Barak.  
  ✏️ _EN 1: "Ehud the son of Gera with the two-edged dagger"; EN 2: "Shamgar the son of Anath with the ox goad"._
- **`ri_031`** · DE · Sprachfehler  
  In den DE-Distraktoren steht ein Rechtschreib- bzw. Füllwortfehler: „Kupfer erz“ ist getrennt geschrieben, das „her“ am Satzende ist sinnlos.  
  ✏️ _DE 2: "Die Schwerter waren alle aus weichem Kupfer"; DE 3: "Es fehlte an Bögen und Köchern für den Kampf"_
- **`ri_036`** · DE · Inhaltlicher Fehler  
  Die DE-Lösung verlegt Gideons Dreschen „unter die Eiche“. Laut Text saß aber der Engel unter der Eiche, Gideon drosch in der Kelter. Die EN-Option sagt korrekt nur „By the winepress in Ophrah“.  
  ✏️ _"In der Kelter zu Ophra"_
- **`ri_043`** · DE+EN · Inhaltlicher Fehler  
  Die Lösung ordnet den Brunnen Harod einem Hügel/Gebirge zu. Laut Text bezieht sich „der Hügel More“ auf die Lage des Midianiterheeres, nicht auf den Brunnen.  
  ✏️ _DE: "Am Brunnen Harod"; EN: "Beside the well of Harod"_
- **`ri_056`** · EN · DE/EN weicht ab  
  Die EN-Distraktoren haben einen anderen Inhalt als DE mit gleichem Index: DE 0 = zwölf Söhne, EN 0 = vierzig Söhne und dreißig Neffen; DE 1 = dreißig Söhne auf Eselsfüllen, EN 1 = zwölf Söhne; DE 3 = zweiundsiebzig Söhne, EN 3 = dreißig Söhne als Hauptleute.  
  ✏️ _EN 0: "Twelve sons, after the number of the tribes"; EN 1: "Thirty sons that rode on ass colts"; EN 3: "Seventy and two sons in his house"._
- **`ri_058`** · EN · DE/EN weicht ab  
  Die EN-Distraktoren haben einen anderen Inhalt als DE (DE 1 Tola, 2 Jephta, 3 Gaal; EN 1 Jether, 2 Gaal, 3 Zebul). Die EN-Frage verrät außerdem schon die Lösung („youngest son“) und fragt zusätzlich nach dem Gleichnis auf dem Garizim, das in der Stelle 9:5 nicht vorkommt.  
  ✏️ _EN: "Which only son of Jerubbaal escaped the slaughter of Abimelech in Ophrah?" 1: "Tola, the later judge in Shamir", 2: "Jephthah, the mighty man of Tob", 3: "Gaal the son of Ebed in Shechem"._
- **`ri_081, ri_082, ri_086, ri_087, ri_088, ri_089, ri_090, ri_091, ri_092, ri_093, ri_094, ri_096, ri_097, ri_104, ri_105, ri_107, ri_108, ri_133, ri_136`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren in EN haben bei gleichem Index einen anderen Inhalt als in DE. Teils sind es völlig andere Falschantworten, bei ri_133 sind sie umsortiert. Die richtige Lösung (Index und Inhalt) stimmt jeweils überein. Die Fassungen sind aber keine Übersetzungen voneinander.  
  ✏️ _Die EN-Distraktoren indexgleich an die DE-Distraktoren angleichen (oder umgekehrt), z. B. ri_086 EN 1: 'In the heathen coastal city of Ashkelon'; ri_133 EN-Reihenfolge an DE anpassen._
- **`ri_094`** · DE · Inhaltlicher Fehler  
  Die DE-Frage verengt den Schaden auf die 'gesamte Olivenernte'. Laut Text verbrannten Garben, stehendes Korn, Weinberge und Ölbäume. EN spricht korrekt allgemein von 'harvest'.  
  ✏️ _'Wie reagierten die erzürnten Philister auf die Verbrennung ihres Korns, ihrer Weinberge und Ölbäume?'_
- **`ri_111, ri_116, ri_118`** · DE · Sprachfehler  
  An einige DE-Distraktoren sind sinnlose Füllwörter angehängt ('da', 'her'), offenbar um die Länge auszugleichen.  
  ✏️ _Füllwörter streichen: 'An einem Brandmal an seiner rechten Hand'; 'Sie nannten sie Gilgal zur Erinnerung'; 'Aus der Stadt Sichem im Gebirge Ephraim'_
- **`ri_132`** · DE · Sprachfehler  
  Die Lösungsoption ist grammatisch verunglückt: 'flohen ... vier Monate' (gemeint ist: blieben dort vier Monate).  
  ✏️ _'Sie flohen zum Fels Rimmon in der Wüste und blieben dort vier Monate'_
- **`ri_140`** · DE+EN · Bibelstelle  
  Die Ordering-Frage betrifft fünf Richter (Othniel, Ehud, Debora, Gideon, Simson). Die Bibelstelle Richter 3:9 belegt aber nur Othniel. Die Reihenfolge selbst (correctAnswers [4,3,1,0,2]) ist korrekt.  
  ✏️ _bibleReference auf 'Richter 3–16' setzen (bzw. 'Judges 3–16')._

</details>

<details>
<summary><b>08_rut.json</b> – 2 kleinere Befunde</summary>

- **`rut_002, rut_013, rut_019`** · EN · Sprachfehler  
  In EN-Optionen fehlen Artikel bzw. Wörter. Die Sätze sind dadurch fehlerhaft, vermutlich um die Länge anzugleichen.  
  ✏️ _'From the tabernacle city of Shiloh'; 'over the land of Canaan'; 'in the tribe of Judah'; 'sole heir of all the house of Elimelech'_
- **`rut_025`** · EN · Sprachfehler  
  Ein abgeschnittenes Wort im EN-Distraktor ('thresh' statt 'threshold').  
  ✏️ _'They poured a full measure of barley upon the threshold of the gate'_

</details>

<details>
<summary><b>09_1_samuel.json</b> – 8 kleinere Befunde</summary>

- **`1sam_002`** · EN · KJV-Wortlaut  
  Die EN-Lösung zitiert die KJV, lässt aber das 'his' weg. Dadurch ist der Satz unvollständig.  
  ✏️ _'To give him unto the LORD all the days of his life'_
- **`1sam_005, 1sam_006, 1sam_007, 1sam_008, 1sam_009, 1sam_011, 1sam_012, 1sam_013, 1sam_014, 1sam_015, 1sam_016, 1sam_017, 1sam_018, 1sam_020, 1sam_022, 1sam_023, 1sam_024, 1sam_025`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren in EN haben bei gleichem Index einen anderen Inhalt als in DE, bei 1sam_008 sind sie zusätzlich umsortiert. Die richtige Lösung stimmt jeweils überein.  
  ✏️ _Die EN-Distraktoren indexgleich an DE angleichen, z. B. 1sam_008 EN: 1 'Twice ...', 2 'Four times ...', 3 'Seven times ...'._
- **`1sam_015`** · DE · Sprachfehler  
  Falsche deutsche Zahlbildung in einem Distraktor.  
  ✏️ _'Genau fünfundsiebzig Jahre alt im Heiligtum'_
- **`1sam_026`** · DE · Inhaltlicher Fehler  
  Die DE-Frage stellt die 20 Jahre als gesamte Verweildauer der Lade im Haus Abinadabs dar. Laut 7:2 waren es 20 Jahre, bis Israel dem HERRN nachklagte. Danach blieb die Lade noch bis zu Davids Zeit dort (2. Sam 6). EN formuliert das korrekt ("while all Israel lamented").  
  ✏️ _"Wie viele Jahre waren vergangen, seit die Lade in Kirjath-Jearim blieb, als das ganze Haus Israel dem HERRN nachklagte?"_
- **`1sam_051`** · EN · Sprachfehler  
  Gekürzte KJV-Zitate in den EN-Lösungen sind durch fehlende Artikel bzw. Verben ungrammatisch. Das gleiche Muster steht auch in 1sam_048 [0] "LORD sought a man" und 1sam_049 [1] "Philistines said: Lest Hebrews make...". Ähnlich bei Distraktoren wie 1sam_056 [3] "offering Gilgal", 1sam_057 [3] "mountain king Jerusalem" und 1sam_054 [0] "priests Nob".  
  ✏️ _"If they say thus, Come up unto us; for the LORD hath delivered them into our hand" (und analog: "the LORD hath sought him a man", "as an offering at Gilgal", "the king of Jerusalem", "the priests of Nob")_
- **`1sam_070`** · DE · Inhaltlicher Fehler  
  (a) Gath wird als "Küstenstadt" bezeichnet, lag aber im Hügelland (Schefela) und nicht an der Küste. (b) Die DE-Erklärung rechnet mit "Handbreit" (Luther), gibt dafür aber das Maß der Spanne (ca. 22 cm) an. Eine Handbreit wären nur ca. 7–8 cm. Das Ergebnis (~2,90 m) stimmt nur mit der Spanne.  
  ✏️ _"aus der Philisterstadt Gath"; Erklärung: "Sechs Ellen und eine Handbreit (hebr. Spanne, ca. 22 cm) entsprechen etwa 2,90 m."_
- **`1sam_085`** · DE · Sprachfehler  
  Der Distraktor 2 ist grammatisch falsch ("Pinchas der Nachkommen").  
  ✏️ _"Pinchas, ein Nachkomme aus dem Hause Elis"_
- **`1sam_108`** · DE+EN · Bibelstelle  
  Die Lösung enthält "erkannte sein künftiges Königtum", das steht aber erst in 24:20 (KJV-Zählung, wie der hinterlegte Text) und nicht in 24:16-19. Außerdem zeigte David Saul den Zipfel nicht "in der Höhle", sondern rief ihm nach, nachdem Saul die Höhle verlassen hatte (24:8).  
  ✏️ _bibleReference auf "1. Samuel 24:16-20" / "1 Samuel 24:16-20" erweitern; Frage z. B. "... als David ihm nach der Begegnung in der Höhle zeigte, dass er ihn verschont hatte?"_

</details>

<details>
<summary><b>11_1_koenige.json</b> – 5 kleinere Befunde</summary>

- **`1kön_011`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 hat in DE und EN eine andere Zahl: DE 'tausend', EN 'an hundred'.  
  ✏️ _EN: 'He spake a thousand wise proverbs' oder DE: 'Genau hundert Sprüche dichtete er'_
- **`1kön_014`** · DE+EN · Inhaltlicher Fehler  
  Die Frage verlegt den Altar ins Allerheiligste (EN: 'in the oracle'). Laut Text stand der goldüberzogene Altar aber 'vor dem Chor' bzw. 'by the oracle', also vor dem Allerheiligsten.  
  ✏️ _DE: 'Womit überzog Salomo das Innere des Hauses und den Altar vor dem Chor (Allerheiligsten)?' / EN: '… and the altar that was by the oracle?'_
- **`1kön_021`** · DE+EN · Sprachfehler  
  Der DE-Distraktor ist unlogisch: Die Warnung richtet sich an Salomo, also passt 'sein Sohn Salomo' nicht. Außerdem sagt EN etwas anderes ('his son should have no heir', also Salomos Sohn).  
  ✏️ _DE: 'Dass sein Sohn keinen Erben auf dem Thron Davids haben werde'_
- **`1kön_037`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 hat in DE und EN einen anderen Zusatz. DE: 'der auf den Bergen regierte'. EN: 'who walked in all the sins of his father'.  
  ✏️ _DE: "König Abiam, der in allen Sünden seines Vaters wandelte" (passt zu 1. Kön 15:3 und zu EN)_
- **`1kön_071`** · DE+EN · Bibelstelle  
  Die Reihenfolge stimmt (correctAnswers 1,4,2,0,3: Raben, Witwe, Karmel, Horeb, Himmelfahrt). Die Bibelstelle 1. Kön 17:6 belegt aber nur das Rabenereignis und nicht die anderen vier.  
  ✏️ _bibleReference auf "1. Könige 17:6 – 2. Könige 2:11" erweitern (EN: "1 Kings 17:6 – 2 Kings 2:11")_

</details>

<details>
<summary><b>12_2_koenige.json</b> – 6 kleinere Befunde</summary>

- **`2kön_007`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 sagt in DE und EN Verschiedenes. DE: Elisa legte ihm die Hände aufs Haupt und betete dreimal. EN: Elisa kam heraus, fuhr mit der Hand über die Stelle und rief seinen Gott an (das ist Naamans Erwartung aus V. 11). In beiden Sprachen bleibt die Option falsch, der Inhalt ist aber nicht derselbe.  
  ✏️ _EN angleichen: "Elisha laid his hands upon his head and prayed three times"_
- **`2kön_016`** · DE+EN · Mehrere richtig  
  Pul gilt historisch weitgehend als derselbe König wie Tiglat-Pileser III. (vgl. auch 1. Chr 5:26). Wer das weiß, kann Distraktor 2 'Tiglat-Pileser' ebenfalls für richtig halten. Nach dem Wortlaut von 2. Kön 15:19 ist Pul richtig, die Frage kann aber verunsichern.  
  ✏️ _Distraktor 2 ersetzen, z. B. "Asarhaddon, der Sohn Sanheribs" / "Esar-haddon the son of Sennacherib"_
- **`2kön_024`** · DE+EN · Inhaltlicher Fehler  
  DE-Distraktor 2 nennt Zephanja 'Urenkel des Königs Hiskia'. Nach Zeph 1:1 (Zephanja, Sohn Kuschis, des Sohnes Gedaljas, des Sohnes Amarjas, des Sohnes Hiskias) wäre er Ururenkel, und dass dieser Hiskia der König ist, steht nicht fest. Außerdem hat EN an dieser Stelle einen anderen Inhalt ('dwelling in Jerusalem').  
  ✏️ _DE: "Zu Zephanja, dem Sohn Kuschis"; EN: "Unto Zephaniah the son of Cushi"_
- **`2kön_035`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 sagt in DE 'nach seinem Vater', in EN 'after his brother'. Der Inhalt ist verschieden, falsch ist die Option in beiden Fassungen.  
  ✏️ _Angleichen, z. B. EN: "He called his name Mattaniah after his father"_
- **`2kön_046`** · DE+EN · KJV-Wortlaut  
  Beide Fassungen kürzen die Zahl so, dass es nach 100.000 Tieren insgesamt klingt. Laut Text sind es aber 100.000 Lämmer UND 100.000 Widder. Die EN-Option sieht aus wie ein KJV-Zitat, lässt aber das zweite 'an hundred thousand' weg.  
  ✏️ _DE: "Die Wolle von hunderttausend Lämmern und hunderttausend Widdern"; EN: "An hundred thousand lambs, and an hundred thousand rams, with the wool"_
- **`2kön_066`** · EN · Sprachfehler  
  Der EN-Fragesatz ist grammatisch unvollständig: Vor 'delivered' fehlt ein Relativanschluss ('into whose hand they delivered').  
  ✏️ _"Why was there no reckoning made with the men into whose hand they delivered the money for the work?"_

</details>

<details>
<summary><b>13_1_chronik.json</b> – 7 kleinere Befunde</summary>

- **`1chr_005`** · DE · Sprachfehler  
  "Das Erstgeburtsrecht des ersten Sohnes Rubens" bedeutet grammatisch 'des Erstgeborenen von Ruben'. Gemeint ist Ruben selbst als erster Sohn Israels.  
  ✏️ _"Warum ging das Erstgeburtsrecht Rubens, des ersten Sohnes Israels, an die Kinder Josephs über?"_
- **`1chr_007`** · EN · DE/EN weicht ab  
  Der Distraktor mit Index 2 hat in DE und EN verschiedenen Inhalt: DE nennt 'Händler aus den Tälern der Stadt Samaria', EN 'merchants of the rich cities in Ephraim'. Ephraimiter werden in V.3 sogar als Bewohner Jerusalems genannt, die EN-Fassung ist dadurch unnötig verwirrend.  
  ✏️ _EN-Option 2: "The merchants out of the valleys of Samaria"_
- **`1chr_009`** · DE+EN · Inhaltlicher Fehler  
  Die DE-Frage schreibt die Worte den 'Ältesten Israels' zu und nennt sie ein 'Versprechen'. Laut V.1 sprach aber 'ganz Israel' die Worte, und es ist eine Aussage, kein Versprechen. Die EN-Frage fragt korrekt nach 'all Israel', DE und EN weichen also voneinander ab. Die EN-Lösung ergänzt zudem 'of old', was im KJV fehlt.  
  ✏️ _DE: "Was sprach ganz Israel zu David, als es sich zu Hebron versammelte?"; EN-Option 1: "Behold, we are thy bone and thy flesh"_
- **`1chr_016`** · DE · Inhaltlicher Fehler  
  Die richtige DE-Option nennt 'ein Maß Wein'. Der hinterlegte Luther-Text sagt jedoch 'ein halbes Maß Wein'.  
  ✏️ _"Jedermann, Mann und Weib, einen Laib Brot, ein Stück Fleisch und ein halbes Maß Wein"_
- **`1chr_029`** · DE · Inhaltlicher Fehler  
  Der Distraktor ordnet Asaph Kehat zu. Laut 1. Chronik 6:39-43 stammte Asaph aber von Gerson ab (Heman war der Kehatiter). Der Distraktor ist also sachlich falsch formuliert und belehrt falsch. In EN steht stattdessen 'the singer'.  
  ✏️ _"Asaph, der Sohn Berechjas, der Sänger"_
- **`1chr_032`** · EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 weichen inhaltlich ab: EN-Option 2 nennt 'gold of Uphaz' (DE: 'edles Gold'), EN-Option 3 ergänzt '20,000 talents of silver', was in DE fehlt ('aus den Schätzen Arabiens').  
  ✏️ _EN-Option 3: "10,000 talents of pure gold out of the treasures of Arabia"; EN-Option 2: "5,000 talents of fine gold, and 10,000 talents of iron"_
- **`1chr_059`** · EN · DE/EN weicht ab  
  Der Distraktor mit Index 2 hat in DE und EN verschiedenen Inhalt: DE 'bereuten Sünden', EN 'wept for Saul'.  
  ✏️ _EN-Option 2: "They fasted in dust and repented of their sins"_

</details>

<details>
<summary><b>14_2_chronik.json</b> – 9 kleinere Befunde</summary>

- **`2chr_010`** · DE+EN · Mehrere richtig  
  Distraktor 0 beginnt mit "Auf dem Gebirge Ephraim", und das ist laut Text richtig: Zemaraim liegt auf dem Gebirge Ephraim. Erst der Zusatz "bei Sichem" macht die Option falsch. Damit überschneidet sich der Distraktor teilweise mit der Lösung.  
  ✏️ _Distraktor 0 ersetzen, z. B. "Auf dem Berge Gilboa in der Ebene Jesreel" / "Upon mount Gilboa in the valley of Jezreel"_
- **`2chr_016`** · DE+EN · Bibelstelle  
  Die Lösung nennt "etliche vom Gebirge Seir". In der angegebenen Stelle 20:1-3 kommt Seir aber nicht vor: Luther hat "Meuniter", KJV "other beside the Ammonites". Seir wird erst in V. 10 und V. 22-23 genannt.  
  ✏️ _bibleReference erweitern auf "2. Chronik 20:1-3.10" (EN "2 Chronicles 20:1-3, 10") oder "20:1-23"_
- **`2chr_034`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 hat in DE und EN einen anderen Inhalt. DE: geraubte Tempelschätze "tilgen", das ist zudem sinnlos formuliert. EN: heilige Geräte "wiederherstellen" (restore).  
  ✏️ _DE-Option 0: "Bis alle heiligen Geräte des Tempels zurückgebracht wären"_
- **`2chr_039`** · DE · Inhaltlicher Fehler  
  Die DE-Lösung nennt den Meister Huram "seinen Rat", also Ratgeber. Der Text nennt ihn nur "meinen Meister", einen weisen, verständigen Mann. Ratgeber ist er nirgends. EN sagt dagegen nur "a cunning man of Huram's".  
  ✏️ _DE-Option 3: "Er lobte den HERRN und sandte den weisen Meister Huram"_
- **`2chr_050`** · DE · Inhaltlicher Fehler  
  Die DE-Lösung vermischt zwei Aussagen. Laut Text werden die Israeliten ausgewurzelt, zum Sprichwort wird aber das Haus (der Tempel) gemacht, nicht das Volk.  
  ✏️ _DE-Option 2: "Er werde sie auswurzeln aus seinem Land, das er ihnen gegeben hat"_
- **`2chr_055`** · DE · Sprachfehler  
  Grammatikfehler (Adjektivdeklination) in Option 2.  
  ✏️ _"Fünfzig Jahre bis zu seinem hohen Alter"_
- **`2chr_067`** · EN · KJV-Wortlaut  
  Die EN-Lösung gibt den KJV-Satz fast wörtlich wieder, hängt aber "in truth" an. Das steht nicht im Text.  
  ✏️ _EN-Option 3: "The LORD is with you, while ye be with him"_
- **`2chr_099`** · EN · Sprachfehler  
  Die EN-Lösung ist grammatisch unvollständig: "plenteous" ist ein Adjektiv und braucht ein Bezugswort.  
  ✏️ _"That the people brought in abundantly, and laid them by heaps" oder "... and there was plenty left"_
- **`2chr_101`** · EN · KJV-Wortlaut  
  Die EN-Lösung spricht von "watercourse of Gihon beneath". Laut KJV verstopfte Hiskia den OBEREN Wasserlauf ("upper watercourse"). "beneath" widerspricht dem Text.  
  ✏️ _EN-Option 3: "He stopped the fountains and the upper watercourse of Gihon"_

</details>

<details>
<summary><b>15_esra.json</b> – 1 kleinere Befunde</summary>

- **`esr_001`** · DE · Mehrere richtig  
  Die DE-Frage fragt allgemein nach "dem Dekret zur Rückkehr und zum Tempelbau". Im Buch Esra erlassen aber auch Darius (Esr 6, Tempelbau) und Arthahsastha (Esr 7:13, Rückkehr) Erlasse; Esr 6:14 nennt alle drei. Gemeint ist nur der erste Erlass (Esr 1:1-3). Die EN-Frage ist mit "made a proclamation throughout his realm" enger gefasst.  
  ✏️ _DE: "Welcher persische König erließ den ersten Aufruf zur Rückkehr und zum Tempelbau (Esr 1)?" bzw. "... ließ durch sein ganzes Königreich ausrufen, das Haus des HERRN zu bauen?"_

</details>

<details>
<summary><b>16_nehemia.json</b> – 2 kleinere Befunde</summary>

- **`neh_033`** · DE+EN · Inhaltlicher Fehler  
  Laut Text lautet der Titel nur "die heilige Stadt". Beide Lösungen fügen etwas hinzu, das nicht im Text steht, und zwar jeweils etwas anderes: DE "des Gottesreiches in Israel", EN "unto the LORD God of the covenant". Die Frage behauptet aber, dieser Titel werde der Stadt "feierlich beigelegt".  
  ✏️ _DE-Option 3: "Die heilige Stadt"; EN-Option 3: "The holy city"_
- **`neh_039`** · EN · KJV-Wortlaut  
  Die EN-Lösung zitiert Neh 13:31, hängt aber "according to mercy" an. Das steht nicht in 13:31 (KJV: "Remember me, O my God, for good."); die Formulierung ähnelt 13:22. Im DE-Text steht der Zusatz nicht.  
  ✏️ _EN-Option 1: "Remember me, O my God, for good!"_

</details>

<details>
<summary><b>17_esther.json</b> – 1 kleinere Befunde</summary>

- **`est_026`** · DE+EN · DE/EN weicht ab  
  Die DE-Frage nennt 'Mardochai und Esther', die EN-Frage nur 'Mordecai'. In der angegebenen Stelle 9,21-22 legt nur Mardochai die Festtage fest; Esther bestätigt sie erst in 9,29-32.  
  ✏️ _DE: 'Welche Tage bestimmte Mardochai als jährliches Freudenfest?' (oder die Referenz auf Esther 9:21-22, 29-31 erweitern und in EN Esther ergänzen)_

</details>

<details>
<summary><b>18_hiob.json</b> – 9 kleinere Befunde</summary>

- **`hi_019`** · DE+EN · Bibelstelle  
  Gefragt ist nach zwei Geschöpfen (Behemoth und Leviathan). Die angegebene Stelle Hiob 40,15 nennt aber nur den Behemoth. Der Leviathan steht in Luther 40,25 bzw. KJV 41,1.  
  ✏️ _DE-Referenz: 'Hiob 40:15; 40:25', EN-Referenz: 'Job 40:15; 41:1'._
- **`hi_030`** · DE · Inhaltlicher Fehler  
  Die richtige DE-Option ergänzt 'vor dem HERRN'. Das steht nicht im Bibeltext, und die EN-Fassung hat den Zusatz auch nicht.  
  ✏️ _Option 3: 'Und Hiob starb alt und lebenssatt'_
- **`hi_031`** · DE+EN · Inhaltlicher Fehler  
  Die Lösung nennt 'tausend Rinder / thousand oxen'. Der Bibeltext spricht von 'fünfhundert Joch Rinder / five hundred yoke of oxen'. Rechnerisch stimmt das (Joch = Paar), aber der Wortlaut weicht ab. Das kann bibelkundige Spieler verwirren, zumal ein Distraktor 'fünfhundert Rinder' nennt und hi_024/42:12 von 'tausend Joch' spricht.  
  ✏️ _DE: 'Siebentausend Schafe, dreitausend Kamele und fünfhundert Joch Rinder'; EN: 'Seven thousand sheep, three thousand camels, five hundred yoke of oxen'_
- **`hi_091`** · DE · Sprachfehler  
  Grammatikfehler im Distraktor: Der Akkusativ heißt 'den Grimm', nicht 'den Grimme'.  
  ✏️ _'... um den Grimm zu besänftigen'_
- **`hi_095`** · DE+EN · KJV-Wortlaut  
  Die EN-Lösung gibt KJV wörtlich wieder, ersetzt aber 'they that know him not see' durch 'none see'. Damit sagt sie aus, niemand sehe seine Tage, während der Text nur von denen spricht, die ihn kennen. Die DE-Lösung 'Zeiten und Tage vorbehalten worden' vermischt die beiden Vershälften von Luther.  
  ✏️ _EN: 'Why, seeing times are not hidden from the Almighty, do they that know him not see his days?'; DE: 'Warum sind vom Allmächtigen nicht Zeiten vorbehalten, und die ihn kennen, sehen seine Tage nicht?'_
- **`hi_113`** · DE · Sprachfehler  
  Die richtige Option ist grammatisch unvollständig: 'und die nagen, schlafen nicht' hat kein Objekt und ist schwer verständlich.  
  ✏️ _'Des Nachts wird sein Gebein durchbohrt, und die ihn nagen, legen sich nicht schlafen'_
- **`hi_115`** · DE · Sprachfehler  
  Die richtige Option ist sprachlich verunglückt: 'nicht blickend achtete' ist kein korrektes Deutsch.  
  ✏️ _'Einen Bund, dass er nicht achtete auf eine Jungfrau'_
- **`hi_120`** · DE+EN · Inhaltlicher Fehler  
  Die Lösung schreibt das Finden der Versöhnung/des Lösegelds dem Engel/Mittler zu. Im Text sagt aber Gott: "ich habe eine Versöhnung gefunden".  
  ✏️ _DE: "Ein Engel als Mittler, einer aus tausend, der dem Menschen verkündigt, wie er recht tun soll"; EN: "A messenger, an interpreter, one among a thousand, to shew unto man his uprightness"_
- **`hi_136`** · DE · Sprachfehler  
  Die Lösungsoption ist verkürzt: "Ich lege die Hand auf!" bedeutet im Deutschen etwas anderes (Handauflegung). Gemeint ist, die Hand auf den Mund zu legen.  
  ✏️ _"Siehe, ich bin zu gering; was soll ich antworten? Ich lege meine Hand auf meinen Mund"_

</details>

<details>
<summary><b>19_psalmen.json</b> – 3 kleinere Befunde</summary>

- **`ps_007, ps_008, ps_009, ps_010, ps_011, ps_012, ps_014, ps_015, ps_016, ps_017, ps_018, ps_020, ps_021, ps_022, ps_023, ps_025, ps_026, ps_028, ps_029, ps_030, ps_031, ps_032, ps_034, ps_036, ps_037, ps_038, ps_039, ps_040, ps_043, ps_044, ps_045, ps_046, ps_047, ps_048, ps_050, ps_054, ps_055, ps_056, ps_057, ps_058, ps_059, ps_060, ps_062, ps_064, ps_065, ps_066, ps_067, ps_068, ps_069, ps_070, ps_071, ps_072, ps_073, ps_075, ps_076, ps_077, ps_078, ps_079, ps_080, ps_082, ps_084, ps_086, ps_087, ps_089, ps_090, ps_091, ps_092, ps_093, ps_094, ps_095, ps_096, ps_097, ps_105, ps_106, ps_107, ps_108, ps_109, ps_110, ps_111, ps_113, ps_114, ps_115, ps_117, ps_118, ps_119, ps_122, ps_123`** · EN · DE/EN weicht ab  
  Systematische Abweichung: Bei diesen Fragen haben die EN-Distraktoren einen anderen Inhalt als die DE-Distraktoren mit gleichem Index (eigenständig formuliert oder in anderer Reihenfolge). Beispiele: ps_067 DE 0/2/3 = Psalm 134/133/131, EN = Psalm 115/120/134; ps_071 DE = 166/144/150 Verse, EN = 150/182/168 Verse. Der Index der richtigen Antwort und die Lösung selbst stimmen jeweils überein, Spieler werden also nicht falsch belehrt. DE und EN sind aber keine parallelen Fassungen.  
  ✏️ _EN-Distraktoren als inhaltliche Übersetzung der DE-Distraktoren mit gleichem Index neu fassen (z. B. ps_067 EN: Psalm 134 / Psalm 117 / Psalm 133 / Psalm 131), oder bewusst als zulässige Abweichung dokumentieren._
- **`ps_050`** · EN · Sprachfehler  
  Die EN-Frage ist grammatisch kaputt: Sie vermischt "What hath the LORD given..." mit "given his angels charge over thee".  
  ✏️ _"For what purpose hath the LORD given his angels charge over thee according to Psalm 91:11?"_
- **`ps_081`** · DE+EN · Bibelstelle  
  Ps 139:7 stellt nur die Frage. Die Antwort mit Himmel, Hölle und Meer steht erst in den Versen 8-9 (bzw. 8-10).  
  ✏️ _bibleReference auf "Psalmen 139:7-10" / "Psalm 139:7-10" erweitern._

</details>

<details>
<summary><b>20_sprueche.json</b> – 5 kleinere Befunde</summary>

- **`spr_004, spr_005, spr_006, spr_008, spr_009, spr_010, spr_011, spr_012, spr_014, spr_015, spr_017`** · EN · DE/EN weicht ab  
  Wie in den Psalmen haben die EN-Distraktoren einen anderen Inhalt als die DE-Distraktoren mit gleichem Index. Beispiele: spr_008 DE = Biene/Spinne/Schwalbe, EN = spider/coney/locust; spr_009 DE = 3/4, 10/11, 12/13, EN = 4/5, 3/4, 8/9; spr_012 DE = 3/4/12 Säulen, EN = 12/3/10. Die Lösung ist jeweils identisch und steht am gleichen Index.  
  ✏️ _EN-Distraktoren an die DE-Distraktoren mit gleichem Index angleichen (z. B. spr_012 EN: Three / Four / Twelve / Seven pillars; spr_008 EN: The bee / The spider / The swallow / The ant)._
- **`spr_010`** · DE+EN · Sprachfehler  
  EN-Option 3 enthält den Tippfehler "offereh" (statt "offereth"). Außerdem nennt die DE-Frage die Frau in Sprüche 7 "Törin". Dort heißt sie aber "Weib im Hurenschmuck" bzw. "fremdes Weib"; "die Törin" ist die Gestalt aus Sprüche 9:13. EN sagt korrekt "the strange woman".  
  ✏️ _EN: "She offereth him precious gold and rich coverings of tapestry"; DE-Frage: "Wie nähert sich das fremde Weib dem unverständigen Jüngling in Sprüche 7?"_
- **`spr_052`** · EN · KJV-Wortlaut  
  Im KJV-Zitat fehlt der Artikel ('with lowly' statt 'with the lowly'), und zwar in der Lösung und parallel in allen Distraktoren.  
  ✏️ _In allen Optionen 'with the lowly' schreiben._
- **`spr_079`** · EN · KJV-Wortlaut  
  Das KJV-Zitat in der EN-Lösung ist verkürzt: Es fehlen Artikel und 'is ... out a matter'. Dadurch ist der Satz ungrammatisch.  
  ✏️ _'It is the glory of God to conceal a thing: but the honour of kings is to search out a matter'_
- **`spr_086`** · EN · KJV-Wortlaut  
  Im KJV-Zitat der EN-Lösung fehlen die Artikel. Dadurch ist der Satz ungrammatisch.  
  ✏️ _'The wicked flee when no man pursueth: but the righteous are bold as a lion'_

</details>

<details>
<summary><b>21_prediger.json</b> – 3 kleinere Befunde</summary>

- **`pred_008`** · DE · Bibelstelle  
  Die DE-Frage nennt Prediger 5:3. Im hinterlegten DE-Text steht das Gelübde aber in V. 4, V. 3 handelt von Träumen und vielen Worten. Die EN-Frage nennt richtig 5:4.  
  ✏️ _DE-Frage: 'Was rät der Prediger in Prediger 5:4 zum Gelübde?'_
- **`pred_018`** · EN · Mehrere richtig  
  EN-Distraktor 0 nennt 'Solomon the son of David'. Das ist nach üblicher Auslegung genau der Prediger, nur der Zusatz 'over the heathen' macht die Option falsch. Die Option ist irreführend nah an der Lösung. In DE steht an dieser Stelle Mose.  
  ✏️ _EN-Option 0 an DE angleichen: 'Moses, the servant of the LORD, who received the law'._
- **`pred_019`** · EN · KJV-Wortlaut  
  Die EN-Lösung zitiert KJV wörtlich, lässt aber das Verb 'increaseth' aus. Der Satz ist dadurch unvollständig und ungrammatisch.  
  ✏️ _'For in much wisdom is much grief: and he that increaseth knowledge increaseth sorrow'_

</details>

<details>
<summary><b>23_jesaja.json</b> – 33 kleinere Befunde</summary>

- **`jes_017`** · DE · Sprachfehler  
  Der DE-Distraktor 1 'Er setzt es mit Härte durch' ergibt für ein Rohr keinen Sinn, denn 'etwas durchsetzen' passt nicht zu einem Gegenstand. Er entspricht auch nicht der EN-Option ('breaketh it with a rod of iron').  
  ✏️ _'Er zerschlägt es mit eisernem Stab'_
- **`jes_023`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN unterschiedliche Inhalte und stehen in anderer Reihenfolge: DE 0 Schweigen/Asche gegenüber EN 0 Altar/Brandopfer, DE 2 Tempelopfer gegenüber EN 2 Binse/Sack und Asche, DE 3 Säcke/Weinen gegenüber EN 3 Zehnten.  
  ✏️ _Distraktoren indexgleich angleichen, z. B. EN 0: 'To keep silence many days and sprinkle ashes', EN 2: 'To bring all offerings faithfully to the temple', EN 3: 'To put on sackcloth and weep aloud'_
- **`jes_025`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN unterschiedliche Inhalte: DE 0 Reich Davids durch Krieg gegenüber EN 0 Heiden mit eisernem Stab, DE 1 Gericht ansagen gegenüber EN 1 Palast bauen, DE 2 neues Priestergeschlecht gegenüber EN 2 levitische Ordnungen.  
  ✏️ _EN 1: 'To declare judgment unto the heathen nations' usw. indexgleich angleichen_
- **`jes_029`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 nennen in DE und EN völlig andere Tiere (DE: Hund/Taube, Esel/Ochse, Pferd/Schaf; EN: Hund/Schaf, Kamel/Pferd, Taube/Vogel).  
  ✏️ _EN-Distraktoren an DE angleichen (oder umgekehrt), z. B. EN 2: 'The ass knoweth his stall, and the ox his pasture'_
- **`jes_032`** · DE+EN · Sprachfehler  
  Die Frage 'Wovon rät ... ab?' passt grammatisch nicht zu den Optionen mit 'Vor dem ...', denn 'vor' gehört zu 'warnen'. Zudem stehen die EN-Distraktoren in anderer Reihenfolge (DE 0 Götzendienst entspricht EN 2, DE 1 Ägypten entspricht EN 0, DE 2 Reichtum entspricht EN 1).  
  ✏️ _Frage: 'Wovor warnt Jesaja 2:22?' und EN-Distraktoren indexgleich ordnen_
- **`jes_035`** · DE+EN · Mehrere richtig  
  Zwei Distraktoren sind zur Hälfte richtig. Bei DE 3 steht 'Statt des Gürtels ... ein Strick' wörtlich im Vers. DE 0 ('statt des Schmucks ein Sack') und EN 0 ('sackcloth') entsprechen 'für einen weiten Mantel ein enger Sack' bzw. 'a girding of sackcloth'. Außerdem passen DE 3 und EN 3 inhaltlich nicht zusammen.  
  ✏️ _DE 3: 'Statt der Ringe wird Rost sein, statt der Krone ein Kranz aus Dornen'; DE 0/EN 0 ohne 'Sack/sackcloth' formulieren_
- **`jes_037`** · EN · KJV-Wortlaut  
  Die EN-Lösung schreibt 'excellent and comely for the escaped' dem Zweig des HERRN zu. In der KJV beziehen sich diese Worte auf 'the fruit of the earth'.  
  ✏️ _'Beautiful and glorious'_
- **`jes_042`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 nennt in DE und EN verschiedene Zahlen: im DE das siebente, im EN das vierzigste Regierungsjahr Salomos.  
  ✏️ _Angleichen, z. B. EN 2: 'In the seventh year of king Solomon's reign'_
- **`jes_043`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 sind in DE und EN völlig verschiedene Sätze. Im DE sind es Abwandlungen des Seraphim-Rufs, im EN Zitate aus Psalmen bzw. der Offenbarung.  
  ✏️ _Die EN-Distraktoren als Übersetzung der DE-Varianten formulieren, z. B. EN 1: 'Holy is the LORD, Lord of the world: all the heavens are full of his glory'_
- **`jes_044`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 3 sind zwischen DE und EN vertauscht bzw. verschieden: DE 0 Docht gegenüber EN 0 Rohre, DE 3 Rohre gegenüber EN 3 Schlangen. Außerdem ist DE 0 grammatisch falsch: Es muss 'Dochte' heißen.  
  ✏️ _DE 0: 'Zwei glimmende Dochte' / EN 0: 'Two smoking wicks'; EN 3: 'Two bruised reeds'_
- **`jes_048`** · DE+EN · Mehrere richtig  
  Distraktor 0 nennt 'das Land jenseits des Jordan'. Genau dieses Gebiet zählt 9:1 ausdrücklich zu der Region auf, über der das Licht scheint ('das Land jenseit des Jordans' / 'beyond Jordan'). Der Distraktor ist deshalb teilweise richtig.  
  ✏️ _Option 0 ersetzen, z. B. 'Das Land Gilead und Baschan' / 'The land of Gilead and Bashan'_
- **`jes_058`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 nennt verschiedene Städte bzw. Länder: im DE Moab, im EN Damaskus.  
  ✏️ _EN 2: 'Against Moab' (oder DE 2: 'Über Damaskus')_
- **`jes_066`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 nennen in DE und EN andere Empfänger bzw. Orte: DE 0 Landesherr gegenüber EN 0 Damaskus, DE 1 Damaskus gegenüber EN 1 Ägypten, DE 2 Tempel in Jerusalem gegenüber EN 2 Höhen des Kemosch.  
  ✏️ _Distraktoren indexgleich angleichen_
- **`jes_080`** · DE · Sprachfehler  
  Die Lösung ist grammatisch unvollständig: In 'wenn so steht' fehlt das Subjekt ('es').  
  ✏️ _'Ist das unsre Zuversicht, dahin wir um Hilfe flohen? Wie könnten wir entrinnen?'_
- **`jes_086`** · EN · Sprachfehler  
  In den EN-Distraktoren fehlen Artikel; die Ausdrücke sind ungrammatisch.  
  ✏️ _'The fishers of the sea' / 'The priests of the land'_
- **`jes_095`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 sind zwischen DE und EN vertauscht: Im DE ist 2 der König und 3 das Gesetz, im EN ist es umgekehrt.  
  ✏️ _Reihenfolge der EN-Optionen 2 und 3 tauschen_
- **`jes_102`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind verschoben bzw. verschieden: DE 1 'Gott handelt nach Laune' fehlt im EN, DE 2 entspricht EN 1, DE 3 entspricht EN 2, und EN 3 ('Man ordereth his own labour') fehlt im DE.  
  ✏️ _EN 1: 'God acteth by whim and leaveth the land without order', EN 2/3 an DE 2/3 anpassen_
- **`jes_111`** · EN · KJV-Wortlaut  
  Die EN-Lösung zitiert KJV wörtlich, ersetzt aber 'Jerusalem' durch 'Zion'.  
  ✏️ _'As birds flying, so will the LORD of hosts defend Jerusalem'_
- **`jes_117`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 unterscheiden sich: DE 1 'Priester, König, Prophet' gegenüber EN 1 'Priest, Prophet, Deliverer', DE 2 'Vater, Sohn, Geist' gegenüber EN 2 'Father, Shield, Fortress'.  
  ✏️ _EN 1: 'Our Priest, our King, and our Prophet'; EN 2: 'Our Father, our Son, and our Spirit'_
- **`jes_118`** · DE · Sprachfehler  
  Die Frage verlangt 'Über welches Volk', die Optionen beginnen aber mit 'Auf ...'.  
  ✏️ _Optionen: 'Über Edom', 'Über Moab', 'Über Ammon', 'Über Tyrus'_
- **`jes_124`** · DE+EN · Mehrere richtig  
  Distraktor 3 ('treacherous friend that turneth against its own' bzw. 'Verbündeter, der in den Rücken fällt') gibt im Grunde die Aussage des Rohrstab-Bildes wieder: Ägypten verletzt den, der sich auf es stützt. Das macht die Frage unscharf.  
  ✏️ _Option 3 ersetzen, z. B. 'Als wilden Stier, der seine Feinde niederstößt' / 'As a wild bull goring all its foes'_
- **`jes_133`** · DE · Sprachfehler  
  Die Lösung passt grammatisch nicht zur Frage ('Mit welchem Bild ...' – 'Als du Würmlein Jakob ...'). Der Satz ist verunglückt.  
  ✏️ _'Das Würmlein Jakob wird zum neuen, scharfen Dreschwagen gemacht'_
- **`jes_139`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 sagt in DE und EN das Gegenteil: im DE ein Gesetz 'in die Herzen geschrieben', im EN ein Gesetz 'on tables of stone'. Auch Distraktor 3 unterscheidet sich (Wüste gegenüber Meer).  
  ✏️ _EN 0: 'Behold, I give a new law written upon the hearts'; EN 3: 'A new city founded in the wilderness'_
- **`jes_143`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich inhaltlich: DE 2 Gutes und Böses tun andere gegenüber EN 2 Erde gegründet, Himmel den Engeln; DE 3 Schöpfung mit anderen Göttern geteilt gegenüber EN 3 ignoriert heidnische Herrscher.  
  ✏️ _EN 2: 'He made light and darkness, yet good and evil are wrought by others'; EN 3: 'He shareth creation with other gods and ruleth only the light'_
- **`jes_144`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN völlig andere Inhalte: DE Götter/Jerusalem/Opfern gegenüber EN Gold zum Tempel/Bundesordnungen/Beugen vor dem König.  
  ✏️ _EN 0: 'Turn unto the gods, and be ye saved, all the ends of the earth' usw. indexgleich angleichen_
- **`jes_147`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 sind vertauscht bzw. verschieden: DE 1 König aus Davids Haus gegenüber EN 1 Engel der Zerstörung, DE 3 Engel gegenüber EN 3 Hoherpriester.  
  ✏️ _Distraktoren indexgleich angleichen_
- **`jes_156, jes_161, jes_167, jes_179, jes_180, jes_181, jes_182, jes_184, jes_185, jes_186, jes_187, jes_198`** · DE+EN · DE/EN weicht ab  
  Die EN-Distraktoren haben einen anderen Inhalt als die DE-Distraktoren mit gleichem Index. Die Lösung ist überall gleich und richtig. Beispiele: jes_156 DE 2 'verehren es, bringen Gold und Weihrauch' (zudem teilweise zutreffend: 'niederfallen') / EN 2 'gold … to build up their own'. jes_161 DE 1 'Heil währt ewig' / EN 1 'salvation waxeth old'. jes_167 alle drei Distraktoren verschieden (Bund aus Gold / fixed stars usw.). jes_179 1 und 3. jes_180 DE 0 Engel / EN 0 prophet, DE 1 Prophet / EN 1 heathen armies, DE 2 Heer / EN 2 fire. jes_181 Index 1. jes_182 DE 0 Feinde einziehen / EN 0 watchmen, DE 2 Priester / EN 2 poor, DE 3 Händler / EN 3 priests. jes_184 Index 0 und 1. jes_185 Index 1 bis 3. jes_186 Index 0, 2, 3. jes_187 DE 1 Feinde erspähen / EN 1 stones of stumbling. jes_198 Index 0 bis 2 völlig verschieden.  
  ✏️ _EN-Distraktoren jeweils inhaltlich an die DE-Option mit gleichem Index angleichen (oder umgekehrt), damit beide Sprachen dieselben Antwortmöglichkeiten in derselben Reihenfolge haben._
- **`jes_168`** · EN · KJV-Wortlaut  
  Die EN-Lösung zitiert KJV wörtlich, hängt aber 'in war' an. Das steht nicht im Text und schränkt die Aussage ein.  
  ✏️ _'No weapon that is formed against thee shall prosper'_
- **`jes_173`** · DE+EN · Mehrere richtig  
  DE-Option 2 'faule Hirten' greift Textwörter auf: 'sind faul' (V.10) und 'die Hirten' (V.11). Das Gleiche gilt für EN-Option 1 'Sleeping shepherds' ('sleeping' V.10, 'shepherds' V.11). Beide sind teilweise zutreffend. Außerdem passen die Distraktoren nicht zum gleichen Index: DE 1 blinde Führer / EN 1 Sleeping shepherds, DE 2 faule Hirten / EN 2 Ravening wolves, DE 3 taube Wächter / EN 3 Blind guides.  
  ✏️ _Option 2 ersetzen durch 'Als reißende Wölfe, die die Herde fressen' / 'Ravening wolves …'. Danach die Reihenfolge angleichen: 1 'Als blinde Führer …' / 'Blind guides …', 3 'Als taube Wächter …' / 'Deaf watchmen that hear not the enemy'._
- **`jes_178`** · DE · Sprachfehler  
  Grammatikfehler: 'ein Lust' statt 'eine Lust'. Außerdem passen die EN-Distraktoren 0, 2 und 3 nicht zu den DE-Optionen mit gleichem Index (DE 0 Sieg/Herrschaft – EN 0 corn and wine, DE 2 langes Leben – EN 2 crown/victory, DE 3 Ertrag/Frieden – EN 3 long life).  
  ✏️ _'… der den Sabbat eine Lust nennt'. Distraktoren angleichen._
- **`jes_188`** · EN · Inhaltlicher Fehler  
  Die EN-Lösung zählt 'Sought out' zu den Namen des Volkes. Nach KJV 62:12 ist 'Sought out' aber der Name der Stadt ('thou shalt be called'). Die DE-Lösung nennt richtig nur 'Das heilige Volk, die Erlösten des HERRN'.  
  ✏️ _EN-Option 3: 'The holy people, The redeemed of the LORD'_
- **`jes_193`** · DE · Bibelstelle  
  Im deutschen Fragetext steht Vers 64:5, die Stelle (bibleReference) und der hinterlegte Luther-Text haben die Aussage aber in 64:6. EN nennt richtig 64:6.  
  ✏️ _'… in Jesaja 64:6?'_
- **`jes_194`** · DE · Bibelstelle  
  Im deutschen Fragetext steht Vers 64:7, Stelle und hinterlegter Text haben das Töpfer-Bild aber in 64:8.  
  ✏️ _'… in Jesaja 64:8?'_

</details>

<details>
<summary><b>24_jeremia.json</b> – 12 kleinere Befunde</summary>

- **`jer_005, jer_007, jer_008, jer_009, jer_010, jer_012, jer_013, jer_014, jer_015, jer_016, jer_018, jer_019, jer_021, jer_022, jer_023, jer_024, jer_025, jer_026, jer_027, jer_028, jer_029, jer_030, jer_032, jer_033, jer_034, jer_035, jer_036, jer_037, jer_038, jer_039, jer_040, jer_041, jer_042, jer_044, jer_045, jer_054, jer_055, jer_056, jer_057, jer_058, jer_060, jer_061, jer_062, jer_063, jer_065, jer_066, jer_067, jer_069, jer_070, jer_071`** · DE+EN · DE/EN weicht ab  
  In diesen Jeremia-Fragen wurden die EN-Distraktoren offenbar unabhängig geschrieben. Sie haben einen anderen Inhalt oder eine andere Reihenfolge als die DE-Optionen mit gleichem Index. Die richtige Antwort stimmt jeweils überein. Auffällig: jer_009 hat andere Zahlen (DE 0 Sieben / EN 0 Forty, DE 1 Vierzig / EN 1 Fifty). jer_018 hat andere Personen (DE 1 Zedekia / EN 1 Gedaliah, DE 2 Gedalja / EN 2 Jonathan). jer_040 hat einen anderen Ort (DE 3 Nob / EN 3 Shechem). jer_062 hat Index 2 und 3 vertauscht (David–Salomo / Elijah–Elisha). jer_042 hat andere Vogelnamen. jer_021 hat Index 1 und 2 vertauscht. jer_026 nennt in DE 'Juda', in EN 'Israel'. jer_056 DE 0 ('Götzen vernichten und nur dem HERRN dienen') liegt zudem nahe an der Lösung.  
  ✏️ _EN-Distraktoren jeweils an die DE-Option mit gleichem Index angleichen (gleiche Person/Zahl/Ort/Aussage), z. B. jer_009 EN: 'Seven years / Forty years / A hundred years / Seventy years'; jer_040 EN-Option 3: 'Unto Nob'; jer_062 EN 2/3 tauschen._
- **`jer_020`** · DE+EN · Inhaltlicher Fehler  
  Das Wort 'allein' in der DE-Lösung steht nicht im Text. V.15 spricht sogar davon, dass die Frauen 'andern Göttern' räucherten (Plural). Außerdem weichen alle EN-Distraktoren von DE ab (Gestirne/Baal, Götzen Babels/Molech, Sonnengott/Ashtaroth). EN 'Ashtaroth' wird zudem oft mit der Himmelskönigin gleichgesetzt, das macht die EN-Fassung etwas mehrdeutig.  
  ✏️ _DE-Option 3: 'Der Himmelskönigin'. EN-Option 2 durch eine eindeutig falsche Gottheit ersetzen, z. B. 'Unto Dagon, the god of the Philistines'. Die übrigen Distraktoren angleichen._
- **`jer_046`** · EN · KJV-Wortlaut  
  Die EN-Lösung zitiert KJV, fügt aber 'of hosts' ein, das in 9:24 nicht steht. Weggelassen ist der Inhalt, den DE nennt (Barmherzigkeit, Recht, Gerechtigkeit). Außerdem passen die Distraktoren nicht zu DE: DE 0 weise / EN 0 wisdom+wealth+strength, DE 2 stark / EN 2 pedigree, DE 3 reich / EN 3 sacrifices.  
  ✏️ _EN-Option 1: 'That he knoweth me, the LORD which exercise lovingkindness, judgment, and righteousness'. Distraktoren an DE angleichen._
- **`jer_047`** · DE · Mehrere richtig  
  Distraktor 0 ('beschnitten, aber unrein im Herzen') kommt der Lösung 'unbeschnittenes Herz' sehr nahe (vgl. 9,25). Falsch ist er nur durch das Wort 'gerecht'. Spieler können hier leicht zweifeln. EN-Option 0 lautet zudem inhaltlich anders ('uncircumcised in deed').  
  ✏️ _DE-Option 0 an EN angleichen und deutlich falsch machen, z. B. 'Es ist gerecht im Fleisch und rein in seinen Taten'._
- **`jer_053`** · EN · Sprachfehler  
  Der Artikel fehlt: 'The princes of king'.  
  ✏️ _'The princes of the king'_
- **`jer_064`** · DE · Sprachfehler  
  Uneinheitliche Person: Die Lösung beginnt mit 'Dich', alle anderen Optionen sprechen in der 3. Person von Jeremia ('Ihn'). Auch die Distraktoren passen nicht zu EN (anderes Land / prince of peace, König / judge, Tod / priest).  
  ✏️ _'Ihn zur festen, ehernen Mauer wider dies Volk zu machen'_
- **`jer_068`** · EN · Mehrere richtig  
  EN-Option 2 nennt 'the horns of altar'. Nach 17,1 ist die Sünde tatsächlich auch 'upon the horns of your altars' eingegraben. Die Option ist also teilweise richtig. Die DE-Option 2 hat einen anderen Inhalt (Tinte auf Priestertafeln).  
  ✏️ _EN-Option 2 an DE angleichen: 'With ink that is easily wiped away, upon the tables of the priests'._
- **`jer_095`** · DE+EN · Bibelstelle  
  Die richtige Antwort nennt auch die Rückkehr Jechonjas. Davon spricht erst 28:4, 28:3 nennt nur die Geräte. Die angegebene Stelle deckt die Antwort also nicht vollständig ab.  
  ✏️ _bibleReference (DE und EN) sowie die Fragetexte auf "Jeremia 28:3-4" / "Jeremiah 28:3-4" ändern_
- **`jer_096`** · DE+EN · Mehrere richtig  
  Distraktor 1 ("Du wirst bald sterben ..." / "Thou shalt die in this year, because thou hast spoken lies") gibt fast wörtlich Jer 28:16 wieder. Dort kündigt Jeremia dem Hananja tatsächlich den Tod an. Die Frage ist zwar auf 28:13 begrenzt, aber wer die Geschichte kennt, hält auch diese Option für richtig.  
  ✏️ _Distraktor 1 durch eine eindeutig falsche Aussage ersetzen, z. B. DE "Du sollst mit mir nach Babel ziehen und dort das Volk trösten" / EN "Thou shalt go with me to Babylon and comfort the captives there"_
- **`jer_124`** · DE+EN · DE/EN weicht ab  
  DE und EN stellen verschiedene Fragen. DE fragt, wen der König von Babel als Statthalter einsetzte (40:5). EN fragt, bei wem Jeremia in Mizpa wohnen wollte (40:6). Die Lösung (Gedalja) ist zwar gleich, der Frageinhalt aber nicht. Außerdem nennt die DE-Frage nur 40:5, während die Stelle 40:5-6 ist.  
  ✏️ _EN angleichen: "Whom did the king of Babylon make governor over the cities of Judah (Jeremiah 40:5)?". Alternativ die DE-Frage an EN anpassen: "Zu wem ging Jeremia nach Mizpa und blieb bei ihm (Jeremia 40:5-6)?"_
- **`jer_151`** · DE · Sprachfehler  
  In DE-Option 1 wechselt die Zeitform mitten im Satz (Präteritum "dankten" neben Präsens "fragen").  
  ✏️ _"Mit Beute beladen; sie danken dem HERRN und fragen nach dem Königsweg"_
- **`jer_153`** · DE+EN · Mehrere richtig  
  Distraktor 2 ("Ein starker Hammer, der alle Reiche zertrümmerte") ist biblisch belegt. Jer 50:23 nennt Babel den "Hammer der ganzen Welt", und Jer 51:20 (Frage jer_154) heißt es "Du bist mein Hammer". Nur die Versangabe 51:7 macht den Distraktor falsch.  
  ✏️ _Distraktor 2 ersetzen, z. B. DE "Ein fester Turm, der alle Völker beschützte" / EN "A strong tower that sheltered all the nations"_

</details>

<details>
<summary><b>25_klagelieder.json</b> – 1 kleinere Befunde</summary>

- **`kla_006`** · DE+EN · Mehrere richtig  
  Die Distraktoren sind wahre Aussagen aus demselben Buch. Option 1 (der Herr hat seinen Altar verlassen und sein Heiligtum verworfen) steht in Klgl 2:7, Option 3 (Fürsten wie Hirsche ohne Weide) in Klgl 1:6, Option 0 (Tore zerbrochen) entspricht etwa 2:9. Nur die Begrenzung auf 2:1 schließt sie aus. Als Beschreibung des Zornes Gottes über Zion sind sie inhaltlich richtig.  
  ✏️ _Mindestens Option 1 (und möglichst auch 3) durch Aussagen ersetzen, die nicht in den Klageliedern stehen, z. B. "Der Herr hat Zion verschont und seinen Zorn abgewandt"_

</details>

<details>
<summary><b>26_hesekiel.json</b> – 8 kleinere Befunde</summary>

- **`hes_024`** · DE · Inhaltlicher Fehler  
  Laut Text macht der HERR die Stirn hart wie Demant, nicht das Angesicht. Das Angesicht wird nur 'hart gemacht gegen ihr Angesicht'. Die DE-Lösung vermischt beides, EN sagt korrekt 'forehead'.  
  ✏️ _'Er machte seine Stirn hart wie Demant, härter als Fels'_
- **`hes_024, hes_025, hes_027, hes_029, hes_030, hes_031, hes_032, hes_033, hes_034, hes_035, hes_037, hes_038, hes_039, hes_040, hes_042, hes_043, hes_044, hes_045, hes_046, hes_047, hes_048 u. v. m. (fast alle Fragen der Datei)`** · DE+EN · DE/EN weicht ab  
  Systematisch: Bei den meisten Fragen haben die EN-Distraktoren einen völlig anderen Inhalt als die DE-Distraktoren mit gleichem Index. Ein Beispiel ist hes_024: DE 0 'scharfes Schwert' gegenüber EN 0 'armed company of soldiers'. Die Lösungen und ihr Index stimmen jeweils überein, nur die falschen Optionen sind keine Übersetzungen voneinander.  
  ✏️ _Wenn DE und EN parallel sein sollen, die EN-Distraktoren als Übersetzung der DE-Distraktoren (oder umgekehrt) neu erzeugen. Sonst bewusst als akzeptiert dokumentieren._
- **`hes_041`** · EN · DE/EN weicht ab  
  Die EN-Frage nennt Pelatja nicht ('What came to pass when Ezekiel prophesied'). Die Distraktoren mit 'He ...' können sich deshalb auch auf Ezekiel beziehen. Ezekiel 'fell down upon my face', was Option 0 ('He fell into a swoon') nahekommt. DE fragt eindeutig nach Pelatja.  
  ✏️ _EN-Frage ändern in: 'What happened to Pelatiah the son of Benaiah while Ezekiel prophesied (Ezekiel 11:13)?'_
- **`hes_046`** · EN · Inhaltlicher Fehler  
  Die EN-Lösung ergänzt 'that tear down and ruin the vineyard'. Das steht nicht in Hesekiel 13:4 (Anklang an Hld 2:15). DE nennt nur 'Füchse in den Wüsten'. EN gibt dem Spieler damit eine nicht belegte Zusatzaussage.  
  ✏️ _EN-Option 1: 'Unto foxes in the deserts'_
- **`hes_047`** · DE+EN · Inhaltlicher Fehler  
  Laut Text baut das Volk bzw. 'einer' die Wand, und die falschen Propheten tünchen sie nur mit losem Kalk. Die Lösung schreibt beides den Propheten zu.  
  ✏️ _DE: 'Sie tünchen die Wand, die das Volk baut, mit losem Kalk und rufen: Friede!' / EN: 'When one built up a wall, they daubed it with untempered morter, saying Peace'_
- **`hes_090`** · DE+EN · Bibelstelle  
  In 27:3 erscheint Tyrus noch nicht als Schiff. Dort wird nur die Stadt am Meer angeredet, die sagt 'Ich bin die Allerschönste'. Das Schiffsbild beginnt erst in 27:4-9.  
  ✏️ _bibleReference auf 'Hesekiel 27:3-5' / 'Ezekiel 27:3-5' erweitern und die Frage entsprechend auf 27:3-5 beziehen._
- **`hes_094`** · DE · Inhaltlicher Fehler  
  Weder Luther ('Cherub, der sich weit ausbreitet und decket') noch KJV ('anointed cherub that covereth') sprechen von einem 'glänzenden' Cherub. DE und EN weichen dadurch voneinander ab.  
  ✏️ _DE: 'Als ein Cherub, der sich weit ausbreitet und deckt, auf dem heiligen Berg Gottes'_
- **`hes_145, hes_147`** · EN · DE/EN weicht ab  
  Einzelne EN-Distraktoren haben einen anderen Inhalt als die DE-Option mit gleichem Index. Die Lösung ist korrekt und gleich.  
  ✏️ _hes_147 EN 1: 'Upon the Moabites and Edomites, worshipping their gods'. Bei hes_145 die EN-Distraktoren an DE angleichen._

</details>

<details>
<summary><b>27_daniel.json</b> – 2 kleinere Befunde</summary>

- **`dan_004, dan_005, dan_006, dan_007, dan_008, dan_009, dan_010, dan_011, dan_014, dan_015, dan_017, dan_018, dan_019, dan_020, dan_023, dan_024, dan_025, dan_026, dan_032, dan_033, dan_034, dan_035, dan_036, dan_037, dan_038`** · EN · DE/EN weicht ab  
  Die EN-Distraktoren sind keine Übersetzung der DE-Distraktoren, sondern eigenständig neu formuliert. Bei gleichem Index stehen andere Personen und Aussagen, bei dan_008 sind die Tiere sogar vertauscht (DE 1 = Bär, EN 1 = Löwe). Die richtige Antwort und ihr Index stimmen jeweils überein, Spieler werden also nicht falsch belehrt. Die Fassungen sind aber nicht parallel.  
  ✏️ _Die EN-Distraktoren als Übersetzung der DE-Distraktoren mit gleichem Index anlegen (oder umgekehrt), z. B. dan_037 EN 2 'Arioch', dan_010 EN 0 'Michael, who came at the time of the morning sacrifice'._
- **`dan_032`** · DE+EN · Bibelstelle  
  Die Frage verweist auf Daniel 11:5-6, die bibleReference ist aber nur Daniel 11:5. Dort kommt nur der König des Südens vor, der König des Nordens erst in V. 6.  
  ✏️ _bibleReference in DE und EN auf 'Daniel 11:5-6' ändern._

</details>

<details>
<summary><b>28_hosea.json</b> – 1 kleinere Befunde</summary>

- **`hos_005, hos_006, hos_007, hos_009, hos_010, hos_011, hos_012, hos_013, hos_014, hos_015, hos_016, hos_017, hos_018, hos_019, hos_020, hos_025, hos_026, hos_027, hos_028, hos_030, hos_031, hos_032, hos_033, hos_034, hos_036, hos_037, hos_038, hos_039, hos_040, hos_043`** · EN · DE/EN weicht ab  
  Wie in Daniel sind die EN-Distraktoren eigenständig neu formuliert und entsprechen inhaltlich nicht den DE-Optionen mit gleichem Index. Die Lösung und ihr Index stimmen überein.  
  ✏️ _Die EN-Distraktoren als Übersetzung der DE-Distraktoren mit gleichem Index anlegen._

</details>

<details>
<summary><b>29_joel.json</b> – 1 kleinere Befunde</summary>

- **`joe_005, joe_006, joe_007, joe_009, joe_010, joe_012, joe_013, joe_015`** · EN · DE/EN weicht ab  
  Die EN-Distraktoren weichen inhaltlich von den DE-Distraktoren mit gleichem Index ab. Die Lösung und ihr Index stimmen überein.  
  ✏️ _Die EN-Distraktoren an die DE-Distraktoren angleichen, z. B. joe_010 EN: 1 'The son of Amoz', 2 'The son of Hilkiah', 3 'The son of Beeri'._

</details>

<details>
<summary><b>30_amos.json</b> – 1 kleinere Befunde</summary>

- **`am_020`** · EN · Sprachfehler  
  Die EN-Lösung ist sinnentstellt formuliert: Sie sagt, der Herr habe mit dem Senkblei auf der Mauer gestanden. Laut KJV stand er auf einer mit dem Senkblei gebauten Mauer und hielt das Senkblei in der Hand.  
  ✏️ _'A plumbline, standing upon a wall made by a plumbline'_

</details>

<details>
<summary><b>32_jona.json</b> – 2 kleinere Befunde</summary>

- **`jon_006`** · DE+EN · KJV-Wortlaut  
  Die Lösung zitiert den Schluss des Gebets mit dem Zusatz 'allein'/'alone', der weder in Luther noch in der KJV steht ('die Hilfe ist des HERRN' / 'Salvation is of the LORD').  
  ✏️ _DE: 'Die Hilfe ist des HERRN' / EN: 'Salvation is of the LORD'_
- **`jon_013`** · DE+EN · Bibelstelle  
  Die Ordering-Frage umfasst Ereignisse aus Jona 1–4 (Schiff, Los, Meer, Gebet im Fisch, Rizinus). Als bibleReference ist aber nur Jona 1:3 angegeben, das lediglich das erste Ereignis enthält. Die Reihenfolge selbst (2,1,4,0,3) stimmt.  
  ✏️ _bibleReference auf 'Jona 1:3-4:8' (EN 'Jonah 1:3-4:8') erweitern_

</details>

<details>
<summary><b>34_nahum.json</b> – 1 kleinere Befunde</summary>

- **`nah_014`** · DE · Sprachfehler  
  Distraktor 3 enthält ein sinnloses Wort: 'die schwachen Becher fing' (gemeint ist wohl 'die Schwachen'). Die EN-Fassung lautet 'tore the weak in pieces'.  
  ✏️ _Als Löwin, die mit großer Grausamkeit die Schwachen zerriss_

</details>

<details>
<summary><b>35_habakuk.json</b> – 2 kleinere Befunde</summary>

- **`hab_004`** · DE · Sprachfehler  
  'Wie nimmt Habakuk … die Antwort des HERRN auf?' fragt danach, wie er die Antwort empfängt. Gemeint ist aber, wie er auf sie wartet (so auch EN 'await').  
  ✏️ _Wie erwartet Habakuk nach Habakuk 2:1 die Antwort des HERRN?_
- **`hab_016`** · DE · Sprachfehler  
  'Wem gleicht der HERR … die Füße des Propheten?' heißt wörtlich 'Wem ähnelt der HERR'. Gemeint ist 'Wem macht der HERR die Füße gleich'.  
  ✏️ _Wie macht der HERR nach Habakuk 3:19 die Füße des Propheten? / Wem macht der HERR … die Füße gleich?_

</details>

<details>
<summary><b>36_zephanja.json</b> – 4 kleinere Befunde</summary>

- **`zef_007`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind in DE und EN völlig verschieden: DE beschreibt Gegenbilder (treue Priester, weise Hirten, gerechte Richter), EN nennt andere Tiere (bears/eagles, dumb dogs/jackals, wild bulls/serpents). Auch die Fragestellung weicht leicht ab ('Führer Jerusalems' vs. 'princes and judges').  
  ✏️ _EN-Distraktoren an DE angleichen: 0 'Her priests are faithful and teach the law in truth', 1 'Her princes are wise shepherds that care for the flock', 2 'Her judges are just and respect no persons'_
- **`zef_010`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren passen pro Index nicht zusammen: DE 1 Jojakim vs. EN 1 Hezekiah, DE 3 Hiskia vs. EN 3 David son of Jesse.  
  ✏️ _EN: 1 'In the days of Jehoiakim the son of Josiah', 2 'In the days of Manasseh the son of Hezekiah', 3 'In the days of Hezekiah the son of Ahaz'_
- **`zef_012`** · DE+EN · DE/EN weicht ab  
  Die Tor-Distraktoren unterscheiden sich pro Index: DE Wassertor/Rosstor/Schaftor vs. EN sheep/dung/corner gate.  
  ✏️ _EN: 0 'From the water gate', 1 'From the horse gate', 2 'From the sheep gate'_
- **`zef_018`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 weichen inhaltlich ab: DE 1 'neuen Bund' vs. EN 1 'foreign king', DE 2 'Ihren König … Richter' vs. EN 2 'Her reproach … earthly rod', DE 3 'Ihre Mauern' vs. EN 3 'Her sorrow'.  
  ✏️ _EN: 1 'Her law, and he hath given her a new covenant', 2 'Her king, and he hath set over her a judge', 3 'Her walls, and he hath opened her gates'_

</details>

<details>
<summary><b>38_sacharja.json</b> – 16 kleinere Befunde</summary>

- **`sach_006`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind in DE und EN verschieden: DE 0 'Vor ihm fliehen', 1 'Ihn mit Opfern ehren', 3 'Ihm Lob singen' vs. EN 0 'offer sacrifices and come with songs', 1 'assemble in Jerusalem', 3 'bow down … and weep'.  
  ✏️ _EN: 0 'Flee before him, for he is raised up out of his holy habitation', 1 'Honour him with sacrifices, for…', 3 'Sing praises unto him, for…'_
- **`sach_010`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren weichen inhaltlich ab: DE 0 'durch den König', 1 'durch deine Macht', 3 'durch die Priester' vs. EN 0 'gold or silver / law of Moses', 1 'wisdom of men / host of angels', 3 'swords or bows / arm of my covenant'.  
  ✏️ _EN: 0 'It shall be done by the king that leadeth the host', 1 'It shall be done by thy might, and thine arm shall finish the temple', 3 'It shall be done by the priests that build the house of the LORD'_
- **`sach_012`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren haben in DE und EN bei gleichem Index einen anderen Inhalt.  
  ✏️ _EN-Optionen 1–3 an DE angleichen: 'The two witnesses…', 'The two kings of Judah and Israel…', 'The two shepherds that feed the flock of the LORD'._
- **`sach_015`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN: 0 'Into the wilderness, to pitch a tent for it', 1 'Into Egypt, to build it a sanctuary', 2 'Into the temple at Jerusalem, to prepare a place for it'._
- **`sach_017`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 nennen in DE und EN andere Personen.  
  ✏️ _Personen angleichen, z. B. EN 2 'Upon the head of David the son of Jesse', EN 3 'Upon the head of the king, the son of Josiah'._
- **`sach_025`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN einen anderen Inhalt.  
  ✏️ _EN 3: 'Just and a prince, on foot with his army and the ark of the covenant before him'._
- **`sach_027`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 sind in DE und EN vertauscht bzw. haben einen anderen Inhalt.  
  ✏️ _Reihenfolge der EN-Distraktoren an DE anpassen (0 ransom, 1 priests/sacrifice, 2 sword of the king)._
- **`sach_028`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`sach_030`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN: 0 'He will send messengers to call them', 1 'He will call them with trumpets', 3 'He will fetch them by force'._
- **`sach_031`** · DE+EN · DE/EN weicht ab  
  Die Distraktor-Namen der Stäbe sind in DE und EN verschieden.  
  ✏️ _EN: 0 'Peace and Blessing', 1 'Judgment and Grace', 2 'Might and Wisdom'._
- **`sach_032`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren haben in DE und EN andere Beträge und Empfänger.  
  ✏️ _EN-Distraktoren an DE angleichen (Twenty pieces of silver … smith; Fifty pieces of silver … priest; An hundred pieces of silver … money changer)._
- **`sach_033`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 2: 'He will send angels to guard the flock'; EN 3: 'He will gather the flock himself and lead it to pasture'._
- **`sach_035`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`sach_036`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN: 1 'mourning for a king and a prince', 2 'mourning for a friend and companion', 3 'mourning for a prophet and servant of the LORD'._
- **`sach_037`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`sach_039`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._

</details>

<details>
<summary><b>39_maleachi.json</b> – 11 kleinere Befunde</summary>

- **`mal_004`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`mal_005`** · DE+EN · DE/EN weicht ab  
  DE fragt nach der Entlassung der Ehefrau, die Lösung lautet 'bedeckt sein Kleid mit Frevel'. EN fragt allgemein nach 'marriage', die Lösung lautet 'He hateth putting away …'. Die Lösungen haben also einen unterschiedlichen Inhalt, und auch alle Distraktoren weichen ab. Dazu kommt ein Rechtschreibfehler in EN-Option 2: 'permiteth' statt 'permitteth'.  
  ✏️ _EN-Lösung: 'He hateth putting away, for one covereth violence with his garment'; EN-Frage: '… concerning putting away a wife'; 'permiteth' korrigieren zu 'permitteth'; Distraktoren angleichen._
- **`mal_006`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`mal_007`** · DE · Mehrere richtig  
  Der DE-Distraktor 1 ('Den Propheten Elia, der den Weg bereitet, und dann den Engel des Bundes') ist nach Mal 4:5 und Mt 11:10-14 (der Wegbereiter von Mal 3:1 = Johannes = Elia) inhaltlich vertretbar und fast gleich der markierten Lösung. Die Frage wird dadurch mehrdeutig. Im EN steht an dieser Stelle ein anderer Distraktor (Moses).  
  ✏️ _Option 1 durch einen klar falschen Distraktor ersetzen, z. B. 'Den Propheten Mose, der das Gesetz aufs Neue schreibt' (passend zu EN-Option 1)._
- **`mal_010`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 1: 'It shall come as a thief, and the proud shall be as chaff'; EN 3: 'It shall bring drought, and the proud shall be as withered grass'._
- **`mal_011`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN einen anderen Inhalt bzw. stehen an anderer Stelle.  
  ✏️ _EN: 0 'The light of the law…', 1 'The morning star…', 2 'The moon of blessing…'._
- **`mal_013`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt bzw. stehen an anderer Stelle.  
  ✏️ _EN-Reihenfolge und -Inhalt an DE anpassen._
- **`mal_014`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`mal_015`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 0: 'The peace of the land, that men may find refuge with him'; EN 3: 'The offerings, that the gifts be brought by his hand'._
- **`mal_016`** · EN · KJV-Wortlaut  
  Die EN-Lösungen geben sich als die Fragen aus Mal 2:10 aus, ergänzen aber 'of old' und 'in heaven'. 'in heaven' legt aus, wer der Vater ist. Das steht nicht im KJV und auch nicht in der DE-Fassung. Außerdem weicht EN-Distraktor 0 ab ('inheritance' statt 'eigenen Gott').  
  ✏️ _EN-Option 2: 'Hath not one God created us?'; EN-Option 3: 'Have we not all one father?'; EN-Option 0: 'Hath not every tribe its own god?'_
- **`mal_018`** · DE+EN · KJV-Wortlaut  
  Die Lösung ergänzt 'in Ewigkeit' bzw. 'for evermore'. Das steht weder bei Luther noch im KJV, wird aber als Wort des HERRN zitiert.  
  ✏️ _DE: 'Ich bin der HERR und wandle mich nicht'; EN: 'I am the LORD, I change not'_

</details>

<details>
<summary><b>40_matthaeus.json</b> – 14 kleinere Befunde</summary>

- **`mt_010`** · DE+EN · DE/EN weicht ab  
  Die Distraktor-Orte sind in DE und EN verschieden.  
  ✏️ _EN: 0 'In Jericho by Jordan', 1 'In Bethany at the mount of Olives', 3 'In Capernaum by the sea'._
- **`mt_013`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`mt_017`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`mt_019`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`mt_021`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN einen anderen Inhalt.  
  ✏️ _EN 3: 'They shall see God'._
- **`mt_025`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt bzw. stehen an anderer Stelle.  
  ✏️ _EN-Reihenfolge und -Inhalt an DE anpassen._
- **`mt_035`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 1: 'Unto a vine planted by the rivers of water'; EN 2: 'Unto a merchant seeking goodly pearls'._
- **`mt_043`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`mt_044`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 2: 'She dipped herself seven times in Jordan'; EN 3: 'Jesus spake a word of power over her'._
- **`mt_048`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen._
- **`mt_050`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 1: 'He that no longer honoureth nor supporteth his parents is worthy'; EN 3: 'He that giveth all his inheritance unto the poor is worthy of him'._
- **`mt_063`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 1: 'He had it set in gold by the goldsmith'; EN 2: 'He brought it as an offering into the temple'._
- **`mt_133`** · DE · Inhaltlicher Fehler  
  Die DE-Lösung spricht von einem "Purpurmantel". Die angegebene Stelle Mt 27:28 nennt aber einen scharlachroten Mantel (Purpur steht bei Mk 15:17). EN sagt korrekt "scarlet robe". Außerdem haben die Distraktoren 0, 2 und 3 in DE und EN verschiedene Inhalte.  
  ✏️ _DE-Option 1: "Sie setzten ihm eine Dornenkrone auf und legten ihm einen scharlachroten Mantel um"._
- **`mt_148`** · DE+EN · Bibelstelle  
  Die Ordering-Frage reicht vom Passahmahl bis zur Auferstehung (Mt 26-28). Die bibleReference nennt aber nur Mt 26:26, wo allein das Brotbrechen beschrieben wird.  
  ✏️ _bibleReference auf "Matthäus 26:17-28:10" (EN: "Matthew 26:17-28:10") ändern._

</details>

<details>
<summary><b>41_markus.json</b> – 22 kleinere Befunde</summary>

- **`mk_015`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 haben in DE und EN unterschiedlichen Inhalt. Dabei ist EN 1 ('The disciples who left all') teilweise plausibel, denn Jesus deutet in V. 34 auf die, die um ihn saßen.  
  ✏️ _EN: 0 'All the inhabitants of Nazareth', 1 'The chief priests and scribes', 2 'The chief men of Galilee'_
- **`mk_016`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN 3: 'It brought forth fruit abundantly, because it had no depth of earth'_
- **`mk_017`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN: 0 'The works of men', 2 'Earthly riches', 3 'The tradition of the elders'_
- **`mk_018`** · DE+EN · DE/EN weicht ab  
  DE fragt nach dem Gleichnis vom unbemerkten Wachstum, EN fragt, welches Gleichnis nur bei Markus steht. Das sind zwei verschiedene Fragen, auch wenn die Lösung dieselbe ist.  
  ✏️ _EN: 'Which parable describeth the secret growth of the kingdom of God?'_
- **`mk_019`** · DE+EN · DE/EN weicht ab  
  DE-Distraktoren sind Bäume oder Pflanzen (Feigenbaum, Mandelbaum, Weinstock), EN-Distraktoren sind Körner (wheat, corn, olive seed). Auch die Fragen unterscheiden sich ('womit' vs. 'unto what grain').  
  ✏️ _Eine Variante für beide Sprachen wählen, z. B. EN: 'Unto a fig tree', 'Unto an almond tree', 'Unto a vine'_
- **`mk_022`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 nennen in DE und EN verschiedene Namen.  
  ✏️ _Gleiche Namen in beiden Sprachen verwenden (z. B. DE 1 'Belial', DE 3 'Apollyon')_
- **`mk_023`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren wörtlich an DE angleichen_
- **`mk_024`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN 2: 'She washed three times in Jordan', EN 3: 'Jesus spake a word of power over her'_
- **`mk_025`** · DE+EN · DE/EN weicht ab  
  Die Zusätze in den Distraktoren 0 und 3 unterscheiden sich.  
  ✏️ _Zusätze vereinheitlichen, z. B. EN 0 '... and she opened her eyes'_
- **`mk_055`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren sind in DE und EN völlig verschiedene Gegenfragen.  
  ✏️ _EN-Distraktoren an DE angleichen (oder umgekehrt)_
- **`mk_057`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 2 sind zwischen DE und EN inhaltlich vertauscht oder verändert.  
  ✏️ _Reihenfolge der EN-Distraktoren 0 und 2 an DE angleichen_
- **`mk_058`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen_
- **`mk_059`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen_
- **`mk_060`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren in der DE-Reihenfolge und mit DE-Inhalt neu formulieren_
- **`mk_061`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen_
- **`mk_062`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen_
- **`mk_063`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen_
- **`mk_064`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen_
- **`mk_065`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 nennt in DE und EN verschiedene Personengruppen.  
  ✏️ _EN 2: 'The scribes, who have reckoned it'_
- **`mk_066`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren haben andere Inhalte, Personen und Zahlen: DE dreißig Silberlinge vs. EN vierzig Schekel, DE Füße mit Tränen gewaschen vs. EN mit Brunnenwasser, DE leinenes Gewand vs. EN Purpurgewand eines Obersten.  
  ✏️ _EN-Distraktoren an DE angleichen (gleiche Zahl und Person)_
- **`mk_067`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 1 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN: 0 'A blind beggar at the city gate', 1 'A white lamb in the market place'_
- **`mk_079`** · DE · Sprachfehler  
  'verkündigt das Evangelium der Schöpfung' liest sich als Genitiv ('Evangelium über die Schöpfung'). Gemeint ist der Dativ ('der ganzen Schöpfung' = allen Geschöpfen). Durch das weggelassene 'ganzen' verschiebt sich der Sinn.  
  ✏️ _'Geht hin in alle Welt und verkündigt das Evangelium der ganzen Schöpfung'_

</details>

<details>
<summary><b>42_lukas.json</b> – 29 kleinere Befunde</summary>

- **`lk_017`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 nennen in DE und EN verschiedene Propheten.  
  ✏️ _EN: 2 'The book of the prophet Daniel', 3 'The book of the prophet Malachi'_
- **`lk_018`** · EN · Sprachfehler  
  In der KJV-nahen Lösung fehlt der Artikel.  
  ✏️ _'They were filled with wrath, and thrust him out of the city'_
- **`lk_018`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN unterschiedlichen Inhalt: DE Anbetung / Königsausrufung / 'bleib bei uns' vs. EN 'received with joy' / 'asked for miracles' / 'brought their sick'.  
  ✏️ _EN-Distraktoren an DE angleichen, z. B. 1: 'They led him in triumph through the city and proclaimed him king'_
- **`lk_020`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben in DE und EN unterschiedlichen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen_
- **`lk_024`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 nennen in DE und EN verschiedene Personen (DE Matthäus/Barabbas, EN Simon der Pharisäer/Nikodemus).  
  ✏️ _DE an EN angleichen (siehe Befund zu Matthäus)_
- **`lk_026`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN völlig verschiedenen Inhalt (DE 0 Ährenlese-Gesetz gegenüber EN 0 Aufhebung des Sabbats; DE 1 Brauch der Väter gegenüber EN 1 Leugnen der Tat; DE 3 Erlaubnis des Statthalters gegenüber EN 3 Feuer vom Himmel).  
  ✏️ _EN-Distraktoren sinngemäß aus DE übernehmen, z. B. 0 'By the law of gleaning that suffereth the poor to glean', 1 'By the custom of the fathers who walked and ate on the sabbath', 3 'By the leave of the governor who opened the fields'_
- **`lk_029`** · DE+EN · DE/EN weicht ab  
  Distraktor 0 hat einen anderen Inhalt: DE 'Euch gehört Reichtum und Ehre', EN 'For they shall inherit the whole earth' (eine Seligpreisung aus Mt 5:5 für die Sanftmütigen).  
  ✏️ _EN 0: 'Yours are riches and honour'_
- **`lk_030`** · DE · Sprachfehler  
  Die richtige Option ist grammatisch falsch: 'dem er tief gegraben hat' ergibt keinen Sinn, gemeint ist 'nachdem er tief gegraben hatte'.  
  ✏️ _'Auf einen Felsen, nachdem er tief gegraben hatte'_
- **`lk_058`** · DE+EN · DE/EN weicht ab  
  DE fragt allgemein nach einem Schöpfungsbeispiel (Ameisen/Fische/Raben/Schafe), EN nur nach Vögeln (eagles/sparrows/ravens/doves). Die Distraktoren unterscheiden sich bei gleichem Index.  
  ✏️ _Angleichen, z. B. EN 'Which creatures did Jesus bid His disciples consider …?' mit 'The ants / The fishes / The ravens / The sheep'_
- **`lk_059`** · DE+EN · DE/EN weicht ab  
  DE fragt nach dem Ort des Herzens und hat Orts-Distraktoren (Vorratshaus des Tempels, Paläste, Acker). EN fragt allgemein nach einer Aussage über das Herz und hat inhaltlich andere Distraktoren (Gold macht das Herz froh, geteiltes Herz …).  
  ✏️ _EN-Frage und Distraktoren an DE angleichen: 'Where did Jesus say a man's heart will be?' – 0 'In the storehouse of the temple', 1 'In the palaces of kings', 2 'Under the earth in the field'_
- **`lk_060`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1-3 unterscheiden sich inhaltlich: DE 'aus dem Haus gejagt / Lohn zurückzahlen / dreißig Tage eingekerkert', EN 'few stripes / outer darkness / pardoned'.  
  ✏️ _Eine Fassung an die andere angleichen, z. B. EN 1 'He shall be driven out of the house for ever', 2 'He shall repay his wages', 3 'He shall be cast into prison thirty days'_
- **`lk_062`** · DE+EN · DE/EN weicht ab  
  Der Distraktor mit Index 3 nennt eine andere Zahl: DE 'Zwanzig Jahre', EN 'Thirty years'.  
  ✏️ _EN 3: 'Twenty years' (oder DE 3: 'Dreißig Jahre')_
- **`lk_064`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1-3 unterscheiden sich: DE 'goldene Tor des Tempels / breite Straße der Menge / offenes Tor der Gnade', EN 'wide door / high wall / broad path'.  
  ✏️ _EN: 1 'Through the golden gate of the temple', 2 'By the broad way of the multitude', 3 'Through the open gate of grace'_
- **`lk_066`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich bei gleichem Index: DE 0 Aussatz / 1 Blindheit / 3 Stummheit, EN 0 palsy / 1 leprosy / 3 fever.  
  ✏️ _EN: 'The leprosy / Blindness / The dropsy / Dumbness'_
- **`lk_069`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE 'Kauf eines Ackers / zehn Joch Ochsen / Bau eines Schiffes', EN 'city wall / great well / new vineyard'.  
  ✏️ _EN: 0 'Buying a piece of ground', 2 'Buying ten yoke of oxen', 3 'Building a ship'_
- **`lk_070`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 1 unterscheiden sich: DE 0 'im Feuer verbrannt, Asche auf die Felder' gegenüber EN 0 'salted again by fire'; DE 1 'den Tieren zu fressen gegeben' gegenüber EN 1 'kept within the storehouse'.  
  ✏️ _EN: 0 'It is burned in the fire and its ashes strewn upon the fields', 1 'It is given unto the cattle in the stall'_
- **`lk_079`** · DE · Sprachfehler  
  Die Frage 'Wo befand sich …' verlangt den Dativ, die Optionen stehen aber im Akkusativ ('Auf den heiligen Berg', 'In den Garten', 'In das Paradies'). Außerdem sind die EN-Distraktoren 1 und 2 gegenüber DE vertauscht bzw. abgewandelt (EN 1 'garden of paradise', EN 2 'glory of heaven').  
  ✏️ _Frage: 'Wohin wurde der arme Lazarus nach seinem Sterben getragen?' (passt zu den Akkusativ-Optionen und zu EN 'carried by the angels')_
- **`lk_082`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat einen anderen Inhalt: DE 'Drei Männer kehrten um, darunter zwei Priester', EN 'None of them returned'.  
  ✏️ _EN 3: 'Three returned, among them two priests of Jerusalem'_
- **`lk_096`** · DE · Sprachfehler  
  Falscher Artikel: 'Welches Gegenfrage' statt 'Welche Gegenfrage'.  
  ✏️ _'Welche Gegenfrage stellte Jesus den Hohenpriestern auf die Frage nach Seiner Vollmacht?'_
- **`lk_099`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 unterscheiden sich: DE 'Essener / Zeloten', EN 'Herodians / Essenes'.  
  ✏️ _EN: 1 'The Essenes', 2 'The Zealots'_
- **`lk_101`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich: DE 'Zehn Kupfermünzen / Einen goldenen Denar', EN 'Ten pieces of silver / A golden half-shekel'.  
  ✏️ _EN: 2 'Ten pieces of brass', 3 'A golden denarius'_
- **`lk_102`** · DE+EN · DE/EN weicht ab  
  DE fragt nach den Vorboten des Endes, EN nach Zeichen vor der Zerstörung des Tempels. Alle drei Distraktoren haben in DE und EN einen anderen Inhalt, z. B. DE 0 'langer Weltfriede' gegenüber EN 0 'parting of the Jordan, falling of stars …'.  
  ✏️ _Die Fragen angleichen (z. B. beide: 'Welche Zeichen nannte Jesus auf die Frage, wann der Tempel zerstört werde?') und die Distraktoren in DE und EN inhaltlich gleich gestalten._
- **`lk_103`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 unterscheiden sich: DE 'Bis alle Römer das Land verlassen / Bis hundert Jahre vergangen sind', EN 'Until seventy weeks are accomplished / Until all the tribes return from exile'.  
  ✏️ _EN: 1 'Until all the Romans depart the land', 2 'Until an hundred years be passed'_
- **`lk_105`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE 'Haus in Rom / Tempelvorhof / Wüste am Jordan', EN 'Capernaum / palace of Pilate / Nazareth'.  
  ✏️ _EN: 0 'In a house at Rome', 2 'In the court of the temple', 3 'In the wilderness by Jordan'_
- **`lk_108`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1-3 unterscheiden sich inhaltlich. Der EN-Distraktor 2 'Who should sit on the right hand of the Master' (Mk 10:37) liegt sehr nah an der Lösung (Streit um den Größten), DE 2 lautet dagegen 'Wer das Passalamm schlachten dürfe'.  
  ✏️ _EN-Distraktoren an DE angleichen: 1 'Who should give the most money', 2 'Who should kill the passover lamb', 3 'Which of them should remain in Jerusalem'_
- **`lk_110`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich bei Index 0, 1 und 3 (DE 0 Stimme und Licht gegenüber EN 0 Blindheit, DE 1 Erdbeben gegenüber EN 1 Engelheere). Der EN-Distraktor 1 ('Legions of holy angels surrounded him and bore him up') liegt nahe an V.43 ('there appeared an angel unto him from heaven, strengthening him') und ist deshalb teilweise wahr und irreführend.  
  ✏️ _EN-Distraktoren an DE angleichen: 0 'A voice spake from heaven, and the disciples saw a great light', 1 'The earth quaked in the garden, and the disciples fell asleep for fear', 3 'The stars were darkened and blackness lay upon mount Olivet'_
- **`lk_111`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 unterscheiden sich: DE 'Statthalter von Samaria / Hoher Rat nach Alexandria', EN 'ruler of Tyre / council of Athens'.  
  ✏️ _EN: 1 'Unto the governor of Samaria', 2 'Unto the council at Alexandria'_
- **`lk_113`** · EN · Sprachfehler  
  Der Artikel fehlt ('coming out of field'), und der KJV-Wortlaut ist 'out of the country'. Derselbe Fehler steht in lk_112, Distraktor 1 ('coming out of country').  
  ✏️ _'Simon of Cyrene, coming out of the country' (ebenso in lk_112 Option 1)_
- **`lk_118`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 lautet in DE 'Beim gemeinsamen Abendgebet', in EN 'When he blessed the evening cup'. Die EN-Fassung liegt sehr nah an der richtigen Antwort, denn er segnete das Brot (V. 30).  
  ✏️ _EN 3: 'At their common evening prayer'_

</details>

<details>
<summary><b>43_johannes.json</b> – 31 kleinere Befunde</summary>

- **`joh_008`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _EN 2: 'Of the sanctuary of the Samaritans'; EN 3: 'Of God's dwelling place in heaven'_
- **`joh_009`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_010`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_012`** · DE+EN · Inhaltlicher Fehler  
  Gefragt wird nach der Bedingung für das SEHEN des Reiches Gottes (V. 3: 'von neuem geboren'). Die Lösung zitiert aber V. 5, die Bedingung für das EINGEHEN. Frage und Antwort passen nicht genau zusammen.  
  ✏️ _Frage ändern in 'Welche Bedingung nannte Jesus für das Eingehen in das Reich Gottes?' / EN: 'What condition did Jesus declare for entering into the kingdom of God?'_
- **`joh_014`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_015`** · DE+EN · Sprachfehler  
  Das großgeschriebene Ehrfurchtspronomen 'Seines' bezieht sich hier auf Johannes den Täufer statt auf Christus. Zusätzlich haben die DE-Distraktoren 0–2 einen völlig anderen Inhalt als die EN-Distraktoren mit gleichem Index.  
  ✏️ _'... bezüglich seines Verhältnisses zu Christus?' und die Distraktoren angleichen._
- **`joh_017`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_022`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_024`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_026`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren haben in DE und EN andere Zahlen bzw. Inhalte.  
  ✏️ _EN-Distraktoren an DE angleichen: 'Five loaves and three fishes', 'Seven loaves and a few small fishes', 'Ten loaves for the apostles'._
- **`joh_028`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_029`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_030`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_036`** · DE+EN · DE/EN weicht ab  
  Die DE-Distraktoren 1–3 sind Varianten von 'werfe den ersten Stein'. Die EN-Distraktoren mit gleichem Index haben einen ganz anderen Inhalt.  
  ✏️ _EN-Distraktoren angleichen, z. B. 'He that knoweth the law by heart, let him first cast a stone at her' usw._
- **`joh_045`** · DE+EN · DE/EN weicht ab  
  Laut DE offenbarte Jesus sich als 'Menschensohn', laut EN als 'Son of God'. Der hinterlegte DE-Text (V. 35) hat ebenfalls 'Sohn Gottes'. Außerdem fügt die EN-Lösung 'with joy' hinzu, das im KJV nicht steht. Die Distraktoren 0, 2 und 3 unterscheiden sich inhaltlich zwischen DE und EN.  
  ✏️ _DE: '... als Jesus Sich ihm als Sohn Gottes offenbarte?' EN-Lösung: 'He said, Lord, I believe. And he worshipped him'_
- **`joh_049`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_050`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_052`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_059`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_060`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_062`** · EN · KJV-Wortlaut  
  Die EN-Lösung gibt V. 8 als wörtliche Rede wieder, ergänzt aber 'Lord' und den ungrammatischen, im KJV nicht vorhandenen Zusatz 'while the world standeth anywhere'.  
  ✏️ _'Thou shalt never wash my feet.' Distraktor 3 angleichen ('He left the room for shame ...' wie DE)._
- **`joh_063`** · DE+EN · DE/EN weicht ab  
  DE fragt, als was Jesus den Bissen bezeichnete. EN fragt, wie Jesus seinen Verräter dem Lieblingsjünger kenntlich machte. Alle Distraktoren haben einen anderen Inhalt (DE: Feindschaft/Segen/Passalamm, EN: Becher/rechte Hand/scharlachroter Mantel).  
  ✏️ _DE an EN angleichen: 'Woran sollte der Lieblingsjünger den Verräter erkennen?' – 'Der ist's, dem ich den Bissen eintauchen und reichen werde', mit übersetzten EN-Distraktoren._
- **`joh_064`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_065`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_066`** · DE · Sprachfehler  
  Kasusfehler: 'Trost' ist hier Akkusativobjekt, also 'Welchen', nicht 'Welcher'.  
  ✏️ _'Welchen Trost spendete Jesus Seinen Jüngern über das Vaterhaus?'_
- **`joh_066`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 haben in DE und EN einen anderen Inhalt (vgl. auch den separat gemeldeten Grammatikfehler).  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_083`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0–2 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_084`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1–3 haben in DE und EN einen anderen Inhalt.  
  ✏️ _Distraktoren in beiden Sprachen inhaltlich gleichsetzen._
- **`joh_085`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN einen anderen Inhalt. Die EN-Lösung ergänzt 'in all ages', das nicht im Text steht.  
  ✏️ _Distraktoren angleichen; EN-Lösung: 'For them also which shall believe on me through their word'_
- **`joh_092`** · DE · Sprachfehler  
  Das großgeschriebene Ehrenpronomen 'Er' bezieht sich hier auf Pilatus statt auf Jesus. Das ist irreführend.  
  ✏️ _'... als er Jesus dem Volk vorführte?'_
- **`joh_110`** · DE+EN · Bibelstelle  
  Die Ordering-Frage enthält die Emmaus-Erscheinung, die nur in Lukas 24 steht. Die Angabe Johannes 20:19 deckt die Reihenfolge nicht ab. Die Reihenfolge selbst ist korrekt.  
  ✏️ _Stelle erweitern auf 'Johannes 20:11-29; Lukas 24:13-36' oder die Emmaus-Option durch ein Ereignis aus Johannes ersetzen._

</details>

<details>
<summary><b>44_apostelgeschichte.json</b> – 14 kleinere Befunde</summary>

- **`apg_003`** · DE · Sprachfehler  
  Grammatikfehler: 'Welcher Name trug' (Akkusativ erforderlich).  
  ✏️ _'Welchen Namen trug die Stätte, ...'_
- **`apg_011`** · DE · Sprachfehler  
  Rechtschreibung: Die von Ortsnamen abgeleitete Form auf -er wird großgeschrieben.  
  ✏️ _'des Jerusalemer Tempels'_
- **`apg_028`** · DE · DE/EN weicht ab  
  Die DE-Option sagt 'voll Gnade', der hinterlegte DE-Text und die EN-Option sagen 'voll Glauben' (faith).  
  ✏️ _'Stephanus, voll Glauben und Kraft'_
- **`apg_083`** · DE · Sprachfehler  
  Das großgeschriebene Ehrenpronomen 'Seine' bezieht sich auf Paulus. Dasselbe gilt für apg_084 ('Seine Predigt').  
  ✏️ _'seine' kleinschreiben (apg_083 und apg_084)._
- **`apg_096`** · DE · Sprachfehler  
  Rechtschreibfehler: "viel" statt "fiel".  
  ✏️ _"Welcher Jüngling fiel während der Predigt des Paulus in Troas aus dem Fenster?"_
- **`apg_103`** · DE+EN · DE/EN weicht ab  
  Der Distraktor an Index 0 nennt in DE Titus, in EN Timotheus.  
  ✏️ _In beiden Sprachen dieselbe Person verwenden, z. B. EN "To circumcise Titus ..."_
- **`apg_105`** · DE+EN · Bibelstelle  
  23:26 nennt nur den Namen Klaudius Lysias im Briefkopf. Die Rettung vor der Menge steht in 21:31-33 bzw. 23:27.  
  ✏️ _bibleReference auf "Apostelgeschichte 23:26-27" erweitern_
- **`apg_106`** · DE · Sprachfehler  
  Das Pronomen für Paulus ist großgeschrieben.  
  ✏️ _"richtete Paulus seine Verteidigungsrede"_
- **`apg_108`** · EN · DE/EN weicht ab  
  Die EN-Frage fragt nach der Tageszeit, die Optionen beschreiben aber Arten von Lichterscheinungen. DE fragt nach der Art der Lichterscheinung. Frage und Optionen passen in EN nicht zusammen.  
  ✏️ _EN: "What appeared unto Saul about noon as he came nigh unto Damascus?"_
- **`apg_112`** · DE · Sprachfehler  
  Falscher Artikel: "Opferdienst" ist maskulin.  
  ✏️ _"Der Opferdienst im Tempel"_
- **`apg_126`** · DE · Sprachfehler  
  Das Pronomen für Paulus ist großgeschrieben, als wäre es eine Ehrfurchtsform für Gott.  
  ✏️ _"vor seiner Bekehrung"_
- **`apg_127`** · DE · Inhaltlicher Fehler  
  "Gegen den Stachel ausschlagen" ist ein griechisch-antikes Sprichwort, kein alttestamentliches Bild. EN sagt korrekt "proverb".  
  ✏️ _"Welches sprichwörtliche Bild gebrauchte die Himmelsstimme bei der Berufung?"_
- **`apg_128`** · DE · Sprachfehler  
  Das Pronomen für Paulus ist großgeschrieben.  
  ✏️ _"als Paulus seine Rede beendete"_
- **`apg_141`** · EN · DE/EN weicht ab  
  EN zitiert ein anderes Wort ("Lord, what wilt thou have me to do?", 9:6) als DE ("Wer bist du, Herr?", 9:5) und verweist im Fragetext auf 9:6, obwohl bibleReference 9:5 ist. Außerdem steht an Index 1 in DE Ananias, in EN Petrus.  
  ✏️ _EN: "Who said, 'Who art thou, Lord?' on the road to Damascus (Acts 9:5)?" mit "Ananias" an Index 1_

</details>

<details>
<summary><b>45_roemer.json</b> – 15 kleinere Befunde</summary>

- **`roem_001`** · DE · Sprachfehler  
  Das Reflexivpronomen für Paulus ist großgeschrieben.  
  ✏️ _"Wie bezeichnet sich Paulus selbst"_
- **`roem_041`** · DE · Sprachfehler  
  Das Pronomen für Paulus ist großgeschrieben.  
  ✏️ _"trägt Paulus in seinem Herzen"_
- **`roem_055`** · DE · Sprachfehler  
  Die Formulierung ist sachlich schief: ein "elf Kapitel langes Kapitel".  
  ✏️ _"Womit beschließt Paulus den lehrhaften Teil des Römerbriefs (Kapitel 1-11)?"_
- **`roem_059`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 hat in DE und EN einen anderen Inhalt: DE 'öffentlich verfluchen', EN 'Break off all fellowship'.  
  ✏️ _EN 2: 'Curse the enemy openly before all men'._
- **`roem_060`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren haben je Index einen anderen Inhalt: 1 DE Statthalter / EN Caesar, 2 DE Älteste der Gemeinde / EN Geschädigter, 3 DE Geschädigter / EN Hoherpriester.  
  ✏️ _Reihenfolge und Inhalte angleichen (z. B. EN 1 'The governor of the province', 2 'The elders of the church', 3 'The injured person himself')._
- **`roem_061`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 hat in DE und EN einen anderen Inhalt: DE 'Behörden nicht beachten', EN 'Flee ... establish separate kingdoms in the desert'. Distraktor 0 ist ebenfalls verschieden: DE Widerstand gegen gottwidrige Gesetze, EN Widerstand wegen heidnischer Herrscher.  
  ✏️ _EN 2: 'Disregard the authorities, for God alone is Lord of the faithful'._
- **`roem_062`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 haben einen anderen Inhalt: DE 1 prächtige Bauten / EN 1 heidnische Statuen und Altäre, DE 3 Heidengötter und Staatsreligion / EN 3 Eroberungskriege.  
  ✏️ _EN 1 'To erect magnificent buildings displaying the might of Rome', EN 3 'To enforce the heathen gods and the state religion'._
- **`roem_063`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 sind inhaltlich vertauscht bzw. verschieden: DE 0 Steuern zahlen / EN 0 nie Geld leihen, DE 1 Geld ausleihen / EN 1 Steuern zurückhalten, DE 2 gemeinsamer Hausbau / EN 2 Zuneigung nur zur Familie.  
  ✏️ _Die Distraktoren 1:1 übertragen (EN 0 'The payment of all taxes', 1 'The lending of money', 2 'The building of houses together')._
- **`roem_064`** · DE+EN · DE/EN weicht ab  
  Alle drei Distraktoren unterscheiden sich: DE Opfer ersetzen / Fasten überflüssig / von allen gelobt, EN Gerichte nutzlos / entschuldigt Sünde / goldener Altar.  
  ✏️ _EN-Distraktoren an DE angleichen (replaceth all sacrifices / maketh fasting needless / is praised of all men)._
- **`roem_065`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE heimlich erforschen / verspotten / der Obrigkeit melden, EN in Höhlen fliehen / neue Feste / nur nachts beten.  
  ✏️ _Die Distraktoren in beiden Sprachen inhaltlich gleich fassen._
- **`roem_067`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE Beschneidung / Steuern / Hausbau, EN Synagogenbau / Ordination von Ältesten / Gebetsriemen.  
  ✏️ _EN 0 'The circumcision of believing Gentiles', 1 'The paying of tribute unto Caesar', 2 'The building of houses and churches'._
- **`roem_074`** · DE · Sprachfehler  
  Das Possessivpronomen für Paulus ist großgeschrieben. Die Großschreibung als Ehrerbietung gilt Gott bzw. Christus, nicht Paulus. Dasselbe in roem_075 ('vor Seiner Romreise').  
  ✏️ _'nach seinem beabsichtigten Besuch in Rom' (und in roem_075 'vor seiner Romreise')_
- **`roem_075`** · DE · Sprachfehler  
  Das Pronomen für Paulus ist großgeschrieben.  
  ✏️ _'vor seiner Romreise'_
- **`roem_077`** · DE · Sprachfehler  
  'wog den eigenen Hals' ist falsches Verb (wiegen). Gemeint ist 'wagte' bzw. 'hielt hin'.  
  ✏️ _'Welches Ehepaar hat für das Leben des Paulus den eigenen Hals hingehalten?'_
- **`roem_080`** · DE · Sprachfehler  
  Die Frage ist ungrammatisch ('verfasste ... im Gruße'). 'Verfasste' legt außerdem Autorschaft nahe, Tertius war aber nur der Schreiber.  
  ✏️ _'Welcher Schreiber, der den Brief niederschrieb, grüßt die Römer in Römer 16,22?'_

</details>

<details>
<summary><b>46_1_korinther.json</b> – 50 kleinere Befunde</summary>

- **`1kor_004`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich: DE strenger Richter / Tempelbaumeister, EN Prophet wie Mose / Gesetzeslehrer.  
  ✏️ _EN 2 'A stern judge', EN 3 'A new builder of the temple'._
- **`1kor_005`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich: DE Gelehrte des Tempels / Könige der Nationen, EN athenische Philosophen / reiche Kaufleute.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_006`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE Stolz / Reichtum / Zorn, EN Prunk / Philosophenworte / bewaffnete Wachen.  
  ✏️ _Die Distraktoren in beiden Sprachen inhaltlich angleichen._
- **`1kor_009`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 2 unterscheiden sich: DE 0 Gesetz verbietet es / EN 0 Statuten Moses nicht erforscht, DE 2 keine Schriften und Lehrer / EN 2 Gott hat ihn absichtlich verblendet.  
  ✏️ _EN 2: 'Because he hath no scriptures nor teachers to learn the truth'._
- **`1kor_010`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE Sinn der Alten / der Philosophen / der Gesetzeslehrer, EN geheime Traditionen / römische Gerichtsbarkeit / weltliche Disputation. Auch der Fragefokus weicht leicht ab ('Welchen Sinn' vs. 'What possession enables to judge').  
  ✏️ _EN: 'What mind have the spiritual believers?' mit Distraktoren 'the mind of the ancients/philosophers/lawyers'._
- **`1kor_011`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 unterscheiden sich: DE Weise und Gelehrte / Feinde des Evangeliums, EN fremde Heiden / heilige Propheten.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_012`** · DE+EN · DE/EN weicht ab  
  Die DE-Distraktoren bleiben im Landwirtschaftsbild (erntete/säte, pflügte/mähte, sammelte/verkaufte), die EN-Distraktoren nicht (Zehnten, Gemeindeleitung, eigene Kraft). Zusätzlich ist das Pronomen für Paulus großgeschrieben ('für Seinen Dienst').  
  ✏️ _EN 1 'Paul reaped, Apollos sowed; but God gave the fruit' usw. In DE 'für seinen Dienst' schreiben._
- **`1kor_015`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 2 unterscheiden sich: DE weltlicher Rat der Stadt / Diener der Könige, EN Provinz unter Rom / geheimer Bund.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_016`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich: DE Richter der Gemeinde / Könige der Weltzeit, EN Philosophen / opfernde Priester.  
  ✏️ _EN 2 'As judges of the church', EN 3 'As kings of this age reigning in Christ's name'._
- **`1kor_018`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE eigene Werke prüfen / Lehren beurteilen / Sünder züchtigen, EN Brüder sofort verdammen / an römische Richter ausliefern / Gerichte einrichten.  
  ✏️ _Die Distraktoren in beiden Sprachen inhaltlich gleich fassen._
- **`1kor_019`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE Siegeszug / Heer / Hofstaat, EN herrschende Könige / reiche Herren / Weisheitslehrer.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_021`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind verschieden bzw. verschoben: DE 0 stahl Gemeindegut / EN 0 Steuern verweigert, DE 2 Treuegelöbnis verweigert / EN 2 Götzendienst, DE 3 Götzendienst / EN 3 Diakone veruntreuen.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_022`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 unterscheiden sich: DE dreijähriges Fasten / in andere Stadt schicken, EN nach Jerusalem schicken / tägliches Fasten im Heiligtum.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_023`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 unterscheiden sich: DE kranker Baum / trüber Quell, EN Tropfen Galle / Wurm im Weinberg.  
  ✏️ _EN 1 'A sick tree that beareth no fruit', EN 2 'A muddy spring that fouleth the whole brook'._
- **`1kor_025`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich: DE Geschenk zur Umkehr / römische Richter, EN Zivilgerichte / Vergehen übersehen und Leitung geben.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_026`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE Habgier / römisches Recht gebrochen / beim Prozess gehungert, EN falsche Gewichte / Witwen vernachlässigt / Gelübde nicht erfüllt.  
  ✏️ _Die Distraktoren in beiden Sprachen inhaltlich gleich fassen._
- **`1kor_027`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE Städte regieren / Gesetz auslegen / Heiligtum verwalten, EN Mauern Roms bauen / Legionen befehligen / Priester in Jerusalem.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_028`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE Arme und Kranke / Ungelehrte im Gesetz / Fremde, EN Besitzlose / Unkundige der griechischen Philosophie / ohne Pilgerfahrt.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_031`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 unterscheiden sich: DE Mann herrscht rücksichtslos / Frau rechtlos / Enthaltsamkeit stets geboten, EN Frau ewig schweigend / Mann entlässt nach Belieben / dauerhafte Trennung.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_032`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich: DE Ehe nur sieben Jahre / Wiederheirat leicht möglich, EN Entlassung ohne Söhne / Ehe nichtig durch Taufe.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_033`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich, teils auch in der Person: DE 2 der Ungläubige muss das Haus verlassen / EN 2 der Gläubige muss weggehen, DE 3 verliert Rechte am Kind / EN 3 Gemeindezucht, DE 0 verdammt / EN 0 Ehe aufzulösen.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_034`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 unterscheiden sich: DE Sklave fliehe / in die Wüste ziehen, EN Freiheit mit geliehenem Gold kaufen / nach Jerusalem ziehen.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_037`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich: DE Götzen lenken das Schicksal / mächtiger als Engel, EN Götzenopfer für den Frieden / Bildnis mit lebender Seele.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_039`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE kein Opfer / nicht fasten / Älteste verbieten es, EN Schriftstudium / Almosen ohne Älteste / Heidenpredigt.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_040`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE nie mehr nach Korinth / nie mehr beschneiden lassen / nur im Tempel dienen, EN nicht vor Schwachen predigen / Schwache zwingen / sich zurückziehen.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_041`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE predigen / Briefe schreiben / taufen und lehren, EN taufen / Schriftrollen tragen / Älteste einsetzen.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_042`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 3 unterscheiden sich: DE nicht stehlen / Sabbat heiligen, EN Geländer am Dach / Schuldenerlass.  
  ✏️ _EN 0 'Thou shalt not steal', EN 3 'Remember the sabbath day, to keep it holy'._
- **`1kor_043`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 unterscheiden sich: DE Wunder / Städte gegründet / allgemein gelobt, EN Reichtum / Titel / Freiheit von Verfolgung.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_045`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 ist verschieden: DE Wurfspiel, EN Ringkampf.  
  ✏️ _EN 3: 'Throwing contests upon the field for the city's wreath'._
- **`1kor_050`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 ist verschieden: DE Umgang mit Menschen meiden, EN Speisetraditionen der Ältesten.  
  ✏️ _EN 3: 'Avoid all fellowship with men'._
- **`1kor_051`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 1 unterscheiden sich: DE vertauschte Hauptschaft Mann/Gott/Frau, EN Caesar/Magistrat bzw. Hohepriester/Diakon.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_052`** · DE+EN · DE/EN weicht ab  
  Alle Distraktoren unterscheiden sich: DE Staubschutz / Gesetz Moses / römische Sitte, EN Gesetze Korinths / Zutritt zum Heiligtum / Gesicht verbergen.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_053`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE Brot verkauft / Wein verweigert / Fremde ausgeschlossen, EN Tieropfer / heidnische Hymnen / Eintrittsgeld.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_054`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 unterscheiden sich: DE Zeichen der Liebe / Brot zum Fasten / Ernteglück, EN Befreiung aus Ägypten / Lohn für Tempelbesuch / Brot des Elends.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_055`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE Besitzverlust / Verbannung aus der Stadt / Tempelverbot, EN Bürgerrechtsverlust / Geldstrafe / Gefängnis.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_056`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 unterscheiden sich: DE Jesus großer Prophet / Gott Schöpfer / Tora heilig, EN Mose der Prophet / Gesetz ewig / Tempel heilig.  
  ✏️ _EN 1 'That Jesus is a great prophet', EN 2 'That God is the Creator', EN 3 'That the law is holy'._
- **`1kor_058`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE Gesetzeserfüllung / gemeinsame Stadt und Besitz / Apostelbeschluss, EN kaiserlicher Bund / Treueeid / gleiche Geldbeiträge.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_059`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind vertauscht bzw. verschieden: DE 1 keine Speise / EN 1 frei von Krankheit, DE 2 unsterblich / EN 2 keine Speise, DE 0 besonders stark / EN 0 göttliche Vollkommenheit.  
  ✏️ _Reihenfolge und Inhalt der Distraktoren angleichen._
- **`1kor_060`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE Weg der Wunder / strenge Zucht / Fasten, EN Kirchenregierung / Handel / militärische Disziplin.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_061`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 unterscheiden sich: DE weise und bewundert / reich belohnt im Himmel / von Sünden frei, EN erhöhter Prophet / Redner / heiliger Engel.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_065`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren unterscheiden sich: DE 0 'die Macht ist die größte' / EN 0 'worldly wisdom', DE 2 'das Gebet' / EN 2 'fasting', DE 3 Zucht, Treue, Wahrheit / EN 3 Knowledge, prophecy, tongues.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_066`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 unterscheiden sich: DE weniger Mühe / Heiden staunen / Gesetz verlangt sie, EN Zeichen und Donner / höherer Lohn / Orakel von Delphi. Außerdem beziehen sich die DE-Optionen mit 'Sie' auf das neutrale 'das prophetische Reden'.  
  ✏️ _Die Distraktoren 1:1 übertragen. In DE 'Es erbaut die Gemeinde' bzw. die Frage mit 'die Weissagung' formulieren._
- **`1kor_068`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 unterscheiden sich: DE Zeichen für Gläubige / Engel / Priester, EN apostolische Autorität / Sündlosigkeit / Verwirrung der Schriftgelehrten.  
  ✏️ _EN 1 'A sign for them that believe', EN 2 'for the angels', EN 3 'for the priests'._
- **`1kor_069`** · DE+EN · Mehrere richtig  
  Distraktor 2 'Alle, die in der Versammlung sitzen' kann durch V.31 der angegebenen Stelle gestützt werden ('ihr könnt einer nach dem anderen alle weissagen'). Das macht die Frage potenziell mehrdeutig.  
  ✏️ _Distraktor 2 ersetzen, z. B. 'Nur die Ältesten der Gemeinde' / 'Only the elders of the church'. Alternativ die Stelle auf 14:29 begrenzen._
- **`1kor_071`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 unterscheiden sich: DE alternative Lebensläufe Jesu, EN Fasten und Feste / Philosophenschule / bewaffneter Widerstand.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_072`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 2 und 3 unterscheiden sich: DE einziger Lehrer der Heiden / Erbe der Verheißung, EN beredtester Redner / sündloser Lehrer. In DE sind außerdem die Pronomen für Paulus großgeschrieben ('Sich ... Selbst').  
  ✏️ _Die Distraktoren 1:1 übertragen. In DE 'bezeichnet sich Paulus selbst' schreiben._
- **`1kor_073`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind verschoben bzw. verschieden: DE 0 Heiden herrschen / EN 0 Römisches Reich zerfällt, DE 2 Gesetz verliert Kraft / EN 2 Tempelopfer, DE 3 Tempelopfer / EN 3 Heiden überwältigen die Heiligen.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_074`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 3 unterscheiden sich: DE verborgener König / neuer Richter / letzter Prophet, EN zweiter Gesetzgeber / irdischer Monarch / Hoherpriester.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`1kor_075`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren sind verschoben bzw. verschieden: DE 0 alle sterben, keiner verwandelt / EN 0 Reinkarnation, DE 1 Erde bleibt ewig / EN 1 nur Apostel und Märtyrer, DE 2 nur Apostel verklärt / EN 2 Erde bleibt.  
  ✏️ _Reihenfolge und Inhalt angleichen._
- **`1kor_079`** · EN · Inhaltlicher Fehler  
  EN bezeichnet 'Anathema Maranatha' als aramäischen Ruf. 'Anathema' ist aber ein griechisches Wort und bedeutet 'verflucht'. Nur 'Maranatha' ist aramäisch. DE nennt korrekt nur 'Maranatha'.  
  ✏️ _EN 3: 'Maranatha: our Lord cometh'_

</details>

<details>
<summary><b>47_2_korinther.json</b> – 8 kleinere Befunde</summary>

- **`2kor_004`** · DE+EN · Sprachfehler  
  In der DE-Frage fehlt 'ge-' in 'geworden'. Außerdem unterscheiden sich die Distraktoren 1 bis 3: DE Gesetz und Wort / Licht und Leben / Heil und Segen, EN fleischliche Satzungen / irdische Herrschaft / Überlieferungen der Ältesten.  
  ✏️ _'... für die Gläubigen geworden?' und die Distraktoren in DE und EN angleichen._
- **`2kor_006`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 unterscheiden sich: DE meiden und verurteilen / bloßstellen, EN Geißelung durch Magistrat / doppelte Geldstrafe.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`2kor_007`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 bis 2 unterscheiden sich: DE Mann verlässt die Stadt / Uneinigkeit / Gesetz gebrochen, EN römische Einmischung / Rühmen der Milde / Friede vor Lehre.  
  ✏️ _Die Distraktoren 1:1 übertragen._
- **`2kor_018`** · EN · KJV-Wortlaut  
  Die EN-Lösung zitiert KJV wörtlich ('yet the inward man is renewed day by day'), hängt aber 'through the Holy Spirit of God' an. Das steht nicht im Vers.  
  ✏️ _'Though our outward man perish, yet the inward man is renewed day by day'_
- **`2kor_025`** · EN · KJV-Wortlaut  
  Die EN-Lösung beginnt als wörtliches KJV-Zitat, verkürzt aber 'that we might be made the righteousness of God in him' zu 'that we might be righteous'.  
  ✏️ _'He hath made him to be sin for us, who knew no sin; that we might be made the righteousness of God in him'_
- **`2kor_032`** · DE · Sprachfehler  
  Falscher Genitiv: 'des Mitarbeiter Titus' statt 'des Mitarbeiters Titus'.  
  ✏️ _'Welche Freude erlebte Paulus durch die Ankunft seines Mitarbeiters Titus in Makedonien?'_
- **`2kor_041`** · DE · Sprachfehler  
  Das Adjektiv 'Gesegneten' ist mitten im Satz fälschlich großgeschrieben, und die Formulierung ist holprig.  
  ✏️ _'Welcher Grundsatz über das Säen und Ernten gilt nach 2. Korinther 9:6 für das Geben?'_
- **`2kor_054`** · DE · Sprachfehler  
  'Seinem' ist großgeschrieben, als ginge es um Gott. Das Pronomen bezieht sich aber auf Paulus.  
  ✏️ _'... in seinem apostolischen Dienst ...'_

</details>

<details>
<summary><b>48_galater.json</b> – 3 kleinere Befunde</summary>

- **`gal_023`** · EN · KJV-Wortlaut  
  Dem KJV-Zitat ist 'unto the end' angehängt. Das steht nicht im Text.  
  ✏️ _'Thou shalt love thy neighbour as thyself'_
- **`gal_026`** · DE · Sprachfehler  
  'zurechthelfen' verlangt den Dativ, hier steht der Akkusativ ('einen Übereilten').  
  ✏️ _'Wie sollen die Geistlichen einem Übereilten nach Galater 6:1 zurechthelfen?'_
- **`gal_031`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren passen pro Index nicht zusammen: DE 0 'Macht' gegenüber EN 0 'Pride', DE 1 'Stärke' gegenüber EN 1 'Power'.  
  ✏️ _EN: '0: Power', '1: Strength'_

</details>

<details>
<summary><b>50_philipper.json</b> – 2 kleinere Befunde</summary>

- **`phil_016`** · EN · DE/EN weicht ab  
  Die EN-Distraktoren weichen inhaltlich von DE ab: Bei Option 1 steht 'Mary and Magdalene' statt 'Maria und Salome'. Mary Magdalene ist eine einzige Person, das Paar ergibt also keinen Sinn. Bei Option 3 steht 'Chloe and Phoebe' statt 'Kloë und Berenike'.  
  ✏️ _EN 1: 'Mary and Salome'; EN 3: 'Chloe and Bernice'_
- **`phil_017`** · EN · KJV-Wortlaut  
  Die EN-Lösung gibt sich als wörtliches KJV-Zitat aus, ergänzt aber 'unto you all', das im KJV nicht steht.  
  ✏️ _"Rejoice in the Lord alway: and again I say, Rejoice"_

</details>

<details>
<summary><b>51_kolosser.json</b> – 3 kleinere Befunde</summary>

- **`kol_014`** · EN · Sprachfehler  
  In der EN-Lösung fehlt der Artikel. Das KJV-Zitat lautet 'as it is fit in the Lord'.  
  ✏️ _"Submit yourselves unto your own husbands, as it is fit in the Lord"_
- **`kol_018`** · DE · Sprachfehler  
  In der deutschen Option steht die englische Namensform 'Timothy' statt 'Timotheus'.  
  ✏️ _"Timotheus, der junge Mitarbeiter, der Paulus treu diente"_
- **`kol_020`** · EN · Sprachfehler  
  Rechtschreibfehler im Distraktor: 'speedly' statt 'speedily'.  
  ✏️ _"Bring the parchments and holy books unto Paul the apostle at Rome speedily"_

</details>

<details>
<summary><b>52_1_thessalonicher.json</b> – 2 kleinere Befunde</summary>

- **`1thess_001`** · DE+EN · Mehrere richtig  
  Der Distraktor 'Silas aus Jerusalem' bezeichnet dieselbe Person wie Silvanus (Silas = Silvanus, vgl. Apg 15,22; 2. Kor 1,19), und Silvanus wird in 1:1 tatsächlich genannt. Die Frage schließt Silvanus zwar ausdrücklich aus, kundige Spieler können 'Silas' aber trotzdem für einen genannten Mitabsender halten.  
  ✏️ _Distraktor 3 ersetzen, z. B. 'Titus aus Kreta' / 'Titus of Crete'._
- **`1thess_019`** · EN · Sprachfehler  
  Die EN-Lösung ist grammatisch unvollständig: Das Hilfsverb 'shall' und der Artikel fehlen.  
  ✏️ _"The Lord himself shall descend from heaven, and the dead in Christ shall rise first"_

</details>

<details>
<summary><b>53_2_thessalonicher.json</b> – 1 kleinere Befunde</summary>

- **`2thess_005`** · EN · DE/EN weicht ab  
  'Wherefore' bedeutet 'warum'. Die EN-Frage fragt also nach dem Grund des Gebets, DE dagegen nach dem Inhalt ('Worum betet Paulus'). Die Optionen nennen den Inhalt.  
  ✏️ _"What does Paul pray always for the Thessalonians in 2 Thessalonians 1:11?"_

</details>

<details>
<summary><b>55_2_timotheus.json</b> – 1 kleinere Befunde</summary>

- **`2tim_004`** · DE · Sprachfehler  
  Die DE-Frage ist grammatisch mehrdeutig: 'Wessen Haus erquickte Paulus' lässt sich auch so lesen, dass Paulus das Haus erquickte. Außerdem passt 'Haus ... schämte sich seiner Ketten nicht' nicht zum Text, denn dort ist es Onesiphorus selbst, der ihn erquickte und sich nicht schämte.  
  ✏️ _"Wer erquickte Paulus oft und schämte sich seiner Ketten nicht, sodass Paulus für sein Haus um Barmherzigkeit bittet (2. Timotheus 1:16)?"_

</details>

<details>
<summary><b>56_titus.json</b> – 1 kleinere Befunde</summary>

- **`tit_006`** · EN · Sprachfehler  
  Die EN-Lösung ist abgeschnitten: 'keepers' ohne 'at home' ergibt keinen Sinn und entspricht nicht dem DE-Begriff 'haushälterisch'.  
  ✏️ _"To love their husbands and children, to be discreet, chaste, keepers at home"_

</details>

<details>
<summary><b>58_hebraeer.json</b> – 2 kleinere Befunde</summary>

- **`hebr_001`** · EN · KJV-Wortlaut  
  Die EN-Lösung ergänzt das KJV-Zitat um 'in heaven'. Damit wird 'heir of all things' unzulässig eingeschränkt, und auch die DE-Fassung kennt diese Einschränkung nicht ('Erben von allem').  
  ✏️ _"By his Son, whom he hath appointed heir of all things"_
- **`hebr_058`** · EN · KJV-Wortlaut  
  Die EN-Lösung ist als KJV-Wortlaut formuliert, fügt aber 'continually' hinzu. Das steht nicht im Text.  
  ✏️ _"Whom the Lord loveth he chasteneth, and scourgeth every son"_

</details>

<details>
<summary><b>59_jakobus.json</b> – 5 kleinere Befunde</summary>

- **`jak_005`** · EN · Sprachfehler  
  EN-Option 0 ist grammatisch fehlerhaft ('keeping it kept').  
  ✏️ _"Silent hearers of the word, keeping it in secret"_
- **`jak_005`** · EN · DE/EN weicht ab  
  Distraktor 3 hat in EN einen anderen Inhalt als in DE: DE 'Hüter, die das Wort vor Fremden hüten', EN 'Richter, die entscheiden, welchen Geboten man folgt'.  
  ✏️ _EN 3: "Keepers of the word, guarding it from strangers"_
- **`jak_006`** · EN · DE/EN weicht ab  
  Distraktor 3 hat in EN einen anderen Inhalt: DE spricht von Arbeit in der Synagoge am Tag des Herrn, EN vom Einfordern des Zehnten.  
  ✏️ _EN 3: "Against labouring in the assembly upon the Lord's day"_
- **`jak_010`** · EN · DE/EN weicht ab  
  Die EN-Frage verrät die Lösung ('when offering his son'), da nur Abraham seinen Sohn opferte. DE fragt neutral nach dem Vorbild für den durch Werke vollendeten Glauben.  
  ✏️ _"Whom doth James set forth as an example of faith made perfect by works (James 2:21-23)?"_
- **`jak_011`** · EN · DE/EN weicht ab  
  Distraktor 2 hat in EN einen anderen Inhalt: DE 'dürfen keine eigenen Güter besitzen', EN 'dürfen kein Amt bekleiden'. Distraktor 1 weicht ebenfalls ab: DE 'Abgaben an die Armen zahlen', EN 'ihren Besitz weggeben'.  
  ✏️ _EN 2: "Because masters may hold no possessions of their own"; EN 1: "Because masters must pay great alms unto the poor"_

</details>

<details>
<summary><b>62_1_johannes.json</b> – 5 kleinere Befunde</summary>

- **`1joh_007`** · EN · Sprachfehler  
  Der EN-Fragesatz ist keine Frage, sondern ein Aussagesatz mit Fragezeichen. Was gefragt ist, bleibt unklar.  
  ✏️ _"Whereby do we know that we know him according to 1 John 2:3?"_
- **`1joh_016`** · EN · Sprachfehler  
  Der EN-Fragesatz ist ein Aussagesatz mit Fragezeichen, keine Frage.  
  ✏️ _"Whereby know ye the Spirit of God according to 1 John 4:2?"_
- **`1joh_019`** · EN · Sprachfehler  
  Der EN-Fragesatz ist ein Aussagesatz mit Fragezeichen, keine Frage.  
  ✏️ _"Wherein is love according to 1 John 4:10?"_
- **`1joh_019`** · DE · Sprachfehler  
  DE-Option 0 ist grammatisch unvollständig: Beim Verb 'erhörten' fehlen Subjekt und Objekt. Wörtlich würde 'wir' Gott erhören.  
  ✏️ _"Dass wir Gott zuerst aus ganzem Herzen liebten und er uns darum erhörte"_
- **`1joh_025`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 hat in DE und EN verschiedenen Inhalt. Die EN-Frage ist schief formuliert ("What do little children hear").  
  ✏️ _EN 3 "Keep yourselves from strange teachers"; EN-Frage "Against what doth John warn the little children in 1 John 5:21?"_

</details>

<details>
<summary><b>64_3_johannes.json</b> – 1 kleinere Befunde</summary>

- **`3joh_003`** · EN · Sprachfehler  
  Tippfehler im Distraktor: "statues" (Statuen) statt "statutes" (Satzungen).  
  ✏️ _"...and denieth the statutes of Moses"_

</details>

<details>
<summary><b>66_offenbarung.json</b> – 30 kleinere Befunde</summary>

- **`off_008`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 nennt in DE eine andere Stadt als in EN.  
  ✏️ _EN 3 "In Rome, the chief city of the empire"_
- **`off_009`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN völlig verschiedenen Inhalt. Auch die Fragen unterscheiden sich: DE fragt "Welches Manna", EN fragt allgemein "What is promised".  
  ✏️ _EN-Distraktoren an DE angleichen (z. B. 0 "Of the bread of the temple and a black stone with the king's name") und DE-Frage: "Was wird dem Überwinder in Pergamon verheißen?"_
- **`off_011`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 1 und 2 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN-Distraktoren übersetzen: 0 "Thou hast a name of perfect holiness", 1 "Thou hast gathered all the riches of the world", 2 "Thou teachest diligently the law of Moses"_
- **`off_012`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben in DE und EN verschiedenen Inhalt. DE bietet verschiedene "Türen" an, EN ganz andere Dinge.  
  ✏️ _EN: 1 "A golden door into the sanctuary of God", 2 "A gate to dominion over all kingdoms", 3 "A door to the treasures of kings"_
- **`off_013`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN-Distraktoren übersetzen: 0 "A servant of the high priest", 2 "A judge over the heathen", 3 "An angel of gold"_
- **`off_015`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 1 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN 0 "Gold from the royal mines of Asia", EN 1 "Precious stones for the high priest's crown"_
- **`off_016`** · DE+EN · DE/EN weicht ab  
  Distraktor 3 nennt in DE 144, in EN 144.000.  
  ✏️ _Angleichen, z. B. EN 3 "An hundred forty and four elders holding branches of palms"_
- **`off_020`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN 1 "Judgment, judgment, judgment is the Lord...", EN 2 "Righteous, righteous, righteous are his ways..."_
- **`off_028`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 nennt in DE andere Mengen und Preise als in EN.  
  ✏️ _EN 1 "A measure of wheat for ten pence, and three measures of barley for ten pence"_
- **`off_029`** · DE+EN · DE/EN weicht ab  
  Distraktor 2 hat in DE und EN verschiedenen Inhalt.  
  ✏️ _EN 2 "The company of the martyrs followed after him"_
- **`off_031`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 2 haben in DE und EN verschiedenen Inhalt und andere Zahlen.  
  ✏️ _EN: 0 "An hundred thousand of all the tribes", 1 "Seven thousand of Jerusalem and the country round about", 2 "Four and twenty thousand of all the tribes"_
- **`off_032`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 sind zwischen DE und EN vertauscht, Distraktor 3 nennt eine andere Zahl.  
  ✏️ _EN: 1 "One thousand out of each tribe", 2 "Ten thousand out of each tribe", 3 "Seven thousand out of each tribe"_
- **`off_043`** · DE · Sprachfehler  
  Die Formulierung "Qual, die ... geschlagen wird" ist ungrammatisch. "unbußfertig" steht nicht in 9:5: Gequält werden die Menschen ohne das Siegel Gottes (9:4), wie die EN-Fassung richtig sagt.  
  ✏️ _"Wie lange dürfen die Heuschrecken die Menschen ohne das Siegel Gottes quälen?"_
- **`off_046`** · EN · KJV-Wortlaut  
  Die EN-Lösung ergänzt "in his right hand". In 10:2 steht nur "in his hand" (DE ebenso "in seiner Hand").  
  ✏️ _"A little book open in his hand"_
- **`off_049`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 3 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN 0 "To write them immediately for all nations", EN 3 "To deliver them unto the elders"_
- **`off_050`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 haben in DE und EN verschiedenen Inhalt (DE 1: bitter/bitter, EN 1: bitter/süß).  
  ✏️ _EN 1 "Bitter in the mouth and bitter in the belly", EN 3 "Without any taste in mouth or belly"_
- **`off_052`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 2 nennen in DE und EN verschiedene Zeitangaben.  
  ✏️ _EN: 1 "Threescore days of judgment", 2 "Three hundred threescore and five days"_
- **`off_053`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0, 2 und 3 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen: 0 "The Roman governor reigning in Jerusalem", 2 "The high priest serving in the temple", 3 "The king of the locusts out of the pit"_
- **`off_059`** · DE · Sprachfehler  
  "knabenhafte Kind" heißt "jungenhaft wirkendes Kind" und gibt "einen Sohn, einen männlichen" falsch wieder.  
  ✏️ _"Wohin wird der männliche Sohn der Frau nach der Geburt entrückt?"_
- **`off_068`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN-Distraktoren an DE angleichen_
- **`off_072`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 bis 3 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN: 1 "The song of David the king and the song of Paul the apostle", 2 "The song of the angels and of the elders", 3 "The song of Abraham and the song of the prophets"_
- **`off_074`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 1 und 3 haben in DE und EN verschiedenen Inhalt.  
  ✏️ _EN 1 "With blood of beasts and smoke of burnt offerings", EN 3 "With the light of angels and the brightness of stars"_
- **`off_075`** · EN · Sprachfehler  
  EN-Distraktor 2 ist unvollständig: Das Wort "elders" fehlt.  
  ✏️ _"The four and twenty elders"_
- **`off_079`** · DE+EN · DE/EN weicht ab  
  Distraktor 1 nennt in DE einen anderen Zeitraum als in EN.  
  ✏️ _EN 1 "To lose her light for seven months"_
- **`off_089`** · EN · Mehrere richtig  
  In EN fehlt bei den Distraktoren das einschränkende "nur" der DE-Fassung. Dadurch sind sie teilweise richtig: Eisen und Erz (V.12), Weizen und Öl (V.13) sowie Schafe (V.13) gehören laut Text alle zu Babylons Waren. Außerdem sind die Inhalte von Index 0 und 2 gegenüber DE vertauscht (DE 0 = Getreide/Öl/Wein, DE 2 = Waffen).  
  ✏️ _EN-Distraktoren wie in DE mit "Only" formulieren und in der DE-Reihenfolge ordnen: 0 "Only wheat, barley, oil and wine, the goods of husbandmen", 2 "Only weapons, swords and chariots of war", 3 "Only sheep, oxen and horses of the herdsmen"_
- **`off_090`** · DE+EN · DE/EN weicht ab  
  Die Distraktoren 0 und 1 haben in DE und EN verschiedenen Inhalt. Der EN-Lösung fehlt außerdem das Verb "cast", der Satz ist unvollständig.  
  ✏️ _EN 2 "He took up a stone like a great millstone, and cast it into the sea"; EN 0/1 an DE angleichen_
- **`off_109`** · EN · DE/EN weicht ab  
  In EN-Distraktor 0 fehlt die Verneinung. DE: "wer es nicht versteht", EN: "he that understandeth". Der Inhalt weicht ab und wird sinnlos.  
  ✏️ _EN 0 "He that readeth not dieth; he that understandeth not is condemned"_
- **`off_110`** · EN · KJV-Wortlaut  
  Die EN-Lösung ist als KJV-Zitat formuliert, hängt aber "in glory" an, das im Text nicht steht.  
  ✏️ _"Surely I come quickly. Amen. Even so, come, Lord Jesus."_
- **`off_112`** · DE+EN · Bibelstelle  
  Die Reihenfolge stimmt (Ephesus, Smyrna, Pergamon, Thyatira), aber bibleReference 2:1 nennt nur Ephesus. Die übrigen Sendschreiben stehen in 2:8, 2:12 und 2:18.  
  ✏️ _bibleReference "Offenbarung 2:1-18" / "Revelation 2:1-18"_
- **`off_113`** · DE+EN · Bibelstelle  
  Die Reihenfolge stimmt (weiß, feuerrot, schwarz, fahl), aber bibleReference 6:2 nennt nur das weiße Pferd. Die anderen Pferde stehen in 6:4, 6:5 und 6:8.  
  ✏️ _bibleReference "Offenbarung 6:1-8" / "Revelation 6:1-8"_

</details>


## Zentral geprüft: Namen und Versbereiche

### Namensschreibweisen in EN (🟡 klein)

Diese Namen weichen von der KJV-Schreibweise ab:

| EN aktuell | KJV | Anzahl | Fragen |
| :-- | :-- | --: | :-- |
| Abiezrites | **Abi-ezrites** | 2 | `ri_022`, `ri_048` |
| Barjesus | **Bar-jesus** | 2 | `apg_037`, `apg_061` |
| Bartimaeus | **Bartimæus** | 1 | `mk_050` |
| Beersheba | **Beer-sheba** | 3 | `1mose_165`, `joh_016`, `ps_056` |
| Benoni | **Ben-oni** | 1 | `1sam_016` |
| Bethel | **Beth-el** | 49 | `1kön_032`, `1kön_033`, `1kön_034`, `1kön_048`, `1mose_084`, `1mose_092` … (+43) |
| Bethelite | **Beth-elite** | 1 | `1kön_063` |
| Bethlehemite | **Beth-lehemite** | 1 | `1chr_052` |
| Ebenezer | **Eben-ezer** | 4 | `1sam_011`, `1sam_016`, `1sam_030`, `jos_128` |
| El-bethel | **El-beth-el** | 1 | `1mose_250` |
| En-dor | **Endor** | 1 | `1sam_094` |
| Ichabod | **I-chabod** | 3 | `1sam_016`, `dan_006`, `jer_075` |
| Malchishua | **Malchi-shua** | 1 | `2sam_005` |
| Nebuzaradan | **Nebuzar-adan** | 2 | `jer_123`, `jer_155` |
| Zacchaeus | **Zacchæus** | 6 | `apg_086`, `lk_024`, `lk_091`, `lk_092`, `lk_093`, `mk_050` |
| Phoebe | **Phebe** | | |
| Paddan-aram | **Padan-aram** | | |
| Zaphenath-paaneah | **Zaphnath-paaneah** | 1 | `1mose_150` |

### Abweichende Versbereiche DE ↔ EN (🟡 klein)

Gleicher Inhalt, aber unterschiedlich weit gefasste Stelle: `phil_009`, `phil_010`, `phil_011`, `kol_010`, `kol_015`, `kol_016`, `1thess_004`, `1thess_013`, `1thess_015`.

Bei `1mose_110`–`1mose_114` (1. Mose 32) ist die DE-Stelle um +1 verschoben, obwohl der hinterlegte DE-Text die KJV-Verszählung nutzt (siehe Befunde oben).

---

## Vorgehen und Legende

1. **Automatischer Lauf** über alle 4754 Fragenpaare: Struktur DE ↔ EN, Vergleich mit `main`, Existenz jeder Bibelstelle, Zahlen, Namen, Duplikate.
2. **Inhaltliche Prüfung** jeder Frage durch 40 parallele Prüfer – DE und EN nebeneinander mit dem hinterlegten Verstext und KJV.
3. **Gegenprüfung:** Jeder Befund wurde von einem unabhängigen Prüfer erneut am Grundtext geprüft. Nicht haltbare Befunde wurden verworfen.

| Symbol | Bedeutung |
| :-- | :-- |
| ✅ | aktuell als richtig markierte Option |
| ⬜ | aktuell als falsch markierte Option |
| 1. 2. 3. | Reihenfolge-Frage: Optionen in gespeicherter Reihenfolge |
| 📖 | Beleg aus dem hinterlegten Bibeltext |
| ✏️ | Korrekturvorschlag |
| 🔎 | Anmerkung der Gegenprüfung |
| **Sprache** | `DE`, `EN` oder `DE+EN` – wo der Fehler steckt |
| **Ursprung** | ob der Fehler durch die Überarbeitung, durch die neue EN-Fassung entstand oder schon in `main` war |
