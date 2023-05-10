---
title: "DOC² - Postman Anleitungen"
description: In dieser Anleitung lernen Sie, wie Sie über Postman HTTP-Anfragen an Ihre DOC²-Organisation senden können.
date: "2022-10-20"
tags:
  - DOC²
  - Postman
  - Anleitung
  - Einrichtung
  - HTTP-Anfrage
  - Admin
---

# Postman für DOC²

Diese Anleitung zeigt Ihnen, wie Sie über Postman HTTP-Anfragen an Ihre DOC²-Organisation senden können. Es ist einfach zu bedienen und sehr nützlich für Organisationadministratoren.

## Einrichtung

Laden Sie zunächst [Postman](https://www.postman.com/downloads/) auf Ihr System herunter und melden Sie sich an oder registrieren Sie sich.

Befolgen Sie dann diese Schritt-für-Schritt-Anleitung, um zu erfahren, wie HTTP-Anfragen in Postman funktionieren.

## Autorisierung

### In Postman

Bevor Sie Ihre HTTP-Anfragen erstellen können, müssen Sie Ihren API-Schlüssel von DOC² eingeben, um sie zu autorisieren.

**1.** Klicken Sie auf die Registerkarte `Autorisierung` und wählen Sie `API-Schlüssel` als Autorisierungstyp aus.

![Picture](/_images/doc2/admin_guides_authorization_API Key.png){ loading=lazy }

**2.** Füllen Sie die Werte aus. Geben Sie "x-api-key" in das Feld `Schlüssel` ein und Ihren API-Schlüssel als Wert (zu finden im DOC²-Einstellungsmenü **Integration**). Wählen Sie `Header hinzufügen`.

Es sollte so aussehen:

![Picture](/_images/doc2/admin_guides_authorize_finish.png){ loading=lazy }

### Auf <a href="https://api.polydocs.io">api.polydocs.io</a>

**1.** Klicken Sie oben rechts auf **Autorisieren**

![Picture](/_images/doc2/admin_guides_doc2-api-authorize.png){ loading=lazy }

**2.** Geben Sie Ihren API-Schlüssel ein und bestätigen Sie durch Klicken auf `Autorisieren`

![Picture](/_images/doc2/admin_guides_doc2-api-authorize_key.png){ loading=lazy }

## Erstellen eines neuen Workspaces in Postman

**1.** Klicken Sie auf Workspaces und erstellen Sie einen neuen Workspace (Sie können ihn nennen, wie Sie möchten).<br>

![Picture](/_images/doc2/admin_guides_postman_guide_workspace_1.png){ loading=lazy }

**2.** Wählen Sie die Sichtbarkeit aus, die bestimmt, wer auf diesen Workspace zugreifen kann.

![Picture](/_images/doc2/admin_guides_postman_guide_create-workspace-visibility.png){ loading=lazy }

**3.** Nachdem Sie Ihre Auswahl getroffen und auf `Workspace erstellen` geklickt haben, wählen Sie auf der linken Seite der Anwendung `Collections` aus und erstellen Sie eine neue Sammlung für Ihre HTTP-Anfragen, indem Sie auf `+` klicken.

![Picture](/_images/doc2/admin_guides_postman_guide_new collection.png){ loading=lazy }

In dieser Sammlung können Sie mehrere HTTP-Anfragen hinzufügen. Klicken Sie dazu auf die 3 Punkte der Sammlung und wählen Sie `Anfrage hinzufügen`.

![Picture](/_images/doc2/admin_guides_add_request.png){ loading=lazy }

## Beispiel für die "GET"-Methode

Die GET-Methode ist sehr nützlich, um Informationen über Benutzer, Unterorganisationen, verarbeitete Dokumente und vieles mehr zu erhalten.

**1.** Wählen Sie die GET-Methode in Ihrer HTTP-Anfrage aus.<br>
**2.** Autorisieren Sie sich wie oben beschrieben [Autorisierung](/doc2/admin-guides/postman-projects/#autorisation).<br>
**3.** Öffnen Sie <a href="https://api.polydocs.io">api.polydocs.io</a> und fügen Sie den Pfad der Funktion hinter der Polydocs-URL hinzu. Zum Beispiel:

![Picture](/_images/doc2/admin_guide_get_api.png){ loading=lazy }



        https://api.polydocs.io/users/get_users


**4.** Fügen Sie diesen Link nun in das Textfeld neben der GET-Methode in Postman ein.

Klicken Sie auf `Senden` und Sie sollten alle Informationen über jeden Benutzer in Ihrer Organisation erhalten.