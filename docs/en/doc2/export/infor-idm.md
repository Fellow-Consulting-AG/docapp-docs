---
title: "Export to Infor IDM"
description: Step by Step guide how to export documents to Infor Document Management (IDM) without publishing the values in a seperate BOD.
date: "2021-10-22"
tags:
  - DOC²
  - Export
  - Infor
  - IDM
  - DOC²
---

#### Export to Infor IDM

**How to export to Infor Document Management without publishing the document values in a seperate BOD**

A step by step guide on how to export documents to Infor Document Management (IDM) without publishing the values in a seperate BOD.

## **Prerequisites:**

- An admin user für InforOS with the security roles "ION Desk Admin", "ION API Admin", "IDM Admin".
- An ION API file to create the communication between DOC² and Infor IDM. Follow the documentation here: [How to create an Infor ION file](/doc2/export/create-a-infor-ion-file/)
- A IDM document type where the documents shall be exported to.
- A IDM Mapping file which IDM uses to know which document content represents which information. You find a example of the IDM mapping file on this page: [How to create a IDM mapping file](/doc2/export/how-to-create-a-idm-mapping-file/)

Login to DOC², click on settings and select **Export**.

![](/_images/doc2/export to Infor idm/DOC2_Settings-Export.png)


Click on `+ NEW`

![](/_images/doc2/export to Infor idm/DOC2_Export-Settings-NEW.png)


Select **Infor IDM**

![](/_images/doc2/export to Infor idm/DOC2_Select Integration-Infor IDM.png)

Click on the ION Mapping File section and select the ION API file that you want to use for the communication between DOC² and IDM. If you don´t have an ION API file follow this documentation to create one: [How to create an Infor ION file](/doc2/export/create-a-infor-ion-api-file/)

For normal exports you will have to pick `CLOUD` on the left slider.
Using the right slider, you can choose if you want to export the invoice as a PDF to Infor or if you want to export the invoice in ZUGFeRD format (PDF with X-Rechnung format ZUGFeRD XML attachment).

![](/_images/doc2/export to Infor idm/Infor-IDM-PDF-cloud-ION-Mapping-file.png)
![](/_images/doc2/export to Infor idm/Infor-IDM-ZUGFeRD-cloud-ION-Mapping-file.png)

For exports using [Watchdog](/doc2/fileshare/), you will have to pick `ONPREM` on the left slider.

![](/_images/doc2/export to Infor idm/Infor-IDM-PDF-onprem-ION-Mapping-file.png)
![](/_images/doc2/export to Infor idm/Infor-IDM-ZUGFeRD-onprem-ION-Mapping-file.png)

Click on the IDM Mapping File section and choose the IDM Mapping file you want to use for the export.
You find an example of the IDM mapping file on this page: [How to create a IDM mapping file](/doc2/export/how-to-create-a-idm-mapping-file/)
![](/_images/doc2/export to Infor idm/Infor-IDM-PDF-cloud-IDM-Mapping-properties.png)
![](/_images/doc2/export to Infor idm/Infor-IDM-ZUGFeRD-cloud-IDM-Mapping-properties.png)
![](/_images/doc2/export to Infor idm/Infor-IDM-PDF-onprem-IDM-Mapping-properties.png)
![](/_images/doc2/export to Infor idm/Infor-IDM-ZUGFeRD-onprem-IDM-Mapping-properties.png)

Click `SAVE` to the save the export settings.
