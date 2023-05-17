---
title: "SSO in Infor Cloud konfigurieren"
date: "2021-10-14"
description: In diesem Schritt-für-Schritt-Leitfaden erfahren Sie, wie Sie SSO in Infor Cloud konfigurieren. Wir beginnen mit den Voraussetzungen, dem Zugriff auf die Cloud und der Überprüfung, um einen neuen Dienstanbieter hinzuzufügen.
tags:
  - Infor
  - SSO
  - Cloud
  - neuer Dienstanbieter
---

# SSO in Infor Cloud konfigurieren

## Schritt für Schritt Anleitung

### **Voraussetzungen**

<table><tbody><tr><td><strong>Erforderliche Informationen</strong></td><td><strong>Beschreibung</strong></td></tr><tr><td>Anmeldedaten für die Cloud</td><td>Zugangsdaten sind erforderlich, um auf die Infor Cloud-Umgebung zuzugreifen.<br>Der Benutzer sollte die Rollen "Infor-Systemadministrator" und "UserAdmin" haben.</td></tr><tr><td>Admin-Details konfigurieren (DOC²)</td><td>Sie sollten eine E-Mail von FellowPro AG mit den Anmeldedaten für die Seite „DOC² SSO-Einstellungen“ erhalten haben.<br><br>Sie benötigen einen Benutzernamen und ein Passwort.<br></td></tr><tr><td>Zertifikat</td><td>Sie können das Zertifikat in DOC² in den Einstellungen unter Integration - SSO Dienstanbieter-Einstellungen herunterladen.</td></tr></tbody></table>

**1\. Zugriff auf die Cloud erhalten und Zugriff überprüfen**

Die URL beginnt mit [https://mingle-portal.eu1.inforcloudsuite.com](https://mingle-portal.eu1.inforcloudsuite.com/<TENANT\_NAME)\> gefolgt von Ihrer persönlichen Erweiterung.

!["Infor Cloud Login-Seite"](/_images/doc2/SSO in infor cloud/infor-signin.png)

a) Wählen Sie die Option "Cloud Identities" und geben Sie Ihre Anmeldedaten ein.

!["Infor Cloud Login"](/_images/doc2/SSO in infor cloud/Infor-cloudidentities-login.png)

b) Nach dem Login haben Sie Zugriff zur Infor Cloud. Sie werden auf diese Seite weitergeleitet, aber im Burger-Menü finden Sie den Zugang zu allen Anwendungen.

!["Infor Cloud Dashboard"](/_images/doc2/SSO in infor cloud/Welcome-to-infor-Ming.le.png)

!["Infor Cloud Burger-Menü"](/_images/doc2/SSO in infor cloud/infor_Burger-Menu.png)

**2\. Öffnen Sie die Benutzerverwaltung, um einen neuen Dienstanbieter hinzuzufügen**

Auf der rechten Seite der Menüleiste finden Sie das Benutzermenü, über das Sie auf die Benutzerverwaltung zugreifen können.

!["Infor Cloud Benutzerverwaltung"](/_images/doc2/SSO in infor cloud/infor-cloud-benutzerverwaltung.png)

a) Wählen Sie dann im linken Menü die Option **Sicherheitseinstellungen** und **Dienstanbieter**.

!["Infor Cloud Sicherheitseinstellungen"](/_images/doc2/SSO in infor cloud/infor-dienstanbieter.png)

b. Sie sehen nun dieses Fenster mit den Dienstanbietern.

!["Infor Cloud Dienstanbieter"](/_images/doc2/SSO in infor cloud/infor-dienstanbieter-1.png)

c. Klicken Sie nun auf das "+"-Symbol und fügen Sie unseren DOC² als Dienstanbieter hinzu. (Siehe Schritt 4)

!["Infor Cloud Dienstanbieter hinzufügen"](/_images/doc2/SSO in infor cloud/infor-dienstanbieter-2.png)

**3\. Greifen Sie in DOC² auf die SSO DIENSTANBIETER-EINSTELLUNGEN zu**

a) Melden Sie sich über die URL [https://app.polydocs.io/](https://app.polydocs.io/) mit den Anmeldedaten an, die Sie von uns erhalten haben.

b) Gehen Sie zu EINSTELLUNGEN (in der oberen Leiste) und wählen Sie Integration.
Dort finden Sie alle Informationen, die Sie für die folgenden Schritte benötigen.

!["DOC² Einstellungen Integration"](/_images/doc2/SSO in infor cloud/doc2-einstellungen-integration.png)

c) Laden Sie das Zertifikat herunter.

!["DOC² SSO Dienstanbieter-Einstellungen"](/_images/doc2/SSO in infor cloud/doc2-sso-dienstanbieter-einstellungen.png)

**4\. Füllen Sie den Dienstanbieter mit Hilfe der SSO Dienstanbieter-Einstellungen in DOC² aus**

![](/_images/doc2/SSO in infor cloud/infor-dienstanbieter-3.png)

