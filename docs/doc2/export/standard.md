---
title: "Export Standard JSON or XML Output"
description: Standard JSON or XML Output 
date: "2023-50-03"
tags:
  - DOC²
  - Export
  - DOC²
  - JSON
  - XML
---


# Standard  Output for Invoices



![Seite 1](/_images/doc2/RG230419-02_Seite_1.jpg)
![Seite 2](/_images/doc2/RG230419-02_Seite_2.jpg)

## Standard JSON output

The JSON output contains all relevant information from the invoice and is presented in a structured and easy to understand form. Here is an example of the JSON output:

### JSON

```json
{
  "Format":  "v1.1",
  "document_type": "Invoice",
  "filename": "RG230419-02.pdf",
  "summary": "This is an invoice from FELLOW Consulting AG to the company GmbH for the purchase of Apples Pink Lady, Chocolate Cookies, and Mineral Waters. The invoice includes details such as the invoice number, invoice date, delivery date, customer number, and payment terms.",
  "keywords": [
    "FELLOW Consulting AG",
    "GmbH",
    "Apples Pink Lady",
    "Chocolate Cookies",
    "Mineral Waters",
    "invoice",
    "invoice number",
    "invoice date",
    "delivery date",
    "customer number",
    "payment terms"
  ],
  "invoice_number": "RG230419-02",
  "invoice_date": "19.04.2023",
  "delivery_date": "28.03.2023",
  "customer_number": "FP8731",
  "payment_terms": "30 Tage Netto",
  "items": [
    {
      "item_number": 1,
      "description": "Apples Pink Lady",
      "quantity": 100,
      "unit_price": 3.49,
      "total_price": 349.00,
      "origin_country": "Österreich",
      "article_number": "IB-2000",
      "batch_number": "CN87293",
      "order_number": "PO0000166",
      "delivery_number": "LS23-1001"
    },
    {
      "item_number": 2,
      "description": "Chocolate Cookies",
      "quantity": 2,
      "unit_price": 12.59,
      "total_price": 25.18,
      "article_number": "IB-2001",
      "batch_number": "CN34283",
      "order_number": "PO0000166",
      "delivery_number": "LS23-1002"
    },
    {
      "item_number": 3,
      "description": "Chocolate Cookies",
      "quantity": 1,
      "unit_price": 12.59,
      "total_price": 12.59,
      "article_number": "IB-2001",
      "batch_number": "CN49282",
      "order_number": "PO0000167",
      "delivery_number": "LS23-1003"
    },
    {
      "item_number": 4,
      "description": "Mineral Waters",
      "quantity": 5,
      "unit_price": 1.50,
      "total_price": 7.50,
      "article_number": "IB-2002",
      "batch_number": "CN56427",
      "order_number": "PO0000167",
      "delivery_number": "LS23-1003"
    }
  ],
  "subtotal": 386.77,
  "tax_rate": 0.19,
  "tax_amount": 74.91,
  "total": 469.18,
  "sender_name": "FELLOW Consulting AG",
  "sender_address": "Anzinger Str 21a",
  "sender_city": "85586 Poing",
  "recipient_name": "Ihr Unternehmen GmbH",
  "recipient_address": "Straße 45",
  "recipient_city": "67809 Stadt",
  "contact_person": "Paul Fischer"
}
```

### XML

