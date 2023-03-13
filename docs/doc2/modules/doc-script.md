---
title: "Doc Script"
description: You will find different modules in DOC² settings.These modules are important if you like to deal with PO Matching and use the table extraction functionality. 
date: "2023-03-10"
tags:
  - DOC²
  - Settings
  - Modules
  - Document Type
  - Script
---


If you want to use scripts that, for example, convert currency characters or written-out currency names into ISO codes, please activate this first in the settings under Module -> Document Type -> Doc Script.

![](/_images/doc2/Modules/doc-script/Script_Settings_Module_Doc Script.png)

After that, go to the desired document type - in our example `Invoice`, open `Scripts` , copy the script below and overwrite the example with this one. Then click on `SAVE`.

![](/_images/doc2/Modules/doc-script/Script_Invoice_Scripts.png)

The result should look like this:

![](/_images/doc2/Modules/doc-script/Script_added.png)


<ins>Script to copy:</ins>

```script
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}

currency_value = get_field_value(fields_dict, "currency", None)

if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(fields_dict, "currency", currency_value)
```

In the next step, upload a document with one of the following criteria: `€`, `EURO`, `$` or `£`.

When the document is ready for validation, open it and click in the Currency validation field. You will be prompted to select the appropriate area on the image. Now do this with the `€` sign. 

![](/_images/doc2/Modules/doc-script/Script_Currency_select area on image€.png)

You will then immediately see that € is converted to EUR by the script.

![](/_images/doc2/Modules/doc-script/Script_conversion_currency_1.png)

The same is done by the script when you mark EURO on the invoice.

![](/_images/doc2/Modules/doc-script/Script_Currency_select area on imageEURO.png)

![](/_images/doc2/Modules/doc-script/Script_conversion_currency_2.png)