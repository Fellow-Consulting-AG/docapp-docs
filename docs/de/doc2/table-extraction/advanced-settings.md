---
title: "Erweiterte Einstellungen für Tabellenextraktion"
description: In DOC² gibt es verschiedene erweiterte Einstellungen zur Extraktion von Tabellen. Auf dieser Seite finden Sie einige Beispiele für unterschiedliche Tabellenmerkmale.
date: "2022-03-01"
tags:
  - Tabelle
  - DOC²
  - Einstellungen
---

Im Tabellenextraktions-View finden Sie in der oberen Aktionsleiste den Menüpunkt `Einstellungen` (stellen Sie sicher, dass der Trainingsmodus aktiviert ist). Wenn Sie auf das Zahnradsymbol klicken, öffnet sich ein Fenster, in dem Sie die `Erweiterten Einstellungen` finden.

![](/_images/doc2/advanced-settings_1.png){ loading=lazy, alt: "DOC² Einstellungen" }



![](/_images/doc2/advanced-settings_2.png){ loading=lazy, alt: "DOC² Erweiterte Einstellungen" }

## Folgende Funktionen sind in den allgemeinen Einstellungen verfügbar:

#### Anzahl der Kopfzeilen

Hier können Sie die Anzahl der Zeilen einer Tabellenkopfzeile definieren. Zum Beispiel kann die Tabellenkopfzeile aus zwei Zeilen bestehen:

![](/_images/doc2/advanced-settings_3.png){ loading=lazy, alt: "DOC² Kopfzeilen" }

Entsprechend ist der Wert in "Anzahl der Kopfzeilen" auf zwei gesetzt:

![](/_images/doc2/advanced-settings_4.png){ loading=lazy, alt: "DOC² Anzahl der Kopfzeilen" }

Warum ist das nötig? Es kann sein, dass DOC² die zweite Zeile in der Tabellenkopfzeile nicht als Kopfzeile erkennt. In diesem Fall fügt es sie fälschlicherweise als extrahierten Wert in die Tabelle ein. Dies kann mit dieser Funktion einfach verhindert werden.

<ins>Beispiel vorher</ins>:

![](/_images/doc2/advanced-settings_5.png){ loading=lazy, alt: "DOC² Beispiel vorher" }

<ins>Beispiel nachher</ins>:

![](/_images/doc2/advanced-settings_6.png){ loading=lazy, alt: "DOC² Beispiel nachher" }


#### Zusätzliche Zeilen verschieben nach

In diesem Beispiel erstreckt sich die Artikelbeschreibung in der Tabelle über mehrere Zeilen, aber Sie benötigen nur die erste Zeile. Um nur diese zu extrahieren und in die Spalte "Beschreibung" aufzunehmen, wählen Sie `Zusätzliche Zeilen verschieben nach` `Papierkorb`.

![](/_images/doc2/advanced-settings_11.png){ loading=lazy, alt: "DOC² Zusätzliche Zeilen verschieben nach" }
![](/_images/doc2/advanced-settings_12.png){ loading=lazy, alt: "DOC² Papierkorb" }

Nachdem Sie die Spalten benannt und ihnen Positionen zugewiesen haben, erhalten Sie das folgende Ergebnis:

![](/_images/doc2/advanced-settings_13.png){ loading=lazy, alt: "DOC² Ergebnis" }



## Folgende Funktionen sind in den erweiterten Einstellungen verfügbar:

![](/_images/doc2/advanced-settings_15.png){ loading=lazy, alt: "DOC² Erweiterte Einstellungen" }


#### Mindestanzahl gruppierte Zeilen

Geben Sie hier die Mindestanzahl von Zeilen in Ihrer gruppierten Spalte ein.

![](/_images/doc2/advanced-settings_16.png){ loading=lazy, alt: "DOC² Mindestanzahl gruppierte Zeilen" }

In dieser Tabelle sehen Sie sechs Zeilen, von denen nur drei für Sie relevant sind. In den ersten beiden Spalten gibt es zwei Kriterien, die separat extrahiert werden müssen. Diese werden Ihre zugeordneten Spalten sein, alle anderen müssen als benutzerdefinierte Spalten trainiert werden. <br> Und so funktioniert es Schritt für Schritt:

Wählen Sie die beiden [Kopfzeilen](/doc2/table-extraction/advanced-settings/#header-row-count) sowie zwei minimale gruppierte Zeilen aus, da diese zu einer Zeile gruppiert werden sollten.

![](/_images/doc2/advanced-settings_17.png){ loading=lazy, alt: "DOC² Kopfzeilen" }
![](/_images/doc2/advanced-settings_18.png){ loading=lazy, alt: "DOC² Mindestanzahl gruppierte Zeilen" }

Wählen Sie auch die Option `Zusätzliche Zeilen verschieben nach` `Papierkorb`, um alle anderen Spalten als benutzerdefinierte Spalten trainieren zu können.

![](/_images/doc2/advanced-settings_19.png){ loading=lazy, alt: "DOC² Papierkorb" }

Nennen Sie die erste Spalte Position und gruppieren Sie diese.

![](/_images/doc2/advanced-settings_20.png){ loading=lazy, alt: "DOC² Position" }

Nachdem Sie alle Spalten benannt und die Werte trainiert haben, erhalten Sie folgendes Ergebnis:


![](/_images/doc2/advanced-settings_21.png){ loading=lazy, alt: "DOC² Ergebnis" }



<!--

##### Maximum grouped rows

Enter the maximum number of rows in your grouped column here.

#### Distinct group columns

If you want only unique values for your grouped column, check the box here.

-->

#### Umgekehrte Gruppierung

Wenn Sie alle Zeilen über dem gruppierten Attribut kombinieren möchten, aktivieren Sie hier das Kontrollkästchen.

In diesem Beispiel beginnt die Tabelle mit einer Zeile, die über allen anderen Informationen liegt, aber auch zusammen mit den Informationen darunter extrahiert werden muss. Es könnte sein, dass DOC² diese Zeile als zusätzliche Zeile extrahiert und die Gruppierung der Informationen, z.B. nach Position, nicht ordnungsgemäß funktioniert.

![](/_images/doc2/advanced-settings_7.png){ loading=lazy, alt: "DOC² Beispiel" }
![](/_images/doc2/advanced-settings_9.png){ loading=lazy, alt: "DOC² Umgekehrte Gruppierung" }

Nachdem Sie nach Nettobetrag gruppiert, das Kontrollkästchen aktiviert und die Option `Zusätzliche Zeilen verschieben nach` `Papierkorb` ausgewählt haben

![](/_images/doc2/advanced-settings_9.1.png){ loading=lazy, alt: "DOC² Papierkorb" }

und alle Spalten benannt haben, erhalten Sie folgendes Ergebnis:

![](/_images/doc2/advanced-settings_10.png){ loading=lazy, alt: "DOC² Ergebnis" }