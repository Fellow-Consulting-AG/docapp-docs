---
title: "Umgang mit unterschiedlichen Mehrwertsteuerbeträgen"
description: Diese Dokumentation bietet Informationen darüber, wie man eine Rechnung mit zwei unterschiedlichen Mehrwertsteuerbeträgen in Ephesoft trainiert. Ihre Batch-Klasse muss dafür geeignet sein.
date: "2021-07-05"
tags:
 - KV²
 - Plugin
 - Ephesoft
 - Mehrwertsteuer
---

## So trainieren Sie eine Rechnung mit zwei unterschiedlichen Mehrwertsteuerbeträgen:

![](https://example.com/_images/docbits/image-1.png "Rechnung mit zwei unterschiedlichen Mehrwertsteuerbeträgen")

1. Rechnungsdetails: Fügen Sie den Gesamtbetrag in das entsprechende Feld Gesamtbetrag ein. Lassen Sie Gesamtnettobetrag und Gesamt-Mehrwertsteuerbetrag leer.

![](https://example.com/_images/docbits/Bildschirmfoto-2021-07-05-um-14.03.57-1024x520.png "Rechnungsdetails")

2. Berechnungsdetails: Fügen Sie den höheren Steuersatz in das Feld Steuersatz Voll und den niedrigeren Satz in Steuersatz Reduziert ein. Die anderen Felder bleiben leer.

![](https://example.com/_images/docbits/image-2-1024x524.png "Berechnungsdetails")

3. Nach der Validierung und dem Export der Batch-ID aus dem ersten Upload werden die extrahierten Felder nach dem zweiten Upload des Dokuments automatisch mit den folgenden Werten gefüllt. Die beiden Nettobeträge sowie die Mehrwertsteuerbeträge werden automatisch addiert.

![](https://example.com/_images/docbits/image-4-1024x589.png "Extrahierte Felder")

* * *

## So trainieren Sie eine Rechnung mit 0 Mehrwertsteuerbetrag:

![](https://example.com/_images/docbits/image-5.png "Rechnung mit 0 Mehrwertsteuerbetrag")

1. Rechnungsdetails: Fügen Sie den Gesamtbetrag in das entsprechende Feld Gesamtbetrag ein. Lassen Sie Gesamtnettobetrag und Gesamt-Mehrwertsteuerbetrag leer.

![](https://example.com/_images/docbits/image-6-1024x485.png "Rechnungsdetails")

2. Berechnungsdetails: Fügen Sie einfach 0 in das Feld Steuerfrei manuell ein, wählen Sie Rechnungsbetrag für das Feld Nettobetrag Frei und geben Sie auch manuell 0 in das Feld Steuerbetrag Frei ein. Die anderen Felder bleiben leer.

![](https://example.com/_images/docbits/image-7-1024x485.png "Berechnungsdetails")

Die meisten Steuerfreien Rechnungen haben weder Mehrwertsteuer noch IBAN. Diese Felder bleiben also leer. In solchen Fällen haben wir die VENDOR_ID zur Identifizierung des Dokuments.

3. Nach der Validierung und dem Export der Batch-ID aus dem ersten Upload werden die extrahierten Felder nach dem zweiten Upload des Dokuments automatisch mit den folgenden Werten gefüllt.