---
title: Datensicherheit mit DOC²
description: Eine Auflistung der Datensicherheitsmaßnahmen von DOC²
tags:
  - DOC²
  - Datensicherheit
  - Datenschutz
  - HTTPS
---

# Datensicherheit


### Hochgeladene Dateien
Alle hochgeladenen Dateien werden in einem Objektspeicher gespeichert, der von unserem Cloud-Anbieter gehostet wird. Der Zugriff ist eingeschränkt und nur möglich, wenn Sie den richtigen Key und Secret Key übergeben.

### Datenbank
Wir führen täglich Datenbank-Backups durch, die dann jeweils sieben Tage lang gespeichert werden.
Die Kommunikation zwischen der Datenbank und den Servern erfolgt ausschließlich über https.
Gespeicherte Passwörter werden so verschlüsselt, dass sie auch bei Zugriff auf die Datenbank nicht gelesen werden können.


### Server-Kommunikation
Die gesamte Kommunikation erfolgt über https, jede nicht-https-Anfrage wird auf https umgeleitet.

