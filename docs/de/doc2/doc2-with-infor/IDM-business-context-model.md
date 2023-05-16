---
title: IDM Business Context Model - Anleitung zur Erstellung von Dokumenttypen in IDM und deren Verbindung mit der entsprechenden Arbeitsumgebung in LN
description: In dieser Dokumentation finden Sie Informationen zur Erstellung neuer Dokumenttypen in IDM und deren Verbindung mit der entsprechenden Arbeitsumgebung in LN.
date: 2023-05-16
tags:
  - DOC²
  - Infor
  - IDM
  - LN

---
## Was ist Infor Document Management (IDM)?

Infor Document Management (IDM) ist eine Unternehmensanwendung zur Dokumentenverwaltung, die im Infor Operating Service-Portal bereitgestellt und integriert wird.

IDM ist eine von mehreren Infor-Anwendungen, die die Benutzeroberfläche von Infor Ming.leTM nutzen.

IDM ist ein zentrales Repository, in dem Sie Ihre allgemeinen Geschäftsregeln für die Erstellung, Speicherung und Verwaltung von Dokumenten - wie Rechnungen, Lieferantendokumente und Mitarbeiterdaten - verwalten können. Sie können die physischen Dateien anzeigen, bearbeiten, erstellen und speichern.

Sie können IDM mit DOC² erweitern. Es bietet Funktionen zur optischen Zeichenerkennung (OCR) und intelligenten Zeichenerkennung (ICR). Diese Werkzeuge ermöglichen umfassendere und verbesserte Prozesse zur Dokumentenerfassung.
Sie können Ihre Dokumente über einen Standard-Webbrowser scannen, verbinden und die Dokumente mit Ihrem Geschäftsprozess verbinden.
Mit IDM finden Sie die Dokumente, die Sie benötigen, und arbeiten immer mit der neuesten, vollständigsten Version eines Dokuments. Durch den kontextbezogenen Zugriff auf alle wichtigen Geschäftsinformationen automatisiert DOC² Ihre Dokumenten-Workflows durch die automatische Kategorisierung und den Abruf wichtiger Dokument-Metadaten weiter.


## Zugriff auf IDM

Greifen Sie über die IDM-URL auf die Anwendung zu.

Durch den Zugriff auf das System über diese URL stellen Sie sicher, dass die erforderlichen Bibliotheken beim Laden der Seite geladen werden. Andernfalls funktionieren einige Funktionen wie Verknüpfungen und Kontextfreigabe nicht ordnungsgemäß. Die IDM-URL wird Ihrem IDM-Administrator zur Verfügung gestellt.

Nach der Anmeldung können Sie über den App-Switcher im Infor Ming.le-Portal auf die Client-Anwendung zugreifen.


### Control Center

To access the Control Center, click the options menu next to the **+ Add Document** button on the **Document Management** landing page and select **Control Center**.

![](/_images/doc2/Infor/IDM_Control Center.png)

If you have the `IDM-AdvancedUser` role or higher, you can perform these actions from the control center:

1. Configure the Exporter/Importer. (See below)

2. Synchronize the data model. Through this action the systems can self-heal by synchronizing the data model.

For all other actions in the control center, see the _Infor Document Management Administration Guide – Cloud Edition_. These actions are only available for users with the `IDM-Administrator` role.

### Configuration Exporter / Importer

![](/_images/doc2/Infor/IDM_ControlCenter_Document Type_Import.png)

Configuration Exporter and Importer allows the user to export / import the Configuration parts of Control Center (Document Types Filter, Result List, Business Context Model, and ION Configuration) using XML documents.

The xml files for all common document types can be downloaded here.

- Order Confirmation: <a href="assets/images/doc2/Infor/IDMconfiguration_OrderConfirmation.xml" download>IDMconfiguration_OrderConfirmation</a>
- Delivery Note: <a href="assets/images/doc2/Infor/IDMconfiguration_DeliveryNote.xml" download>IDMconfiguration_DeliveryNote</a>
- Invoice: <a href="assets/images/doc2/Infor/IDMconfiguration_Invoice.xml" download>IDMconfiguration_Invoice</a>

If you are using Infor LN as ERP also upload these xml files:

- Order Confirmation: <a href="assets/images/doc2/Infor/IDMconfiguration_BusinessContext_OrderConfirmation.xml" download>IDMconfiguration_BusinessContext_OrderConfirmation</a>
- Delivery Note: <a href="assets/images/doc2/Infor/IDMconfiguration_BusinessContext_DeliveryNote.xml" download>IDMconfiguration_BusinessContext_DeliveryNote</a>
- Delivery Note2:<a href="assets/images/doc2/Infor/IDMconfiguration_BusinessContext_DeliveryNote2.xml" download>IDMconfiguration_BusinessContext_DeliveryNote2</a>
- Invoice: <a href="assets/images/doc2/Infor/IDMconfiguration_BusinessContext_Invoice.xml" download>IDMconfiguration_BusinessContext_Invoice</a>


