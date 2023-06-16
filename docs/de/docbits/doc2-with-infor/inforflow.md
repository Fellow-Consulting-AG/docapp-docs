---
title: "Docbits (Doc²) - Infor API Flow"
description: Hier finden Sie verschiedene Anwendungsfälle, wie Prozesse Ihrer verschiedenen Dokumententypen aussehen und in Infor integriert werden können.
date: "2022-01-24"
tags:
  - Docbits (Doc²)
  - PO Matching
  - Infor LN
  - Infor M3
  - Anwendungsfälle
---

## API mit Infor OS & Infor CloudSuite

![Infor CloudSuite API Flow Docbits (Doc²)](/_images/docbits/infor/Doc2-Infor.png "Infor CloudSuite API Flow Docbits (Doc²)")

Die Integration von Docbits (Doc²) in Infor LN / M3 erfolgt hauptsächlich über ION API, ION Desk und die Infor Standard BODs. Es gibt zwei Hauptpfade, die bei der Integration berücksichtigt werden müssen: 
wie wir die Daten nach Infor exportieren und wie wir Daten für die Validierung von Stammdaten in Docbits (Doc²) erhalten.

Der erste Exportpfad beginnt mit der ION API, die es Docbits (Doc²) ermöglicht, nicht nur das PDF mit den Attributen an IDM zu senden, sondern auch das BOD Sync.CaptureDocument an ION Desk zu senden. In ION Desk transformieren wir dieses Sync.CaptureDocument über ION-Mappings in die gewünschten Ziel-BODs, je nachdem, welchen Dokumententyp wir verarbeiten. Diese transformierten Infor BODs werden dann automatisch in LN oder M3 importiert.

Der zweite Pfad ist dann relevant, wenn wir in Docbits (Doc²) eine Validierung von Stammdaten durchführen möchten, um den Lieferanten zu identifizieren oder die Bestellpositionen zu vergleichen / abzugleichen. Deshalb aktivieren wir automatisch einen Trigger in LN / M3, damit wir die Sync.RemitToPartyMaster-, Sync.SupplierPartyMaster- und Sync.PurchaseOrder-BODs in Docbits (Doc²) erhalten, wenn ein neuer Eintrag oder Änderungen in den Stammdaten vorgenommen werden. Der Prozess wird erneut in ION Desk konfiguriert, wo wir den Datenfluss zu einem bestimmten Verbindungspunkt zu Docbits (Doc²) definieren.

[Infor Export](/docbits/export/export-to-infor/)

[IDM Geschäftskontextmodell](/docbits/doc2-with-infor/IDM-business-context-model/)

[Infor SSO mit Docbits (Doc²)](/docbits/doc2-with-infor/configuring-sso-in-cloud/)

[Infor Anwendungsinfrastruktur & Sicherheit](/docbits/doc2-with-infor/infrastructure/)