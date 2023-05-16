---
title: "Feedback-Funktion aktivieren"
date: "2021-07-05"
description: Erfahren Sie, wie Sie die Feedback-Funktion innerhalb der Ephesoft-Plugins aktivieren können. Feedback wird während des Validierungsprozesses eines Dokuments erstellt und gesendet.
tags:
  - Ephesoft-Plugins
  - Hilfe
  - Feedback
---

Dieses Dokument erklärt, wie Sie die Feedback-Funktion innerhalb der Ephesoft-Plugins aktivieren können.

Die Feedback-Funktion ermöglicht es Kunden, Feedback zu jedem einzelnen Test direkt während des Tests zu senden. Feedback wird während des Validierungsprozesses erstellt und gesendet. Für jede "Validierung", bei der der Benutzer Feedback eingibt, wird automatisch ein Ticket in unserem Ticket-System [Zammad](https://support.cloudintegration.eu/#ticket/view/all_open) erstellt. Das Ticket enthält Informationen über das Ergebnis (Feedback-Typ), die E-Mail-Adresse des Reporters und das Feedback (Textfeld), die vom Tester während der Validierung festgelegt wurden, sowie eine Kopie des getesteten Dokuments, das automatisch mit dem Ticket verknüpft wird.

Die Feedback-Funktion wird in der Batch-Klasse eingerichtet und konfiguriert und ist für die Kunden auf der Validierungs-Benutzeroberfläche von Ephesoft im Tab "5 Feedback" sichtbar.

![](/_images/doc2/Bildschirmfoto-2021-07-05-um-13.43.36-1024x475.png)

## Schritte zur Aktivierung des Feedbacks:

Laden Sie die Feedback-Feldtypen von unten herunter oder gehen Sie zu einer Batch-Klasse, in der Feedback bereits aktiviert ist, um sie von dort zu erhalten.
**Wenn Sie sie hier herunterladen, können Sie den in Schritt 1 erklärten Schritt überspringen**.

[INVOICE\_DE\_FieldTypes](https://docs.cloudintegration.eu/wp-content/uploads/2021/07/INVOICE_DE_FieldTypes.zip)[Herunterladen](https://docs.cloudintegration.eu/wp-content/uploads/2021/07/INVOICE_DE_FieldTypes.zip)

**Schritt 1: Feedback-Felder-Zip-Ordner erhalten**
Gehen Sie zur Batch-Klasse, in der Feedback eingerichtet ist, öffnen Sie "Indexfelder" und navigieren Sie zur letzten Seite, um die Feedback-Felder zu sehen (die letzten vier: FEEDBACK\_TYPE, FILE\_ID, FEEDBACK\_EMAIL, FEEDBACK\_DESCRIPTION).

Wählen Sie die letzten vier Felder aus und klicken Sie auf Exportieren, um sie auf Ihren Computer herunterzuladen.

![](/_images/doc2/Bildschirmfoto-2021-07-05-um-14.45.42-1024x476.png)

**Schritt 2: Importieren in (andere) Dokumenttypen**
Sobald Sie den Feedback-Felder-Zip-Ordner auf Ihrem Computer gespeichert haben, können Sie ihn in jeden Dokumenttyp in Ihrer Batch-Klasse importieren, in dem Sie ihn verfügbar haben möchten. Ziehen Sie einfach die Zip-Datei in den Ordner "Indexfelder" der einzelnen Dokumenttypen.

![](/_images/doc2/Bildschirmfoto-2021-07-05-um-15.02.15-1024x479.png)

_Hinweis: Dieser Schritt muss für jeden Dokumenttyp durchgeführt/wiederholt werden!_