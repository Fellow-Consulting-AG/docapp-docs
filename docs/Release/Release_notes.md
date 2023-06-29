---
title: "Changelog"
description: Change log for Polydocs Apps
tags:
  - Change Log
---


:fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**

:fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**

:fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**


# Release Notes

## 2.48

- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Classification model consistency
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: The cloud loading sign is inconsistent on the Dashboard

- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: When the date is wrong - make the field red 
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Add a key combo to refresh the dashboard 
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Clone Sub Doc Type 
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Future Changes: Add Fuzzy fields in field settings for standard fields 
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Filter reset 
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Filter goes away after uploading a document
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Email notification for status "export error"
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Filter reset 
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Add a warning about why email notifications cannot be saved

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Buttons for Email Import IMAP/POP3 are gone 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Classification model not working properly 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Upload Error 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Fuzzy field settings are missing from the field settings 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Add Fuzzy fields in field settings  
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Sub Organisation creation is wrong —> Sub-organization named DeliveryNotes can be created for different organizations 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Table: Not able to save the rules for the table 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Model training not working 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Documents uploaded via the API are not showing on the dashboard
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Change the popup message behind the exclamation mark 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Buttons on the Dashboard have the wrong popup message 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Missing German Translation 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Grey line is longer than the field 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Change this label  
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: UI: Master Data Lookup - Change upper case letters to lower case letters 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: The bin button does not work anymore 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: UI: ADD USER Button is gone 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: The language of the document types in the dropdown of the validation screen does not change correctly to the selected language 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Wrong translation in popup "Reassign Fields Group" 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Error displaying Tax Details - Old View 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: The calculator icon is not being displayed attached document 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: German translation popup message fuzzy icon in field settings 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Correct alignment of the AI Indicator 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Column Order can not change 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Dashboard last page deleting all documents doesn't set you on a different page 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: IMAP Email import - not all attachments got fetched 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: E-Mail configuration with OAuth2 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Suborg add user - no users show up 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Esc close popup 

## 2.29

- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Fields can be selected by click or tab, extracted area will be highlighted on image
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Extraction through model training
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: If document subtypes are created, only these can be selected during reclassification
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Implementation of group shortcut keys can be defined by admin. After this is done, when the user presses the defined shortcut key on the validation screen, it jumps to the position and the PDF becomes visible at that position.
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Adjustment of the coordinates in the layout
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Tool tip placed on dashboard so that user can see complete length of filename on hover of the text as column widths cannot be adjusted
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: for single digits and empty fields on the document by updating the number model and adding empty fields in training
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Various UI improvements
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Filter on the dashboard to filter documents by type. It is only possible to filter for active document types on the dashboard
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Fields can be validated/confirmed by pressing the Enter key (instead of clicking the tick) and this will take you directly to the next field marked in red that requires validation.
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: only numbers can be entered to field `TOTAL AMOUNT`
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Implementation of a date field to correctly validate the date field of a document
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Secure documents can also be processed
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Table extraction - grouping of columns
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Table extraction - rules can only be saved, if columns are properly mapped
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Table extraction - implementation of table selection popup on column select
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Customization for specific formats of an invoice number (combination on numbers, letters and special characters
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Fuzzy fields visible in field settings
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: The default value for OCR quality has been set to 75 so that not every imported document runs into errors. How to handle documents that do not meet this quality can be defined separately and individually
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Document Type - Field settings: Individual fields can be moved to a newly created or other existing group
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: It is possible to delete an incorrectly created field for a sub-doctype
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: ZUGFeRD export only allowed for invoices

- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Document type "Order forms" including sketches, checkboxes and tables - this new document type will be available upon request
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Creation of a workflow for order documents where multiple order options have been selected. All these documents can only view but can not be edited
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Files containing multiple document types are classified as a separate type, can be opened and reclassified
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Extraction of checkboxes
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: If you have a list with the data extracted from the order, of which each order criterion has its own code, the article number can be created from this using appropriate scripts
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Implementation of a `REJECT` button. You will then be redirected to the dashboard and see the corresponding status
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: layout manager -> the documentation for this will be available soon
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: If the layout builder is turned on in the settings, you will see the new layout on the validation screen
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Implementation of button that will validate all fields of a section
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Implementation of a button that enables the restart with the correct classification via a popup
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: List of values for currency will be set to ISO Currency and checkbox for `enforce list of values` will be checked. Validation rule will show error if values inside field does not match value from list -> the documentation for this will be available soon
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Model Training Schedule Counter for document types - `NEXT MODEL TRAINING UPDATE`
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: `HOME`Button and Polydocs Logo have both same functionality back to dashboard
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Copy button on sub doc type settings. It will copy all the fields, layout etc of that sub doc type
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Upload TIF Support
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Implementation of a help center link that redirects to the support tool if a URL cannot be accessed while logged in (<https://app.polydocs.io/not_found>)  

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: wrong classification of certain documents
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: extraction of wrong values
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Translation errors
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Error with saving cache. Filters are now saved by user
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: If a user has sub-organizations and has not selected any yet, the first organization is displayed by default in the profile view in the upper right corner. Once the user is assigned to the suborganizations, they will be displayed in the user profile


## 2.00

- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Overwrite Class by user. If the classification is incorrect, the user can now manually select the class.

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Link to Help Page for Email notifications 
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Link to Help Page for Company information 

## 1.19

- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Document assigne should be able to perform action on the document even if he/she does not have permissions
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Active organization is displayed in the upper right corner so you know which org or suborg you are currently in
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Various UI improvements
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Adding the document status `Pending Second Approval` in the approval settings and for the email notification

- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Functionality to split a document into different pages and delete specific pages
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: DESKEW - If user activates this option the quality of the document will automatically optimized. The rotation of the scan will be centered and the DPI quality will be automatically changed to the minimum of 300 DPI
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Switch organisation via profile popup
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Notification of version update in the app after deployment 

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Upload is not working for document with 100 pages
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Table extraction and training errors
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Correction SSO Url
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: E-Mail notification not working

## 1.18


- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Implementation of Document Sub Types
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: PO Matching - Quantity match delivery note
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: PO Matching - Hiding empty columns
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Visibility of Document Sub Types on dashboard
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Fields required for validation on the document details screen are always shown marked with red asterisk
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: numerous changes to the UI: alignment of buttons -size and placement, translations, new upload popup, a check box to select the entire column in the document type Permissions view for groups, Keyboard shortcuts
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Dashboard (list) filters based on Groups & Roles

- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: [E-Mail notifications for Document Type and Status](/docbits/settings/email-notification/)

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Delete WF access possible again

## 1.17

- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Handling of rotated documents
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: PO Sort - The order on purchase order table must be exactly as in Infor LN
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: UI
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** TE: Adding a button to send additional description to trash<br> - find example [here](/docbits/table-extraction/advanced-settings/#move-extra-rows-to)

- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: [Training vs Correction Mode](/docbits/table-extraction/training-of-table-extraction/#training-vs-correction-mode)

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Date issue on Dashboard

## 1.16

- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: DocBits (DOC²) - functionality document details: Save Rules & Save and close
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: DocBits (DOC²) - Adding possibility to delete a not standard document type
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: DocBits (DOC²) - email import IMAP/SSL
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: DocBits (DOC²) - Error message when other file type than pdf gets uploaded

- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: [Insight²](/insight2/)
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: DocBits (DOC²) - Status Pending Approval on dashboard
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: DocBits (DOC²) - Symbol for locked documents/instances on dashboard
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: DocBits (DOC²) - Ability to select multiple documents on the dashboard to restart and/or delete at the same time
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: DocBits (DOC²) - Document lock:
     - Unlock Option for Admin user if doc is already being viewed by someone else
     - Reload Option if document is modified before user can save
     - For External Application, this feature will be disabled
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: DocBits (DOC²) - Login Mobil Responsive
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Display how long the free trial access is running

## 1.15

- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Customization of permissions for users - User ist not able to switch products on and off - only Admin can
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Adding new domain for Workflow² / Moving the domain for Workflow² from Modules to Apps
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: to UI (Translations, Colours and position of Icons, Buttons, Cloud while uploading documents)
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: for e-mail notifications and e-mail verification
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Clarification FORCE OCR functionality when headers of tables are not being extracted (instead numbers got extracted)
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: in User registration (verify Email, admin/user,Reset/Forgot Password)
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: for email notifications - registration, Add user, send confirmation email again
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Building functionality with safari browser
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: embed SSL certificate
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: TE²: cosmetic repairs UI
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Length of password
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Implemenation of HELP Links to documentation in DocBits (DOC²)
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: in training specific fields
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: confirm e-mail and password with Enter when logging in
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Changed button to activate/deactivate WF² from Settings Modules  to APPS
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Changed dropdown 'Origin' on Field validation page to 'Amount & Date Format'
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: in classifying the correct document type
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: redirect to dashboard instead of success page after export
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**:  TE² - select new locale for table_train_v3
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Button to enable or disable export configuration
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Confirmation Box for all delete buttons
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT**: Updated structure to handle multiple OCRs


- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Invalid Authorization Code when login
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: errors on displaying PO Matching Screen
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: errors uploading documents
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Lack of access to the field settings
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Document Approval - Invalid Document
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Error while uploading documents
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: ZUGFeRD Export - Pdf with xml attachment
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: issues with restarted documents got stuck on status restarted
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: TE - Missing Training Mode Button
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: error on validation screen after adjusting field settings for ZUGFeRD doctype invoice
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: redirecting document restarted on third page to first page of all uploaded documents
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: fields show up empty even though data is recognized


- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Added Link to Changelog
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Login - Implementation of language switch
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Added [SugarCRM](/workflow/integrations/nodes/workflow-nodes-base.sugarcrm/) Node Icon to Workflow²
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Warning before turning off/deleting Workflow - manual input required
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Broken pages: Implementation of solution using provided normalized coordinates by api
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Link to Apps when using Workflow²
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Login with LinkedIn
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Login with google
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Login with Microsoft
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Email notification when uploaded/imported documents are Ready For Validation can be enabled/disabled in Settings/Email Notification
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Page division of one pdf by barcode
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: General Settings for documents
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE**: Implementation of Workflow Nodes for DocBits (DOC²) (assign employee, extract invoice, status trigger)


## 1.14

- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Table Column Sort for PO Line Table as Done in TEv3
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** TE² V2 STAGE - Ungroup button "hidden"
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Watcher exported document should be opened in exported/finished mode
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Remove delete rules button from the field validation screen
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Correct translation for NOCOLUMNSFOUND for es-es and fr
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Only 10 pages of a PDF are displayed
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Allow more than 10 pages in PDF in DocBits (DOC²)
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** PO image component and its functionality
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** languages drop down is not appearing
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Total is trainded wrong
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Number value Formatting
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Table - Quantity bug
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** More table extraction settings
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Table Train - Error in Group mapping needs to be set again
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** export configuration update
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** zammad customer is ticket autor
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Advance Settings on Table extraction view
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Supplierer Match not working


- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Header line disappearing when activating training mode in TE2 (via Ephesoft)
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: TE - Calculation details are not extracted
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED**: Extracted columns don't show on page 2
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** TE - Table is not extracted correctly
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Document Export table data
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Click on cancel changes the language
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Issue with Restore extracted columns
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** TE V3 Error when we test with Swiss Format
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** TE V3 Row area keeps changing
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** TE Can't find the Table
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Table Extraction Error
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Number are not extracted all
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Auftragsbestätigung gets to Rechnung
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** After addition of two new fields, the existing tests are breaking
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** DocBits (DOC²) TableExtraction, can't delete a columns
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Supplier: IDG, DocBits (DOC²) doesn't work but TE² does?!
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Amount Formatting Issues
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Button Visibility issue on Some invoice
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Checkbox extraction not working correctly
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** The document fields and table is not mapped which was already exported
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** [Extraction View] Mapped Columns
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Calc is wrong


- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Column selection should not be enable after selecting the tick
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Search PO Matching can we use alike
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Table data editable and show errors without   having to enable table training mode
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** No mapping on hide/show for amount fields
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** trash icon on field validation and delete rules button
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Add Training mode flag for all api calls on TE3
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Set istabletraining_doc attribute to true when sending call from table training page
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Table training
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** all reformat api call send difference of format_options
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Ability to make line item table from PO Table
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** AI Indicator button for training mode
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Translation on Stage missing: "Auftragsdaten"
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Overlay for Custom Color
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Show number by fields
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Delete a Custom Table Column
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** table Extraction new flow implementation
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** KOMISSION (NACHNAME, VORNAME) / MAßNUMMER
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** ZUGFeRD Export UI
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** PO table sort
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Document restart alert if it takes more than 5 minutes
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Keystrokes Hints Tooltip
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** DocBits (DOC²) Export Flow²
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** PO - Help
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** " Full " row should show if all other fields are empty
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Setting - Master Data Validation
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** PEPPOL BIS Billing 3.0
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Option to switch table extraction version
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Auftrag - Accept / Recject PO Update
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Kommission
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Infor Table Export
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Save dashboard filters and selected language Unless user clear it
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Custom Field Label and Fuzzy
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Doc2API dashboard API Test
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Basic UI Test for Doc2Landing
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Table Export Column Mappings and Formatted Data


## 1.13

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Rules are not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Button delete rule is not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** AI Indicator update counter
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** New OCR 13.3.0
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** DocBits (DOC²) TE V3: Save rules doesn't work
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** DocBits (DOC²) TE V3: What is being extracted? Weird & Wrong data
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Button make PO auto matching
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Exporting a document, if you re-open the file, the layout is standard
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Fields that are marked red prevent exporting
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Artikelnummer ist not calculated automatically when pressing the +/- button
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Save data before redirect to PO Page from Field Validation and Table Extraction
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Restore Extracted columns on a button click
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Mapping Columns Dropdown in Alphabetical Order
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Delete and Save Rule button
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Document Form - Export cannot be triggered
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Doc2app Translation - Pending
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** No column mapping option for "Item Number"
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Document Caching Issue after doc is deleted
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Add 3 more fields in in the advanced setting and also in response
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Overlay color issue
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** TE Columns remapping not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Row selection is not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Table Extraction V3 Cache issue
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Key or Value can not be empty
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** TE Module settings aren't saved
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** cE and Cf fields switched
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Document Checkboxes aren't working
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** colors will be populated based on the closest match to the already defined colors list
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Checkbox Paar is not correct
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Account search for Company Order based on the Customer Number
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** PO The Header of both tables are always german
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Invoice Number at Delivery Note doc type - change to Order Number
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Title in PO is wrong - Should be based on the doc type
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** f-key is select the Search but it types f as well
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** The font size of the Restore Defaults is too small, need to increase on Field Settings screen
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Placeholder for calc fields
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Rechtschreibfehler bei Lieferschein fix
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Extra space between additional amount fields
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** highlight group column
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Add PO ICON in Dashboard
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Documentation for Table Extraction
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Calc was not trained after 2 times exporting
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Mapping removed but still there
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Table training page in Doc2
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Dashboard List update to sort the Columns
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** MWST - make field green
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Move error message Popup
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Issue with column selection - looses selection
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** TE3 column selection near the edge is difficult
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Dashboard Pagination Issue
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** table data edit mode -> column selected but no indication on table which row is selected
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** gettexttable column background color remain purple on firefox
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Click on column send call for gettexttable without selection
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Error on upload we add unit
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Double Click TE to extract
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Checkbox export description - Infor ( Cloud or OnPremise )
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Selecting Images should only be possible with edit
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Extra Button when PO Matching is enabled
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** All customer Invoices Error out
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Option to refresh user settings in Account Settings
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** clean image required to be used in html
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** PO Image panel improvements
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Artikelnummer erfassen
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** doc2app table extraction page for ephesoft and others
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** selected area edit should not be enable on column mode
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Table Train for TE²
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** different url for image based on source of the image in detail view response
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** click on column should also open the mapping column in extraction view
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** quotation mark in amount swiss invoice support
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Customers documents are not finished automatic
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Form from Company
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** PO - Matching
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Document Classification Change
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** API Endpoint to manage organisation preferences
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Group by show object object instead of proper line item
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Calc MwSt.
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Free Tax is mapped wrong

## 1.10

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Add browser support for Safari
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Option to refresh user settings in Account Settings
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Missing link to IDM

## 1.9

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** edit export config is not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Doc2Landing - No Back by Table
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Add the Address in the fuzzy DB
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Fuzzy Error - Auftrag not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Lieferschein is shown as Invoice in the dashboard
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Calc Fields Optional Due Date
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Button for auto Detecting Tables

## 1.8

- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Can not check config files or download here
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** WatchDog - Logik Error Fix
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** edit export config is not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Dutch Invoice extraction isn't working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Belgium Invoice extraction isn't working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** French Invoice extraction isn't working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Zoom + Column is not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Column removal not possible
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Order Confirmation Table not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** missing translation on dashboard
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** resize handlers visible not resizing the selected area
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Deleted Table Column can be mapped
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** TE column change doesn't save the changes
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** DocBits (DOC²) - Flow² Export Setting is not open
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Table train zoom in/out pdf
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Table Train field draw click instead click hold
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Dashboard - DocType is not Translated
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Console Errors are shown when logged in successfully
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Selected currency: € finishing not possible
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** [TableExtractionView] Resize selected areas
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** doc2 validation: navigate with keyboard
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Dashboard status - grid view
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** increase font of tooltip
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Tooltip for the Format for Amount + Date
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** origin dropdown sometimes dont show options
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Upload File Drag & Drop works select is not working
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Total Discount Training
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Draw Columns and change the size - the columns are lost
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** DocBits (DOC²) Change Table Size is not working
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** multiple selected area draw
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Line item mapping resets when switch to field validation screen
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** DocBits (DOC²) - > Export to Flow²
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** dynamic validation screen layout
- :fontawesome-solid-thumbs-up:{ style="color: #03900c" }  **NEW FEATURE** Hide Doctype option
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Title of the page is wrong in Settings > PO Module
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Only Admins should have access to settings
- :fontawesome-solid-award:{ style="color: #eee20e" } **IMPROVEMENT** Design Changes on Extraction view
- :fontawesome-solid-bug-slash:{ style="color: #EE0F0F" } **FIXED** Multipage Table extract not working







