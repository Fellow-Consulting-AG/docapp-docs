---
title: "Export zu Infor ION und IDM"
description: Schritt-für-Schritt-Anleitung, wie man Dokumente von DocBits (Doc²) nach Infor Document Management (IDM) exportiert und dabei die Werte in einem separaten Sync.CaptureDocument BOD veröffentlicht.
icon: material/application-export
date: "2021-10-22"
tags:
  - DocBits (Doc²)
  - Export
  - Infor
  - Infor OS
  - ION
  - IDM
---

####
Export zu Infor Document Management mit Veröffentlichung der Dokumentwerte in einem separaten BOD

In dieser Schritt-für-Schritt-Anleitung wird erklärt, wie man Dokumente von DocBits (Doc²) nach Infor Document Management (IDM) exportiert und dabei die Werte in einem separaten Sync.CaptureDocument BOD veröffentlicht.

**Voraussetzungen:**

- Ein Admin-Benutzer für InforOS mit den Sicherheitsrollen "ION Desk Admin", "ION API Admin" und "IDM Admin".
- Eine ION-API-Datei, um die Kommunikation zwischen DocBits (Doc²) und Infor IDM zu erstellen. Folgen Sie der Dokumentation hier: [Wie man eine Infor ION API-Datei erstellt](/docbits/export/create-a-infor-ion-api-file/)
- Ein IDM-Dokumenttyp, in den die Dokumente exportiert werden sollen.

#### Schritte in DocBits (Doc²)

Melden Sie sich bei DocBits (Doc²) an, klicken Sie auf **EINSTELLUNGEN** und wählen Sie **Export**.

![Einstellungen Export](/_images/docbits/export/doc2-einstellungen-export.png)


Klicken Sie in den Export-Einstellungen auf `+HINZUFÜGEN`.

![Export Einstellung hinzufügen](/_images/docbits/export/doc2-export einstellung hinzufügen.png)


Wählen Sie "Infor IDM + ION BOD".

![](/_images/docbits/export/doc2-export-infor idm + ion bod.png)

Klicken Sie auf den Abschnitt "ION-Zuordnungsdatei" und wählen Sie die ION-API-Datei aus, die Sie für die Kommunikation zwischen DocBits (Doc²) und IDM verwenden möchten. Wenn Sie keine ION-API-Datei haben, folgen Sie dieser Dokumentation, um eine zu erstellen: [Wie man eine Infor ION API-Datei erstellt](/docbits/export/create-a-infor-ion-api-file/)

![](/_images/docbits/export/doc2-infor-ion-ion-zuordnungsdatei.png)

Klicken Sie auf den Abschnitt "IDM-Zuordnungsdatei" und wählen Sie die IDM-Mapping-Datei aus, die Sie für den Export verwenden möchten.
Ein Beispiel für die IDM-Zuordnungsdatei finden Sie auf dieser Seite: [Wie man eine IDM-Mapping-Datei erstellt](/docbits/export/how-to-create-a-idm-mapping-file/)

![](/_images/docbits/export/doc2-infor-ion-idm-zuordnungsdatei.png)

Klicken Sie auf den Abschnitt "BOD-Zuordnungsdatei" und wählen Sie die BOD-Mapping-Datei aus, die Sie für den Export verwenden möchten.
Ein Beispiel für die BOD-Zuordnungsdatei finden Sie auf dieser Seite: [Wie man eine BOD-Mapping-Datei erstellt](/docbits/export/how-to-create-a-bod-mapping-file/)

![](/_images/docbits/export/doc2-infor-ion-bod-zuordnungsdatei.png)

Klicken Sie auf `SPEICHERN`, um die Exporteinstellungen zu speichern.

Fügen Sie die Export-Einstellungen für jeden zur Verarbeitung gewünschten Dokumententyp beispielsweise wie folgt hinzu:
![](/_images/docbits/export/doc2-export-einstellungen für alle dokumententypen.png)

Nutzen Sie eine On-Premise ERP Software müssen Sie lediglich auf dem linken Schieberegler statt `CLOUD` `ONPREM` auswählen.

![](/_images/docbits/export/doc2-infor-schaltfläche-onprem.png)


#### Schritte in Infor ION

Öffnen Sie **Infor ION API**, wählen Sie "Autorisierte Apps" und klicken Sie auf die DocBits (Doc²)-Anwendung.

![](/_images/docbits/Infor/infor-ion-api-autorisierte app-doc2export.png)

Kopieren und speichern Sie die "Client-ID", diese ID wird später benötigt.

![](/_images/docbits/Infor/infor-ion-api-autorisierte app-client-id.png)

Öffnen Sie **ION Desk** über das Burger-Menü, wählen Sie "ION Connect" und klicken Sie auf "Verbindungspunkte".

Klicken Sie auf "+Hinzufügen" und wählen Sie "IMS über ION API".

![](/_images/docbits/Infor/infor-ion-desk-verbindungspunkte.png)

Geben Sie einen aussagekräftigen Namen und eine aussagekräftige Beschreibung ein.

Deaktivieren Sie das Kontrollkästchen "Anwendung verfügt über IMS-Endpunkt" und geben Sie die "Client-ID" ein, die aus ION API kopiert wurde.

![](/_images/docbits/Infor/infor-ion-desk-anwendungsverbindungspunkt.png)

Wechseln Sie zur Registerkarte `Dokumente`.

Klicken Sie auf das "+"-Symbol und geben Sie im Filterfeld "Sync.CaptureDocument" ein. Die Liste sollte nun den richtigen BOD anzeigen. Aktivieren Sie das Kontrollkästchen vor "Sync.CaptureDocument" und klicken Sie auf "OK".

![](/_images/docbits/Infor/infor-ion-desk-anwendungsverbindungspunkt-dokumente.png)

Klicken Sie oben links auf das Disketten-Symbol, um die Einstellungen zu speichern.


Wechseln Sie zu "Datenflüsse" und klicken Sie auf "+Hinzufügen" und wählen "Dokument-Flow".

![](/_images/docbits/Infor/infor-ion-desk-datenflüsse.png)

Geben Sie einen aussagekräftigen Namen und eine aussagekräftige Beschreibung ein.

Ziehen Sie eine "Anwendung" in den Fluss und nennen Sie sie "DocBits (Doc²)".

![](/_images/docbits/Infor/infor-ion-desk-datenflüsse-anwendung.png)

Klicken Sie auf das "+"-Symbol und wählen Sie die "DocBits (Doc²)"-Anwendung, in diesem Fall "Doc2Export", und klicken Sie auf "OK".

![](/_images/docbits/Infor/infor-ion-desk-datenflüsse-anwendung auswählen.png)

Klicken Sie auf das Disketten-Symbol, um den neuen Dokumentenfluss zu speichern.

![](/_images/docbits/Infor/infor-ion-desk-dokument-flow-speichern.png)