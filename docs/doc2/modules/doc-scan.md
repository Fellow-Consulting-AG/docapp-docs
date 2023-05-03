---
title: "Doc Scan"
description: You will find different modules in DOC² settings.These modules are important if you like to deal with PO Matching, use the table extraction functionality or upload scans directly.
date: "2023-04-28"
tags:
  - DOC²
  - Settings
  - Modules
  - Document Processing
  - Scan
---

Already using DOC² and want to upload documents to your dashboard right after scanning? 
This is how it works:
## Download Scanner Software

Click **Scan Document** on DOC² Dashboard

![](/_images/doc2/Modules/doc-scan/DOC2-dashboard-scan-document.png)

As your scanner is not installed yet you’ll get according message

![](/_images/doc2/Modules/doc-scan/DOC2-download-scanner.png)

:fontawesome-solid-circle-info:{ style="color: #0F17E4" } <br>
Depending on which operating system you use, press the appropriate button to download.

Open the installation file and you will see the following

![](/_images/doc2/Modules/doc-scan/DOC2-welcome-to-doc2scan-installer.png)

Click on `Continue`, accept the Software License Agreement with `Agree` and continue to install the software.<br> 
:fontawesome-solid-circle-info:{ style="color: #0F17E4" } Installing this software requires 33,6 MB of space.<br> 
You can change install location before clicking `Install` in the next step.

As soon as following screen is displayed you’re almost done.

![](/_images/doc2/Modules/doc-scan/DOC2-Scan-Manager-installation-completed.png)

Open web browser to test if the app works by entering: <https://local.polydocs.io:12500/> <br>
If you see this message on the screen, you must first make some settings in your FritzBox network settings if you are using one.

![](/_images/doc2/Modules/doc-scan/DOC2-this site cant be reached.png)

All information can be found **[here](https://docs.polydocs.io/doc2/modules/doc-scan/#fritzbox-network-settings)**.

When you see this screen you are ready to click on `Doc2`.

![](/_images/doc2/Modules/doc-scan/DOC2-main-website.png)

You will be redirected to the DOC² login page where you can enter your credentials to access your dashboard.

![](/_images/doc2/Modules/doc-scan/DOC2_Login_EN.png)

All you need to do now is to activate Doc Scan in the settings under Modules.

![](/_images/doc2/Modules/doc-scan/DOC2-Settings-Modules-Doc Scan.png)

---

## FritzBox Network Settings

If you get the following error after installing and going to url <https://local.polydocs.io:12500/>, here are the reasons:<br>
* DNS resolution of private IP addresses not possible.<br>
* DNS resolution for domain names pointing to private IP addresses in the FRITZ!Box home network is not possible via FRITZ!Box. As a result, no access to server services in the FRITZ!Box home network is possible via the domain name. In this case, one of the following error messages may be displayed:<br>
"DNS timed out"<br>
"DNS request timed out"

<ins>Cause</ins><br>
For security reasons, FRITZ!Box suppresses DNS responses that point to IP addresses in its own home network. This is a security feature of the FRITZ!Box to protect against so called DNS rebinding attacks.

If you use a FritzBox you have to make the following settings in the menu of the FritzBox:

1. Click on `Home Network` in the user interface of the FRITZ!Box.

2. Click on `Network` in the `Home network` menu.

3. Click the `Network Settings` tab.

    In the `DNS rebind protection` section, enter `local.polydocs.io` in the **Host name exceptions** input field for which DNS rebind protection should not apply.<br>                                           Confirm with `Apply`.

---

## Uninstall Doc2Scan Service Manager
Run the following command to uninstall Doc2Scan Manager:
```command
sudo bash /Library/doc2scan/uninstall.sh
```


