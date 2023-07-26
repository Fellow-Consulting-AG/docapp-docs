---
title: "PO Matching"
description: There are three ways you can match your Purchase Order. With corresponding invoice, delivery note and/or order confirmation.
date: "2022-01-24"
tags:
  - DocBits (DOC²)
  - PO Matching
  - Order Confirmation
  - Delivery Note
  - Invoice
---

# PO Matching Process/Setup

1. Sign in to [Infor Ming.le](https://mingle-sso.eu1.inforcloudsuite.com/inforsts/AB5C7D2B7902464D8D7BC9C471DFCE6D/idp/wsfed?wtrealm=urn%3Amingle12f-portal_core_443%3Aportal&wa=wsignin1.0&wreply=https%3A%2F%2Fmingle-portal.eu1.inforcloudsuite.com%2Fsignin-wsfed&wctx=CfDJ8DmYSJds8XROmddbMpIJ8lnf7B2vqzZ-xoTtf3KKUV35dOR3fNrXM_CLah__BKZQ6HF38Acx2rWocqPni0dSQ5p_5U7pvnXyv-qoIZMYxzrfyggIDVNYTkfT2bDtt2Ei31uXuoAFGHiZZQV-1bCKrdJMoQxDse9BKrb8m4C6F9f3vF6l313EPYeA6XhUFOK9sLSMILJU7vXJc_D-q7LwofWaFvcLwIJy2EdRX5ZFn3gB0rp6L6pps_B5ynS1xzxungruIZQPvsJmiTuhzsbC5r8)

2. Click on the [Infor Ming.le](https://mingle-sso.eu1.inforcloudsuite.com/inforsts/AB5C7D2B7902464D8D7BC9C471DFCE6D/idp/wsfed?wtrealm=urn%3Amingle12f-portal_core_443%3Aportal&wa=wsignin1.0&wreply=https%3A%2F%2Fmingle-portal.eu1.inforcloudsuite.com%2Fsignin-wsfed&wctx=CfDJ8DmYSJds8XROmddbMpIJ8lnf7B2vqzZ-xoTtf3KKUV35dOR3fNrXM_CLah__BKZQ6HF38Acx2rWocqPni0dSQ5p_5U7pvnXyv-qoIZMYxzrfyggIDVNYTkfT2bDtt2Ei31uXuoAFGHiZZQV-1bCKrdJMoQxDse9BKrb8m4C6F9f3vF6l313EPYeA6XhUFOK9sLSMILJU7vXJc_D-q7LwofWaFvcLwIJy2EdRX5ZFn3gB0rp6L6pps_B5ynS1xzxungruIZQPvsJmiTuhzsbC5r8)  URL to start using LN UI with a valid LN username and password

![](/_images/docbits/PO Matching/DocBits PO Matching/image_1_infor_signin.png)

After successful “Sign In”, User’s are logged on to the server.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_2_ln_dashboard.png)

**Override directly to any desired step in Infor LN workbench application**: 
User’s can now go to any step in Infor LN workbench applications directly by writing the system generated parameters of each business enhancements based on server location, username and workbench application. The parameters are shown in lower right side of screen. 

Choose  **Menu → Options → Run Program**

Shortcut is here “gr” on the keyboard

![](/_images/docbits/PO Matching/DocBits PO Matching/image_3_run_program.png)

**List of some Program Codes to override directly to any desired step in Infor LN**:

![](/_images/docbits/PO Matching/DocBits PO Matching/image_4_workbench.png)

### Sales-related enhancements

In this section, we will provide a brief explanation of the sales-related enhancements.

## Generate Purchase Order

- In order to generate a new Purchase Order Click on Workbench Bestellungsaufkommen

![](/_images/docbits/PO Matching/DocBits PO Matching/image_5_workbench_2.png)

- Customers should enter all the necessary details in the new purchase order layout such as Quantity, Supplier name, Article number etc. 

- Next step is to save the Purchase Order details and then click on ‘GENEHMIGEN’

- Each Purchase Order has a unique ID which is generated once you approved the order. 

![](/_images/docbits/PO Matching/DocBits PO Matching/image_6_workbench_3.png)

- Once the order is created by the user, next is to print the order and sent that Purchase Order invoice to the supplier.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_7_diagram.png)

## Order Confirmation

Once the Purchase Order is delivered to the supplier, the supplier sends backs an “Order Confirmation”. 

This order confirmation needs to be matched against the PO. 

**PO Matching**

The process of matching PO against the Order Confirmation is called “PO matching”.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_8_dashboard.png)

For PO matching the best tool is DocBits (DOC²), which can be easily automated. The easy training and AI swarm intelligence enable fast results at a high level, not just for header data but for line items in table extraction. The seamless Infor integration with the Infor BODs allows for automating the entire process with validation and export. Reduce time and costs very fast and effectively with DocBits (DOC²).

- Upload the Order Confirmation in DocBits (DOC²)

![](/_images/docbits/PO Matching/DocBits PO Matching/image_9_po_match_dashboard.png)

- Here you will find the PO matching button either Red or Green. If PO matching button is “Red” this means  documents do not match, else quantity on the order confirmation does match the quantity of the purchase order then PO matching button turns “Green” as in the picture below.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_10_po_match_vs.png)

