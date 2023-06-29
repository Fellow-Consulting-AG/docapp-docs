---
title: Infor ION API-Datei erstellen - Schritt-für-Schritt-Anleitung
description: Erfahren Sie, wie Sie eine Infor ION API-Datei erstellen, die für den Export von DocBits (Doc²) nach Infor mit den erforderlichen Berechtigungen des InforOS-Benutzers benötigt wird.
date: 2022-04-24
hero: Infor ION API-Datei erstellen
og_title: DocBits (Doc²) - Infor ION API-Datei erstellen
tags:
  - Export nach Infor
  - ION
  - DocBits (Doc²)
  - Einstellungen
---

# Infor ION API-Datei erstellen

#### Schritt-für-Schritt-Anleitung zur Erstellung einer Infor ION API-Datei, die für den Export nach Infor erforderlich ist.

**Voraussetzungen:**

- Ein Administrator-Benutzer für Infor OS mit den Sicherheitsrollen `ION Desk Admin`, `ION API Admin` und `IDM Admin`.
- Ein Infor OS-Benutzer, der als Servicekonto verwendet werden kann und über die Berechtigung zum Erstellen von Dokumenten in IDM mit den Sicherheitsrollen `IDM-AdvancedUser`, `Infor-SuiteUser` und `MingleEnterprise` verfügt.


**1\.** Öffnen Sie Infor OS mit einem Administrator-Benutzer und wechseln Sie zum **Infor ION API**-Bildschirm.<br>
    Klicken Sie auf **Autorisierte Apps** und dann auf das `+`-Symbol.

!["Infor ION API-Datei erstellen - Schritt 1"](/_images/docbits/Infor/Infor-ion-api-autorisierte apps-hinzufügen.png)

**2\.** Geben Sie einen aussagekräftigen Namen und eine Beschreibung wie 'Doc2Export' ein. Wählen Sie `Back-End-Dienst` und klicken Sie auf das Diskettensymbol, um zu speichern.

!["Infor ION API-Datei erstellen - Schritt 2"](/_images/docbits/Infor/Infor-ion-api-neue-autorisierte-app-erstellen.png)

**3\.** Sobald die Einträge gespeichert sind, klicken Sie auf die Schaltfläche **Anmeldedaten herunterladen**.

!["Infor ION API-Datei erstellen - Schritt 3"](/_images/docbits/Infor/Infor-ion-api-autorisierte-app-anmeldedaten-herunterladen.png)

**4\.** Aktivieren Sie `Dienstkonto erstellen` und geben Sie den Namen des Service-Benutzers in das Feld ein.

!["Infor ION API-Datei erstellen - Schritt 4"](/_images/docbits/Infor/Infor-ion-api-anmeldedaten-herunterladen.png)

**5\.** Klicken Sie auf `HERUNTERLADEN`, um die ION API-Datei herunterzuladen.

!["Infor ION API-Datei"](/_images/docbits/Infor/Infor-ion-api-datei.png)