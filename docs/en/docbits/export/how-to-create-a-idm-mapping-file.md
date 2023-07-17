---
title: "How to create an IDM mapping file"
description: This is a step by step guide how to create an IDM mapping file. You will find all values and fields that would need an adjustment in DocBits (DOC²) and the BOD.
date: "2021-10-28"
tags:
  - DocBits (DOC²)
  - Export
  - Infor
  - IDM
  - Mapping
---
## Define the name of document type

#Example: <Doc2DocumentType>=<IDMDocumentType>
**Invoice=LN_SupplierInvoice**

Check the document type code as it is in DocBits (DOC2), like in BOD Mapping File it should match the name of the document type in the URL of the field settings.

Check the name of the document type as it should be in INFOR, this can be done by:
- Navigating to the Document Manager application within InforOS
- Search and select the name of the current document type you are trying to export, for example Supplier Invoice.

INVOICE=LN_SupplierInvoice
