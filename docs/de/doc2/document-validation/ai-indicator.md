---
title: "KI-Indikatoren"
description: "In der Dokumentation finden Sie Optionen zur Anzeige der Extraktionsqualität mithilfe von grafischen Indikatoren. Die sogenannten KI-Indikatoren."
date: "2022-03-23"
tags:
  - KI
  - DOC²
---

In der Dokumentenansicht finden Sie Optionen zur Anzeige der Extraktionsqualität mithilfe von grafischen Indikatoren. Die sogenannten KI-Indikatoren.

Um dies zu tun, öffnen Sie ein Dokument wie gewohnt über das Dashboard:

![Dokumentenansicht](/_images/doc2/ki indikator/dokumentenansicht oeffnen.png)

In der Dokumentenansicht gibt es zwei Indikatoren für die Qualität der Extraktion.

- Extraktionsqualität in Prozent pro Feld und aktuellem Dokument
- Gesamte Extraktionsqualität einschließlich vorheriger Extraktionen von Dokumenten des gleichen Typs.

![Extraktionsqualität](/_images/doc2/ki indikator/KI Indikator-Extraktionsqualitaet.png)

**Extraktionsqualität in Prozent pro Feld und aktuellem Dokument**

Für jedes Feld steht auf der rechten Seite ein Wert zur Verfügung, der die Extraktionsqualität für das aktuelle Dokument anzeigt. Es wird ein Prozentwert angezeigt:

![Extraktionsqualität pro Feld](/_images/doc2/ki indikator/KI Indikator-Extraktionsqualitaet-pro Feld.png)

**Gesamte Extraktionsqualität einschließlich vorheriger Extraktionen von Dokumenten des gleichen Typs**

Darüber hinaus gibt es ein Diagramm, das die Qualität aller vorherigen Extraktionen für einen Dokumententyp anzeigt. Dies bezieht sich jeweils auf den Extraktionswert mit der niedrigsten Qualität:

![Gesamte Extraktionsqualität](/_images/doc2/ki indikator/KI Indikator-gesamte-Extraktionsqualitaet.png)

**Technische Details:**

Der KI-Indikator zeigt an, wie gut ein Dokument trainiert ist. Dies geschieht über eine interne Punktzahl. Das bedeutet, dass sobald ein Dokument eingelesen wird und die von DOC² extrahierten Felder vom Benutzer bestätigt werden, erhöht sich diese Punktzahl. Je höher die Punktzahl, desto weiter befindet sich die Anzeige des KI-Indikators im grünen Bereich. Werden Felder nach dem Export manuell vom Benutzer geändert, verringert sich dieser Wert wieder und die Anzeige des AI-Indikators fällt wieder in den roten Bereich. Erst wenn das Dokument angelernt wurde und die Extraktion für einige Importe ohne manuelles Eingreifen den korrekten Wert ermittelt hat, erreicht die Punktzahl 100 %.