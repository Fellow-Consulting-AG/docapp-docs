---
title: "Export zu Infor ION und IDM"
description: Schritt-für-Schritt-Anleitung, wie man Dokumente von DOC² nach Infor Document Management (IDM) exportiert und dabei die Werte in einem separaten Sync.CaptureDocument BOD veröffentlicht.
icon: material/application-export
date: "2021-10-22"
tags:
  - DOC²
  - Export
  - Infor
  - Infor OS
  - ION
  - IDM
---

####
Export zu Infor Document Management mit Veröffentlichung der Dokumentwerte in einem separaten BOD

In dieser Schritt-für-Schritt-Anleitung wird erklärt, wie man Dokumente von DOC² nach Infor Document Management (IDM) exportiert und dabei die Werte in einem separaten Sync.CaptureDocument BOD veröffentlicht.

**Voraussetzungen:**

- Ein Admin-Benutzer für InforOS mit den Sicherheitsrollen "ION Desk Admin", "ION API Admin" und "IDM Admin".
- Eine ION-API-Datei, um die Kommunikation zwischen DOC² und Infor IDM zu erstellen. Folgen Sie der Dokumentation hier: [Wie man eine Infor ION-Datei erstellt](/doc2/export/create-a-infor-ion-file/)
- Ein IDM-Dokumenttyp, in den die Dokumente exportiert werden sollen.

#### Schritte in DOC²

Melden Sie sich bei DOC² an, klicken Sie auf **EINSTELLUNGEN** und wählen Sie **Export**.

![Einstellungen Export](/_images/doc2/export/doc2-einstellungen-export.png)


Klicken Sie in den Export-Einstellungen auf `+HINZUFÜGEN`.

![Export Einstellung hinzufügen](/_images/doc2/export/doc2-export einstellung hinzufügen.png)


Wählen Sie "Infor IDM + ION BOD".

![](/_images/doc2/export/doc2-export-infor idm + ion bod.png)

Klicken Sie auf den Abschnitt "ION-Zuordnungsdatei" und wählen Sie die ION-API-Datei aus, die Sie für die Kommunikation zwischen DOC² und IDM verwenden möchten. Wenn Sie keine ION-API-Datei haben, folgen Sie dieser Dokumentation, um eine zu erstellen: [Wie man eine Infor ION-Datei erstellt](/doc2/export/create-a-infor-ion-file/)

![](/_images/doc2/image-32-1024x347.png)

Klicken Sie auf den Abschnitt "IDM-Mapping-Datei" und wählen Sie die IDM-Mapping-Datei aus, die Sie für den Export verwenden möchten.
Ein Beispiel für die IDM-Mapping-Datei finden Sie auf dieser Seite: [Wie man eine IDM-Mapping-Datei erstellt](/doc2/export/how-to-create-a-idm-mapping-file/)

![](/_images/doc2/image-33-1024x344.png)

Klicken Sie auf den Abschnitt "BOD-Mapping-Datei" und wählen Sie die BOD-Mapping-Datei aus, die Sie für den Export verwenden möchten.
Ein Beispiel für die BOD-Mapping-Datei finden Sie auf dieser Seite: [Wie man eine BOD-Mapping-Datei erstellt](/doc2/export/how-to-create-a-bod-mapping-file/)

![](/_images/doc2/image-34-1024x343.png)

Klicken Sie auf "Speichern", um die Exporteinstellung zu speichern.

#### Schritte in Infor ION

Öffnen Sie "Infor ION API", wählen Sie "Autorisierte Apps" und klicken Sie auf die DOC²-Anwendung.

![](/_images/doc2/image-35.png)

Kopieren und speichern Sie die "Client-ID", diese ID wird später benötigt.

![](/_images/doc2/image-36.png)

Öffnen Sie "ION Desk", öffnen Sie das Burger-Menü, wählen Sie "Verbinden" und klicken Sie auf "Verbindungspunkte".

Klicken Sie auf "+Hinzufügen" und wählen Sie "IMS via ION API".

![](/_images/doc2/image-37.png)

Geben Sie einen aussagekräftigen Namen und eine aussagekräftige Beschreibung ein.

Deaktivieren Sie das Kontrollkästchen "Anwendung hat IMS EndPoint" und geben Sie die "Client-ID" ein, die aus ION API kopiert wurde.

![](/_images/doc2/image-39-1024x438.png)

Wechseln Sie zur Registerkarte "Dokumente".

Klicken Sie auf das "+"-Symbol und geben Sie im Filterfeld "Sync.CaptureDocument" ein. Die Liste sollte nun das richtige BOD anzeigen. Aktivieren Sie das Kontrollkästchen vor "Sync.CaptureDocument" und klicken Sie auf "OK".

![](/_images/doc2/image-40-1024x944.png)

Klicken Sie auf das Disketten-Symbol, um die Einstellungen zu speichern.

![](/_images/doc2/image-41.png)

Wechseln Sie zu "Datenflüsse" und klicken Sie auf "+Hinzufügen" und wählen Sie "Dokumentenfluss".

![](/_images/doc2/image-43.png)

Geben Sie einen aussagekräftigen Namen und eine aussagekräftige Beschreibung ein.

Ziehen Sie eine "Anwendung" in den Fluss und nennen Sie sie "Doc2".

![](/_images/doc2/image-44.png)

Klicken Sie auf das "+"-Symbol und wählen Sie die "Doc2"-Anwendung, in diesem Fall "Doc2Export", und klicken Sie auf "OK".

![](/_images/doc2/image-45.png)

Klicken Sie auf das Disketten-Symbol, um den neuen Dokumentenfluss zu speichern.

![](/_images/doc2/image-46.png)