---
layout: default
title: "BA/MA Info"
author: “Oliver Dürr”
---

# Information zu Master und Bachelor Arbeiten 
Diese Informationen sind für Bachelor- und Masterarbeiten gedacht, die ich an der HTWG betreue. 
Es gibt im Prinzip zwei Modi. Entweder machen Sie die Arbeit in einem Betrieb [siehe Arbeiten in einer Firma](#arbeiten-in-einer-firma) oder bei mir am Institut für optische Systeme [siehe Arbeiten am Institut](#arbeiten-am-institut) . 

## Generelles
**Neu ab WS 2024:** Ich erwarte, dass auch Bachelorarbeiten in einem Kolloquium präsentiert werden

Der Software-Engineering-Aspekt spielt bei mir keine Rolle. Ob Sie in der verwendeten Arbeit Design Pattern verwenden oder eine Reihe von Skripten ist mir egal, solange Sie auf Reproduzierbarkeit der Ergebnisse achten. 

### Forschungsthema: Deep Learning / Machine Learning
Ich betreue vorzugsweise Arbeiten aus dem Bereich Deep Learning / Machine Learning. Einen Überblick über die bisher betreuten Arbeiten können Sie sich unter [http://oduerr.github.io/teaching/](https://oduerr.github.io/teaching/bama/bama_htwg.html) verschaffen.

### Voraussetzungen

Es muss Vorwissen in den relevante Bereichen vorhanden sein. Dazu gehören:

* Umgang mit Daten: Sie kennen die elementaren Grundlagen um Daten zu analysieren, Mittelwerte, Diagnose Plots usw.

* Für Master: Vorwissen in Deep Learning, Machine Learning oder Data Analytics: Falls Sie die Vorlesung Deep Learning oder Machine Learning nicht besucht haben, sollten Sie Erfahrung vorweisen können, wie zum Beispiel durch die Teilnahme an einem Kaggle Wettbewerb.

* Für Bachelor: Sie sollten gute Statitikkentnisse haben. Idealerweise habe Sie schon einmal etwas von Maschine Learning oder Data Mining gehört.  

### Wissenschaftlicher Anspruch und Engineering 

Informatik ist bei uns ein Bachelor of Science (B.Sc.) bzw. Master of Science (M.Sc.) – entsprechend erwarte ich wissenschaftliches Arbeiten auch im Bachelor (im Master mit höherem Anspruch). Gleichzeitig ist Engineering ein zentraler Teil guter Informatik. Iteratives Entwickeln und Optimieren ist daher ausdrücklich erlaubt und oft notwendig. Entscheidend ist aber, dass daraus eine übertragbare Erkenntnis wird: Sie sollen nicht nur zeigen, dass etwas besser wird, sondern wogegen, wie zuverlässig und idealerweise warum.

Arbeiten, deren Schwerpunkt im iterativen Optimieren/Tuning eines Systems liegt („Parameter drehen, bis es besser wird“), sind nur dann geeignet, wenn ein klarer wissenschaftlicher Evaluationsrahmen vorliegt (begründete Metriken, Vergleich gegen Baselines/Referenzen, getrennte Testdaten, Quantifizierung der Zuverlässigkeit).


#### Evaluationsrahmen (Metriken, Zuverlässigkeit, Vergleich)

* **Vergleichsrahmen:** Mindestens Vergleich gegen eine Baseline; idealerweise zusätzlich gegen etablierte Referenzen/Stand der Technik (sofern fair und machbar).
* **Saubere Evaluation:** Trennung von Entwicklungs-/Tuningdaten und finaler Evaluation auf unabhängigen Testdaten (keine Optimierung auf dem Testset).
* **Metriken & Zuverlässigkeit:** Geeignete, begründete Metriken und eine Quantifizierung der Zuverlässigkeit (z. B. mehrere Runs/Seeds, Bootstrap/Konfidenzintervalle, Sensitivitätsanalysen).
<!-- * **Probabilistische Methoden:** Wenn Sie probabilistische Vorhersagen/Unsicherheiten evaluieren, erwarte ich eine Diskussion geeigneter **Proper Scoring Rules** (z. B. Log-Score/NLL, CRPS, Brier Score). -->


## Arbeiten in einer Firma 

Auch bei Arbeiten in einer Firma gilt der Abschnitt **„Wissenschaftlicher Anspruch und Engineering“** inkl. **Evaluationsrahmen** unverändert.

* **Wichtig:** Falls Sie Arbeit in einer Firma machen, muss die Betreuung vollständig im Betrieb erfolgen. Es muss dort eine kompetente Ansprechperson vorhanden sein. In diesem Fall bin ich in der Regel nur beratend (1-2 Termine) und bewertend tätig. Es muss also in der Firma zwingend das benötigte Know-how vorhanden sein. D. h. Sie brauchen dort eine Betreuungsperson, die auf dem Gebiet schon gearbeitet hat, Sie fachlich begleiten kann und ein wissenschaftliches Vorgehen (Fragestellung, saubere Evaluation, Dokumentation) sicherstellt.

* Auch wenn die Arbeit in einem Betrieb betreut wird, nehme ich nur **quantitative** Arbeiten an, bei denen ich über hinreichendes Fachwissen verfüge, um sie adäquat bewerten zu können. Reine Arbeiten im Stil „Evaluation eines Softwarepakets / einer Technologie XY“ nehme ich nicht an, da ich solche Arbeiten fachlich nicht sinnvoll bewerten kann und sie nicht zu meinem Betreuungsprofil passen.

* Formal muss die Betreuungsperson in der Firma mindestens den gleichen Abschluss haben. Ich gehe aber davon aus das diese Person mindestens in jedem Fall einen Master, idealerweise eine Promotion, haben sollte.

* Bei allen Besprechungen mit mir muss die Betreuungsperson aus der Firma in der Regel anwesend sein.  

### Geheimhaltung: 

* Grundsätzlich gilt: Wissenschaft gehört veröffentlicht. Ich bevorzuge daher Arbeiten, bei denen Ergebnisse (ggf. anonymisiert/aggregiert) publiziert werden dürfen. Eine Sperrklausel ist zur Not in Ordnung, sollte aber zeitlich befristet und inhaltlich klar abgegrenzt sein.

* **NDAs:** Kommen nicht in Frage. Ich darf sie nicht unterzeichnen (keine Zeichnungsberechtigung der Hochschule) und nehme keine Arbeiten an, bei denen ein NDA vorausgesetzt wird.

* Idealerweise arbeiten Sie mit einem öffentlichen Datensatz (ggf. zusätzlich zu einem firmeninternen).


### Erster Kontakt, wenn Sie die Arbeit in einer Firma machen wollen
Sie bereiten ein paar Folien (3-10) und vor und schicken Sie mir dann. 

* Anwendungsidee (falls vorhanden): Schildern Sie die (Business-)idee ihrer Arbeit.

* Vorwissen / Motivation: Was qualifiziert / motiviert, Sie diese Arbeit zu machen. 

* Wissenschaftliche Fragestellung:
	* Destillieren Sie aus der Anwendungsidee eine wissenschaftliche Fragestellung 

* Methoden
	* Welche Methoden wollen Sie verwenden?

* Datenlagen (falls anwendbar):
	* Wie sehen die Daten aus, wieviel Daten sind Vorhanden?
	* Sind alle Daten schon vorhanden? Falls nicht, erstellen Sie einen Plan B mit öffentlichen Daten.

* In der Firma: 
	* Ist ein fachlich kompetenter Ansprechpartner in der Firma vorhanden? 
	* Falls benötigt, ist IT-Infrastruktur vorhanden?
	* Ist es erlaubt die Daten und die Ergebnisse der Arbeit zu veröffentlichen? 

Falls das Thema passt, machen wir dann einen ersten Termin aus, um unverbindlich darüber zu sprechen. Bei diesem ersten Gespräch muss der Betreuer der Firma mit dabei sein.

### Erster Kontakt, wenn Sie die Arbeit am Institut schreiben wollen
Wir treffen uns persönlich und ich gebe Ihnen eine Übersicht über mögliche Themen und meine Erwartungen an eine Arbeit. Schicken Sie mir bitte eine kurze E-Mail (ein paar Absätze reichen). Damit ich schnell einschätzen kann, ob und wie das passt, sollte Folgendes drinstehen:

* Studiengang & Abschluss: BA/MA, Studiengang, ggf. Schwerpunkt.
* Zeitfenster: gewünschter Start, spätester Abgabetermin (oder ob Sie flexibel sind).
* Interessen (2–4 Stichpunkte): z. B. Computer Vision, NLP, Zeitreihen, Unsicherheit, Bayes, Causality, Generative Models, RL, etc.
* Vorwissen & Tools: relevante Vorlesungen (z. B. Data Analysis / ML / DL), Programmiererfahrung (Python), ggf. Frameworks (PyTorch/JAX/Keras), Statistikkenntnisse.
* Motivation: warum das Thema, warum am Institut (1–3 Sätze).
* Falls vorhanden: Ideen/Skizzen: gern als Stichpunkte (Problem → mögliche Methode → mögliche Daten).

### Formulierung einer Disposition
Nach dem ersten Gespräch, formulieren Sie dann eine Disposition aufgrund derer ich dann die Arbeit formal als Betreuer annehme. In dieser Disposition, erweitern Sie die Rohfassung. Das heißt Sie führen Teilfragestellungen ein und erweitern den Methodenteil. Skizzieren Sie auch einen groben Projektplan.


## Arbeiten am Institut 
Wenn Sie die Arbeit am Institut schreiben, werden Sie entweder von mir direkt oder von einem Doktoranden betreut. Das Thema muss dann in das Forschungsportfolio passen. Auch wenn es nicht immer klappt, ist das Ziel eine Veröffentlichung in einem Journal oder für eine Konferenz oder Workshop. 

### Forschung
Aktuelle Ausschreibungen finden Sie unter: http://www.ios.htwg-konstanz.de/jobs-and-projects. Haben Sie Data Analysis oder Deep Learning gehört, können Sie mich auch so gerne anschreiben und nach aktuellen Themen fragen.

### Betreuung
* Wir treffen uns in der Regel einmal die Woche, um Fragen zu besprechen. 
* Nach etwa 4 Wochen, werden Sie einen Einführungsvortrag halten, bei dem Sie Ihr Projekt der Gruppe (2-10) Personen vorstellen. Dies dient dazu, dass wir alle das gleiche Verständnis haben und evt. neue Ideen zu kreieren.  



## Allgemeine Hinweise zur Arbeit



Format, Textverarbeitungsprogramm (Word,Google-Docs,LaTeX,...), Zitierweise (IEEE, Harvard,...) und Sprache (Deutsch oder Englisch) ist mir egal. Auf was ich wert lege:

* Schreiben Sie nicht mehr als 30-35 Seiten (inklusive von Figuren und Tabellen) Haupttext (für eine BA) bzw. 45-50 (für eine MA). Versuchen Sie eine "Geschichte zu erzählen". Alles, was nicht direkt damit zu tun hat, sollte man weglassen oder es gehört in den Anhang.  
* Stil: wissenschaftlich, knapp und prägnant (concise)
* Die Figuren sind sehr wichtig und fliessen in die Bewertung ein. Sie müssen eine aussagekräftige Unterschrift / Caption haben (in der Regel mehr als ein Satz). Bei Grafen müssen die Achsen beschriftet sein.
* Alle Variablen in Formel müssen erklärt sein (ich sehe eher Fehler in Formeln als Rechtschreibfehler). Schreiben Sie in LaTex ist https://bochang.me/blog/posts/latex/ eine gute Quelle für den Formelsatz
* Sprache/Lesbarkeit: Ich bewerte nicht primär Grammatik oder Rechtschreibung. Im Jahr 2026 setze ich aber voraus, dass Sie bei Bedarf geeignete Tools zur sprachlichen Überarbeitung einsetzen (z. B. Duden Mentor, Grammarly oder KI-gestützte Assistenz), sodass der Text gut lesbar und weitgehend fehlerfrei ist. **Wichtig:** Für Inhalt, Faktentreue tragen Sie immer die volle Verantwortung (Nutzung von KI-gestützten Werkzeugen)
* Alle abgesetzten Formel (also nicht Text) sollten eine Nummer haben (das erleichtert Diskussion)  
* Fehlerbalken müssen, sofern möglich, angegeben werden. In R gibt schon immer die Möglichkeit Konfidenzintervalls zu berechnen, in python geht es nun auch <https://github.com/jacobgil/confidenceinterval>  
* In der Regel kein Code im Haupttext (eher Pseudocode)
* Arbeit muss das Ausgabedatum und Abgabedatum enthalten
* Wenn keine Geheimhaltung dageben spricht sollte alles (Code und Daten oder download-links) was nötig ist um die Ergebnisse zu reproduzieren in einem öffentlichen git-hub repository liegen.
* Keine Tabellen- / Figurenverzeichnisse. Allerdings gerne ein Abkürzungsverzeichniss dort auch Symbole angeben (z.B. $p(x)$ Dichte der Zufallsvariable x)  
* Lassen Sie die Arbeit noch von jemand anderen Korrekturlesen. Gute Quellen für Rechtschreibungs- und Grammatik-Korrektur sind Duden Mentor (deutsch) oder Grammarly (englisch)

Ein gutes Beispiel für eine Master Arbeit ist die Arbeit von Ivonne Kovylov https://github.com/IvonneKo/Master_Thesis/blob/main/Thesis_MSI_Kovylov_.pdf 

Weitere gute Quellen sind

Beispielglieder einer MA (im Prinzip auch für BA): [https://git.ios.htwg-konstanz.de/ios_public/thesis_teamprojekt_templates/-/blob/master/thesis.pdf](https://git.ios.htwg-konstanz.de/ios_public/thesis_teamprojekt_templates/-/blob/master/thesis.pdf) unter [https://git.ios.htwg-konstanz.de/ios_public/thesis_teamprojekt_templates/](https://git.ios.htwg-konstanz.de/ios_public/thesis_teamprojekt_templates/) finded  man die LaTeX Quellen

### Nutzung von KI-gestützten Werkzeugen

Bitte fügen Sie der Arbeit einen kurzen Abschnitt zur Nutzung KI-gestützter Werkzeuge bei.  
Dabei sollen die verwendeten Tools (z. B. ChatGPT, GitHub Copilot, Prism oder vergleichbare Anwendungen) sowie deren Einsatzbereiche kurz benannt werden.

Eine detaillierte Dokumentation einzelner Text- oder Codestellen ist nicht erforderlich.  
Die Angabe der einzelnenTools dient der Transparenz und ist nicht relevant für die Bewertung der Arbeit.

**Wichtig:** Unabhängig von der Nutzung solcher Werkzeuge übernehmen Sie die **volle Verantwortung** für **alle Inhalte, Ergebnisse und Schlussfolgerungen** der Arbeit, einschließlich Text, Code und Abbildungen. Dies schließt auch Inhalte ein, die mithilfe KI-gestützter Werkzeuge erzeugt wurden und von Ihnen eigenständig geprüft und verantwortet werden müssen.


#### Beispiel 

```text
Bei der Erstellung dieser Arbeit wurden KI-gestützte Werkzeuge eingesetzt:
- ChatGPT zur sprachlichen Überarbeitung und Strukturierung von Text,
- GitHub Copilot zur Unterstützung bei der Erstellung von Analyse- und Visualisierungscode,
- Google Colab Notebooks zur Erstellung von Abbildungen und Datenvisualisierungen,
- Prism zur Erzeugung von LaTeX-Code sowie zur Erstellung grafischer Diagramme.

Alle KI-unterstützten Inhalte wurden vom Verfasserin/Verfasser sorgfältig geprüft und bei Bedarf überarbeitet; die Verantwortung für die endgültige Fassung liegt vollständig bei ihr/ihm.
```
## Allgemeine Hinweise zum Kolloquium 

### Dauer & Ablauf
* **Bachelorarbeit:** ca. 20 Minuten Vortrag + etwa 15 Minuten Fragen.
* **Masterarbeit:** ca. 35 Minuten Vortrag + etwa 15 Minuten Fragen.

Die Fragerunde kann bei Interesse auch länger dauern.

### Zielgruppe
Die Zuhörerschaft verfügt über ein **allgemeines Verständnis von Machine/Deep Learning oder Statistik**. Nutzen Sie diese Basis, um die **spezifischen Besonderheiten Ihrer Arbeit** herauszuarbeiten (z. B. besondere Daten, Modellarchitektur, Evaluationsstrategie, überraschende Erkenntnisse).
