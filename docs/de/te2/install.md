---
title: "TE² Installation & Konfiguration"
description: In dieser Dokumentation erfahren Sie, wie Sie das TE²-Plugin installieren und konfigurieren. Dies erfolgt direkt in Ephesoft Transact.
date: "2021-07-05"
tags:
  - TE²
  - Tabellenextraktion
  - Plugin
  - Ephesoft
  - Installation
  - Konfiguration
---

# TE²-Plugin Installation & Konfiguration

Das TE²-Plugin wird direkt in Ephesoft Transact installiert. Der Installationsprozess ist für Cloud- oder On-Premise-Instanzen gleich.

Voraussetzungen
Laden Sie das TE²-Plugin von hier herunter.
Sie müssen Administratorrechte in Ephesoft Transact haben.
Sie müssen eine funktionierende Batch-Klasse eingerichtet haben oder die Standard-Batch-Klasse von Polydocs GmbH für die Plugin-Verwendung installieren, wenn noch keine Batch-Klasse in Ihrem Ephesoft-System eingerichtet ist. (Kontaktieren Sie uns, um die Standard-Batch-Klasse von Polydocs GmbH zu erhalten.)

## Installation

### Schritt 1:

Öffnen Sie Ihr Ephesoft Transact-System.

![TE² - Table Extraction für Ephesoft Transact - 1 ](/_images/te/Ephesoft1.png)

### Schritt 2:

Als Administrator klicken Sie bitte auf den Administratorbereich und wählen z.B. "Batch-Klassen-Verwaltung". Öffnen Sie die Menüleiste auf der linken Seite und klicken Sie auf "Systemkonfiguration".

![TE² - Table Extraction für Ephesoft Transact - 2 ](/_images/te/Ephesoft2.png)

### Schritt 3:

Öffnen Sie das Workflow-Management. Ziehen Sie die Plugin-Zip-Dateien in den Bereich "Plugin importieren", um das Plugin automatisch zu installieren.

Stellen Sie sicher, dass der Dateiname genau "fellowtable2extractionplugin.zip" lautet und dass die Dateien nicht umbenannt werden (z.B. durch mehrfaches Herunterladen), da Ephesoft Dateien mit einem anderen Namen nicht erkennen kann.

![TE² - Table Extraction für Ephesoft Transact - 3 ](/_images/te/Ephesoft3.png)

Stellen Sie sicher, dass die Installation erfolgreich war, indem Sie die Liste unter Workflow-Management überprüfen, ob das neue Plugin aufgeführt ist (siehe Beispiel unten).

![TE² - Table Extraction für Ephesoft Transact - 4 ](/_images/te/Ephesoft4.png)


Der Installationsprozess des Plugins ist nun abgeschlossen und es kann einer Batch-Klasse zugeordnet und konfiguriert werden.

## Zuordnung zur Batch-Klasse & Konfiguration

### Schritt 1:

Öffnen Sie die Menüleiste auf der linken Seite und klicken Sie auf "Batch-Klassen-Verwaltung" und öffnen Sie die Batch-Klasse, in der das Plugin ausgeführt werden soll.

![TE² - Table Extraction für Ephesoft Transact - 5 ](/_images/te/Ephesoft5.png)

### Schritt 2:

Ordnen Sie das TE²-Plugin einer Batch-Klasse zu (FELLOW_TABLE2_EXTRACT). Klicken Sie auf Module und dann auf Extraction auf der linken Seite des Batch-Klassen-Konfigurationsbildschirms. Es werden alle Extraktionsmodule angezeigt, die für diese Batch-Klasse konfiguriert sind. Finden Sie FELLOW_TABLE2_EXTRACT in der Spalte "Zugeordnete Plugins" und verschieben Sie es durch Klicken auf den Pfeil nach rechts in die Spalte "Ausgewählte Plugins", wie im Bild unten gezeigt.

Halten Sie das Plugin FELLOW_TABLE2_EXTRACT in der Spalte "Ausgewählte Plugins" unten in der Liste und klicken Sie dann auf "Anwenden" und anschließend auf "Bereitstellen", um Ihre Änderungen zu aktivieren.

![TE² - Table Extraction für Ephesoft Transact - 6 ](/_images/te/Ephesoft6.png)

### Schritt 3:

