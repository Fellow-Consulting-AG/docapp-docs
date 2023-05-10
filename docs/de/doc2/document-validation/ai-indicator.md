---
title: "AI Indikatoren"
description: "In der Dokumentation finden Sie Optionen zur Anzeige der Extraktionsqualität mithilfe von grafischen Indikatoren. Die sogenannten AI-Indikatoren."
date: "2022-03-23"
tags:
  - AI
  - DOC²
---

In der Dokumentenansicht finden Sie Optionen zur Anzeige der Extraktionsqualität mithilfe von grafischen Indikatoren. Die sogenannten AI-Indikatoren.

Um dies zu tun, öffnen Sie ein Dokument wie gewohnt über das Dashboard:

![Dokumentenansicht](/_images/doc2/image-50-1024x391.png "Dokumentenansicht")

In der Dokumentenansicht gibt es zwei Indikatoren für die Qualität der Extraktion.

- Extraktionsqualität in Prozent pro Feld und aktuellem Dokument
- Gesamte Extraktionsqualität einschließlich vorheriger Extraktionen von Dokumenten des gleichen Typs.

![Extraktionsqualität](/_images/doc2/image-51-1024x474.png "Extraktionsqualität")

**Extraktionsqualität in Prozent pro Feld und aktuellem Dokument**

Für jedes Feld steht auf der rechten Seite ein Wert zur Verfügung, der die Extraktionsqualität für das aktuelle Dokument anzeigt. Es wird ein Prozentwert angezeigt:

![Extraktionsqualität pro Feld](/_images/doc2/image-52.png "Extraktionsqualität pro Feld")

**Gesamte Extraktionsqualität einschließlich vorheriger Extraktionen von Dokumenten des gleichen Typs**

Darüber hinaus gibt es ein Diagramm, das die Qualität aller vorherigen Extraktionen für einen Dokumententyp anzeigt. Dies bezieht sich jeweils auf den Extraktionswert mit der niedrigsten Qualität:

![Gesamte Extraktionsqualität](/_images/doc2/image-53.png "Gesamte Extraktionsqualität")

**Technische Details:**

Der AI-Indikator zeigt an, wie gut ein Dokument trainiert ist. Dies geschieht über eine interne Punktzahl. Das bedeutet, dass sobald ein Dokument eingelesen wird und die von DOC² extrahierten Felder vom Benutzer bestätigt werden, diese Punktzahl erhöht wird. Je höher die Punktzahl, desto weiter wird die Anzeige des AI-Indikators im grünen Bereich sein. Wenn Felder nach dem Export manuell vom Benutzer geändert werden, wird diese Punktzahl wieder abnehmen und die Anzeige des AI-Indikators wird in den roten Bereich zurückfallen. Nur wenn das Dokument trainiert wurde und die Extraktion den korrekten Wert für einige Importe ohne manuelle Intervention bestimmt hat, wird die Punktzahl 100% erreichen.