Same Information as XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<document>
  <document_type>Invoice</document_type>
  <filename>RG230419-02.pdf</filename>
  <summary>This is an invoice from FELLOW Consulting AG to the company GmbH for the purchase of Apples Pink Lady, Chocolate Cookies, and Mineral Waters. The invoice includes details such as the invoice number, invoice date, delivery date, customer number, and payment terms.</summary>
  <keywords>
    <keyword>FELLOW Consulting AG</keyword>
    <keyword>GmbH</keyword>
    <keyword>Apples Pink Lady</keyword>
    <keyword>Chocolate Cookies</keyword>
    <keyword>Mineral Waters</keyword>
    <keyword>invoice</keyword>
    <keyword>invoice number</keyword>
    <keyword>invoice date</keyword>
    <keyword>delivery date</keyword>
    <keyword>customer number</keyword>
    <keyword>payment terms</keyword>
  </keywords>
  <invoice_number>RG230419-02</invoice_number>
  <invoice_date>19.04.2023</invoice_date>
  <delivery_date>28.03.2023</delivery_date>
  <customer_number>FP8731</customer_number>
  <payment_terms>30 Tage Netto</payment_terms>
  <items>
    <item>
      <item_number>1</item_number>
      <description>Apples Pink Lady</description>
      <quantity>100</quantity>
      <unit_price>3.49</unit_price>
      <total_price>349.00</total_price>
      <origin_country>Österreich</origin_country>
      <article_number>IB-2000</article_number>
      <batch_number>CN87293</batch_number>
      <order_number>PO0000166</order_number>
      <delivery_number>LS23-1001</delivery_number>
    </item>
    <item>
      <item_number>2</item_number>
      <description>Chocolate Cookies</description>
      <quantity>2</quantity>
      <unit_price>12.59</unit_price>
      <total_price>25.18</total_price>
      <article_number>IB-2001</article_number>
      <batch_number>CN34283</batch_number>
      <order_number>PO0000166</order_number>
      <delivery_number>LS23-1002</delivery_number>
    </item>
    <item>
      <item_number>3</item_number>
      <description>Chocolate Cookies</description>
      <quantity>1</quantity>
      <unit_price>12.59</unit_price>
      <total_price>12.59</total_price>
      <article_number>IB-2001</article_number>
      <batch_number>CN49282</batch_number>
      <order_number>PO0000167</order_number>
      <delivery_number>LS23-1003</delivery_number>
    </item>
    <item>
      <item_number>4</item_number>
      <description>Mineral Waters</description>
      <quantity>5</quantity>
      <unit_price>1.50</unit_price>
      <total_price>7.50</total_price>
      <article_number>IB-2002</article_number>
      <batch_number>CN56427</batch_number>
      <order_number>PO0000167</order_number>
      <delivery_number>LS23-1003</delivery_number>
    </item>
  </items>
  <subtotal>386.77</subtotal>
  <tax_rate>0.19</tax_rate>
  <tax_amount>74.91</tax_amount>
</document>
```


## Position output

### JSON

Position JSON output contains detailed information about individual positions in the invoice and is also presented in a structured and easy-to-understand form. Here is an example of the Position JSON output:

```json

