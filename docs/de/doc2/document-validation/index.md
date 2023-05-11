---
title: "Dokumentenvalidierung"
date: "2021-10-29"
description: Erfahren Sie, wie Sie DOC² zur Validierung von Dokumenten verwenden können.
tags:
  - DOC²
  - Dokument
  - Validierung
---

### Wie man ein Dokument validiert

Nachdem Sie ein Dokument wie hier beschrieben [hier](/doc2/dashboard/) hochgeladen haben, führen Sie die folgenden Schritte aus, um es zu validieren:

1\. Gehen Sie zu `HOME`, wo Sie das DASHBOARD mit den hochgeladenen Dokumenten finden.

![DOC2 Dashboard](/_images/doc2/DOC2_Dashboard-1024x640.png "DOC2 Dashboard")

2\. Klicken Sie auf die Leiste, um das Dokument zu öffnen. In diesem Fall ist es egal, ob Sie auf den Dokumentennamen oder den Status klicken.

![DOC2 Dokument](/_images/doc2/DOC2_Document-1024x640.png "DOC2 Dokument")

Auf der linken Seite sehen Sie eine Vorschau des Dokuments, wo Sie auch von einer Seite zur anderen springen können, wenn Ihr Dokument mehr als eine Seite hat. Im mittleren Teil des Bildschirms haben Sie eine große Übersicht des Dokuments, wo Sie auch die extrahierten Werte in Lila sehen können. Und schließlich haben Sie auf der rechten Seite alle Segmente der extrahierten Werte.

Konzentrieren wir uns auf diesen letzten Teil.

Zunächst können Sie auf der oberen rechten Seite den Dokumentenursprung definieren, falls erforderlich:

![DOC2 Dokumentenursprung](/_images/doc2/image-9.png "DOC2 Dokumentenursprung")

Für verschiedene Ursprünge kann das Dokument unterschiedliche Mengen- und Datumsformate haben. Stellen Sie sicher, dass der Dokumentenursprung richtig eingestellt ist, um sicherzustellen, dass Daten und Beträge korrekt extrahiert werden.

Nun erhalten wir die grundlegenden Informationen wie Rechnungsnummer, Datum usw. Wenn Sie beispielsweise auf das Feld der Rechnungsnummer klicken, wird direkt markiert, wo auf der Rechnung es extrahiert wurde.

![DOC2 Dokument Rechnungsnummer](/_images/doc2/DOC2_Document_Invoice-Number-1024x640.png "DOC2 Dokument Rechnungsnummer")

Sie können nun überprüfen, ob die Nummer korrekt extrahiert wurde. Alle Werte, die korrekt extrahiert wurden, bestätigen Sie mit dem Häkchen. Sie können dies mit jedem einzelnen Feld tun. Ein weiterer wichtiger Punkt ist, dass Sie auf der rechten Seite jedes Feldes einen Prozentsatz des Vertrauensniveaus von DOC² erhalten.

Alle Werte, die korrekt extrahiert und mit dem Häkchen bestätigt wurden, haben eine grüne Leiste am Anfang des Feldes.

![DOC2 Dokument korrekt extrahierte Werte](/_images/doc2/DOC2_Document_correct_green-colour-1024x640.png "DOC2 Dokument korrekt extrahierte Werte")

Ein großartiges Beispiel ist das nächste Segment des Feldes IBAN, wo die IBAN nicht einmal extrahiert wird, da das Vertrauensniveau gleich Null ist. Um den Wert zu trainieren und zu extrahieren, geben Sie einfach das Feld ein und markieren Sie die IBAN auf der Rechnung. Sie erhalten diese Nachricht, wenn Sie sich Ihrer Auswahl sicher sind, also klicken Sie auf Ja.

![DOC2 trainiertes Feld Bestätigung](/_images/doc2/DOC2_trained-field-confirmation-1024x640.png "DOC2 trainiertes Feld Bestätigung")

Der ausgewählte Wert wird in das IBAN-Feld extrahiert und auf der Rechnung angezeigt. Bitte bestätigen Sie den Wert mit dem Häkchen, um ihn abzuschließen.

![DOC2 extrahierter Wert Bestätigung](/_images/doc2/DOC2_confirm-extracted-value-1024x640.png "DOC2 extrahierter Wert Bestätigung")

Das Verfahren für jeden extrahierten oder nicht extrahierten Wert ist immer dasselbe. Hier sind einige Beispiele für die Werte, die aus einer Rechnung extrahiert wurden:

![DOC2 VAT und Beträge](/_images/doc2/DOC2-_VAT-and-amounts-1024x640.png "DOC2 VAT und Beträge")

![DOC2 Lieferantendetails](/_images/doc2/DOC2_Vendor-details-1024x640.png "DOC2 Lieferantendetails")

Für die Lieferantendetails haben wir die Fuzzy-Suche konfiguriert, bei der die Lieferantenidentifikation mit den aus Ihrem ERP-System importierten Stammdaten abgeglichen wird. Wenn beispielsweise der Name des Lieferanten fehlte, könnten Sie ihn auch in dieser Tabelle nachschlagen. Alles ist sehr einfach und benutzerfreundlich eingerichtet, damit diese Validierung schneller vonstattengeht.

Nachdem Sie alle verfügbaren Felder für die Extraktion überprüft haben, können Sie die Änderungen bestätigen und direkt exportieren. Wenn Sie die Bearbeitung unterbrechen müssen, z.B. wegen eines Last-Minute-Termins oder eines Telefonanrufs, können Sie auch die Änderungen speichern, die Sie bis zu diesem Zeitpunkt bestätigt haben, und später fortsetzen.

![DOC2 Änderungen speichern, bestätigen und exportieren](/_images/doc2/DOC2_Save_Confirm-and-Export-1024x640.png "DOC2 Änderungen speichern, bestätigen und exportieren")

Wenn Sie die Änderungen gespeichert haben, bleibt das Dokument im Status "Bereit zur Validierung".

![DOC2 Status "Bereit zur Validierung"](/_images/doc2/DOC2_Ready-for-Validation-status-1024x640.png "DOC2 Status 'Bereit zur Validierung'")

Weitere Details finden Sie in den folgenden Abschnitten: