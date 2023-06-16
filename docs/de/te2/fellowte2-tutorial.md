---
title: "TE² Tutorial: Schritt-für-Schritt-Anleitung für das Table Extraction Plugin"
description: "Erfahren Sie, wie Sie das TE² Plugin verwenden, nachdem Sie es installiert und konfiguriert haben. In diesem Tutorial finden Sie alle Schritte in Ephesoft, die durchgeführt werden müssen, um zur Tabellenansicht zu gelangen."
date: "2021-07-05"
tags:
  - TE²
  - Plugin
  - Ephesoft
  - Table Extraction
---

### Voraussetzungen

Um dieses Tutorial zu verwenden, müssen Sie den Abschnitt [Installation & Konfiguration](/te2/install/) für dieses Plugin abgeschlossen haben.

* * *

### Wie man das KV² Plugin verwendet

##### **Schritt 0: Einloggen**

- Melden Sie sich mit Benutzername und Passwort in der Ephesoft Transact Software an.

![Einloggen in Ephesoft Transact Software](/_images/docbits/login1Unbenannt.png)

![Ephesoft Transact Software Dashboard](/_images/docbits/login2Unbenannt.png)

- Nach dem Einloggen sehen Sie das Menü auf der linken Seite mit zwei Modulen: Administrator & Operator mit ihren definierten Funktionen:

<table><tbody><tr><td><strong>Administrator</strong></td><td><strong>Operator</strong></td></tr><tr><td>Batch Class Management</td><td>Batch List</td></tr><tr><td>Batch Instance Management</td><td>Review Validate</td></tr><tr><td>Folder Management</td><td>Web Scanner</td></tr><tr><td>System Configuration</td><td>Upload New Document</td></tr><tr><td>Report</td><td></td></tr></tbody></table>

#### **Schritt 1: Anwendungsoberfläche des FellowTE2 Plugins**

- Laden Sie Ihre Dokumente über das Operator-Modul in "Upload Batch" hoch:

![Dokumente hochladen in Ephesoft Transact Software](/_images/docbits/step1_1.png)

- Starten Sie den Batch mit der entsprechenden Batch-Klasse.

![Batch starten in Ephesoft Transact Software](/_images/docbits/startbatch.png)

- Warten Sie im Administrator-Modul in "Batch Instance Management", bis der Batch verarbeitet und zur Validierung bereit ist.

![Batch-Verarbeitung in Ephesoft Transact Software](/_images/docbits/Process3Unbenannt.png)

- Wählen Sie Ihren Batch in der Liste aus und klicken Sie auf "Öffnen", um den Batch zu öffnen und die Header- und Footer-Felder zu validieren:

![Batch-Validierung in Ephesoft Transact Software](/_images/docbits/4-open-batchUnbenannt.png)

- Sie werden nun zum Ephesoft-Validierungsfenster weitergeleitet. Neben den Optionen "Validieren", "Nächster Batch", "Zusammenführen", "Aufteilen" und "Mehr" finden Sie hier den Button, um zur "Table"-Ansicht zu gelangen.

![Ephesoft Validierungsfenster](/_images/docbits/image-39-1024x541.png)

![Ephesoft Table Extraction Plugin](/_images/docbits/image-40-1024x541.png)

Es gibt ein Standard-Schema, das standardmäßig verwendet wird und die meisten Rechnungs- / Tabellenlayouts verarbeiten kann. Für bestimmte Rechnungs- / Tabellenlayouts gibt es spezielle (benutzerdefinierte) Layouts, und es können sicherlich weitere vorhanden sein, wenn es spezielle Anforderungen innerhalb Ihrer Organisation gibt.

Das Standard-Schema kann die in der folgenden Tabelle aufgeführten Werte erkennen. Wenn ein Feld, das in der Tabelle als erforderlich markiert ist, fehlt, kann diese Zeile nicht als gültige Zeile erkannt werden.

<table><tbody><tr><td><strong>Name</strong></td><td><strong>Typ</strong></td><td><strong>Erforderlich</strong></td></tr><tr><td>POSITION</td><td>string</td><td>false</td></tr><tr><td>BESCHREIBUNG</td><td>string</td><td>true</td></tr><tr><td>ARTIKELNUMMER</td><td>string</td><td>false</td></tr><tr><td>MENGE</td><td>number</td><td>true</td></tr><tr><td>EINZELPREIS</td><td>currency</td><td>true</td></tr><tr><td>GESAMTBETRAG</td><td>currency</td><td>true</td></tr><tr><td>BESTELLNUMMER</td><td>string</td><td>false</td></tr></tbody></table>

![Ephesoft Table Extraction Plugin Schema](/_images/docbits/image-43-1024x732.png)

Die Backend-Intelligenz des TE²-Plugins führt eine Analyse und Optimierung der Daten- / Tabellenansicht durch, die dann vom Benutzer validiert oder korrigiert werden kann, falls erforderlich. Auch wenn die meisten Tabellen erkannt und ausgeführt werden können, gibt es einige Einschränkungen in der Technologie, d.h. dass bestimmte Arten von Tabellen nicht erkannt werden können.

Die folgenden Merkmale sind einige Gründe, warum Tabellen nicht extrahiert werden können:

1. Mehrzeilige Tabellen.
2. Gemischte Trennung von Spalten (Gitter und kein Gitter).
3. Überlappende Tabellengitter.
4. Zu großer Abstand zwischen den Spaltenüberschriften und den eigentlichen Zeilen.

In jedem Fall werden Tabellen von PolyDocs GmbH i. Gr. analysiert, um die Möglichkeit und Durchführbarkeit der Tabellenextraktion zu bestimmen.

Beispiele:

![Ephesoft Table Extraction Plugin Beispiel 1](/_images/docbits/image-41-1024x727.png)

![Ephesoft Table Extraction Plugin Beispiel 2](/_images/docbits/image-42-1024x648.png)