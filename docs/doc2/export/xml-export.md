---
title: XML Export
description: API integration provides functions and services that connect applications and processes. Here are examples of how to make API calls through api.polydocs.io.
date: "2022-10-26"
icons: material/api
tags:
  - DOC²
  - Export
  - API Call
  - api.polydocs.io
---

## XML Export with API Call via [api.polydocs.io](https://api.polydocs.io/docs).


### Authentication is the first step

**1.** Open [api.polydocs.io](https://api.polydocs.io/docs)<br>
**2.** Click on **Authorize** in the upper right corner

![Picture](/_images/doc2/admin_guides_doc2-api-authorize.png){ loading=lazy }

**3.** Enter your [API Key](/doc2/settings/integration/api-integration/) and confirm by clicking `Authorize`

![Picture](/_images/doc2/admin_guides_doc2-api-authorize_key.png){ loading=lazy }



### XML Export

This allows you to take the fields we provide to you and convert them into a format that suites your needs. Download a XSLT template <a href="/doc2/export/Template_xslt.xslt" download>here</a><br>

After completing steps **1.-3.**<br>
**4.** Scroll down to<br>

- **/xml export/get standard xml output**<br>

This endpoint allows you to convert a document into XML format.

![Picture](/_images/doc2/DOC2_API_v1 or compact.png){ loading=lazy }

Enter the doc_id and select the desired version depending on the details you want the XML file to contain. :fontawesome-solid-circle-info:{ style="color: #0F17E4" }

You can find the doc_id here:
![Picture](/_images/doc2/DOC2_API_Banana invoive File ID.png){ loading=lazy }

:fontawesome-solid-circle-info:{ style="color: #0F17E4" } You can choose between **v1** and **v1_compact**. v1 displays all information in the document including the OCR and Confidence level scores where as v1_compact displays only the most important extracted data.

- **/xml export/get transformed xml output**<br>

This endpoint allows you to enter the document ID of a document uploaded to DOC² and upload a XSLT file, configured in your preferred format. It also gives you the option of choosing between v1 and v1_compact. 

The standard XML file will then be transformed into a file formatted the same way the XLST file you uploaded was formatted.

![Picture](/_images/doc2/DOC2_API_XML Export Banana compact output.png){ loading=lazy }

- **/ml _export/get_transformed xml_ output _file**

This endpoint performs the same functions as the /xml export/get transformed xml output endpoint, but rather gives you a downloadable file of the transformed/reformatted standard XML file instead of just displaying the result. 

- **/xl export/get transformed xml output using xslt record**

This endpoint performs the same functions as the /xml export/get transformed xml output endpoint, but also allows you to add/record a specific XSLT ID so that it is not necessary for you to re-enter the same ID for every conversion.

- **/xml_export/get_transformed _xl_ output_ file using_xslt_record**

This endpoint performs the same functions as the /ml _export/get_transformed xml_ output _file endpoint, but also gives you the ability to record a specific XSLT ID as well as provide a downloadable file.

- **/xml export/xslt/list**

This endpoint retrieves a list of all uploaded XSLT files and the information associated with the files.

- **/xml export/xslt/create**

This endpoint allows you to create a record of an XSLT file so that it is not necessary to upload the same XSLT file. You can then use this XSLT ID in place of uploading the file each time you wish to format a document in that specific XSLT format.

- **/xml export/xslt/(id}**

This endpoint allows you to upload a XSLT file and, once you execute, retrieve the assigned XSLT ID for that file.

- **/xml export/xslt/{id}**

This endpoint allows you to update an existing record of an XSLT file.

- **/xl export/xslt/(id}**

This endpoint allows you to delete an existing record of a XSLT file.