---
title: "Data Flow"
description: Data Flow 
date: "2023-05-03"
tags:
  - Data Flow
---


# Data Flow

``` mermaid
sequenceDiagram
    participant doc2api
    participant fellow2kv
    participant ocrserver

    doc2api ->> fellow2kv: Call Fellow2KV API
    fellow2kv -->> doc2api: Return Fellow2KV results
    fellow2kv ->> ocrserver: Call Doc2API OCR Celery
    ocrserver -->> fellow2kv: Return OCR results
    note over ocrserver: OCR results will be stored for 6 days
    ocrserver ->> ocrserver: Delete OCR results after 6 days

```

The diagram shows that data delivery is done in three steps:
1. Doc2API calls the Fellow2KV API to receive data.
2. Fellow2KV calls the OCR server to process the received data.
3. the OCR server sends the OCR results back to Fellow2KV, which in turn returns them to Doc2API.
This process allows Doc2API to receive OCR information generated from the data processed by Fellow2KV.
To ensure data delivery, all systems involved are configured to meet data protection requirements. This includes compliance with data protection laws and the implementation of security measures to ensure the confidentiality, integrity and availability of the data. Overall, this diagram shows how data is delivered between different systems to obtain the OCR information required by Doc2API.

Doc² places great importance on the data privacy and security of its customers and users. When processing PDF files, only tokens related to the layout of the documents are stored. These tokens do not contain any personal data and cannot be used to recover the actual contents of the documents.
The actual data contained in the PDF files is only retained for a limited period of time and then deleted to ensure that it is not retained for longer than necessary. The exact period after which the data is deleted depends on various factors, such as customer requirements or legal regulations. However, as a rule, the data is deleted within 30 days after processing.
The use of layout tokens and the deletion of data after a certain period of time ensures that user privacy and data are protected. This is an important part of Doc²'s privacy practices and demonstrates the company's commitment to protecting the privacy of its customers and users.

``` mermaid
stateDiagram-v2
    [*] --> start
    state API {
        [*] --> TIFF_to_PDF
        [*] --> Process_Metadata
        [*] --> Split
        [*] --> PDFCheck
        [*] --> TRIM
    }
    state KV {
        [*] --> OCRed
        [*] --> Deskew
    }
    state KV_Step2 {
        [*] --> Classify
        [*] --> OCR Data
        [*] --> TFIDF
        [*] --> Fields
        [*] --> Table
    }
    state AI {
        [*] --> Handwriting
        [*] --> Classification
    }
    state OCR {
        [*] --> PDF

    }
    state API_Step2 {
        [*] --> Thumbnails
        [*] --> TROCR
        [*] --> Formating_Fields
        [*] --> Formating_Table

    }
    state API

    start --> API
    TIFF_to_PDF --> Save 
    Process_Metadata --> Save 
    Split --> Save
    PDFCheck --> Save
    TRIM --> Save
    Save --> Assign_Batch 
    Assign_Batch --> QRCode
    QRCode --> XML_INVOICE
    XML_INVOICE --> KV
    KV --> OCR
    OCR --> AI
    OCR --> KV_Step2
    KV_Step2 --> Result
    Result --> API_Step2
    TROCR --> Classification
    API_Step2 --> End
    End --> [*]
```



