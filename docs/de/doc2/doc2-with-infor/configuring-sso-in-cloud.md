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

## Schritt-für-Schritt-Anleitung

### **Voraussetzungen**

<table><tbody><tr><td><strong>Erforderliche Informationen</strong></td><td><strong>Beschreibung</strong></td></tr><tr><td>Login-Daten für die Cloud</td><td>Zugangsdaten sind erforderlich, um auf die Infor Cloud-Umgebung zuzugreifen.<br>Der Benutzer sollte die Rollen "Infor-Systemadministrator" und "UserAdmin" haben.</td></tr><tr><td>Admin-Details konfigurieren (DOC²)</td><td>Sie sollten eine E-Mail von FellowPro AG mit den Anmeldedaten für die Seite „DOC² SSO-Einstellungen“ erhalten haben.<br><br>Sie benötigen einen Benutzernamen und ein Passwort.<br></td></tr><tr><td>Zertifikat</td><td>Sie können das Zertifikat in DOC² in den Einstellungen unter Integration - SSO Dienstanbieter-Einstellungen herunterladen.</td></tr></tbody></table>

**1\. Zugriff auf die Cloud erhalten und Zugriff überprüfen**

Die URL beginnt mit [https://mingle-portal.eu1.inforcloudsuite.com/<TENANT\_NAME](https://mingle-portal.eu1.inforcloudsuite.com/)\> gefolgt von Ihrer persönlichen Erweiterung.

![](/_images/doc2/infor-signin-1024x520.png){ loading=lazy alt="Infor Cloud Login-Seite" }

a) Wählen Sie die Option "Cloud Identities" und geben Sie Ihre Anmeldedaten ein.

![](/_images/doc2/LogIn-infor-1024x640.png){ loading=lazy alt="Infor Cloud Login" }

b) Nach dem Login haben Sie Zugriff zur Infor Cloud. Sie werden auf diese Seite weitergeleitet, aber im Burger-Menü finden Sie den Zugang zu allen Anwendungen.

![](/_images/doc2/Welcome-to-infor-Ming.le_-1024x585.png){ loading=lazy alt="Infor Cloud Dashboard" }

![](/_images/doc2/infor_Burger-Menu-1024x586.png){ loading=lazy alt="Infor Cloud Burger-Menü" }

**2\. Öffnen Sie die Benutzerverwaltung, um einen neuen Dienstanbieter hinzuzufügen**

Auf der rechten Seite der Menüleiste finden Sie das Benutzermenü, über das Sie auf die Benutzerverwaltung zugreifen können.

![](/_images/doc2/infor_User-Management-1024x548.png){ loading=lazy alt="Infor Cloud Benutzerverwaltung" }

a) Wählen Sie dann im linken Menü die Option **Sicherheitsverwaltung** und **Dienstanbieter**.

![](/_images/doc2/infor_Service-Provider-1024x523.png){ loading=lazy alt="Infor Cloud Sicherheitsverwaltung" }

b. Sie sehen nun dieses Fenster mit den Dienstanbietern.

![](/_images/doc2/infor_Service-Provider_2-1-1024x479.png){ loading=lazy alt="Infor Cloud Dienstanbieter" }

c. Klicken Sie nun auf das "+"-Symbol und fügen Sie unseren DOC² als Dienstanbieter hinzu. (Siehe Schritt 4)

![](/_images/doc2/infor6.png){ loading=lazy alt="Infor Cloud Dienstanbieter hinzufügen" }

**3\. Greifen Sie auf die SSO SERVICE PROVIDER SETTINGS in DOC² zu**

a) Melden Sie sich auf der URL [https://app.polydocs.io/](https://app.polydocs.io/) mit den Login-Daten an, die Sie von uns erhalten haben.

b) Gehen Sie zu EINSTELLUNGEN (in der oberen Leiste) und wählen Sie SSO-Einstellungen unten auf der Liste.

Hier finden Sie alle Informationen, die Sie für die folgenden Schritte benötigen.

c) Laden Sie das Zertifikat herunter.

![](/_images/doc2/DOC2_SSO-Service-Provider-Settings-1024x640.png){ loading=lazy alt="DOC² SSO Service Provider Einstellungen" }

**4\. Füllen Sie den Dienstanbieter mit Hilfe der SSO Service Provider Settings in DOC² aus**

![](/_images/doc2/infor_Service-Provider_3-1024x891.png)

<table><tbody><tr><td><strong>Feld</strong></td><td><strong>Wert</strong></td></tr><tr><td><strong>Anwendungstyp</strong></td><td>DEFAULT_SAML</td></tr><tr><td><strong>Anzeigename</strong></td><td>DOC²</td></tr><tr><td><strong>Entity ID</strong></td><td>Siehe Entity ID unter SSO SERVICE SETTINGS</td></tr><tr><td><strong>SSO-Endpunkt</strong></td><td>Kopieren Sie die SSO-URL aus SSO SERVICE SETTINGS und fügen Sie sie in das Feld <strong>SSO-Endpunkt</strong> ein.</td></tr><tr><td><strong>SLO-Endpunkt</strong></td><td>Kopieren Sie die SLO-URL aus SSO SERVICE SETTINGS und fügen Sie sie in das Feld <strong>SLO-Endpunkt</strong> ein.</td></tr><tr><td><strong>Signaturzertifikat</strong></td><td>Laden Sie die entsprechende .cer-Datei hoch, die Sie in Schritt 3c) aus SSO SERVICE SETTINGS heruntergeladen haben.</td></tr><tr><td><strong>Name ID-Format und Mapping</strong></td><td>E-Mail-Adresse</td></tr></tbody></table>

![](/_images/doc2/infor_Service-Provider_completed-956x1024.png)

a) Wenn Sie alles ausgefüllt haben, denken Sie daran, es mit dem Diskettensymbol über dem Anwendungstyp zu speichern.

b) Geben Sie dann den Dienstanbieter DOC² erneut ein.

c) Klicken Sie auf "Identity Provider Information anzeigen" darunter.

![](/_images/doc2/infor_Identity-Provider-Information-copy-1024x559.png){ loading=lazy alt="Infor Cloud Identity Provider Information" }

![](/_images/doc2/infor_Identity-Provider-Information-806x1024.png){ loading=lazy alt="Infor Cloud Identity Provider Information" }

d) Exportieren Sie das **SAML METADATA.**

Die Datei sieht so aus: ServiceProviderSAMLMetadata\_10\_20\_2021.xml

**5\. Importieren Sie die SAML METADATA in den SSO-Einstellungen.**

Gehen Sie zu IDENTITY SERVICE PROVIDER SETTINGS, geben Sie Ihre Mandanten-ID ein (z.B. FELLOWCONSULTING\_DEV) und darunter sehen Sie die Schaltfläche "Datei hochladen" und den IMPORT-Button, über den Sie die zuvor exportierte SAML METADATA-Datei hochladen müssen.

a) Klicken Sie auf IMPORT und wählen Sie dann die METADATA-Datei aus, die Sie bereits aus den SSO SERVICE PROVIDER SETTINGS heruntergeladen haben.

b) Klicken Sie auf CONFIGURE

![](/_images/doc2/DOC2_identity-service-provider-settings_completed-1024x316.png){ loading=lazy alt="DOC² Identity Service Provider Einstellungen" }

Dieser Teil ist erfolgreich abgeschlossen, wenn Sie das folgende Popup sehen.

![](/_images/doc2/DOC2_File-successfully-saved.png){ loading=lazy alt="DOC² Datei erfolgreich gespeichert" }

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