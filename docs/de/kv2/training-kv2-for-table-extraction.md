---
title: "KV2-Training zur Tabellenextraktion"
description: In dieser Dokumentation wird die Funktion zur Extraktion von Tabellen aus verschiedenen Dokumenttypen (Rechnungen, Verträgen, Formularen, medizinischen Rezepten usw.) erklärt.
date: "2021-12-16"
tags:
  - KV²
  - Plugin
  - Ephesoft
  - Training
  - Tabellenextraktion
---

In dieser Dokumentation wird die Funktion zur Extraktion von Tabellen aus verschiedenen Dokumenttypen (Rechnungen, Verträgen, Formularen, medizinischen Rezepten usw.) erklärt. Die Extraktion von Daten aus Tabellen kann durch folgende Schritte erreicht werden:

1\. Melden Sie sich mit Ihrer E-Mail-Adresse und Ihrem Passwort in Ihrem Konto an.

2\. Importieren Sie das gewünschte Dokument auf Ihr Dashboard.

3\. Klicken Sie auf das Dokument, um es im Bearbeitungsbildschirm zu öffnen.

4\. Scrollen Sie nach unten zu **Zeilenartikel** (befindet sich ganz unten rechts der verfügbaren Felder).

5\. Klicken Sie auf das Tabellensymbol innerhalb des Textfeldes.

![Line Items](/_images/docbits/Line-Items-1-1024x194.png "Line Items")

**TIPP**: Wenn keine Tabellenextraktion im ausgewählten Dokument durchgeführt werden soll, kann dies mit dem Symbol neben "Zeilenartikel" festgelegt werden.

![Line Items 2](/_images/docbits/Line-Items-2.png "Line Items 2")

6\. Der folgende Bildschirm wird angezeigt.

![Adjust Table](/_images/docbits/TE_Adjust-table-1024x548.png "Adjust Table")

Die folgenden Optionen und Funktionen sind jetzt verfügbar (auf der linken Bildschirmhälfte dargestellt):

- **Zoomen:** ermöglicht es dem Benutzer, in das Dokument hineinzuzoomen.

![Zoom In](/_images/docbits/zoom-in.png "Zoom In")

- **Zoomen raus:** ermöglicht es dem Benutzer, aus dem Dokument herauszuzoomen.

![Zoom Out](/_images/docbits/zoom-out.png "Zoom Out")

- **Tabelle automatisch erkennen:** Diese Funktion dient zur automatischen Erkennung der Tabelle im Dokument - falls das Plugin die Tabelle nicht erkennen kann, muss sie manuell ausgewählt werden.

![Autodetect Table](/_images/docbits/autodetect-table.png "Autodetect Table")

- **Tabelle auswählen:** Diese Funktion ermöglicht es dem Benutzer, die gewünschte Tabelle manuell per Drag & Drop auszuwählen.

![Select Table](/_images/docbits/edit-table.png "Select Table")

Die Tabelle kann hier auch angepasst werden (z.B. Höhe und Breite).

![Adjust and Save](/_images/docbits/TE_adjust-table-and-save-1024x549.png "Adjust and Save")

- **Spalten hinzufügen:** Diese Funktion ermöglicht es dem Benutzer, manuell Richtlinien hinzuzufügen, um dem System zu helfen, die richtigen Spalten (blaue Linien) zu bestimmen, wie auf dem folgenden Screenshot dargestellt.

![Add Columns](/_images/docbits/add-line.png "Add Columns")

![Table Select 2](/_images/docbits/Table-select-2.png "Table Select 2")

Sobald diese Richtlinien hinzugefügt sind, stehen zusätzliche Funktionen zur Verfügung.

![Extend Line](/_images/docbits/exend-line.png "Extend Line")

Die erste Funktion ermöglicht es dem Benutzer, alle Linien zu löschen, während die zweite Funktion diese Richtlinien auf alle Seiten des Dokuments ausdehnt.

Wenn nur eine Linie ausgewählt ist, wird eine Löschschaltfläche hinzugefügt, mit der der Benutzer die ausgewählte Linie löschen kann.

![Delete 1 Line](/_images/docbits/delete-1-line.png "Delete 1 Line")

