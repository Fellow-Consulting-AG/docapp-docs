---
title: Alle Docbits (Doc²)-Dokumentstatus
description: Hier finden Sie eine Liste aller Status, die ein Dokument in Docbits (Doc²) haben kann.
date: 2022-09-14
tags:
  - Status
  - Dokument
  - Liste
  - Docbits (Doc²)

---

##  Alle Docbits (Doc²)-Dokumentstatus

- `WatchDog Start`: Watchdog wird gestartet
- `WatchDog Split`: Das Dokument wird in Watchdog aufgeteilt
- `WatchDog Upload`: Das Dokument wird in Watchdog hochgeladen
- `Hochladen`: Das Dokument wird hochgeladen
- `OCR`: OCR wird derzeit für dieses Dokument ausgeführt
- `Klassifizierung`: Das Dokument wird klassifiziert
- `ZUGFeRD-Import`: Ein ZUGFeRD-Dokument wird importiert
- `Bereit für Validierung`: Das Dokument ist zur Validierung bereit
- `ZUGFeRD-Export`: Ein ZUGFeRD-Dokument wird exportiert
- `Workflow`: Der Workflow wird derzeit mit diesem Dokument ausgeführt
- `Genehmigung ausstehend`: Das Dokument muss genehmigt werden
- `Zweite Genehmigung ausstehend`: Das Dokument muss ein zweites Mal genehmigt werden
- `Auto Accounting`: Automatic Accounting läuft
- `Export`: Das Dokument wird exportiert
- `Fehler`: Das Dokument ist auf Fehler gelaufen

##  Hochladen und Klassifizieren

``` mermaid
sequenceDiagram
  Hochladen->>Status: DocId vom Upload abrufen?
  loop Status
      Status->>Status: Bis Endstatus nicht Klassifizieren ist
  end
  Status->>Klassifizieren: Endstatus is Klassifizieren
	Klassifizieren->>Löschen: Dokument mit DocId löschen

```

