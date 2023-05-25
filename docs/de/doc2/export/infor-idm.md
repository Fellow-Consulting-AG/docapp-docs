---
title: "Export nach Infor IDM"
description: Schritt-für-Schritt-Anleitung, wie man Dokumente ohne Veröffentlichung der Werte in einem separaten BOD nach Infor Document Management (IDM) exportiert.
date: "2021-10-22"
tags:
  - DOC²
  - Export
  - Infor
  - IDM
---

#### Export mach Infor Document Management ohne Veröffentlichung der Dokumentwerte in einem separaten BOD

In dieser Schritt-für-Schritt-Anleitung wird erklärt, wie man Dokumente nach Infor Document Management (IDM) exportiert, ohne die Werte in einem separaten BOD zu veröffentlichen.

**Voraussetzungen:**

- Ein Admin-Benutzer für Infor OS mit den Sicherheitsrollen "ION Desk Admin", "ION API Admin" und "IDM Admin".
- Eine ION-API-Datei, um die Kommunikation zwischen DOC² und Infor IDM zu erstellen. Folgen Sie der Dokumentation hier: [Wie man eine Infor ION-Datei erstellt](/doc2/export/create-a-infor-ion-file/)
- Ein IDM-Dokumenttyp, zu dem die Dokumente exportiert werden sollen.
- Eine IDM-Mapping-Datei, die IDM verwendet, um zu wissen, welcher Dokumentinhalt welche Informationen darstellt. Ein Beispiel für die IDM-Mapping-Datei finden Sie auf dieser Seite: [Wie man eine IDM-Mapping-Datei erstellt](/doc2/export/how-to-create-a-idm-mapping-file/)

Melden Sie sich bei DOC² an, klicken Sie auf "Einstellungen" und wählen Sie "Export".

![](/_images/doc2/ExportToInforIDM_1.png)

Einstellungen - Export

Klicken Sie auf "Integration hinzufügen".

![](/_images/doc2/ExportToInforIDM_2.png)

Einstellungen - Export - Integration hinzufügen

Wählen Sie "Infor IDM".

![](/_images/doc2/ExportToInforIDM_3.png)

Klicken Sie auf den Abschnitt "ION-API-Datei" und wählen Sie die ION-API-Datei aus, die Sie für die Kommunikation zwischen DOC² und IDM verwenden möchten. Wenn Sie keine ION-API-Datei haben, folgen Sie dieser Dokumentation, um eine zu erstellen: [Wie man eine Infor ION-Datei erstellt](/doc2/export/create-a-infor-ion-file/)

Bei normalen Exporten müssen Sie auf dem linken Schieberegler "CLOUD" auswählen. Mit dem rechten Schieberegler können Sie wählen, ob Sie die normale PDF-Rechnung an Infor exportieren möchten oder ob Sie die Rechnung als ZUGfERD (PDF mit X-Rechnung im ZUGfERD-XML-Format) exportieren möchten.
![](/_images/doc2/ExportToInforIDM_4_PDF_Cloud.png)
![](/_images/doc2/ExportToInforIDM_4_ZUGfERD_Cloud.png)
Bei Exporten mit [Watchdog](/doc2/fileshare/) müssen Sie auf dem linken Schieberegler "ONPREM" auswählen.
![](/_images/doc2/ExportToInforIDM_4_PDF_OnPrem.png)
![](/_images/doc2/ExportToInforIDM_4_ZUGfERD_OnPrem.png)

Klicken Sie auf den Abschnitt "IDM-Mapping-Datei" und wählen Sie die IDM-Mapping-Datei aus, die Sie für den Export verwenden möchten.
Ein Beispiel für die IDM-Mapping-Datei finden Sie auf dieser Seite: [Wie man eine IDM-Mapping-Datei erstellt](/doc2/export/how-to-create-a-idm-mapping-file/)
![](/_images/doc2/ExportToInforIDM_5_PDF_Cloud.png)
![](/_images/doc2/ExportToInforIDM_5_ZUGfERD_Cloud.png)
![](/_images/doc2/ExportToInforIDM_5_PDF_OnPrem.png)
![](/_images/doc2/ExportToInforIDM_5_ZUGfERD_OnPrem.png)

Klicken Sie auf "Speichern", um die Exporteinstellung zu speichern.