- **Änderungen speichern:** ermöglicht es dem Benutzer, alle vorgenommenen Änderungen zu speichern.

![Save Changes](/_images/docbits/save.png "Save Changes")

**TIPP**: Wenn die Markierung der Tabelle falsch ist und gelöscht werden soll, wählen Sie die Markierung der betreffenden Tabelle aus - ein rotes Symbol wird angezeigt, das die Entfernung der Markierung ermöglicht.

![Delete Table Marking](/_images/docbits/Bildschirmfoto-2021-12-16-um-14.53.08-1024x307.png "Delete Table Marking")

7) Sobald die Änderungen gespeichert sind, extrahiert das Plugin automatisch die gefundenen Daten und zeigt sie in einer Tabelle auf der rechten Seite an.

![Table 1](/_images/docbits/Table-1-1.png "Table 1")

Die verfügbaren Funktionen auf dieser Seite des Bildschirms sind wie folgt:

- **Änderungen rückgängig machen:** ermöglicht es dem Benutzer, alle Änderungen rückgängig zu machen.

![Undo Changes](/_images/docbits/undo.png "Undo Changes")

- **Erweiterte Einstellungen:** Diese Funktion ermöglicht zusätzliche Einstellungen, um die Daten weiter korrekt zu extrahieren.

![Advanced Settings 1](/_images/docbits/advanced-settings-1.png "Advanced Settings 1")

Sobald ausgewählt, wird der folgende Bildschirm angezeigt:

![Table 2](/_images/docbits/Table-2-1.png "Table 2")

"Headerzeilenanzahl" definiert, wie viele Zeilen zum Header gehören. Wenn der Header beispielsweise zwei Zeilen hat, muss die entsprechende Anzahl (2 in diesem Fall) ausgewählt werden.

"Extra-Zeile in desc verschieben"

- **Neue Zeile hinzufügen:** Fügt eine zusätzliche Zeile am unteren Rand der Tabelle hinzu.

![Add New Line](/_images/docbits/add-new-line.png "Add New Line")

- **Alle extrahierten Daten löschen:** Löscht alle extrahierten Daten aus der Tabelle.

![Delete Extracted Data](/_images/docbits/delete-extr.-data.png "Delete Extracted Data")

- **Tabellenextraktion für diesen Lieferanten blockieren:** Dies muss ausgewählt werden, wenn keine Tabelle von diesem Lieferanten extrahiert werden soll.

![Block Table Extraction](/_images/docbits/blox-table-ex.png "Block Table Extraction")

Jeder Spaltenname muss korrekt zugeordnet werden, z.B. "POS.NO." entspricht "Position".

**Dies muss für alle Spaltennamen erfolgen - sonst wird ein Fehler produziert!**

![Position](/_images/docbits/position-1024x590.png "Position")

Wählen Sie als nächstes die drei Punkte neben der Position aus, auf die sich der Inhalt bezieht, z.B. die Positionsnummer.

![Position 2](/_images/docbits/position-2.png "Position 2")

Neben der Möglichkeit, die Zeile (die natürlich auch in allen anderen Spalten zu finden ist) zu löschen (über das Papierkorbsymbol), ist hier die Option "Zeilen gruppieren" wichtig.

![Group Data](/_images/docbits/group-data-1024x495.png "Group Data")

Diese Option gruppiert alle Daten, die zur Position gehören.

Wenn das System leere oder unerwünschte Daten erkennt, löschen Sie sie über das lila "X" auf der linken Seite der Tabelle.

![Delete Row](/_images/docbits/delete-row.png "Delete Row")

Sobald die Tabelle wie gewünscht eingerichtet ist, können die Einstellungen durch Klicken auf "Speichern" gespeichert werden. Es wird den Benutzer dann sofort zum Dashboard zurückbringen.

![Save Settings](/_images/docbits/Bildschirmfoto-2021-12-16-um-14.41.25-1024x92.png "Save Settings")

Alternativ kann das Dokument sofort exportiert werden, indem auf "Bestätigen & Exportieren" geklickt wird.

![Confirm and Export](/_images/docbits/Bildschirmfoto-2021-12-16-um-14.41.30-1024x83.png "Confirm and Export")