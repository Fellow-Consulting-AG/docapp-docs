---
title: "Erkennung von Inhaltsseiten"
description: In diesem Teil der API können wir spezielle Teile Ihres Dokuments erkennen und extrahieren. Der Abschnitt ist in drei verschiedene Teile unterteilt.
date: "2021-07-06"
tags:
  - OCR
  - API
---

In diesem Teil der API können wir spezielle Teile Ihres Dokuments erkennen und extrahieren. Der Abschnitt ist in drei verschiedene Teile unterteilt:

![Erkennung von Inhaltsseiten](/_images/doc2/image-21-1024x194.png "Erkennung von Inhaltsseiten")

## Erkennung von leeren Seiten

TBD

## Erkennung von Sprache

![Erkennung von Sprache](/_images/doc2/image-22-1024x252.png "Erkennung von Sprache")

Diese Funktion ermöglicht es Ihnen, einen Text Ihrer Wahl einzugeben und unsere API erkennt automatisch die Sprache, in der er geschrieben ist.

### _Fertig!_

## Erkennung von Tabellen

Wir tauchen nun in einen Teil der API ein, der sich mit der Extraktion von Tabellen befasst und automatisch Metadaten aus Ihrem Dokument extrahiert.

Um zu beginnen, ermöglicht Ihnen die API auch in diesem Abschnitt, Ihre Ergebnisse in einer Antwort oder per E-Mail zu erhalten. Wenn Sie sich dafür entscheiden, sie per E-Mail zu erhalten, geben Sie einfach Ihre Adresse am Anfang des Abschnitts ein.

Nun werden Sie aufgefordert, Ihr Dokument hochzuladen, bevor Sie erneut Parameter auswählen.

### Funktionalitäten und Parameter

**Bericht** (true/false) ermöglicht es Ihnen, zu wählen, ob Sie einen Genauigkeitsbericht erhalten möchten oder nicht.

![Beispiel für einen Genauigkeitsbericht](/_images/doc2/image-23.png "Beispiel für einen Genauigkeitsbericht")

**Gitter und Kontur** (true/false): Dieser Parameter entscheidet, ob Sie das Dokument zusätzlich zu Ihren extrahierten Daten als Base64-Datei erhalten. Dies kann hilfreich sein, ist aber für die allgemeine Verwendung nicht unbedingt erforderlich.

**Modus** (Stream/Lattice) entscheidet darüber, wie die Tabelle extrahiert wird. Wir empfehlen, dies auf Auto zu lassen, da beide Methoden dieselben Metadaten extrahieren sollten.

**Format** (Excel, Json, HTML) ermöglicht es Ihnen, das Format auszuwählen, in dem Ihre Metadaten extrahiert werden sollen.

### Ausführen

Nach dem Klicken auf "Ausführen" erhalten Sie Ihre extrahierten Daten im Code-Format wie unten gezeigt oder Sie lassen sich die Metadaten per E-Mail zusenden:

![Extrahierte Daten im Code-Format](/_images/doc2/image-24-1024x369.png "Extrahierte Daten im Code-Format")

### _Fertig!_