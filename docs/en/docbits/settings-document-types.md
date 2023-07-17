---
title: Document Types, Field Settings and Profile
description: Here you will find all document types available in DocBits (DOC²) as invoice, credit note, delivery note, order confirmation and many more
date: "2021-10-29"
tags:
  - DocBits (DOC²)
  - Settings
  - Document Types
  - Field Settings
---


In DocBits (DOC²) you will find the `SETTINGS` menu in the upper bar on `HOME` screen.

![Dashboard](/_images/docbits/Settings/Document Types/Image_1_settings.png)

If you are logged in to DocBits (DOC²) as an admin, you will find all fields of a document that can be extracted under the respective document type.

Open the menu **Document Types**.

![Menu](/_images/docbits/Settings/Document Types/Image_2_doc_types_location.png)

In the following overview you will find all standard document types available for you:

![DocumentTypes](/_images/docbits/Settings/Document Types/Image_3.png)

To see which fields can be extracted, for example from an invoice, click on `FIELDS` for this document type.

![Fields](/_images/docbits/Settings/Document Types/Image_4_fields.png)

### Field Settings

Here you will find all the fields that can be extracted:

| INVOICE DETAILS    | PAYMENT DETAILS     |  VAT & AMOUNTS      |  VENDOR DETAILS     |
|       :----:       |        :----:       |       :----:        |      :----:         |
| INVOICE NUMBER     | IBAN                | CURRENCY            | ADDRESS             |
| INVOICE DATE       | PAYMENT TERMS       | NET AMOUNT FULL     | SUPPLIER NAME       |
| DELIVERY DATE      |                     | NET AMOUNT REDUCED  | VENDOR ID           |
| PO NUMBER          |                     | NET AMOUNT FREE     | VENDOR VAT          |
| ORDER DATE         |                     | TAX AMOUNT FULL     |                     |
|                    |                     | TAX AMOUNT REDUCED  |                     |
|                    |                     | TAX AMOUNT FREE     |                     |
|                    |                     | VAT RATE FULL       |                     |
|                    |                     | VAT RATE REDUCED    |                     |
|                    |                     | VAT RATE FREE       |                     |
|                    |                     | TOTAL NET AMOUNT    |                     |
|                    |                     | TOTAL TAX AMOUNT    |                     |
|                    |                     | TOTAL AMOUNT        |                     |




For every overpoint you can also **CREATE FIELDS** like freight, postage or any field with an amount you want to extract from your invoices.

For each field you can check the boxes if they are

- REQUIRED: Here you can define if the field must contain a value to continue.

- READ ONLY: Here you can define if a field can only be displayed but not edited.

- HIDDEN: Here you can define whether a field should be hidden or displayed in the extraction view.

- FORCE VALIDATION: Here you can define whether a field must always be validated manually, even if it has been read 100% by DocBits (DOC²).

- OCR and MATCH SCORE: Setting as described below, per field.

- FORMULA: Creation of a formula per field.


![FieldSettings](/_images/docbits/Settings/Document Types/Image_5_field_settings.png)

If all settings are made and should be saved, please confirm this with the `SAVE SETTINGS` button, otherwise the settings will not be applied.

![Save](/_images/docbits/Settings/Document Types/Image_6_save_settings.png)



### Recognition Settings

![Recognition](/_images/docbits/Settings/Document Types/Image_7_recog_settings.png)

**OCR:**

Here you can set the sensitivity of the OCR (Optical Character Recognition) function for all fields at once. This value determines the sensitivity with which a field is marked in red if it could not be extracted with 100% certainty (OCR related!).

**MATCH SCORE:**

Here you can set the sensitivity of the MATCH SCORE function for all fields at once. This value determines from when a field is marked in red if DocBits (DOC²) has not extracted the field with 100% probability. In this case the field needs to be validated manually.

The button `RESTORE DEFAULTS` will set back both values to "50".

![OCR](/_images/docbits/Settings/Document Types/Image_8_ocr_matchscore_slider.png)


### Profile

Here you can define the profile that shall be used. Either Default or ZUGFeRD.<br> In profile ZUGFeRD there are predefined fields that are mandatory for this type of invoice.<br> If you do not explicitly use ZUGFeRD, please select "Default".

![Profiles](/_images/docbits/Settings/Document Types/Image_9_profiles.png)




