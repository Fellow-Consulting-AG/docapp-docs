---
title: Infor ION API-Datei erstellen - Schritt-für-Schritt-Anleitung
description: Erfahren Sie, wie Sie eine Infor ION API-Datei erstellen, die für den Export von DOC² nach Infor mit den erforderlichen Berechtigungen des InforOS-Benutzers benötigt wird.
date: 2022-04-24
hero: Infor ION API-Datei erstellen
og_title: DOC² - Infor ION API-Datei erstellen
tags:
  - Export nach Infor
  - ION
  - DOC²
  - Einstellungen
---

# Infor ION API-Datei erstellen

#### Schritt-für-Schritt-Anleitung zur Erstellung einer Infor ION API-Datei, die für den Export nach Infor erforderlich ist.

**Voraussetzungen:**

- Ein Administrator-Benutzer für InforOS mit den Sicherheitsrollen `ION Desk Admin`, `ION API Admin` und `IDM Admin`.
- Ein InforOS-Benutzer, der als Servicekonto verwendet werden kann und die Berechtigung hat, Dokumente in IDM zu erstellen, mit den Sicherheitsrollen `IDM-AdvancedUser`, `Infor-SuiteUser` und `MingleEnterprise`.


**1\.** Öffnen Sie InforOS mit einem Administrator-Benutzer und wechseln Sie zum **Infor ION API**-Bildschirm.<br>
    Klicken Sie auf **Autorisierte Apps** und dann auf das `+`-Symbol.

![](/_images/doc2/infor-ion-api-1.png "Infor ION API-Datei erstellen - Schritt 1")

**2\.** Geben Sie einen aussagekräftigen Namen und eine Beschreibung wie 'Doc2Export' ein. Wählen Sie `Backend Service` und klicken Sie auf das Diskettensymbol, um zu speichern.

![](/_images/doc2/infor-ion-api-2.png "Infor ION API-Datei erstellen - Schritt 2")

**3\.** Sobald die Einträge gespeichert sind, klicken Sie auf die Schaltfläche **Anmeldeinformationen herunterladen**.

![](/_images/doc2/infor-ion-api-3.png "Infor ION API-Datei erstellen - Schritt 3")

**4\.** Schalten Sie `Create Service Account` ein und geben Sie den Namen des Service-Benutzers in das Feld ein.

![](/_images/doc2/infor-ion-api-4.png "Infor ION API-Datei erstellen - Schritt 4")

**5\.** Klicken Sie auf `DOWNLOAD`, um die ION API-Datei herunterzuladen.