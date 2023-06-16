---
title: "Wie man eine BOD-Mapping-Datei erstellt"
description: "Eine Schritt-für-Schritt-Anleitung zur Erstellung einer BOD-Mapping-Datei. Hier finden Sie alle Werte und Felder, die in Docbits (Doc²) und BOD angepasst werden müssen."
date: "2021-10-28"
tags:
  - Docbits (Doc²)
  - Export
  - Infor
  - BOD
  - Mapping
---

#### Schritt-für-Schritt-Anleitung zur Erstellung einer BOD-Mapping-Datei

Hier können Sie eine Beispiel-Mapping-Datei herunterladen:

[BOD-Mapping-Beispiel](https://docs.cloudintegration.eu/wp-content/uploads/2021/11/BOD_Mappings.txt)[Download](https://docs.cloudintegration.eu/wp-content/uploads/2021/11/BOD_Mappings.txt)

Um die Beispiel-Datei zu verwenden, benennen Sie die Datei von "BOD_Mapping.txt" in "BOD_Mapping.properties" um.

****Hier finden Sie eine Erklärung zur Struktur der Datei.****

Im ersten Block werden alle statischen Werte definiert. Felder, die angepasst werden müssen, sind "LogicalID" und "AccountingEntityID".

Die "LogicalID" muss auf die logische ID des IMS-Verbindungspunkts gesetzt werden, der für den Docbits (Doc²) BOD-Export definiert wurde.

Die "AccountingEntity" muss auf die Buchhaltungseinheit des Ziel-Infor-ERP-Systems gesetzt werden.

```
#Alle statischen Feldattribute.
Static_Fields=AlternateDocSchema,AlternateDocLocation,LogicalID,ConfirmationCode,actionCode,AccountingEntityID

SFP_AlternateDocSchema=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\AlternateDocumentID\\ID\\schemeName
SFV_AlternateDocSchema=CorrelationID

SFP_AlternateDocLocation=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\AlternateDocumentID\\ID\\location
SFV_AlternateDocLocation=doc2

SFP_LogicalID=SyncCaptureDocumentType\\ApplicationArea\\Sender\\LogicalID
SFV_LogicalID=lid://infor.ims.doc2export

SFP_ConfirmationCode=SyncCaptureDocumentType\\ApplicationArea\\Sender\\ConfirmationCode
SFV_ConfirmationCode=OnError

SFP_actionCode=SyncCaptureDocumentType\\DataArea\\Sync\\ActionCriteria\\ActionExpression\\actionCode
SFV_actionCode=Add

SFP_AccountingEntityID=SyncCaptureDocumentType\\DataArea\\Sync\\AccountingEntityID
SFV_AccountingEntityID=infor.ln.100
```

Im zweiten Block können Sie die Dokumenttypzuordnung anpassen. Auf der linken Seite haben Sie den Dokumenttyp von Docbits (Doc²) und auf der rechten Seite den Dokumenttyp von BOD.

```
#Alle generierten Felder.
Generated_Fields=CreationDateTime,BODID

GFP_BODID=SyncCaptureDocumentType\\ApplicationArea\\BODID
GFV_BODID=BODID

GFP_CreationDateTime=SyncCaptureDocumentType\\ApplicationArea\\CreationDateTime
GFV_CreationDateTime=CurrentDate

#Dokumenttyp-Pfad.
DT_Path=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentType

#Zuordnung zwischen doc2-Dokument und IDM-Dokument.
Document_Types=Invoice
Invoice=SupplierInvoice
```

Im dritten Block können Sie die Feldzuordnung anpassen. Auf der linken Seite stehen die Felder von Docbits (Doc²) und auf der rechten Seite die Feldnamen von BOD.

```
#Index-Feldzuordnung
Index_Fields=INVOICE_TYPE,PURCHASE_ORDER,INVOICE_NUMBER,INVOICE_DATE,DELIVERY_DATE,PAYMENT_TERMS,TAX_RATE,TAX_AMOUNT,NET_AMOUNT,TOTAL_AMOUNT,CURRENCY,VENDOR_ID,VENDOR_NAME,VAT_NO_EXTRACTED,IBAN_EXTRACTED,ACCOUNTING_ENTITY,CORRELATION_ID
IF_INVOICE_TYPE=InvoiceType
IF_PURCHASE_ORDER=PurchaseOrder
IF_INVOICE_NUMBER=InvoiceNumber
IF_INVOICE_DATE=InvoiceDate
IF_DELIVERY_DATE=DeliveryDate
IF_PAYMENT_TERMS=PaymentTerms
IF_TAX_RATE=VatPercent
IF_TAX_AMOUNT=VATAmount
IF_NET_AMOUNT=NetAmount
IF_TOTAL_AMOUNT=TotalAmount
IF_CURRENCY=Currency
IF_VENDOR_ID=SupplierID
IF_VENDOR_NAME=SupplierName
IF_IBAN_EXTRACTED=AccountNumber
IF_VAT_NO_EXTRACTED=VATRegNo
#IF_ACCOUNTING_ENTITY=AccountingEntityID
IF_CORRELATION_ID=AlternateDocumentID
#IF_VENDOR_IBAN=BankAccount
```

Der Rest der Datei sollte unverändert bleiben und keine Änderungen erfordern.

```
#Wenn der Indexfeldwert an anderer Stelle verwendet werden soll, definieren Sie hier den Pfad.

IFP_CORRELATION_ID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\AlternateDocumentID\\ID
IFP_INVOICE_NUMBER=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentID\\ID
IFP_INVOICE_DATE=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentDateTime
#IFP_ACCOUNTING_ENTITY=SyncCaptureDocumentType\\DataArea\\Sync\\AccountingEntityID

#Indexfeld gemeinsamer Pfad
IF_COMMON_PATH=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField

IF_Attributes=languageID

IFP_languageID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\Name\\languageID
IFV_languageID=en-us


#IF_Elements=name,value,fieldOrderNumber,datatype,category,pageID,fieldEnumeration
IF_Elements=name,value,fieldOrderNumber,page,fieldEnumeration
IFP_name=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\Name
IFP_value=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\Value
IFP_fieldOrderNumber=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\FieldOrderNumber
IFP_page=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\PageID
IFP_fieldEnumeration=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\FieldValueEnumerationString


Pages_COMMON_PATH=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentPage

Page_Elements=pageID,sourceFileName,fileMimeType
PFP_pageID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentPage\\PageID
PFP_sourceFileName=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentPage\\SourceFileName
PFP_fileMimeType=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentPage\\SourceMimeType

Batch_Level_Properties=fileSize,lastModificationPerson,lastModifiedDateTime

#Path_CreatePerson=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\CreationPerson\\Name
Path_fileSize=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\FileSize
Path_lastModificationPerson=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\LastModificationPerson\\Name
Path_lastModifiedDateTime=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\LastModificationDateTime
```