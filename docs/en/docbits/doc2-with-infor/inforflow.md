---
title: "Docbits (DOC²) - Infor API Integration for PO Matching"
description: "Learn how Docbits (DOC²) integrates with Infor LN/M3 for PO matching and document processing. Explore our use cases and API flow for seamless integration."
date: "2022-10-27"
tags:
  - Docbits (DOC²)
  - PO Matching
  - Infor LN
  - Infor M3
  - API Integration
---

## API Integration with Infor OS & Infor CloudSuite

![Infor CloudSuite API Flow for Docbits (DOC²)](/_images/docbits/infor/Doc2-Infor.png "Infor CloudSuite API Flow for Docbits (DOC²)")

Docbits (DOC²) seamlessly integrates with Infor LN/M3 through ION API, ION Desk, and Infor Standard BODs. Our API integration allows us to export data to Infor and perform master data validation in Docbits (DOC²).

### Exporting Data to Infor

We use the ION API to send the PDF with attributes to IDM and the BOD Sync.CaptureDocument to ION Desk. In ION Desk, we transform the Sync.CaptureDocument to the desired target BODs based on the document type being processed. These transformed Infor BODs are then automatically imported to LN or M3.

### Master Data Validation in Docbits (DOC²)

To identify the supplier or compare/match purchase order lines, we activate a trigger in LN/M3 that sends the Sync.RemitToPartyMaster, Sync.SupplierPartyMaster, and Sync.PurchaseOrder BODs to Docbits (DOC²). We configure this process in ION Desk by defining the dataflow to a specific connection point to Docbits (DOC²).

Explore our use cases and learn more about our API integration with Infor LN/M3:

- [Exporting Data to Infor](/docbits/export/export-to-infor/)
- [IDM Business Context Model](/docbits/doc2-with-infor/IDM-business-context-model/)
- [Infor SSO with Docbits (DOC²)](/docbits/configuring-sso-in-cloud/)
- [Infor Infrastructure & Security](/docbits/doc2-with-infor/infrastructure/)
