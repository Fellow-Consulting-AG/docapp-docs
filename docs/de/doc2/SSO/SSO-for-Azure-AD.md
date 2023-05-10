---
title: "SSO für Azure AD"
date: "2021-10-14"
description: In diesem Schritt-für-Schritt-Handbuch erfahren Sie, wie Sie SSO in Infor Cloud konfigurieren. Beginnend mit den Voraussetzungen, dem Zugriff auf die Cloud und der Überprüfung, um einen neuen Dienstanbieter hinzuzufügen.
tags:
  - DOC²
  - Azure Active Directory
  - SSO
---

# Konfigurieren von Azure Active Directory

## Erstellen von SAML SSO in Azure AD

Führen Sie die folgenden Schritte aus, um SAML SSO in Azure AD hinzuzufügen:

**1.** Gehen Sie in Azure zu Ihrer `Azure Active Directory`-Konsole.

![Azure Active Directory-Konsole](/_images/doc2/SSO/Azure_1.png "Azure Active Directory-Konsole")

**2.** Klicken Sie im linken Bereich auf `Unternehmensanwendungen`.

![Unternehmensanwendungen](/_images/doc2/SSO/Azure_2.png "Unternehmensanwendungen")

**3.** Klicken Sie auf `+ Neue Anwendung`.

![Neue Anwendung](/_images/doc2/SSO/Azure_3.png "Neue Anwendung")

**4.** Klicken Sie auf `+ Erstellen Sie Ihre eigene Anwendung`.

![Erstellen Sie Ihre eigene Anwendung](/_images/doc2/SSO/Azure_4.png "Erstellen Sie Ihre eigene Anwendung")

**5.** Geben Sie einen Namen für Ihre Anwendung ein. Behalten Sie die restlichen Standardauswahlen bei.

![Anwendungsnamen](/_images/doc2/SSO/Azure_5.png "Anwendungsnamen")

**6.** Klicken Sie auf `Erstellen`.


## Benutzer der SSO-Konfiguration zuweisen

Weisen Sie als Nächstes Benutzer oder Gruppen der SSO-Konfiguration zu.

:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }
Wichtig: Sie sollten bereits Benutzer und Gruppen in Azure AD erstellt haben. Wenn Sie keine Benutzer oder Gruppen haben, erstellen Sie diese jetzt, bevor Sie fortfahren.
:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }

**1.** Klicken Sie unter `Erste Schritte` auf `Benutzer und Gruppen zuweisen`.


**2.** Klicken Sie auf `+ Benutzer hinzufügen`.

![Benutzer hinzufügen](/_images/doc2/SSO/Azure_6.png "Benutzer hinzufügen")


**3.** Wählen Sie die Benutzer und Gruppen aus, die Sie dieser SSO-Konfiguration zuweisen möchten. Diese Benutzer können sich mit SSO bei DOC² authentifizieren.

![Benutzer und Gruppen auswählen](/_images/doc2/SSO/Azure_7.png "Benutzer und Gruppen auswählen")

**4.** Klicken Sie auf `Auswählen`.


**5.** Wenn Sie mit Ihrer Auswahl zufrieden sind, klicken Sie auf `Zuweisen`.

![Zuweisen](/_images/doc2/SSO/Azure_8.png "Zuweisen")

![Zuweisen bestätigen](/_images/doc2/SSO/Azure_9.png "Zuweisen bestätigen")

**6.** Gehen Sie zur Gruppenansichtsliste und suchen Sie die zugewiesenen Gruppen.


## SSO in Azure einrichten

Als Nächstes müssen Sie die Einrichtung der Einmalanmeldung in Azure abschließen.

**1.** Klicken Sie im linken Bereich auf `Einmalanmeldung`.

![Einmalanmeldung](/_images/doc2/SSO/Azure_10.png "Einmalanmeldung")

**2.** Klicken Sie auf `SAML`.

![SAML](/_images/doc2/SSO/Azure_11.png "SAML")

**3.** Klicken Sie auf `Metadatendatei hochladen`.

![Metadatendatei hochladen](/_images/doc2/SSO/Azure_12.png "Metadatendatei hochladen")

**4.** Laden Sie die DOC² **metadata.xml** hoch, die Sie im Menü `Integration` unter `SSO Service Provider Settings` Ihres DOC²-Kontos finden.

![metadata.xml](/_images/doc2/SSO/Azure_Metadata.png "metadata.xml")

**5.** Bearbeiten Sie die `Grundlegende SAML-Konfiguration`.

![Grundlegende SAML-Konfiguration](/_images/doc2/SSO/Azure_13.png "Grundlegende SAML-Konfiguration")

**6.** Überprüfen Sie, ob die `Entity ID`, `ACS-URL`, `Anmelde-URL` und `Logout-URL` richtig ausgefüllt sind.

![SAML-Konfiguration überprüfen](/_images/doc2/SSO/Azure_13.1.png "SAML-Konfiguration überprüfen")

**7.** Laden Sie die neu generierte **Federation Metadata XML** herunter.

![Federation Metadata XML herunterladen](/_images/doc2/SSO/Azure_14.png "Federation Metadata XML herunterladen")

**8.** Laden Sie die FederationMetadata.xml in die **Identity Service Provider Settings** Ihres DOC²-Kontos hoch, die Sie im Menü `Integration` finden.

![FederationMetadata.xml hochladen](/_images/doc2/SSO/Azure_15.png "FederationMetadata.xml hochladen")