---
title: "Watchdog for Windows"
description: In this documentation you will find how to configure Watchdog for Windows for easy Fileshare Import of your local documents to DOC².
date: "2022-01-28"
tags:
  - DOC²
  - Fileshare Import
  - Watchdog
  - Windows
---
---

# Watchdog for Windows

### Download the files here:
<a href="/doc2/fileshare/Watchdog.exe" download>Watchdog Download</a><br>
<a href="/doc2/fileshare/poppler.zip" download>Poppler Download</a> & [install](#install-poppler)

## Running Watchdog
Watchdog can run in [headless](#headless-watchdog) mode as a servcie and in UI mode.<br> 
The UI mode can be used to make changes to the configuration file `watchdog-config.yml`.

To start the Watchdog UI mode in a cmd window opened with admin rights, enter 
```
Watchdog.exe ui
``` 


## Folder configuration

First configure the following folders:

* Read folder → documents that should be uploaded to DOC² have to be in this folder
* Error folder → documents that ran into an error during the export are saved here
* Processed folder → successfully processed documents are stored here

To configure these folders, you must select the **Settings folder** and press `Browse` for each folder.

![](/_images/doc2/Import_Watchdog_Windows_FolderConfiguration.png)



#### Select an environment to which your documents should be exported.
  :fontawesome-solid-circle-info:{ style="color: #0F17E4" } The following options are available:

  **DOC²** → the documents will only be exported to DOC²

  ![](/_images/doc2/Import_Watchdog_Windows_General_Settings_2.png)

  **INFOR OS** → here WATCHDOG checks if there are export orders for Infor OS On-Premise issued by DOC² and then the document is exported to IDM.

  There are two more specific parameters:

  When exporting to Infor OS three document types are available.

![](/_images/doc2/Import_Watchdog_Windows_General_Settings_1.png)

#### API Key
This key can be found under the Integration settings of your DOC² account.

#### Barcode splitting
If you want to process documents in which several documents with barcodes are combined into one PDF, these are separated by the barcode using the following setting when uploading to DOC².

:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" } When enabling barcode splitting, be sure to [install Poppler](#install-poppler), otherwise Watchdog will not be able to process the documents.

![](/_images/doc2/Import_Watchdog_Windows_Barcode_Splitting.png)


## Install poppler
:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" } When enabling barcode splitting, be sure to install Poppler, otherwise Watchdog will not be able to process the documents.<br>
e.g. `C:\Users\SomeUser\Downloads\poppler-0.68.0_x86\poppler-0.68.0\bin`

<br>

## Headless Watchdog

To start Watchdog in headless mode:

1. Open a cmd window with admin priveleges
2. `cd` directory where the **Watchdog.exe** is located, e.g.```C:\Users\Administrator\Documents\watchdog```<br>
3. execute these commands: 
    1. 
      ```
      Watchdog.exe install
      ```

    2. 
      ```
      Watchdog.exe start
      ```

    3. Optional - To enable Autostart on reboot: 
        ```
        Watchdog.exe --startup delayed install
        ```

If Watchdog can't find the config file or the configuration is invalid it will start in UI mode for you to make adjustments to the Settings.
Save the changes, close the UI and run 
```
Watchdog.exe start
``` 
command and Watchdog will start in headless mode. 

## Stopping and Uninstalling Headless Watchdog
To stop the Watchdog service run: 
```
Watchdog.exe stop
``` 

To remove the Watchdog service: 
```
Watchdog.exe remove
```