Konfigurieren Sie das TE²-Plugin (FELLOW_TABLE2_EXTRACT). Erweitern Sie den Ordner "Extraktion" im linken Menü und wählen Sie das neu hinzugefügte Modul FELLOW_TABLE2_EXTRACT aus.

![TE² - Table Extraction für Ephesoft Transact - 7 ](/_images/te/Ephesoft7.png)

Richten Sie nun die Konfigurationsdetails wie unten beschrieben ein und klicken Sie dann auf "Anwenden" und "Bereitstellen".

| Feld                                          | Wert                                       | Beschreibung                          |
| ---------------------------------------------- | ------------------------------------------ | ------------------------------------ |
| Tabellenextraktion aktiviert (Version:1.0.3):*     | True                                       | Hier sehen Sie die Versionsnummer des installierten Plugins und setzen den Wert "True" für die Plugin-Aktivierung.  |
| Schlüsselwerte DLF-Namen (durch &#124; Symbol getrennt):* |	VAT_NO_EXTRACTED&#124;IBAN_EXTRACTED&#124;VENDOR_ID |	Liste der Schlüsselwerte, durch Pipe-Zeichen ("&#124;") getrennt |
|  Fellow Webservice-URL:*                       | https://cloudintegration.eu/api/fellowkv/extract_table/extract_table | Link zum Fellow-Cloud-Repository  |
| Fellow Webservice-API-Schlüssel:*                    | — von Fellow Consulting pro Abonnement bereitgestellt — | Persönlicher API-Schlüssel zur Verbindung mit dem Fellow-Cloud-Repository |


Bevor Sie das Plugin verwenden können.

Schritt 4: Erstellen Sie eine Tabelle in Ihrem Batch-Klassen-Dokumenttyp
HINWEIS: Dieser Schritt ist nur erforderlich, wenn Sie die Standard-Batch-Klasse von Fellow nicht verwenden.

Es ist erforderlich, eine Rechnungstabelle in der Konfiguration zu erstellen, damit Ephesoft Tabellen anzeigen kann.

Öffnen Sie das Menü und gehen Sie erneut zur Batch-Klassen-Verwaltung.

![TE² - Table Extraction für Ephesoft Transact - 8 ](/_images/te/Ephesoft8.png)

Öffnen Sie Ihre dedizierte Batch-Klasse.

![TE² - Table Extraction für Ephesoft Transact - 9 ](/_images/te/Ephesoft9.png)

Wählen Sie einen bestimmten Dokumenttyp (z.B. INVOICE_DE), öffnen Sie den Ordner "Indexfelder", wählen Sie "Tabellen" und klicken Sie auf "Hinzufügen".

![TE² - Table Extraction für Ephesoft Transact - 10 ](/_images/te/Ephesoft10.png)

Fügen Sie eine neue Tabelle mit dem Namen "InvoiceTable" hinzu und klicken Sie auf "Anwenden" und dann auf "Bereitstellen" (siehe zwei Screenshots unten).

![TE² - Table Extraction für Ephesoft Transact - 11 ](/_images/te/Ephesoft11.png)

![TE² - Table Extraction für Ephesoft Transact - 12 ](/_images/te/Ephesoft12.png)

Öffnen Sie den neu erstellten Ordner "InvoiceTable" und fügen Sie eine Spalte mit dem Namen "DESCRIPTION" hinzu.

![TE² - Table Extraction für Ephesoft Transact - 13 ](/_images/te/Ephesoft13.png)

![TE² - Table Extraction für Ephesoft Transact - 14 ](/_images/te/Ephesoft14.png)

Klicken Sie auf "Anwenden" und "Bereitstellen".

Beachten Sie, dass der Schritt "Erstellen Sie eine Tabelle in Ihrem Batch-Klassen-Dokumenttyp" für jeden Dokumenttyp durchgeführt werden muss.
Sobald Sie es für einen Dokumenttyp erledigt haben, können Sie es exportieren und in andere Dokumenttypen importieren:

Export

![TE² - Table Extraction für Ephesoft Transact - 15 ](/_images/te/Ephesoft15.png)

Importieren Sie es in einen anderen Dokumenttyp und klicken Sie auf "Anwenden" und "Bereitstellen".

Die Zuordnungs- und Konfigurationsphase des Plugins ist nun abgeschlossen. Beachten Sie, dass Sie den Transact-Server neu starten müssen.

## FINAL Schritt 5:

Starten Sie den Transact-Server neu. Lesen Sie den Artikel, wie Sie Transact neu starten können.