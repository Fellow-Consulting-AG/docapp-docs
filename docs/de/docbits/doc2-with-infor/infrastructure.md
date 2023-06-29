---
title: Infrastruktur für Infor Cloud und On-Premise
description: Eine visuelle Darstellung der Infrastruktur, die für unsere Anwendungen verwendet wird, wenn Infor Cloud oder On-Premise ausgeführt wird.
tags:
  - DocBits (DOC²)
  - Infrastruktur
  - Infor
---

# Anwendungsinfrastruktur

### Offener Port
* 443

### Kommunikation mit der Datenbank
Kubernetes und unsere Datenbanken befinden sich im selben VPC. Wir greifen nur über die lokale IP auf die Datenbank zu, sodass die übertragenen Daten niemals das lokale Netzwerk verlassen.
Zusätzlich verwenden wir nur SSL-gesicherte Verbindungen, um mit der Datenbank zu kommunizieren.

### Spaces
Die hochgeladenen Dokumente werden in einem Space gespeichert. Der Datenverkehr ist über SSL gesichert und mehrere Schlüssel sind erforderlich, um auf die gespeicherten Dateien zuzugreifen.

### Sicherer Datentransfer
Wir erlauben nur https-gesicherte Verbindungen, um mit unseren Servern zu kommunizieren. Dies stellt sicher, dass die übertragenen Daten verschlüsselt und sicher sind.

## Infor Cloud
![cloud-infor](/_images/security/infra-cloud.png "Infrastruktur für Infor Cloud")

## Infor On-Premise
Mit unserer On-Premise-Lösung müssen Sie keine Ports öffnen. Dies stellt sicher, dass die Sicherheit Ihres Netzwerks nicht beeinträchtigt wird.
![on-prem-infor](/_images/security/infra-on-prem.png "Infrastruktur für Infor On-Premise")