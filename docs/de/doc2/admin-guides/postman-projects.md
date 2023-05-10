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

Diese Anleitung zeigt Ihnen, wie Sie über Postman HTTP-Anfragen an Ihre DOC²-Organisation stellen können. Es ist einfach zu bedienen und sehr nützlich für Organisationadministratoren.

## Einrichtung

Laden Sie zunächst [Postman](https://www.postman.com/downloads/) auf Ihr System herunter und melden Sie sich an oder registrieren Sie sich.

Folgen Sie nun dieser Schritt-für-Schritt-Anleitung, um zu erfahren, wie HTTP-Anfragen in Postman funktionieren.

## Autorisierung

### In Postman

Bevor Sie Ihre HTTP-Anfragen erstellen können, müssen Sie Ihren API-Schlüssel von DOC² eingeben, um sie zu autorisieren.

**1.** Klicken Sie auf die Registerkarte `Autorisierung` und wählen Sie `API-Schlüssel` als Autorisierungstyp aus.

![Picture](/_images/doc2/admin_guides_authorization_API Key.png){ loading=lazy }

**2.** Füllen Sie die Werte aus. Geben Sie "x-api-key" in das Feld `Schlüssel` ein und Ihren API-Schlüssel als Wert (zu finden im DOC²-Einstellungsmenü **Integration**). Wählen Sie `Zum Header hinzufügen`.

Es sollte so aussehen:

![Picture](/_images/doc2/admin_guides_authorize_finish.png){ loading=lazy }

### Auf <a href="https://api.polydocs.io">api.polydocs.io</a>

**1.** Klicken Sie oben rechts auf **Autorisieren**

![Picture](/_images/doc2/admin_guides_doc2-api-authorize.png){ loading=lazy }

**2.** Geben Sie Ihren API-Schlüssel ein und bestätigen Sie mit einem Klick auf `Autorisieren`

![Picture](/_images/doc2/admin_guides_doc2-api-authorize_key.png){ loading=lazy }

## Erstellen eines neuen Workspace in Postman

**1.** Klicken Sie auf Workspace und erstellen Sie einen neuen Workspace (Sie können ihn nennen, wie Sie möchten).<br>

![Picture](/_images/doc2/admin_guides_postman_guide_workspace_1.png){ loading=lazy }

**2.** Sie müssen die Sichtbarkeit auswählen, die bestimmt, wer auf diesen Workspace zugreifen kann.

![Picture](/_images/doc2/admin_guides_postman_guide_create-workspace-visibility.png){ loading=lazy }

**3.** Nachdem Sie Ihre Auswahl getroffen und auf `Workspace erstellen` geklickt haben, wählen Sie auf der linken Seite der Anwendung `Collections` aus und erstellen Sie eine neue Sammlung für Ihre HTTP-Anfragen, indem Sie auf `+` klicken.

![Picture](/_images/doc2/admin_guides_postman_guide_new collection.png){ loading=lazy }

In dieser Sammlung können Sie mehrere HTTP-Anfragen hinzufügen. Klicken Sie dazu auf die 3 Punkte der Sammlung und wählen Sie `Anfrage hinzufügen`.

![Picture](/_images/doc2/admin_guides_add_request.png){ loading=lazy }

## Beispiel für die "GET"-Methode

Die GET-Methode ist sehr nützlich, um Informationen über Benutzer, Unterorganisationen, verarbeitete Dokumente und vieles mehr zu erhalten.

**1.** Wählen Sie die GET-Methode in Ihrer HTTP-Anfrage aus.<br>
**2.** Autorisieren Sie sich wie oben beschrieben [Autorisierung](/doc2/admin-guides/postman-projects/#autorisierung).<br>
**3.** Öffnen Sie <a href="https://api.polydocs.io">api.polydocs.io</a> und fügen Sie den Pfad der Funktion hinter der Polydocs URL ein. Zum Beispiel:

![Picture](/_images/doc2/admin_guide_get_api.png){ loading=lazy }



        https://api.polydocs.io/users/get_users


**4.** Fügen Sie diesen Link nun in das Textfeld neben der GET-Methode in Postman ein.

Klicken Sie auf `Send` und Sie sollten alle Informationen über jeden Benutzer in Ihrer Organisation erhalten.


## Beispiele für die "POST"-Methode

Die POST-Methode wird üblicherweise verwendet, um z.B. Benutzer oder Organisationen anzulegen. Diese Methode fügt Informationen in die Datenbank ein.

### Benutzer anlegen

**1.**  Wählen Sie die POST-Methode<br>
**2.**  Autorisieren Sie sich wie oben beschrieben [Autorisierung](/doc2/admin-guides/postman-projects/#autorisierung).<br>
**3.**  Öffnen Sie <a href="https://api.polydocs.io">api.polydocs.io</a> und fügen Sie den Pfad der Funktion hinter der Polydocs URL ein. In diesem Fall:

![Picture](/_images/doc2/admin_guides_post_api.png){ loading=lazy }



    https://api.polydocs.io/users/create


**4.**  Fügen Sie diesen Link nun in das Textfeld neben der POST-Methode in Postman ein.<br>
**5.**  Wählen Sie in Ihrer HTTP-Anfrage die Registerkarte `Body` und geben Sie die Schlüssel und Werte für jeden Berechtigungsnachweis ein, der neben seinem Namen ein rotes Sternchen hat.

Wenn Sie fertig sind, sollte es so aussehen:

![Picture](/_images/doc2/admin_guide_post_body.png){ loading=lazy }

Wenn Sie ein Administratorkonto erstellen möchten, setzen Sie den Wert `is_admin` auf **true**.

Klicken Sie abschließend auf `Send` und Sie können alle von Ihnen festgelegten Anmeldeinformationen in der Antwort unten sehen. Dies bedeutet, dass der Benutzer erstellt wurde.

![Picture](/_images/doc2/admin_guides_post_response.png){ loading=lazy }


### Dokument hochladen

Sie können die POST-Methode auch verwenden, um ein Dokument in DOC² hochzuladen.

**1.**  Wählen Sie die POST-Methode<br>
**2.**  Autorisieren Sie sich wie oben beschrieben [Autorisierung](/doc2/admin-guides/postman-projects/#autorisierung).<br>
**3.**  Öffnen Sie <a href="https://api.polydocs.io">api.polydocs.io</a> und fügen Sie den Pfad der Funktion hinter der Polydocs URL ein. In diesem Fall:

![Picture](/_images/doc2/admin_guides_post_document-process.png){ loading=lazy }



    https://api.polydocs.io/document/process


**4.**  Fügen Sie diesen Link nun in das Textfeld neben der POST-Methode in Postman ein.<br>
**5.**  Wählen Sie in Ihrer HTTP-Anfrage die Registerkarte `Body` und wählen Sie `form-data`.
![Picture](/_images/doc2/admin_guides_post_document-process_body-form-data-file.png){ loading=lazy }
![Picture](/_images/doc2/admin_guides_post_document-process_key-value-send.png){ loading=lazy }
**6.**  Geben Sie **file** in das Feld `KEY` ein, wo Sie das versteckte Dropdown-Menü "File" finden. Wählen Sie `File` und gehen Sie zum Feld `VALUE`, wo Sie Ihre Datei auswählen können, indem Sie auf `Select Files` klicken.<br>
**7.** Wenn Sie auf `Send` klicken, sollte in der Antwort „success“: true angezeigt werden.

Es sollte so aussehen:

![Picture](/_images/doc2/admin_guides_upload_body.png){ loading=lazy }


## Beispiel für die "DELETE"-Methode

Die DELETE-Methode wird verwendet, um z.B. Benutzer, Organisationen usw. zu löschen.

**1.**  Wählen Sie die DELETE-Methode<br>
**2.**  Autorisieren Sie sich wie oben beschrieben [Autorisierung](/doc2/admin-guides/postman-projects/#autorisierung).<br>
**3.**  Öffnen Sie <a href="https://api.polydocs.io">api.polydocs.io</a> und fügen Sie den Pfad der Funktion hinter der Polydocs URL ein. Zum Beispiel:


![Picture](/_images/doc2/admin_guides_delete_api.png){ loading=lazy }



    https://api.polydocs.io/users/delete/{user_id}



**4.**  Fügen Sie diesen Link nun in das Textfeld neben der DELETE-Methode in Postman ein.<br>
**5.**  Ersetzen Sie die {user_id} am Ende der URL durch die tatsächliche Benutzer-ID, die Sie löschen möchten. (Sie können die Benutzer-ID mit der GET-Methode abrufen).<br>
**6.**  Wenn Sie die user_id in die URL eingefügt haben, müssen Sie keinen `KEY` und `VALUE` für den `Body` hinzufügen.
**7.**  Wenn Sie auf `Send` klicken, sollte in der Antwort „success“: true angezeigt werden.

Es sollte so aussehen:

![Picture](/_images/doc2/admin_guides_delete_body.png){ loading=lazy }


## Beispiel für die "PUT"-Methode

Die PUT-Methode wird hauptsächlich zur Aktualisierung von Benutzer- oder Organisationsdaten verwendet. Sie ist sehr einfach zu verstehen und anzuwenden.

**1.**  Wählen Sie die PUT-Methode<br>
**2.**  Autorisieren Sie sich wie oben beschrieben [Autorisierung](/doc2/admin-guides/postman-projects/#autorisierung).<br>
**3.**  Öffnen Sie <a href="https://api.polydocs.io">api.polydocs.io</a> und fügen Sie den Pfad der Funktion hinter der Polydocs URL ein. Zum Beispiel:

![Picture](/_images/doc2/admin_guides_put_api.png){ loading=lazy }



    https://api.polydocs.io/users/update/{user_id}



**4.**  Fügen Sie diesen Link nun in das Textfeld neben der PUT-Methode in Postman ein.<br>
**5.**  Ersetzen Sie die {user_id} am Ende der URL durch die tatsächliche Benutzer-ID, die Sie bearbeiten möchten. (Sie können die Benutzer-ID mit der GET-Methode abrufen).<br>

Angenommen, Sie möchten die E-Mail-Adresse eines Benutzers in Ihrer Organisation ändern.

**1.**  Geben Sie im `body`, "email" als `KEY` und die neue E-Mail-Adresse als `VALUE` ein.<br>
**2.**  Klicken Sie dann einfach auf `Send` und in der Antwort sollte „success“ angezeigt werden.


Wenn Sie das alles noch anschaulicher und interaktiver haben möchten, können Sie das Postman-Projekt <a href="/example/downloadables/doc2app.postman_collection.json" download>hier</a> herunterladen, um alles auszuprobieren.
Klicken Sie einfach auf `Import` und wählen Sie diese Datei aus, um sofort loszulegen.

![Picture](/_images/doc2/admin_guides_import_json.png){ loading=lazy }
