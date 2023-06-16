---
title: "Export nach Infor IDM"
description: Schritt-für-Schritt-Anleitung, wie man Dokumente ohne Veröffentlichung der Werte in einem separaten BOD nach Infor Document Management (IDM) exportiert.
date: "2021-10-22"
tags:
  - Docbits (Doc²)
  - Export
  - Infor
  - IDM
---

#### Export mach Infor Document Management ohne Veröffentlichung der Dokumentwerte in einem separaten BOD

In dieser Schritt-für-Schritt-Anleitung wird erklärt, wie man Dokumente nach Infor Document Management (IDM) exportiert, ohne die Werte in einem separaten BOD zu veröffentlichen.

**Voraussetzungen:**

- Ein Admin-Benutzer für InforOS mit den Sicherheitsrollen "ION Desk Admin", "ION API Admin" und "IDM Admin".
- Eine ION-API-Datei, um die Kommunikation zwischen Docbits (Doc²) und Infor IDM zu erstellen. Folgen Sie der Dokumentation hier: [Wie man eine Infor ION API-Datei erstellt](/docbits/export/create-a-infor-ion-api-file/)
- Ein IDM-Dokumenttyp, in den die Dokumente exportiert werden sollen.
- Eine IDM-Zuordnungsdatei, die IDM verwendet, um zu wissen, welcher Dokumentinhalt welche Informationen darstellt. Ein Beispiel für die IDM-Mapping-Datei finden Sie auf dieser Seite: [Wie man eine IDM-Mapping-Datei erstellt](/docbits/export/how-to-create-a-idm-mapping-file/)

Melden Sie sich bei Docbits (Doc²) an, klicken Sie auf **EINSTELLUNGEN** und wählen Sie **Export**.

![Einstellungen Export](/_images/docbits/export/doc2-einstellungen-export.png)


Klicken Sie in den Export-Einstellungen auf `+HINZUFÜGEN`.

![Export Einstellung hinzufügen](/_images/docbits/export/doc2-export einstellung hinzufügen.png)


Wählen Sie "Infor IDM".

![](/_images/docbits/export/doc2-export-infor idm.png)

Klicken Sie auf den Abschnitt "ION-Zuordnungsdatei" und wählen Sie die ION-API-Datei aus, die Sie für die Kommunikation zwischen Docbits (Doc²) und IDM verwenden möchten. Wenn Sie keine ION-API-Datei haben, folgen Sie dieser Dokumentation, um eine zu erstellen: [Wie man eine Infor ION API-Datei erstellt](/docbits/export/create-a-infor-ion-api-file/)

Bei normalen Exporten müssen Sie auf dem linken Schieberegler `CLOUD` auswählen. Mit dem rechten Schieberegler können Sie wählen, ob Sie die normale PDF-Rechnung an Infor exportieren möchten oder ob Sie die Rechnung im ZUGFeRD-Format (PDF mit X-Rechnung Format ZUGFeRD XML Anhang) exportieren möchten.

![](/_images/docbits/export/doc2_infor-idm-cloud-pdf.png)
![](/_images/docbits/export/doc2_infor-idm-cloud-ZUGFeRD.png)
Bei Exporten mit [Watchdog](/docbits/fileshare/) müssen Sie auf dem linken Schieberegler "ONPREM" auswählen.
![](/_images/docbits/export/doc2_infor-idm-onprem-pdf.png)
![](/_images/docbits/export/doc2_infor-idm-onprem-ZUGFeRD.png)

Klicken Sie auf den Abschnitt "IDM-Zuordnungsdatei" und wählen Sie die IDM-Mapping-Datei aus, die Sie für den Export verwenden möchten.
Ein Beispiel für die IDM-Zuordnungsdatei finden Sie auf dieser Seite: [Wie man eine IDM-Mapping-Datei erstellt](/docbits/export/how-to-create-a-idm-mapping-file/)

![](/_images/docbits/export/doc2_infor-idm-cloud-pdf_2.png)
![](/_images/docbits/export/doc2_infor-idm-cloud-ZUGFeRD_2.png)
![](/_images/docbits/export/doc2_infor-idm-onprem-pdf_2.png)
![](/_images/docbits/export/doc2_infor-idm-onprem-ZUGFeRD_2.png)

Klicken Sie auf `SPEICHERN`, um die Exporteinstellungen zu speichern.