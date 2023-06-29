---
title: "Watchdog for macOS"
description: In this documentation you will find how to configure Watchdog for macOS for easy Fileshare Import of your local documents to DocBits (Doc²).
date: "2021-11-22"
tags:
  - DocBits (Doc²)
  - Fileshare Import
  - Watchdog
  - macOS
---

# Watchdog for macOS

### Download the file here:



## Folder configuration

First configure the following folders:

* Read folder → documents that are exported to DocBits (Doc²) are uploaded here
* Error folder → documents that ran into an error during the export are saved here
* Processed folder → successfully processed documents are stored here

To configure these folders, you must select the **Settings folder** and press `Browse` for each folder

![](/_images/docbits/Import_Watchdog_Windows_FolderConfiguration.png)


## General configuration

Next, configure general parameters:

  * Environment → where you want to export the documents, the following options are available here:
    - DocBits (Doc²) → here the watchdog exports the documents only to DocBits (Doc²)
    - INFOR OS → here the watchdog checks if there are export orders for Infor OS On-Premise issued by DocBits (Doc²) and then the document is exported to IDM.
  * API key → this key can be found under Integration settings of your DocBits (Doc²) account

There are two more specific parameters:

  * When exporting to Infor OS:
    - Document types → here you have the choice between three different document types

![](/_images/docbits/Import_Watchdog_Windows_GeneralConfiguration.png)
