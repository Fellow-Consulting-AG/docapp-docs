---
title: "LN: Export to Infor ION and IDM"
description: Step by Step guide how to export documents from DocBits (DOC²) to Infor Document Management (IDM) with LN.
date: "2021-10-22"
tags:
  - DocBits (DOC²)
  - Export
  - Infor
  - Infor OS
  - ION
  - IDM
  - LN
---

####
Export to Infor Document Management with publishing the document values in a seperate BOD

Step by Step guide how to export documents to Infor Document Management (IDM) with LN.

**Prerequisites:**

- An admin user für InforOS with the security roles "ION Desk Admin", "ION API Admin", "IDM Admin".
- An ION API file to create the communication between DocBits (DOC²) and Infor IDM. Follow the documentation here: [How to create an Infor ION file](/docbits/export/create-a-infor-ion-file/)
- A IDM document type where the documents shall be exported to.

## DocBits (DOC²) steps

1. Login to DocBits (DOC²), click on settings and select "Export".

![Settings](/_images/docbits/Export to Infor/Export to Infor ION and IDM/image_1_settings.png)
2. Click on "+ NEW"

![ADD](/_images/docbits/Export to Infor/Export to Infor ION and IDM/image_2_add.png)
3. Choose "Infor IDM + ION BOD"

![](/_images/docbits/Export to Infor/Export to Infor ION and IDM/image_3_idm_ion.png)

- Click on the ION API File section and select the ION API file that you want to use for the communication between DocBits (DOC²) and IDM. If you don't have a ION API file follow this documentation to create one: [How to create an Infor ION file](/docbits/export/create-a-infor-ion-file/)

- Click on the IDM Mapping file section and choose the IDM Mapping file you want to use for the export. You find a example of the IDM mapping file on this page: [How to create a IDM mapping file](/docbits/export/how-to-create-a-idm-mapping-file/)

- Click on the BOD Mapping file section and choose the BOD Mapping file you want to use for the export. You find a example of the BOD mapping file on this page: [How to create a BOD mapping file](/docbits/export/how-to-create-a-bod-mapping-file/)

![](/_images/docbits/Export to Infor/Export to Infor ION and IDM/image_4_mapping_files.png)
4. Click "Save" to the save the export setting.

## Infor ION steps

### Create Applications

Open "Infor ION API", select "Authorized Apps" and click on the DocBits (DOC²) application.

![](/_images/docbits/image-35.png)

Copy and store the "Client ID", this ID will be required later.

![](/_images/docbits/image-36.png)

#### DocBits (DOC²)

Open "ION Desk", open the burger menu, select "Connect" and click on "Connection points"

Click on "+Add" and choose "IMS via ION API"

![](/_images/docbits/image-37.png)

Enter a name like "Doc2Export" and give it a meaningful description.

Uncheck the box "Application has IMS EndPoint" and enter the "Client ID" copied from ION API.

![](/_images/docbits/image-39-1024x438.png)

Change to the "Documents" tab. Once you have added all the necessary documents, it should contain the following

![](/_images/docbits/Export to Infor/Exporting with LN/image_1_docbits_connectionpoint.png)

Click the disk icon to save the settings.

![](/_images/docbits/image-41.png)

#### LN

The process of creating this application for the dataflow is very similar but, instead of the documents added for DocBits, documents can vary as in this section it depends on which BODs you plan to receive/send in/to M3 so there will be variations depending on the use case. 

### LN Dataflow

Change to "Data Flows" and click on "+Add" and select "Document Flow".

![](/_images/docbits/image-43.png)

Enter a meaningful name and description.

The most simple dataflow from DocBits (DOC²) to LN will look as follows

![](/_images/docbits/Export to Infor/Exporting with LN/image_2_ln_dataflow.png)

In practical use cases, a dataflow from DocBits (DOC²) to LN will look more similar to what is shown below

![](/_images/docbits/Export to Infor/Exporting with LN/image_7_practical_dataflow.png)

The increase in branches and data is due to the amount of document types and departments you may need. This can be seen in the first mapping connection point as each point has a different document type listed which will then be taken to its unique second mapping file which has a unique LN location as each document type will be sent to a different department within the organisation. In this way, no documents are sent to a member of the organisation unnecessarily and  therefore there is more internal control.

#### DocBits (DOC²)

Drag and drop an "Application" to the flow and name it "Doc2".

![](/_images/docbits/image-44.png)

Click on the "+" icon and select the "Doc2" application, in this case "Doc2Export" and click "OK".

![](/_images/docbits/image-45.png)

#### Mapping 1

**Sync.CaptureDocument → Sync.SupplierInvoice**

The configuration for this mapping should look as follows

![](/_images/docbits/Export to Infor/Exporting with LN/image_4_ln_mapping1.png)

#### Mapping 2 

**Sync.SupplierInvoice → Load.SupplierInvoice**

The configuration for this mapping should look as follows

![](/_images/docbits/Export to Infor/Exporting with LN/image_5_ln_mapping2.png)

####  LN

This is the endpoint for the data in this dataflow as LN is the application we are using in this instance.

Here is an example of what the information stored in this connection point may look like, this can vary from user to user. It should contain the connection point you created for the application, along with the unique name you assigned it.

![](/_images/docbits/Export to Infor/Exporting with LN/image_6_ln.png)  

Once you have finished all the above configurations, click on the "Activate" button to activate the dataflow.

![](/_images/docbits/Export to Infor/Exporting with M3/image_9_activate.png) 