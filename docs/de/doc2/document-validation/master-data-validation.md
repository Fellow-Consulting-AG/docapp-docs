---
title: "Validierung von Stammdaten"
description: Mit DOC² können Sie in der Übersicht zur Dokumentenvalidierung die Lieferantendaten, die aus dem Dokument extrahiert wurden, mit den Stammdaten aus Ihrem ERP-System abgleichen und das Dokument im besten Fall automatisch dem richtigen Lieferanten zuordnen, ohne manuelle Arbeit.
date: "2022-02-24"
tags:
  - DOC²
  - Dokumentenvalidierung
  - Stammdatenvalidierung
---

Mit DOC² können Sie in der Übersicht zur Dokumentenvalidierung die Lieferantendaten, die aus dem Dokument extrahiert wurden, mit den Stammdaten aus Ihrem ERP-System abgleichen und das Dokument im besten Fall automatisch dem richtigen Lieferanten zuordnen, ohne manuelle Arbeit (Voraussetzung: [Ihre Stammdaten wurden in DOC² hochgeladen](/doc2/settings-master-data-validation/)).

Es gibt derzeit zwei Möglichkeiten, dies zu tun.

**Abgleich der extrahierten Umsatzsteuer-Identifikationsnummer (USt-IdNr.) des Lieferanten**:

Die USt-IdNr. wird aus dem Dokument mit DOC² extrahiert:

![Extrahierte USt-IdNr.](/_images/doc2/DOC2_master-data-validation_1.png)

Im Hintergrund wird die USt-IdNr. mit den Lieferantenstammdaten abgeglichen, die von Ihnen an DOC² bereitgestellt wurden, und die Lieferanten-ID einschließlich der entsprechenden Lieferantendaten wie Name und Adresse werden automatisch ermittelt.

Der Benutzer kann jederzeit manuell eingreifen und den bereitgestellten Lieferanten aufrufen. Dies erfolgt über die folgende Schaltfläche:

![Schaltfläche zum Aufrufen des Lieferanten](/_images/doc2/image-21.png)

Das folgende Fenster wird aufgerufen und zeigt die Lieferantendaten für die entsprechende USt-IdNr. an. Über das Suchfeld kann jede USt-IdNr. eingegeben werden und somit der Lieferantenstamm, den Sie an DOC² bereitgestellt haben, durchsucht werden. Wenn der richtige Lieferant gefunden wurde, kann er ausgewählt und akzeptiert werden.

![Fenster zur Anzeige der Lieferantendaten](/_images/doc2/image-23-1024x276.png)

Die zweite Möglichkeit besteht darin, **den Lieferanten über den Lieferantennamen zu finden**:

Über die Schaltfläche im Feld für den Lieferantennamen kann auch der Lieferantenstamm (der von Ihnen an DOC² bereitgestellt wird) aufgerufen werden. In diesem Fall kann der Lieferantenname im Lieferantenstamm gesucht werden:

![Schaltfläche zum Aufrufen des Lieferantenstamms](/_images/doc2/image-24.png)

![Suchfeld im Lieferantenstamm](/_images/doc2/image-25-1024x192.png)