- Main advantage of PO matching in DocBits(DOC²) is that DocBits automatically extract table and line items correctly from Order Confirmation with the help of AI. which results in less time and costs.

- Access the matching overview by clicking on the PO matching symbol on the Dashboard.

- This can also be done by choosing **PO MATCHING** in the lower left side when you have opened the document.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_11_po_match_screen.png)

### Scenario 1: PO gets matched

![](/_images/docbits/PO Matching/DocBits PO Matching/image_12_exported_dashboard.png)

- As the purchase order matched against the Order confirmation. 

- All matched rows have a green icon at the start as shown in figure above.   

- After dragging and dropping the appropriate data row(s), the document is ready to be exported.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_13_buyers_confirmation.png)

**Buyers Conformation (Matched)**

Once the matched Order Confirmation is exported in DocBits(DOC²), the next crucial step is Buyer Confirmation. The Buyer must confirm it again.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_14_po_not_matched.png)

### Scenario 2: PO does not get matched

- As the purchase order not matched against the Order confirmation. 

- Unmatched rows have a red icon at the start as shown in figure above.   

- After dragging and dropping the appropriate data row(s), the document is ready to be exported.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_15_exported_dashboard_2.png)

**Buyers Conformation (Not Matched)**

![](/_images/docbits/PO Matching/DocBits PO Matching/image_16_ln.png)

Once the unmatched Order Confirmation is exported in DocBits(DOC²), the status on Infor LN changed to “Geändert”. The next crucial step is Buyer Confirmation. As the Buyer confirms with terms & conditions of supplier, the status on Infor LN changed to “In Bearbeitung”.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_17_ln.png)

## Delivery Note

As the Buyer confirm it in Infor LN, only then supplier sends a delivery note to Warehouse, for inventory shipment to buyer address. This Delivery Note needs to be matched against the PO. 

**PO Matching**
The process of matching PO against the Delivery Note is called “PO matching”. For PO matching the best tool is DocBits (DOC²), which can be easily automated. The easy training and AI swarm intelligence enable fast results at a high level, not just for header data but for line items in table extraction. The seamless Infor integration with the Infor BODs allows for automating the entire process with validation and export. Reduce time and costs very fast and effectively with DocBits (DOC²).

- Upload the Delivery Note in DocBits (DOC²)

![](/_images/docbits/PO Matching/DocBits PO Matching/image_18_delivery_note_upload.png)

- Here you will find the PO matching button either Red or Green. If PO matching button is “Red” this means  documents do not match, else quantity on the order confirmation does match the quantity of the purchase order, so PO matching button turns “Green” as in the picture below.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_19_po_match_icon.png)

- Main advantage of PO matching in DocBits(DOC²) is that DocBits automatically extract table and line items correctly from Delivery Note with the help of AI. which results in less time and costs.

- Access the matching overview by clicking on the PO matching symbol on the Dashboard.

- This can also be done by choosing PO MATCHING in the lower left side when you have opened the document.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_20_delivery_note_vs.png)
![](/_images/docbits/PO Matching/DocBits PO Matching/image_21_delivery_note_po_screen.png)

- A new match from the purchase order can be added to the delivery note by dragging and dropping the appropriate data row(s). You need to confirm the mismatched properties.

- Save to apply all changes.

Once everything is correct and all the ticks are green, it means PO is matched . This means you will find the green ticks symbol as the both documents match. After quantity on the delivery note matches the quantity of the purchase order then the document is ready for validation and is exported.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_22_delivery_note_exported.png)

**Export file need to Reconfirm through One View Function of Infor LN**

In order to check whether the export file was accepted or rejected, we use OneView from ION Desk in Infor LN.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_23_oneview.png)

User can easily found his Delivery confirmation either by Date & Time or by Document ID. 

![](/_images/docbits/PO Matching/DocBits PO Matching/image_24_bods.png)

Once the user found his/her Delivery Note. He needs to click on the File sign to check whether the file is accepted or rejected.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_25_accepted_rejected.png)
![](/_images/docbits/PO Matching/DocBits PO Matching/image_26_code.png)

This means that the Delivery Note was successfully integrated in Infor LN

**Change in Status**

![](/_images/docbits/PO Matching/DocBits PO Matching/image_27_status_change.png)

Once the Delivery Note is exported in DocBits(DOC²), the status of Purchase Order in Infor LN changed from “ In Process” to “Completed”. This means purchase is completed and delivery will be send to Buyer address not later than the promised Delivery Confirmation Date.

![](/_images/docbits/PO Matching/DocBits PO Matching/image_28_completed.png)

### Checking whether goods have arrived in the warehouse

![](/_images/docbits/PO Matching/DocBits PO Matching/image_29_warehouse.png)

In case if Goods are received in warehouse as shown in the picture above, the section “Wareneingang” have all the details regarding the Goods and status will be “confirmed” in wareneingang. 

![](/_images/docbits/PO Matching/DocBits PO Matching/image_30_warehouse_2.png)

However, if Goods are not received in warehouse as shown in the picture above, the section “Wareneingang” is empty and has no details regarding the Goods.