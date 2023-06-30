---
title: "Doc Scan"
description: This module feature allows you to assign users and/or groups with the ability to approve a document before it can be exported.
date: "2023-05-23"
tags:
  - DocBits (DOC²)
  - Settings
  - Module
  - Doc Scan
---

Already using DOC² and want to upload documents to your dashboard right after scanning? This is how it works:

## Download Scanner Software

Click Scan Document on DOC² Dashboard

![Dashboard](/_images/docbits/Settings/Module/Doc Scan/Image_1_DOC2-dashboard-scan-document.png)

As your scanner is not installed yet, you’ll get the following message

![Download Scanner Message](/_images/docbits/Settings/Module/Doc Scan/Image_2_doc_scan_installer.png)

:fontawesome-solid-circle-info:{ style="color: #0F17E4" }
Depending on which operating system you use, press the appropriate button to download.

Open the installation file and you will see the following

![Installer](/_images/docbits/Settings/Module/Doc Scan/Image_3_installer_2.png)

Click on `Continue`, accept the Software License Agreement with `Agree` and continue to install the software.

:fontawesome-solid-circle-info:{ style="color: #0F17E4" }Installing this software requires 33,6 MB of space.
You can change the install location before clicking `Install` in the next step.

 As soon as following screen is displayed you’re almost done.

![Installer](/_images/docbits/Settings/Module/Doc Scan/Image_4_DOC2-Scan-Manager-installation-completed.png)

Open web browser to test if the app works by entering: https://local.polydocs.io:12500/
If you see this message on the screen, you must first configure some settings in your FritzBox network settings if you are using one.

![Browser](/_images/docbits/Settings/Module/Doc Scan/Image_5_fritzbox.png)

When you see this screen you are ready to click on Doc².

![HomePage](/_images/docbits/Settings/Module/Doc Scan/Image_6_homepage.png)

You will be redirected to the DocBits (DOC²) login page where you can enter your credentials to access your dashboard.

![Login](/_images/docbits/Settings/Module/Doc Scan/image_7_docbits_login.png)

All you have to do now is activate Doc Scan in the settings under Modules.

![Settings](/_images/docbits/Settings/Module/Doc Scan/Image_8_Settings-Modules-Doc Scan.png)

## FritzBox network settings

If you get the following error after installing and calling up the url https://local.polydocs.io:12500/
, here are the reasons:
- DNS resolution of private IP addresses not possible.
- DNS resolution for domain names that refer to private IP addresses in the FRITZ!Box home network is not possible via the FRITZ!Box. This means that server services in the FRITZ!Box home network cannot be accessed via the domain name. 

You may see one of the following error messages:
"DNS timed out"
"DNS request timed out"

*Caused*

For security reasons, the FRITZ!Box suppresses DNS responses that refer to IP addresses in your own home network. This is a security feature of the FRITZ!Box to protect against so-called DNS rebinding attacks.

If you use a FritzBox, you must first make the following settings in the FritzBox menu:

1. In the FRITZ!Box user interface, click on `Heimnetz`.
2. `Heimnetz` Click in the menu `Netzwerk`.
3. Click on the tab `Netzwerkeinstellungen`.

In the Hostname exceptions `DNS-Rebind-Schutz section`, enter local.polydocs.io for which DNS rebind protection should not apply. Confirm with .
`Übernehmen`

## Uninstall Doc2Scan Service Manager

Run the following command to uninstall Doc2Scan Manager:


     sudo bash /Library/doc2scan/uninstall.sh


## Scanner Compatability

Legend:

- Yes - device works perfectly
- No - protocol not supported by device
- ? - device works with sane-airscan, but protocol is not reported by user
- Space - author has no information on this mode/device combination

Definition:

- eSCL stands for Airscan is a SANE WebScan frontend that supports Apple's AirScan protocol. The scanners are automatically detected and published via mDNS.