<table><tbody><tr><td><strong>Feld</strong></td><td><strong>Wert</strong></td></tr><tr><td><strong>Anwendungstyp</strong></td><td>DEFAULT_SAML</td></tr><tr><td><strong>Anzeigename</strong></td><td>DOC²</td></tr><tr><td><strong>Entitäts-ID</strong></td><td>Siehe Entitäts-ID unter SSO Dienstanbieter-Einstellungen</td></tr><tr><td><strong>SSO-Endpunkt</strong></td><td>Kopieren Sie die SSO-URL aus SSO Dienstanbieter-Einstellungen und fügen Sie sie in das Feld <strong>SSO-Endpunkt</strong> ein.</td></tr><tr><td><strong>SLO-Endpunkt</strong></td><td>Kopieren Sie die SLO-URL aus SSO Dienstanbieter-Einstellungen und fügen Sie sie in das Feld <strong>SLO-Endpunkt</strong> ein.</td></tr><tr><td><strong>Signaturzertifikat</strong></td><td>Laden Sie die entsprechende .cer-Datei hoch, die Sie in Schritt 3c) aus SSO Dienstanbieter-Einstellungen heruntergeladen haben.</td></tr><tr><td><strong>Name ID-Format und Mapping</strong></td><td>E-Mail-Adresse</td></tr></tbody></table>

![](/_images/doc2/SSO in infor cloud/infor-dienstanbieter-mit zertifikat.png)

a) Wenn Sie alles ausgefüllt haben, denken Sie daran, es mit dem Diskettensymbol über dem Application Type zu speichern. Sie gelangen automatisch zurück auf die Übersicht der Dienstanbieter.

b) Wählen Sie dann den eben angelegten Dienstanbieter DOC² aus und klicken Sie auf den `Stift` zum Bearbeiten.

c) Klicken Sie auf `ANZEIGEN`unter **Identitätsanbieterdaten** 

!["Identitätsanbieterdaten anzeigen"](/_images/doc2/SSO in infor cloud/infor-dienstanbieter-identitätsanbieterdaten-anzeigen.png)

!["Identitätsanbieterdaten"](/_images/doc2/SSO in infor cloud/identitätsanbieterdaten_saml-metadaten-export.png)

d) Exportieren Sie die **SAML METADATEN**.

Die Datei sieht so aus: ServiceProviderSAMLMetadata_xxxxxxx_02_02_2022

**5\. Importieren Sie die SAML METADATEN in den Identitätsanbieter-Einstellungen.**

Gehen Sie zu Identitätsanbieter-Einstellungen, geben Sie Ihre Tenant ID ein (z.B. FELLOWPRO_DEV) und darunter sehen Sie neben `Datei hochladen` die Schaltfläche **IMPORTIEREN**, über die Sie die zuvor exportierte SAML METADATA-Datei hochladen müssen.

a) Klicken Sie auf IMPORTIEREN und wählen Sie dann die METADATA-Datei aus, die Sie bereits aus den SSO SERVICE PROVIDER SETTINGS heruntergeladen haben.

b) Klicken Sie auf KONFIGURIEREN

!["Identitätsanbieter-Einstellungen"](/_images/doc2/SSO in infor cloud/doc2-identitätsanbieter-einstellungen.png)

Dieser Teil ist erfolgreich abgeschlossen, wenn Sie das folgende Popup sehen.

!["Identitätsanbieter-Einstellungen Datei erfolgreich gespeichert"](/_images/doc2/SSO in infor cloud/doc2-identitätsanbieter-einstellungen_erfolgreich gespeichert.png)

**6\. Fügen Sie eine neue Anwendung in Infor Ming.le hinzu**

a) Gehen Sie zu den Admin-Einstellungen und

![](/_images/doc2/infor_Admin-Settings_Manage-Applications-1024x528.png){ loading=lazy alt="Infor Cloud Admin-Einstellungen" }

b) Klicken Sie oben rechts auf ANWENDUNG HINZUFÜGEN

![](/_images/doc2/infor_Add-Application.png){ loading=lazy alt="Infor Cloud Anwendung hinzufügen" }

c) Füllen Sie alle Felder wie auf dem folgenden Bild aus, aber mit Ihrer eigenen SSO-URL. Vergessen Sie nicht, ein Symbol auszuwählen und auf SPEICHERN zu klicken.

![](/_images/doc2/infor_Add-New-Application.png){ loading=lazy alt="Infor Cloud Neue Anwendung hinzufügen" }

**Und jetzt der letzte Schritt:**

- Melden Sie sich von DOC² ab.
- Gehen Sie zurück zum Burger-Menü in Infor und wählen Sie das von Ihnen erstellte Symbol.
- Und Sie sind bereits auf dem Dashboard von DOC².

![](/_images/doc2/Sign-in-over-SSO-1024x640.png){ loading=lazy alt="DOC² Dashboard" }