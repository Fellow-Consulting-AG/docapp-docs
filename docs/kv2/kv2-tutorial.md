---
title: "KV² Tutorial"
description: This is a step by step guide how to use our KV² Plugin after you installed and configured it. You will find all steps in Ephesoft to train the correct values.
date: "2021-07-02"
tags:
  - KV²
  - Tutorial
  - Plugin
  - Ephesoft
---

### Prerequisites

To work with this tutorial you have to complete the [Installation & Configuration](/kv2/installation/) sections of this Plugin.

* * *

### How To Use KV² Plugin

##### **Step 1: Log-in**

- Log into the Ephesoft Transact Software with username and password

![](/_images/doc2/login1Unbenannt.png)

![](/_images/doc2/login2Unbenannt.png)

- After logging in, you will see a menu with two modules: Administrator & Operator with their defined functions:

<table><tbody><tr><td><strong>Administrator</strong></td><td><strong>Operator</strong></td></tr><tr><td>Batch Class Management</td><td>Batch List</td></tr><tr><td>Batch Instance Management</td><td>Review Validate</td></tr><tr><td>Folder Management</td><td>Web Scanner</td></tr><tr><td>System Configuration</td><td></td></tr><tr><td>Report</td><td></td></tr></tbody></table>

#### **Step 2: Interface application of the FellowKV2 Plugin**

- Upload your documents through the Operator Module in “Upload Batch”:  
    

![](/_images/doc2/step1_1.png)

- Start the batch with the according batch class.

![](/_images/doc2/startbatch.png)

- Wait in the Administrator Module in “Batch Instance Management” for the batch to be processed and ready for validation.

![](/_images/doc2/Process3Unbenannt.png)

- Select your Batch and in the list and click to open the batch in order to validate the header and footer fields:

![](/_images/doc2/4-open-batchUnbenannt.png)

- You will then be redirected to a new window for validation. The document is displayed on the right side, the validation screen on the left. Here you can can check all the extracted fields and add/correct the values if necessary.  
    

![](/_images/doc2/validationScreen.png)

<<<<<<< Updated upstream
- Go through all the fields by clicking the "Tab" button or with your mouse and check the values. In case you there is a missing or incorrect value, you have 4 options:
    - Click on the particular field on the validation screen, then move your mouse over the document on the right and select the respective value by double click on it. The selected value will be marked yellow on the document and will appear in the validation field on the left (preferred - as this way you train on which position on a certain invoice you find the respective values).
    - Click on the particular field on the validation screen, then move your mouse over the document on the right and select the respective value by right-clicking with your mouse, hold it while selecting the full value (it will be marked yellow) and confirm by clicking on the right tab again. The selected value will be marked yellow on the document and will appear in the validation field on the left (preferred - as this way you train on which position on a certain invoice you find the respective values)
=======
- Go through all the fields by clicking the "Tab" button or with your mouse and check the values. In case you notice a missing or wrong value, you have 3 options to set the correct value:
    - click into the particular field in the validation screen, then move your mouse over the document on the right and select the respective value by double click on it. The selected value will be marked yellow on the document and will appear in the validation field on the left (preferred - as this way you train on which position on a certain invoice you find the respective values)
    - click into the particular field in the validation screen, then move your mouse over the document on the right and select the respective value by click right mouse, hold it while select the full value (it will be marked yellow) and confirm by click on right tab again. The selected value will be marked yellow on the document and will appear in the validation field on the left (preferred - as this way you train on which position on a certain invoice you find the respective values)
>>>>>>> Stashed changes
    - Type the value manually to the validation cell.
    - If a value is detected wrong or incomplete, please click in respective cell, clear the value and select the correct one in the document as explained above.

For fields you have corrected in the first run, you should see the value set correct and highlighted yellow on the document for the next invoice you run for this vendor.

- Now just add all the fields with the accurate data and validate the invoice in order for it to be exported.

![](/_images/doc2/validate1Unbenannt.png)

![](/_images/doc2/validate2Unbenannt.png)

![](/_images/doc2/validate3Unbenannt.png)

With this process you are not only validating your document but also training the plugin. With a one-time human assistance validating and exporting the documents, new extraction rules are created. For the next run of that type of document no adaptation or configuration of the batch class is needed and the plugin will recognize values which have been missing in the first run.

## Usage of Fellows Feedback and Support Function

KV² Plugin comes with an integrated Feedback Function where you can send us Support to each Document Validation.  
The Feedback Function can be found in tab #5 of the Ephesoft Validation UI (it is usually the last tab).

![](/_images/doc2/Bildschirmfoto-2021-07-12-um-17.01.16-2-1024x477.png)

If you want to send us some feedback you just need to move to this tab and fill out the three fields on this tab:

- **Feedback Type** -> here you can choose from list below.  
    _NOTE that support tickets will be created only if Feedback types is different than "Perfect"_
    - \--NONE--
    - Perfect
    - Good
    - Bad
    - Nothing is working
- **Reporter Email Address** \-> this is your email address which we use for our reply
- **Feedback** -> this is a textfield where you can send us your detail feedback, like which value showed a problem or was not detected correct

If fields are filled the feedback is created during the validation process and sent directly to our Support Tool and we can work on the case.

![](/_images/doc2/Bildschirmfoto-2021-07-12-um-17.01.16-1024x477.png)
