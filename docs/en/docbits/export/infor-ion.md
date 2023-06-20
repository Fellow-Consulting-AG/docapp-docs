---
title: "Export to Infor ION and IDM"
description: Step by Step guide how to export documents from Docbits (DOC²) to Infor Document Management (IDM) with publishing the values in a seperate Sync.CaptureDocument BOD.
icon: material/application-export
date: "2021-10-22"
tags:
  - Docbits (DOC²)
  - Export
  - Infor
  - Infor OS
  - ION
  - IDM
---

####
Export to Infor Document Management with publishing the document values in a seperate BOD

Step by Step guide how to export documents to Infor Document Management (IDM) with publishing the values in a seperate Sync.CaptureDocument BOD.

**Prerequisites:**

- An admin user für InforOS with the security roles "ION Desk Admin", "ION API Admin", "IDM Admin".
- An ION API file to create the communication between Docbits (DOC²) and Infor IDM. Follow the documentation here: [How to create an Infor ION file](/docbits/export/create-a-infor-ion-file/)
- A IDM document type where the documents shall be exported to.

#### Docbits (DOC²) steps

Login to Docbits (DOC²), click on settings and select "Export".

![This image has an empty alt attribute; its file name is image-1-1024x695.png](/_images/docbits/image-1-1024x695.png)


Settings - Export

Click on "Add integration"

![This image has an empty alt attribute; its file name is image-7-1024x751.png](/_images/docbits/image-7-1024x751.png)

Settings - Export - Add integration

Choose "Infor ION"

![](/_images/docbits/image-31-1024x342.png)

Click on the ION API File section and select the ION API file that you want to use for the communication between Docbits (DOC²) and IDM. If you don't have a ION API file follow this documentation to create one: [How to create an Infor ION file](/docbits/export/create-a-infor-ion-file/)

![](/_images/docbits/image-32-1024x347.png)

Click on the IDM Mapping file section and choose the IDM Mapping file you want to use for the export.
You find a example of the IDM mapping file on this page: [How to create a IDM mapping file](/docbits/export/how-to-create-a-idm-mapping-file/)

![](/_images/docbits/image-33-1024x344.png)

Click on the BOD Mapping file section and choose the BOD Mapping file you want to use for the export.
You find a example of the BOD mapping file on this page: [How to create a BOD mapping file](/docbits/export/how-to-create-a-bod-mapping-file/)

![](/_images/docbits/image-34-1024x343.png)

Click "Save" to the save the export setting.

#### Infor ION steps

Open "Infor ION API", select "Authorized Apps" and click on the Docbits (DOC²) application.

![](/_images/docbits/image-35.png)

Copy and store the "Client ID", this ID will be required later.

![](/_images/docbits/image-36.png)

Open "ION Desk", open the burger menu, select "Connect" and click on "Connection points"

Click on "+Add" and choose "IMS via ION API"

![](/_images/docbits/image-37.png)

Enter the name meaningful "Doc2Export" and give it a meaningful description.

Uncheck the box "Application has IMS EndPoint" and enter the "Client ID" copied from ION API.

![](/_images/docbits/image-39-1024x438.png)

Change to the "Documents" tab.

Click on the "+" icon and enter to the filter field "Sync.CaptureDocument". The list should show the correct BOD now, check the box in front of "Sync.CaptureDocument" and click "OK".

![](/_images/docbits/image-40-1024x944.png)

Click the disk icon to save the settings.

![](/_images/docbits/image-41.png)

Change to "Data Flows" and click on "+Add" and select "Document Flow".

![](/_images/docbits/image-43.png)

Enter a meaningful name and description.

Drag and drop an "Application" to the flow and name it "Doc2".

![](/_images/docbits/image-44.png)

Click on the "+" icon and select the "Doc2" application, in this case "Doc2Export" and click "OK".

![](/_images/docbits/image-45.png)

Click on the disk icon to save the new document flow.

![](/_images/docbits/image-46.png)