---
title: "DOC² - Infor API Flow"
description: Hier finden Sie verschiedene Anwendungsfälle, wie Prozesse Ihrer verschiedenen Dokumententypen aussehen und in Infor integriert werden können.
date: "2022-01-24"
tags:
  - DOC²
  - PO Matching
  - Infor LN
  - Infor M3
  - Anwendungsfälle
---

## API mit Infor OS & Infor CloudSuite

![Infor CloudSuite API Flow DOC²](/_images/doc2/infor/Doc2-Infor.png "Infor CloudSuite API Flow DOC²")

Die Integration von DOC² in Infor LN / M3 erfolgt hauptsächlich über ION API, ION Desk und die Infor Standard BODs. Es gibt hauptsächlich zwei Pfade, die berücksichtigt werden müssen, wenn eine Integration durchgeführt wird: wie wir die Daten an Infor exportieren und wie wir Daten für die Validierung von Stammdaten in DOC² erhalten.

Der erste Exportpfad beginnt mit der ION API, die es DOC² ermöglicht, nicht nur das PDF mit den Attributen an IDM zu senden, sondern auch das BOD Sync.CaptureDocument an ION Desk zu senden. In ION Desk transformieren wir dieses Sync.CaptureDocument über ION-Mappings in die gewünschten Ziel-BODs, abhängig davon, welcher Dokumententyp verarbeitet wird. Diese transformierten Infor BODs werden dann automatisch in LN oder M3 importiert.

Der zweite Pfad ist dann relevant, wenn wir in DOC² eine Validierung von Stammdaten durchführen möchten, um den Lieferanten zu identifizieren oder die Bestellpositionen zu vergleichen / abzugleichen. Aus diesem Grund aktivieren wir automatisch einen Trigger in LN / M3, damit wir die Sync.RemitToPartyMaster-, Sync.SupplierPartyMaster- und Sync.PurchaseOrder-BODs in DOC² erhalten, wenn ein neuer Eintrag oder Änderungen in den Stammdaten vorgenommen werden. Der Prozess wird erneut in ION Desk konfiguriert, wo wir den Datenfluss zu einem bestimmten Verbindungspunkt zu DOC² definieren.

[Infor Export](/doc2/export/export-to-infor/)

[IDM Business Context Model](/doc2/doc2-with-infor/IDM-business-context-model/)

[Infor SSO mit DOC²](/doc2/configuring-sso-in-cloud/)

[Infor Infrastructure & Security](/doc2/doc2-with-infor/infrastructure/)