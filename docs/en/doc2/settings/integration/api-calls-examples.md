---
title: API Calls for Document Upload and Status Check | Polydocs
description: Learn how to make API calls for document upload and status check using api.polydocs.io. Follow the step-by-step guide to authenticate and upload documents with metadata.
date: "2022-10-27"
icons: material/api
tags:
  - DOC²
  - Settings
  - API Calls
  - api.polydocs.io
---

<div class='video-container'>

#### API Calls for Document Upload and Status Check

API integration provides functions and services that connect applications and processes. In this guide, we will show you how to make API calls through api.polydocs.io for document upload and status check.

## Authentication

To make API calls, authentication is the first step. Follow the steps below to authenticate:

1. Open [api.polydocs.io](https://api.polydocs.io/docs).
2. Click on **Authorize** in the upper right corner.
3. Enter your [API Key](/doc2/settings/integration/api-integration/) and confirm by clicking `Authorize`.

![Authorize API Key](/_images/doc2/Settings/Integration/API calls examples/1-admin_guides_doc2-api-authorize.png){ loading=lazy }

## Upload Document

To upload a document, follow the steps below:

1. After authentication, scroll down to the **POST /document/process** endpoint.
2. Open the tab and click on `Try it out` in the upper right corner.
3. Enter the following value in the `source` field: `email:{Pattern name}`.
4. Select the file you want to upload and click `Execute`.

Your document will be uploaded to your dashboard with the rules you set in [DOC²](https://app.polydocs.io/settings/classify-extract).

![Classification Rules](/_images/doc2/Settings/Integration/API calls examples/5-classification_rules.png){ loading=lazy }
![Uploaded Document on Dashboard](/_images/doc2/Settings/Integration/API calls examples/6-dashboard_mango.png){ loading=lazy }

## Document Status Check

To check the status of a document, follow the steps below:

1. After authentication, scroll down to the **GET /document/status** endpoint.
2. Open the tab and click on `Try it out` in the upper right corner.
3. Enter the document ID in the `doc-id` field. You can find the document ID when you open the document on the dashboard. This is the last part of the URL when the document is open.

![Document ID](/_images/doc2/Settings/Integration/API calls examples/8-DOC2_API_GET_Document-Status_doc_id.png){ loading=lazy }

You will receive the following response:

![Document Status Response](/_images/doc2/Settings/Integration/API calls examples/9-DOC2_API_GET_Document-Status_Response.png){ loading=lazy }

If the status is "Ready For Validation," it means that the user can check the document.

## Upload Document with Metadata

To upload a document with metadata, follow the steps below:

1. After authentication, scroll down to one of these endpoints: `/document/process_documents`, `/document/process`, or `/document/process_base64`.
2. Open the tab and click on `Try it out` in the upper right corner.
3. Enter the metadata in the `metadata` field. The metadata needs to be in a valid JSON format. An example of a metadata entry would be: `{"custom-key": "the custom value", "custom_doc_id": "8a5cf33b-c923-4879-96ca-94d69965d508"}`.
4. Select a file to upload.
5. Click `Execute`.
6. Wait for the response. If the metadata field is not a valid JSON, an error message will appear. If "success": true, then your document will be uploaded to your dashboard with the rules you set in [DOC²](https://app.polydocs.io/settings/classify-extract).

By following these simple steps, you can easily make API calls for document upload and status check using api.polydocs.io. For more information, visit [Polydocs](https://polydocs.io/).
