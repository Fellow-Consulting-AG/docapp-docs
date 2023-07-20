---
title: "How to create an IDM mapping file"
description: This is a step by step guide how to create an IDM mapping file. You will find all values and fields that would need an adjustment in DocBits (DOC²), InforOS and the Mapping File.
date: "2021-10-28"
tags:
  - DocBits (DOC²)
  - Export
  - Infor
  - IDM
  - Mapping
---

## Mapping File

Mapping files provided by us can be found [here](https://github.com/Fellow-Consulting-AG/docbits)

## File Structure

`Invoice=LN_SupplierInvoice OR Invoice=M3_SupplierInvoice (Depends on whether you are using M3 or LN)`

Check the document type code as it is in DocBits (DOC²), like in BOD Mapping File it should match the name of the document type in the URL of the field settings.

![Editor](/_images/docbits/Export to Infor/Create IDM Mapping File/image_1_vscode.png)

Check the name of the document type as it should be in InforOS, this can be done by:

1. Navigating to the Document Manager application within InforOS
2. Search and select the name of the current document type you are trying to export, for example Supplier Invoice.

![DocumentManager](/_images/docbits/Export to Infor/Create IDM Mapping File/image_2_document_manager.png)
3. Click the above icon and then click Administration → Document Type and then find the document type you need in the list

![DocType](/_images/docbits/Export to Infor/Create IDM Mapping File/image_3_doc_type.png)
4. As shown below, you will then see the doc type name as it is in InforOS

![DocName](/_images/docbits/Export to Infor/Create IDM Mapping File/image_4_doc_name.png)
5. Other things to check include:

- The LN/M3 company
- The Entity ID (SF_MDS_EntityType), this value should be the same as it was in the BOD Mapping File.
- IndexFieldFromEphesoft=IDMAttributeID.






