---
title: "Validierung von Stammdaten"
description: Mit DocBits (Doc²) können Sie in der Übersicht zur Dokumentenvalidierung die Lieferantendaten, die aus dem Dokument extrahiert wurden, mit den Stammdaten aus Ihrem ERP-System abgleichen und das Dokument im besten Fall automatisch dem richtigen Lieferanten zuordnen, ohne manuelle Arbeit.
date: "2022-02-24"
tags:
  - DocBits (Doc²)
  - Dokumentenvalidierung
  - Stammdatenvalidierung
---

Mit DocBits (Doc²) können Sie in der Übersicht zur Dokumentenvalidierung die Lieferantendaten, die aus dem Dokument extrahiert wurden, mit den Stammdaten aus Ihrem ERP-System abgleichen und das Dokument im besten Fall automatisch dem richtigen Lieferanten zuordnen, ohne manuelle Arbeit (Voraussetzung: [Ihre Stammdaten wurden in DocBits (Doc²) hochgeladen](/docbits/settings-master-data-validation/)).

Es gibt derzeit zwei Möglichkeiten, dies zu tun.

**Abgleich der extrahierten Umsatzsteuer-Identifikationsnummer (USt-IdNr.) des Lieferanten**:

Die USt-IdNr. wird aus dem Dokument mit DocBits (Doc²) extrahiert:

![Extrahierte USt-IdNr.](/_images/docbits/DOC2_master-data-validation_1.png)

Im Hintergrund wird die USt-IdNr. mit den Lieferantenstammdaten abgeglichen, die von Ihnen an DocBits (Doc²) bereitgestellt wurden, und die Lieferanten-ID einschließlich der entsprechenden Lieferantendaten wie Name und Adresse werden automatisch ermittelt.

Der Benutzer kann jederzeit manuell eingreifen und den bereitgestellten Lieferanten aufrufen. Dies erfolgt über die folgende Schaltfläche:

![Schaltfläche zum Aufrufen des Lieferanten](/_images/docbits/image-21.png)

Das folgende Fenster wird aufgerufen und zeigt die Lieferantendaten für die entsprechende USt-IdNr. an. Über das Suchfeld kann jede USt-IdNr. eingegeben werden und somit der Lieferantenstamm, den Sie an DocBits (Doc²) bereitgestellt haben, durchsucht werden. Wenn der richtige Lieferant gefunden wurde, kann er ausgewählt und akzeptiert werden.

![Fenster zur Anzeige der Lieferantendaten](/_images/docbits/image-23-1024x276.png)

Die zweite Möglichkeit besteht darin, **den Lieferanten über den Lieferantennamen zu finden**:

Über die Schaltfläche im Feld für den Lieferantennamen kann auch der Lieferantenstamm (der von Ihnen an DocBits (Doc²) bereitgestellt wird) aufgerufen werden. In diesem Fall kann der Lieferantenname im Lieferantenstamm gesucht werden:

![Schaltfläche zum Aufrufen des Lieferantenstamms](/_images/docbits/image-24.png)

![Suchfeld im Lieferantenstamm](/_images/docbits/image-25-1024x192.png)