You can import the files as follows:

### Using the Import tab

1. Navigate to **Control Center** > **Administration** > **Import / Export** and click the **Import** tab.
2. Click **Select XML file** and browse for the XML file. A file validation applies. Only XML files that were created by the exporter are accepted. If validation fails, **Import XML** file remains disabled.
3. When the configuration file is uploaded, an import preview is displayed and includes any or all of these parts:
    <table>
    <tr>
        <td style="max-width: 100%; white-space: nowrap">Document Types and Value Sets</td>
        <td style="max-width: 100%; white-space: nowrap">The list of document types and value sets to be imported.</td>
    </tr>
    <tr>
        <td>Document Type Filter</td>
        <td>A list of document types that is displayed for the user when importing this configuration.</td>
    </tr>
    <tr>
        <td>Result List</td>
        <td>Result list configuration to be imported.</td>
    </tr>
    <tr>
        <td>Business Context Models</td>
        <td>Business context model configuration to be imported.</td>
    </tr>
    <tr>
        <td>ION</td>
        <td>ION configuration to be imported.</td>
    </tr>
    </table>
4. You can collapse or expand each part to see possible warnings or information:
   + :fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" } Warning - yellow sign: The warning sign does not disable **Import XML file**. We recommend that you go through all warning messages before starting the importer. This could be due to these situations:
    + Some configuration parts already exist in the repository that might be overwritten, for example, Result List.
    + Some configuration parts already exist in the repository that might be lost, for example, Document Type Filter.
   + :fontawesome-solid-info:{ style="color: #eee20e" } Information - blue sign: The information sign does not disable Import XML file. It is usually displayed in these situations:
    + If some parts cannot be imported, for example, Items.
    + If some existing parts are merged with new ones from the XML file, for example, Result List.
   + A green OK sign with no message required.
5. Click **Import XML file** to run the importer. When the import is finished, a report window is displayed with an information table that summarizes the status of the import. If any error occurs during the import, the error message informs the user what went wrong.

When the import is successful, **Import XML file** is disabled.

This is how the general Information and attributes look like in IDM under the corresponding document type:

**Order Confirmation**

![](/_images/doc2/Infor/IDM_DocumentType_OrderConfirmation.png)
![](/_images/doc2/Infor/IDM_Attributes_OrderConfirmation.png)

**Delivery Note**

![](/_images/doc2/Infor/IDM_DocumentType_DeliveryNote.png)
![](/_images/doc2/Infor/IDM_Attributes_DeliveryNote.png)

**Invoice**

![](/_images/doc2/Infor/IDM_DocumentType_Invoice.png)
![](/_images/doc2/Infor/IDM_Attributes_Invoice.png)

When you open the **Business Context Model** menu item
![](/_images/doc2/Infor/IDM_BusinessContextModel.png)
you will find the information here as follows:

**Order Confirmation**

![](/_images/doc2/Infor/BusinessContextModel_XQuery_OrderConfirmation.png)
```oc
/ORDER_CONFIRMATION[@MDS_EntityType = "{entityType}" AND @MDS_id1 = "{id1}"]
```

**Delivery Note**

![](/_images/doc2/Infor/BusinessContextModel_XQuery_DeliveryNote.png)
```dn
/DELIVERY_NOTE[@MDS_EntityType = "{entityType}" AND @MDS_id1 = "{id1}"]
```

![](/_images/doc2/Infor/BusinessContextModel_XQuery_DeliveryNote2.png)
```dn2
/DELIVERY_NOTE[@Delivery_Note_Id="{id3}"]
```

**Invoice**

![](/_images/doc2/Infor/BusinessContextModel_XQuery_Invoice.png)
```inv
/LN_SupplierInvoice[@MDS_EntityType = "{entityType}" AND @MDS_id1 = "{id1}"]
```

All these steps connect all documents from IDM to the corresponding workbench in LN, where they are also displayed. And this is how it looks in LN:

**Order Confirmation**

![](/_images/doc2/Infor/LN_Order_Order Confirmation.png)

**Delivery Note**

![](/_images/doc2/Infor/LN_Workbench Order volume_Delivery Note.png)

**Invoice**

![](/_images/doc2/Infor/LN_Workbench Accounts Payable Processing_Invoice.png)
