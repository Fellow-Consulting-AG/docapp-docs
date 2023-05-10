---
title: Export von DOC² nach Infor OS
description: Dokumentation für den Export von DOC² nach Infor OS
tags:
  - DOC²
  - Export
  - Infor
---

# Export nach Infor :fontawesome-solid-file-export:

``` mermaid
graph LR
  A[Start] --> B{Rechnung?};
  B -->|Ja| C[Extraktion];
  C --> D[Infor LN oder M3];
  D --> E[Senden an IDM];
  B ---->|Nein| E[Senden an IDM];
  E --> F[Ende];
```

Hier finden Sie alle nützlichen Seiten, um Ihre Infor-Umgebung korrekt zu verbinden:

- [:octicons-file-24: Wie man eine BOD-Mapping-Datei erstellt](/doc2/export/how-to-create-a-bod-mapping-file/)
- [:fontawesome-solid-file-export: Export nach Infor ION und IDM](/doc2/export/infor-ion/)
- [:octicons-file-24: Wie man eine IDM-Mapping-Datei erstellt](/doc2/export/how-to-create-a-idm-mapping-file/)
- [:octicons-file-24: Wie man eine Infor ION API-Datei erstellt](/doc2/export/create-a-infor-ion-api-file/)
- [:fontawesome-solid-file-export: Export nach Infor IDM](/doc2/export/infor-idm/)