- WSD stands for "Web Services on Devices" and is a network communication protocol used for printer discovery and management over a local area network. In WSD mode, printers can be automatically discovered and added to a computer system without requiring manual configuration or installing additional printer drivers. It enables easy setup and printing to compatible printers over a network. WSD mode is commonly used in Windows operating systems to discover and connect printers on the network.

**Device**|**eSCL mode**|**WSD mode**
-----|-----|-----
Brother ADS-2700W|No|Yes
Brother DCP-7055W|No|Yes
Brother DCP-9020CDW|No|Yes
Brother DCP-J552DW|No|Yes
Brother DCP-L2540DW|No|Yes
Brother DCP-L2550DN / DCP-L2550DW|Yes| 
Brother HL-L2380DW series|No|Yes
Brother HL-L2395DW series|Yes| 
Brother MFC-7360N|No|Yes
Brother MFC-8710DW|No|Yes
Brother MFC-J1012DW|Yes| 
Brother MFC-J1300DW|Yes| 
Brother MFC-J4410DW|No|Yes
Brother MFC-J4620DW|No|Yes
Brother MFC-J485DW|Yes| 
Brother MFC-J625DW|No|Yes
Brother MFC-L2700DW|No|Yes
Brother MFC-L2710DW|Yes|Yes
Brother MFC-L2720DW|No|Yes
Brother MFC-L2750DW|Yes|Yes
Canon D570|Yes| 
Canon G600 series|Yes| 
Canon imageCLASS MF642C/643C/644C|Yes| 
Canon imageCLASS MF743cdw|Yes1| 
Canon imageRUNNER 2625/2630|Yes|Yes
Canon imageRUNNER ADVANCE 4545/4551|Yes|Yes
Canon imageRUNNER ADV C5550/5560|Yes| 
Canon imageRUNNER C3120L|Yes|Yes
Canon i-SENSYS MF4780w|No|Yes
Canon i-SENSYS MF641C|No|Yes
Canon LiDE 300|Yes| 
Canon LiDE 400|Yes| 
Canon MB5100 series|Yes| 
Canon MB5400 series|Yes|Yes
Canon MF110/910|Yes| 
Canon MF240 Series|No|Yes
Canon MF260 Series|Yes|Yes
Canon MF410 Series|Yes|Yes
Canon MF440 Series|Yes|Yes
Canon MF645Cx|Yes| 
Canon MF745C/746C|Yes|Yes
Canon MG5300 series|No|Yes
Canon PIXMA G3000 series|No|Yes
Canon PIXMA MG3600 series|Yes| 
Canon PIXMA MG5500 Series|No|Yes
Canon PIXMA MG7700 Series|Yes| 
Canon PIXMA TS5000 Series|Yes| 
Canon PIXMA TS 9550 Series|Yes| 
Canon TR4529 (PIXMA TR4500 Series)|Yes|Yes
Canon TR7500 Series|No|Yes
Canon TR8600 Scanner|Yes| 
Canon TS 3100|Yes| 
Canon TS 3300|Yes| 
Canon TS 3400|Yes| 
Canon TS 6151|Yes| 
Canon TS 6200 series|Yes|Yes
Canon TS 6400 series|Yes| 
Canon TS 8230 series|No|Yes
Dell C1765nfw Color MFP|No|Yes
Dell C2665dnf Color Laser Printer|No|Yes
Dell C3765dnf Color MFP|No|Yes
EPSON ET-2710 Series|No|Yes
EPSON ET-2750 Series|Yes| 
EPSON ET-2760 Series|Yes| 
EPSON ET-2810 Series|No|Yes
EPSON ET-2850 Series|Yes| 
EPSON ET-3750 Series|Yes| 
EPSON ET-4850 Series|Yes| 
EPSON ET-M2170 Series|Yes| 
EPSON Stylus SX535WD|No|Yes
EPSON WF-7710 Series|No|Yes
EPSON XP-2100 Series|No|Yes
EPSON XP-340 Series|Yes| 
EPSON XP-442 445 Series|Yes| 
EPSON XP-5100 Series|Yes| 
EPSON XP-6100 Series|Yes| 
EPSON XP-7100 Series|Yes| 
EPSON XP-8600 Series|Yes| 
HP Color Laserjet MFP m178-m181|Yes| 
HP Color LaserJet MFP M182nw|Yes| 
HP Color LaserJet MFP M281fdw|Yes| 
HP Color LaserJet MFP M283fdw|Yes| 
HP Color LaserJet MFP M477fdw|Yes|Yes
HP Color LaserJet Pro M478f-9f|Yes| 
HP Color LaserJet Pro MFP M277dw|Yes| 
HP DeskJet 2540|Yes| 
HP DeskJet 2600 series|Yes| 
HP DeskJet 2700 series|Yes| 
HP DeskJet 3700 series|Yes| 
HP DeskJet 5000 series|Yes| 
HP DeskJet 5200 series|Yes| 
HP ENVY 4500|Yes| 
HP ENVY 5055 series|Yes| 
HP ENVY 5530 series|Yes| 
HP ENVY 5540|Yes| 
HP ENVY 5640|Yes| 
HP ENVY Photo 6200 series|Yes| 
HP ENVY Photo 7800 series|Yes| 
HP ENVY Pro 6400 series|Yes| 
HP LaserJet 200 colorMFP M276n|No|Yes
HP LaserJet MFP E62655|Yes| 
HP LaserJet MFP M130fw|No|Yes
HP LaserJet MFP M227sdn|Yes| 
HP LaserJet MFP M426dw|Yes| 
HP LaserJet MFP M630|Yes| 
HP LaserJet Pro M28a|Yes3| 
HP LaserJet Pro M28w|Yes|Yes
HP LaserJet Pro M329|Yes9| 
HP LaserJet Pro MFP 148fdw|Yes| 
HP LaserJet Pro MFP M125 series|No|Yes
HP LaserJet Pro MFP M225dn|No|Yes
HP LaserJet Pro MFP M428dw|Yes| 
HP LaserJet Pro MFP M521 series|No|Yes
HP Laser MFP 131 133 135-138|Yes| 
HP Neverstop Laser MFP 1202nw|Yes| 
HP OfficeJet 3830 series|Yes| 
HP Officejet 4630|Yes| 
HP Officejet Pro 6970|Yes| 
HP OfficeJet Pro 6978|Yes| 
HP OfficeJet Pro 7740|Yes|No
HP OfficeJet Pro 8010 series|Yes| 
HP OfficeJet Pro 8020 Series|Yes| 
HP OfficeJet Pro 8730|Yes|Yes
HP OfficeJet Pro 9010 series|Yes| 
HP ScanJet Pro 3500 fn1|Yes3| 
HP ScanJet Pro 4500 fn1|Yes| 
HP Smart Tank Plus 550 series|Yes| 
Kyocera ECOSYS M2035dn|No|Yes
Kyocera ECOSYS M2040dn|Yes|Yes
Kyocera ECOSYS M5521cdw|Yes|Yes
Kyocera ECOSYS M5526cdw|Yes| 
Lexmark CX317dn|Yes|Yes
Lexmark MB2236adw|Yes| 
Lexmark MC2535adwe|Yes| 
Lexmark MC3224adwe|Yes| 
Lexmark MC3326adwe|Yes| 
OKI-MC853|Yes| 
Panasonic KV-S1058Y|No|Yes
Pantum M6500W series|Yes| 
Ricoh MP C3003|No|Yes
Samsung M2070 Series|No|Yes
Samsung M267x 287x Series|No|Yes
Samsung M288x Series|No|Yes
Samsung M337x 387x 407x Series|No|Yes
Samsung SCX-3400 Series|No|Yes
SHARP MX-3060N|Yes| 
Xerox B205|Yes|Yes
Xerox B215|Yes| 
Xerox C235|Yes| 
Xerox VersaLink B405|Yes| 
Xerox WorkCentre 3025|No|Yes

