---
title: Docbits (DOC²) to Infor OS
description: Documentation for Export Docbits (DOC²) to Infor OS
tags:
  - Docbits (DOC²)
  - Export
  - Infor
  - Docbits (DOC²)
---

# Export to Infor :fontawesome-solid-file-export:



``` mermaid
graph LR
  A[Start] --> B{Invoice?};
  B -->|Yes| C[Extraction];
  C --> D[Infor LN or M3];
  D --> E[Send to IDM];
  B ---->|No| E[Send to IDM];
  E --> F[End];
```



Here you can find all the useful pages to connect your infor environment correctly:

- [:octicons-file-24: How to create a BOD mapping file](/docbits/export/how-to-create-a-bod-mapping-file/)
- [:fontawesome-solid-file-export: Export to Infor ION and IDM](/docbits/export/infor-ion/)
- [:octicons-file-24: How to create a IDM mapping file](/docbits/export/how-to-create-a-idm-mapping-file/)
- [:octicons-file-24: How to create an Infor ION API file](/docbits/export/create-a-infor-ion-api-file/)
- [:fontawesome-solid-file-export: Export to Infor IDM](/docbits/export/infor-idm/)
