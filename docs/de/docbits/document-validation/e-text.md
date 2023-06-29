---
title: "E-Text"
description: "Alle E-Text-Dokumente sind bereits OCR-verarbeitet. Sie können diese Dokumente erkennen, wenn Sie die PDF-Datei öffnen, den gesamten Text markieren und diesen in ein Word-Dokument kopieren können."
date: "2023-06-22"
tags:
  - E-Text
  - OCR
  - DocBits (DOC²)
---

Um den Unterschied zwischen E-Text und Nicht E-Text Dokumenten zu erkennen und zu verstehen, hier eine kurze Erklärung:

## **E-Text Dokumente**

Alle E-Text Dokumente sind bereits OCR-verarbeitet. Sie können diese Dokumente erkennen, wenn Sie die PDF-Datei öffnen, den gesamten Text markieren und diesen in ein Word-Dokument kopieren können.

![E-Text](/_images/docbits/dokumentenvalidierung/E-Text Dokument.png)

## **Dokumente ohne E-Text**

Dokumente, die keinen E-Text enthalten, sind nicht bearbeitbar und lassen sich leicht daran erkennen, dass die Seite nach einem Doppelklick vollständig hervorgehoben wird.

![E-Text](/_images/docbits/dokumentenvalidierung/Dokument ohne E-Text.png)

In den OCR-Einstellungen finden Sie die Option **E-Text verwenden falls verfügbar**, die durch setzen oder entfernen den Hakens im Kontrollkösten aktiviert oder deaktiviert werden kann.

![E-Text](/_images/docbits/dokumentenvalidierung/OCR Einstellungen_E-Text.png)


:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }
Mit dieser Option werden Dokumente die E-Text beinhalten nicht noch einmal vom OCR verarbeitet.


``` mermaid
graph LR
  Dokument --> Condition1{E-Text}
  Condition1 -->|Ja| ReadEText[E-Text lesen]
  Condition1 -->|Nein| OCREveryhting[gesamten OCR verarbeiten]
  ReadEText --> Condition2{beschädigt}
  Condition2 --> |Ja| Combine[Kombination von OCR und E-Text]
  Condition2 --> |Nein| Ende
  Combine --> OCR[nur Teile des OCR verarbeiten]
  OCR --> Ende
  OCREveryhting --> Ende
```

Um zu sehen welche Schritte wir durchgeführt haben und wie das Dokument verarbeitet wurde, öffnen Sie die folgende [Aktion](/_images/docbits/dokumentenvalidierung/Aktionen_dokument-flow_ansehen.png).