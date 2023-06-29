---
title: "Manuelle Zeilenauswahl"
date: "2022-02-18"
description: "Es kann vorkommen, dass in einigen Dokumenten Text in Zeilen nicht nur unter einer Spalte geschrieben wird, sondern durch verschiedene Spalten hindurch. Hier erfahren Sie, wie Sie Zeilen in DocBits (Doc²) manuell auswählen können."
tags:
  - DocBits (Doc²)
  - Zeile
  - Auswahl
  - manuell
  - Tabellenextraktion
---

# Manuelle Zeilenauswahl

Es kann vorkommen, dass in einigen Dokumenten Text in Zeilen nicht nur unter einer Spalte geschrieben wird, sondern durch verschiedene Spalten hindurch, wie im folgenden Beispiel:

![Beispiel für Text, der durch verschiedene Spalten hindurch geschrieben wurde](/_images/docbits/image-10-1024x606.png "Beispiel für Text, der durch verschiedene Spalten hindurch geschrieben wurde")

Auf dem Screenshot sehen Sie, dass die Tabelle und Spalten bereits definiert wurden. Wenn Sie sich die markierten Informationen (PRAEF) genauer ansehen, werden Sie feststellen, dass der Text durch die Spalten "Bezeichnung", "Menge", "ME" und "Preis in EUR" geschrieben wurde.

[Registrieren Sie sich für eine 30-tägige kostenlose Testversion](https://app.polydocs.io){ .md-button .md-button--primary }

In diesem Fall ist es für das System nicht möglich, automatisch zu definieren, welcher Spalte die Informationen zugeordnet werden sollen.

Um dieses Problem zu lösen, bietet DocBits (Doc²) die Möglichkeit, Informationen auf einem Dokument manuell auszuwählen und einer beliebigen Spalte zuzuordnen.

Stellen Sie zunächst sicher, dass der Trainingsmodus aktiviert ist:

![Aktivierung des Trainingsmodus](/_images/docbits/image-11.png "Aktivierung des Trainingsmodus")

Zusätzlich müssen Sie den Zeilenbearbeitungsmodus aktivieren:

![Aktivierung des Zeilenbearbeitungsmodus](/_images/docbits/image-13-1024x314.png "Aktivierung des Zeilenbearbeitungsmodus")

Bitte beachten Sie, dass die manuelle Zuordnung von Text zu einer Spalte nur für extrahierbare Spalten (blau) möglich ist:

![Extrahierbare Spalten](/_images/docbits/image-14-1024x669.png "Extrahierbare Spalten")

Die violetten Spalten können nicht manuell zugeordnet werden, da die Zuordnung bereits über die auf dem Dokument definierten Spalten erfolgt ist.

Extrahierbare Spalten müssen zuerst erstellt werden. Hier erfahren Sie, wie das funktioniert: [Neue Tabellenspalte hinzufügen](/docbits/table/add-new-table-column/)

Sobald die Spalte erstellt wurde und der Trainingsmodus sowie der Zeilenbearbeitungsmodus aktiviert sind, können Sie den Text auf dem Dokument der Spalte zuordnen, wie im folgenden Video gezeigt:

<video controls>
  <source src="/_videos/docbits/manual-row-selection.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Im Video sehen Sie, wie Sie:

- einen Bereich mit der Maus auswählen
- auf einen Wert doppelklicken, um den Bereich auszuwählen (nur für Werte ohne Leerzeichen möglich)
- die Zuordnung löschen und den Bereich erneut zuordnen können