{
  "Format":  "v1.1",
  "company": "FELLOW Consulting AG",
  "address": "Anzinger Str 21a",
  "zipCode": "85586",
  "city": "Poing",
  "invoiceNumber": "RG230419-02",
  "invoiceDate": "19.04.2023",
  "customerCompany": "Ihr Unternehmen GmbH",
  "deliveryDate": "28.03.2023",
  "customerAddress": "Straße 45",
  "customerNumber": "FP8731",
  "contactPerson": "Paul Fischer",
  "items": [
    {
      "pos": 1,
      "description": "Apples Pink Lady",
      "quantity": 100,
      "unitPrice": "3,49 €",
      "totalPrice": "349,00 €",
      "originCountry": "Österreich",
      "articleNumber": "IB-2000",
      "batchNumber": "CN87293",
      "orderNumber": "PO0000166",
      "deliveryNumber": "LS23-1001",
      "deliveryDate": "28.03.2023"
    },
    {
      "pos": 2,
      "description": "Chocolate Cookies",
      "quantity": 2,
      "unitPrice": "12,59 €",
      "totalPrice": "25,18 €",
      "articleNumber": "IB-2001",
      "batchNumber": "CN34283",
      "orderNumber": "PO0000166",
      "deliveryNumber": "LS23-1002",
      "deliveryDate": "28.03.2023"
    },
    {
      "pos": 3,
      "description": "Chocolate Cookies",
      "quantity": 1,
      "unitPrice": "12,59 €",
      "totalPrice": "12,59 €",
      "articleNumber": "IB-2001",
      "batchNumber": "CN49282",
      "orderNumber": "PO0000167",
      "deliveryNumber": "LS23-1003",
      "deliveryDate": "29.03.2023"
    },
    {
      "pos": 4,
      "description": "Mineral Waters",
      "quantity": 5,
      "unitPrice": "1,50 €",
      "totalPrice": "7,50 €",
      "articleNumber": "IB-2002",
      "batchNumber": "CN56427",
      "orderNumber": "PO0000167",
      "deliveryNumber": "LS23-1003",
      "deliveryDate": "29.03.2023"
    }
  ],
  "subtotal": "386,77 €",
  "netTotal": "394,27 €",
  "tax": "74,91 €",
  "total": "469,18 EUR",
  "paymentTerms": "30 Tage Netto",
  "sender": "Paul Fischer"
}
```


### XML 

Same Information as XML



```xml
<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <company>FELLOW Consulting AG</company>
  <address>Anzinger Str 21a</address>
  <zipCode>85586</zipCode>
  <city>Poing</city>
  <invoiceNumber>RG230419-02</invoiceNumber>
  <invoiceDate>19.04.2023</invoiceDate>
  <customerCompany>Ihr Unternehmen GmbH</customerCompany>
  <deliveryDate>28.03.2023</deliveryDate>
  <customerAddress>Straße 45</customerAddress>
  <customerNumber>FP8731</customerNumber>
  <contactPerson>Paul Fischer</contactPerson>
  <items>
    <item>
      <position>1</position>
      <description>Apples Pink Lady</description>
      <quantity>100</quantity>
      <unitPrice>3,49 €</unitPrice>
      <totalPrice>349,00 €</totalPrice>
      <originCountry>Österreich</originCountry>
      <articleNumber>IB-2000</articleNumber>
      <batchNumber>CN87293</batchNumber>
      <orderNumber>PO0000166</orderNumber>
      <deliveryNumber>LS23-1001</deliveryNumber>
      <deliveryDate>28.03.2023</deliveryDate>
    </item>
    <item>
      <position>2</position>
      <description>Chocolate Cookies</description>
      <quantity>2</quantity>
      <unitPrice>12,59 €</unitPrice>
      <totalPrice>25,18 €</totalPrice>
      <articleNumber>IB-2001</articleNumber>
      <batchNumber>CN34283</batchNumber>
      <orderNumber>PO0000166</orderNumber>
      <deliveryNumber>LS23-1002</deliveryNumber>
      <deliveryDate>28.03.2023</deliveryDate>
    </item>
    <item>
      <position>3</position>
      <description>Chocolate Cookies</description>
      <quantity>1</quantity>
      <unitPrice>12,59 €</unitPrice>
      <totalPrice>12,59 €</totalPrice>
      <articleNumber>IB-2001</articleNumber>
      <batchNumber>CN49282</batchNumber>
      <orderNumber>PO0000167</orderNumber>
      <deliveryNumber>LS23-1003</deliveryNumber>
      <deliveryDate>29.03.2023</deliveryDate>
    </item>
    <item>
      <position>4</position>
      <description>Mineral Waters</description>
      <quantity>5</quantity>
      <unitPrice>1,50 €</unitPrice>
      <totalPrice>7,50 €</totalPrice>
      <articleNumber>IB-2002</articleNumber>
      <batchNumber>CN56427</batchNumber>
      <orderNumber>PO0000167</orderNumber>
      <deliveryNumber>LS23-1003</deliveryNumber>
      <deliveryDate>29.03.2023</deliveryDate>
    </item>
  </items>
  <subtotal>386,77 €</subtotal>
  <netTotal>394,27 €</netTotal>
  <tax>74,91 €</tax>
  <total>469,18 EUR</total>
  <paymentTerms>30 Tage Netto</paymentTerms>
  <sender>Paul Fischer</sender>
</invoice>
```


## Legal Seller Information


###  JSON

```json

{
  "seller": {
    "name": "FELLOW Consulting AG",
    "address": "Anzinger Str 21a",
    "postalCode": "85586",
    "city": "Poing",
    "country": "Germany",
    "bank": {
      "name": "FELLOWPRO AG",
      "iban": "DE12345678901234567890",
      "bic": "GENODEF1M04"
    },
    "legal": {
      "taxId": "DE123456789",
      "register": "Amtsgericht München",
      "registerNumber": "HRB 123456"
    }
  }
}
```

### XML


```xml
<?xml version="1.0" encoding="UTF-8"?>
<seller>
  <name>FELLOW Consulting AG</name>
  <address>Anzinger Str 21a</address>
  <postalCode>85586</postalCode>
  <city>Poing</city>
  <country>Germany</country>
  <bank>
    <name>FELLOWPRO AG</name>
    <iban>DE12345678901234567890</iban>
    <bic>GENODEF1M04</bic>
  </bank>
  <legal>
    <taxId>DE123456789</taxId>
    <register>Amtsgericht München</register>
    <registerNumber>HRB 123456</registerNumber>
  </legal>
</seller>
```
