---
title: "Dokumentenvalidierung"
date: "2023-05-12"
description: Erfahren Sie, wie Sie DOC² zur Validierung von Dokumenten verwenden können.
tags:
  - DOC²
  - Dokument
  - Validierung
---

### Wie man ein Dokument validiert

Nachdem Sie ein Dokument wie [hier](/doc2/manual-import/) beschrieben hochgeladen haben, führen Sie die folgenden Schritte aus, um es zu validieren:

1\. Gehen Sie zu `HOME`, wo Sie das DASHBOARD mit den hochgeladenen Dokumenten finden.

![DOC2 Dashboard](/_images/doc2/dokumentenvalidierung/dashboard.png)

2\. Klicken Sie auf die Zeile, um das Dokument zu öffnen. In diesem Fall spielt es keine Rolle, ob Sie auf den Dokumentennamen oder den Status klicken.

![DOC2 Dokument](/_images/doc2/dokumentenvalidierung/dokument.png)

Auf der linken Seite sehen Sie die Dokumentenvorschau, in der Sie auch von einer Seite zur anderen springen können, wenn Ihr Dokument mehr als nur eine Seite hat. Im mittleren Teil des Bildschirms haben Sie die große Übersicht über das Dokument, in der Sie auch die extrahierten Werte in Lila sehen können. Und schließlich sehen Sie auf der rechten Seite alle Segmente der extrahierten Werte.

Konzentrieren wir uns auf diesen letzten Teil.

Zunächst können Sie oben rechts bei Bedarf den Dokumentenursprung definieren:

![DOC2 Dokumentenursprung](/_images/doc2/dokumentenvalidierung/dokumentenursprung.png)

Bei unterschiedlichen Ursprüngen kann das Dokument unterschiedliche Betrags- und Datumsformate aufweisen. Stellen Sie sicher, dass der Dokumentenursprung richtig eingestellt ist, damit Daten und Beträge korrekt extrahiert werden.

Nun erhalten wir die grundlegenden Informationen wie Rechnungsnummer, Datum usw. Wenn Sie beispielsweise auf das Feld der Rechnungsnummer klicken, wird direkt markiert, wo auf der Rechnung sie extrahiert wurde.

![DOC2 Dokument Rechnungsnummer](/_images/doc2/dokumentenvalidierung/dokument-rechnungsnummer.png)

Sie können nun überprüfen, ob die Nummer korrekt extrahiert wurde. Alle Werte, die korrekt extrahiert wurden, bestätigen Sie mit dem Häkchen. Sie können dies mit jedem einzelnen Feld tun. Ein weiterer wichtiger Punkt ist, dass Sie auf der rechten Seite jedes Feldes einen Prozentsatz des Vertrauensniveaus von DOC² erhalten.

Alle Werte, die korrekt extrahiert und mit dem Häkchen bestätigt wurden, haben eine grüne Leiste am Anfang des Feldes.

![DOC2 Dokument korrekt extrahierte Werte](/_images/doc2/dokumentenvalidierung/dokument-korrekt-gruene leiste.png)

Ein großartiges Beispiel ist das nächste Segment des Feldes IBAN, wo die IBAN nicht einmal extrahiert wird, da das Vertrauensniveau gleich Null ist. Um den Wert zu trainieren und zu extrahieren, klicken Sie einfach in das Feld und markieren Sie die IBAN auf der Rechnung. 

![DOC2 Wert nicht extrahiert](/_images/doc2/dokumentenvalidierung/IBAN nicht extrahiert.png)

Der ausgewählte Wert wird in das IBAN-Feld extrahiert und auf der Rechnung angezeigt. Bitte bestätigen Sie den Wert mit dem Häkchen, um ihn endgültig zu übernehmen.

![DOC2 extrahierter Wert Bestätigung](/_images/doc2/dokumentenvalidierung/IBAN bestaetigen.png)

Die Vorgehensweise für jeden extrahierten oder nicht extrahierten Wert ist immer gleich. Hier sind einige Beispiele für die aus dieser Rechnung extrahierten Werte:

![DOC2 VAT und Beträge](/_images/doc2/dokumentenvalidierung/gesamtbetrag-extrahiert.png)

![DOC2 Lieferantendetails](/_images/doc2/dokumentenvalidierung/lieferantenname-extrahiert.png)

Für die Lieferantendetails haben wir die Fuzzy-Suche konfiguriert, bei der die Lieferantenidentifikation mit den aus Ihrem ERP-System importierten Stammdaten abgeglichen wird. Sollte beispielsweise der Name des Lieferanten fehlen, können Sie ihn auch in dieser Tabelle nachschlagen. Alles ist sehr einfach und benutzerfreundlich eingerichtet, damit diese Validierung schneller durchgeführt werden kann.

Nachdem Sie alle zur Extraktion verfügbaren Felder überprüft haben, können Sie die Änderungen bestätigen und direkt exportieren. Wenn Sie die Bearbeitung unterbrechen müssen, z.B. wegen eines Last-Minute-Termins oder eines Telefonanrufs, können Sie die bis dahin bestätigten Änderungen auch speichern und später fortfahren.

![DOC2 Änderungen speichern, bestätigen und exportieren](/_images/doc2/dokumentenvalidierung/dokument-speichern-bestaetigen-exportieren.png)

Wenn Sie die Änderungen gespeichert haben, bleibt das Dokument im Status "Bereit zur Validierung".

![DOC2 Status "Bereit zur Validierung"](/_images/doc2/dokumentenvalidierung/dasboard-bereit-zur-validierung.png)

Weitere Details finden Sie in den folgenden Abschnitten.