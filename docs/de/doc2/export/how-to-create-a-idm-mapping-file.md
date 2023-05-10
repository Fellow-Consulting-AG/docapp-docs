---
title: "Wie man eine IDM-Mapping-Datei erstellt"
description: "Eine Schritt-für-Schritt-Anleitung zur Erstellung einer IDM-Mapping-Datei. Erfahren Sie, was im ersten, zweiten und dritten Block zu tun ist."
date: "2021-10-26"
tags:
  - DOC²
  - Export
  - Infor
  - IDM
  - Mapping
---

#### Schritt-für-Schritt-Anleitung zur Erstellung einer IDM-Mapping-Datei

Sie können hier eine Beispiel-Mapping-Datei herunterladen:

[IDM-Mapping-Beispiel](https://docs.cloudintegration.eu/wp-content/uploads/2021/10/IDM_Mappings.txt)[Herunterladen](https://docs.cloudintegration.eu/wp-content/uploads/2021/10/IDM_Mappings.txt)

Um die Beispiel-Datei zu verwenden, benennen Sie die Datei von "IDM\_Mapping.txt" in "IDM\_Mapping.properties" um.

**Hier finden Sie eine Erklärung zur Struktur der Datei.**

Im ersten Block wird der Dokumenttyp zugeordnet. Auf der linken Seite sehen Sie den Dokumenttypnamen von DOC² und auf der rechten Seite den Dokumenttypnamen von IDM.

```
#Definieren Sie den Namen des Dokuments
#Beispiel: <Doc2DocumentType>=<IDMDocumentType>
#Invoice=LN_SupplierInvoice
INVOICE=LN_SupplierInvoice
```

Im zweiten Block können Sie statische Werte definieren, die in der Mapping-Datei verwendet werden.

Im Beispiel gibt es ein statisches Feld für FileNameSeperator und ACLString.

Mit dem Feld ACLString können Sie die ACL definieren, die in IDM für jedes exportierte Dokument festgelegt wird.

```
#Definieren Sie Zuordnungen für die statischen Werte
#Beispiel: Static_Values=<StaticVariableName>:<type>
Static_Values=FileNameSeparator,ACLString
#Beispiel: SF_<StaticVariableName> = StaticValue
SV_FileNameSeparator=_
SV_ACLString=Public
```

Im dritten Block können Sie statische Werte definieren, die an IDM übertragen werden.

Es wird verwendet, um die EntityType, AccountingEntity und GroupAccountingEntity in IDM festzulegen.

Die Werte müssen entsprechend Ihrer Umgebung festgelegt werden.

```
#Definieren Sie Zuordnungen für die statischen Felder
#Beispiel: Static_Fields=<IDMAttributeId>:<type>
Static_Fields=MDS_EntityType:STRING,MDS_AccountingEntity,MDS_BodRefAccEntity
#Beispiel: SF_<IDMAttributeId> = StaticValue
SF_MDS_EntityType=InforERPEnterpriseFinancialsReceivedInvoice
SF_MDS_AccountingEntity=100
SF_MDS_BodRefAccEntity=infor.ln.0100
```

Im vierten Block können Sie die DOC²-Felder den IDM-Attributen zuordnen.

```
#Definieren Sie Indexfelder
#Beispiel: Index_Fields=<IndexFieldIdFromEphesoft>:<type>
Index_Fields=INVOICE_NUMBER:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,INVOICE_DATE:STRING,GROUP_ACCOUNTING_ENTITY:STRING,SUPPLIER_NAME:STRING
#Beispiel: IF_<IndexFieldIdFromDoc2> = <IDMAttributeId>
IF_INVOICE_NUMBER=SupplierInvoiceNumber
IF_CORRELATION_ID=MDS_id1
IF_INVOICE_DATE=InvoiceDate
IF_SUPPLIER_NAME=SupplierName
```

Im fünften Block wird der ACL-String des zweiten Blocks dem ACL-Feld von IDM zugeordnet. Normalerweise sollte dies nicht geändert werden.

```
#Definieren Sie den ACL-Feldwert
#Beispiel: ACL_Fields= Konkatenation anderer definierter Felder, die zusammen eine gültige ACL in IDM ergeben sollten
ACL_Fields=SV_ACLString
```

Im letzten Block können Sie den "Searchable\_PDF\_Name" definieren. Das wird der Name des Dokuments in IDM sein.

Es kann ein einzelner Feldname oder eine Konkatenation verschiedener Felder sein. Zum Beispiel:

Searchable\_PDF\_Name=IF\_INVOICE\_NUMBER+SV\_FileNameSeparator+IF\_SUPPLIER\_NAME

```
#Definieren Sie die Ressourcenzuordnung
#Beispiel: Searchable_PDF_Name= Konkatenation anderer definierter Felder
Searchable_PDF_Name=IF_INVOICE_NUMBER
```