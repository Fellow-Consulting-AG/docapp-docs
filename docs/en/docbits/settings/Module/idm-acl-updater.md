---
title: "IDM ACL Updater"
description: This a new feature which, every 6 hours, uses the ION-API file to connect to your Infor-IDM and check through the newest/latest documents of the IDM-document-type(s) you selected, and if they have your specified ACL-Setting right now (for example public), they change it to the ACL-Setting that you want it to (example Private).
date: "2023-05-23"
tags:
  - Docbits (DOC²)
  - Settings
  - Module
  - IDM ACL Updater
---

## What does it do?

This a feature which, every 6 hours, uses the ION-API file to connect to your Infor-IDM and check through the newest/latest documents of the IDM-document-type(s) the Docbits (DOC²) team has configured at your request, and if the document type has an incorrect ACL-Setting (for example public), it will then be changed to the ACL-Setting you want (for example private). The images below illustrate the configuration of the API performing this feature:

![Dataflow](/_images/docbits/Settings/Module/IDM:ACL Updater/image_1_data_flow.png)
![API Configuration](/_images/docbits/Settings/Module/IDM:ACL Updater/image_2_api_config_1.png)
![API Configuration](/_images/docbits/Settings/Module/IDM:ACL Updater/image_3_api_config_2.png)

## How to enable the IDM ACL Updater

To enable this feature, from the Dashboard, go to Settings.

![Settings](/_images/docbits/Settings/Module/IDM:ACL Updater/image_2_settings.png)

Navigate to Document processing → Module

![Module](/_images/docbits/Settings/Module/IDM:ACL Updater/image_3_module.png)

Once in the Module menu, you will find the slider to enable the IDM ACL Updater at the bottom of the page.

![Slider](/_images/docbits/Settings/Module/IDM:ACL Updater/image_4_enable_slider.png)

Simply click the slider so that it moves to the right to enable the feature.