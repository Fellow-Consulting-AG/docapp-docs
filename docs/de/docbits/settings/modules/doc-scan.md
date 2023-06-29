---
title: "Doc Scan"
description: In den Docbits (DOC²)-Einstellungen finden Sie verschiedene Module, die wichtig sind, wenn Sie mit dem PO-Matching arbeiten, Genehmigungsprozesse nutzen und Ihre Dokumententypen individuell anpassen möchten. 
date: "2023-06-28"
tags:
  - Docbits (DOC²)
  - Einstellungen
  - Dokumentenverarbeitung
  - Module
  - Doc Scan
---

Sie nutzen bereits Docbits (DOC²) und möchten Dokumente direkt nach dem Scannen in Ihr Dashboard hochladen?<br> So funktioniert es:

## Laden Sie die Scannersoftware herunter

Klicken Sie auf **Dokument scannen** auf dem Docbits (DOC²) Dashboard

![Dashboard](/_images/docbits/einstellungen/module/docscan/Dashboard-Dokument-scannen.png)

Da die Scannersoftware noch nicht installiert ist, erhalten Sie die folgende Meldung

![Software nicht gefunden](/_images/docbits/einstellungen/module/docscan/Scanner Software herunterladen.png)

:fontawesome-solid-circle-info:{ style="color: #0F17E4" } <br>
Je nachdem, welches Betriebssystem Sie verwenden, klicken Sie zum Herunterladen auf die entsprechende Schaltfläche. <br> Die Installationsdatei ist nur auf englisch verfügbar.
:fontawesome-solid-circle-info:{ style="color: #0F17E4" }


Öffnen Sie die Installationsdatei und Sie werden folgendes sehen

![Welcome](/_images/docbits/einstellungen/module/docscan/Install doc2scan.png)

Klicken Sie auf `Continue`, akzeptieren Sie die Software-Lizenzvereinbarung mit `Continue` sowie `Agree` und fahren Sie mit der Installation der Software fort.<br> 
![Agree](/_images/docbits/einstellungen/module/docscan/Install doc2scan-software-licence-agreement-agree.png)
:fontawesome-solid-circle-info:{ style="color: #0F17E4" } Für die Installation dieser Software werden 33,9 MB Speicherplatz benötigt.<br> 
![Speicherplatz](/_images/docbits/einstellungen/module/docscan/Install doc2scan-select destination-space.png)

Sie können den Speicherort ändern, bevor Sie auf `Install` klicken.

Sobald der folgende Bildschirm angezeigt wird, sind Sie fast fertig.

![](/_images/docbits/einstellungen/module/docscan/Install doc2scan-installation-completed-successfully.png)

Öffnen Sie den Webbrowser, um zu testen, ob die App funktioniert, indem Sie folgende Url eingeben: <https://local.polydocs.io:12500/> <br>
Wenn Sie folgende Meldung auf dem Bildschirm sehen, müssen Sie zunächst einige Einstellungen in den Netzwerkeinstellungen Ihrer FritzBox konfigurieren, sofern Sie eine solche verwenden.

![](/_images/docbits/einstellungen/module/docscan/browser_FritzBox.png)

Alle Informationen finden Sie **[hier](/docbits/settings/modules/doc-scan/#fritzbox-netzwerk-einstellungen)**.

Wenn Sie diesen Bildschirm sehen, können Sie auf `Doc2` klicken.

![](/_images/docbits/einstellungen/module/docscan/browser_bereit-fuer-doc2scan.png)

Sie werden zur Docbits (DOC²)-Anmeldeseite weitergeleitet, wo Sie Ihre Anmeldedaten eingeben können, um auf Ihr Dashboard zuzugreifen.

![Anmelden](/_images/docbits/einstellungen/module/docscan/docbits-doc2-anmeldeseite-browser.png)

Alles, was Sie jetzt noch tun müssen, ist, Doc Scan in den Einstellungen unter Module zu aktivieren.

![](/_images/docbits/einstellungen/module/docscan/docbits-doc2-einstellungen-module-docscan.png)

---

## FritzBox-Netzwerk-Einstellungen

Sollten Sie nach der Installation und dem Aufrufen der url https://local.polydocs.io:12500/ folgenden Fehler erhalten, hier die Gründe dafür:<br>
* DNS-Auflösung von privaten IP-Adressen nicht möglich.<br>
* Die DNS-Auflösung für Domainnamen, die auf private IP-Adressen im FRITZ!Box-Heimnetz verweisen, ist über die FRITZ!Box nicht möglich. Dadurch ist über den Domainnamen kein Zugriff auf Serverdienste im FRITZ!Box-Heimnetz möglich. Dabei wird eventuell eine der folgenden Fehlermeldungen angezeigt:<br>
"DNS timed out"<br>
"DNS request timed out"

<ins>Ursache</ins><br>
Aus Sicherheitsgründen unterdrückt die FRITZ!Box DNS-Antworten, die auf IP-Adressen im eigenen Heimnetz verweisen. Dies ist ein Sicherheitsmerkmal der FRITZ!Box zum Schutz vor so genannten DNS-Rebinding-Attacken.

Wenn Sie also eine FritzBox nutzen müssen Sie im Menü der FritzBox zuerst folgende Einstellungen vornehmen:

1. Klicken Sie in der Benutzeroberfläche der FRITZ!Box auf `Heimnetz`.

2. Klicken Sie im Menü `Heimnetz` auf `Netzwerk`.

3. Klicken Sie auf die Registerkarte `Netzwerkeinstellungen`.

    Tragen Sie im Abschnitt `DNS-Rebind-Schutz` im Eingabefeld **Hostnamen-Ausnahmen** local.polydocs.io ein, für den der DNS-Rebind-Schutz nicht gelten soll.<br> 
    Bestätigen Sie mit `Übernehmen`.
---
## Doc2Scan Service Manager deinstallieren
Führen Sie den folgenden Befehl aus, um Doc2Scan Manager zu deinstallieren:
```command
sudo bash /Library/doc2scan/uninstall.sh
```
---
## Scanner Kompatibilität

Legende:

- Ja - Gerät funktioniert einwandfrei
- Nein - Protokoll wird vom Gerät nicht unterstützt
- ? - Gerät arbeitet mit SANE-AirScan, aber Protokoll wird vom Benutzer nicht gemeldet
- Leer - dem Autor liegen keine Informationen über diese Modus/Geräte-Kombination vor

Definition:

**eSCL** steht für Airscan ist ein SANE WebScan-Frontend, dass das AirScan-Protokoll von Apple unterstützt. Die Scanner werden automatisch erkannt und über mDNS veröffentlicht.

**WSD** steht für "Web Services on Devices" und ist ein Netzwerkkommunikationsprotokoll, das für die Druckererkennung und -verwaltung über ein lokales Netzwerk verwendet wird. Im WSD-Modus können Drucker automatisch erkannt und zu einem Computersystem hinzugefügt werden, ohne dass eine manuelle Konfiguration oder die Installation zusätzlicher Druckertreiber erforderlich ist. Er ermöglicht eine einfache Einrichtung und Druckfunktionen für kompatible Drucker über ein Netzwerk. Der WSD-Modus wird häufig in Windows-Betriebssystemen verwendet, um Drucker im Netzwerk zu erkennen und anzuschließen.


**Gerät**|**eSCL-Modus**|**WSD-Modus**
-----|-----|-----
Brother ADS-2700W|Nein|Ja
Brother DCP-7055W|Nein|Ja
Brother DCP-9020CDW|Nein|Ja
Brother DCP-J552DW|Nein|Ja
Brother DCP-L2540DW|Nein|Ja
Brother DCP-L2550DN / DCP-L2550DW|Ja| 
Brother HL-L2380DW series|Nein|Ja
Brother HL-L2395DW series|Ja| 
Brother MFC-7360N|Nein|Ja
Brother MFC-8710DW|Nein|Ja
Brother MFC-J1012DW|Ja| 
Brother MFC-J1300DW|Ja| 
Brother MFC-J4410DW|Nein|Ja
Brother MFC-J4620DW|Nein|Ja
Brother MFC-J485DW|Ja| 
Brother MFC-J625DW|Nein|Ja
Brother MFC-L2700DW|Nein|Ja
Brother MFC-L2710DW|Ja|Ja
Brother MFC-L2720DW|Nein|Ja
Brother MFC-L2750DW|Ja|Ja
Canon D570|Ja| 
Canon G600 series|Ja| 
Canon imageCLASS MF642C/643C/644C|Ja| 
Canon imageCLASS MF743cdw|Ja1| 
Canon imageRUNNER 2625/2630|Ja|Ja
Canon imageRUNNER ADVANCE 4545/4551|Ja|Ja
Canon imageRUNNER ADV C5550/5560|Ja| 
Canon imageRUNNER C3120L|Ja|Ja
Canon i-SENSYS MF4780w|Nein|Ja
Canon i-SENSYS MF641C|Nein|Ja
Canon LiDE 300|Ja| 
Canon LiDE 400|Ja| 
Canon MB5100 series|Ja| 
Canon MB5400 series|Ja|Ja
Canon MF110/910|Ja| 
Canon MF240 Series|Nein|Ja
Canon MF260 Series|Ja|Ja
Canon MF410 Series|Ja|Ja
Canon MF440 Series|Ja|Ja
Canon MF645Cx|Ja| 
Canon MF745C/746C|Ja|Ja
Canon MG5300 series|Nein|Ja
Canon PIXMA G3000 series|Nein|Ja
Canon PIXMA MG3600 series|Ja| 
Canon PIXMA MG5500 Series|Nein|Ja
Canon PIXMA MG7700 Series|Ja| 
Canon PIXMA TS5000 Series|Ja| 
Canon PIXMA TS 9550 Series|Ja| 
Canon TR4529 (PIXMA TR4500 Series)|Ja|Ja
Canon TR7500 Series|Nein|Ja
Canon TR8600 Scanner|Ja| 
Canon TS 3100|Ja| 
Canon TS 3300|Ja| 
Canon TS 3400|Ja| 
Canon TS 6151|Ja| 
Canon TS 6200 series|Ja|Ja
Canon TS 6400 series|Ja| 
Canon TS 8230 series|Nein|Ja
Dell C1765nfw Color MFP|Nein|Ja
Dell C2665dnf Color Laser Printer|Nein|Ja
Dell C3765dnf Color MFP|Nein|Ja
EPSON ET-2710 Series|Nein|Ja
EPSON ET-2750 Series|Ja| 
EPSON ET-2760 Series|Ja| 
EPSON ET-2810 Series|Nein|Ja
EPSON ET-2850 Series|Ja| 
EPSON ET-3750 Series|Ja| 
EPSON ET-4850 Series|Ja| 
EPSON ET-M2170 Series|Ja| 
EPSON Stylus SX535WD|Nein|Ja
EPSON WF-7710 Series|Nein|Ja
EPSON XP-2100 Series|Nein|Ja
EPSON XP-340 Series|Ja| 
EPSON XP-442 445 Series|Ja| 
EPSON XP-5100 Series|Ja| 
EPSON XP-6100 Series|Ja| 
EPSON XP-7100 Series|Ja| 
EPSON XP-8600 Series|Ja| 
HP Color Laserjet MFP m178-m181|Ja| 
HP Color LaserJet MFP M182nw|Ja| 
HP Color LaserJet MFP M281fdw|Ja| 
HP Color LaserJet MFP M283fdw|Ja| 
HP Color LaserJet MFP M477fdw|Ja|Ja
HP Color LaserJet Pro M478f-9f|Ja| 
HP Color LaserJet Pro MFP M277dw|Ja| 
HP DeskJet 2540|Ja| 
HP DeskJet 2600 series|Ja| 
HP DeskJet 2700 series|Ja| 
HP DeskJet 3700 series|Ja| 
HP DeskJet 5000 series|Ja| 
HP DeskJet 5200 series|Ja| 
HP ENVY 4500|Ja| 
HP ENVY 5055 series|Ja| 
HP ENVY 5530 series|Ja| 
HP ENVY 5540|Ja| 
HP ENVY 5640|Ja| 
HP ENVY Photo 6200 series|Ja| 
HP ENVY Photo 7800 series|Ja| 
HP ENVY Pro 6400 series|Ja| 
HP LaserJet 200 colorMFP M276n|Nein|Ja
HP LaserJet MFP E62655|Ja| 
HP LaserJet MFP M130fw|Nein|Ja
HP LaserJet MFP M227sdn|Ja| 
HP LaserJet MFP M426dw|Ja| 
HP LaserJet MFP M630|Ja| 
HP LaserJet Pro M28a|Ja3| 
HP LaserJet Pro M28w|Ja|Ja
HP LaserJet Pro M329|Ja9| 
HP LaserJet Pro MFP 148fdw|Ja| 
HP LaserJet Pro MFP M125 series|Nein|Ja
HP LaserJet Pro MFP M225dn|Nein|Ja
HP LaserJet Pro MFP M428dw|Ja| 
HP LaserJet Pro MFP M521 series|Nein|Ja
HP Laser MFP 131 133 135-138|Ja| 
HP Neverstop Laser MFP 1202nw|Ja| 
HP OfficeJet 3830 series|Ja| 
HP Officejet 4630|Ja| 
HP Officejet Pro 6970|Ja| 
HP OfficeJet Pro 6978|Ja| 
HP OfficeJet Pro 7740|Ja|Nein
HP OfficeJet Pro 8010 series|Ja| 
HP OfficeJet Pro 8020 Series|Ja| 
HP OfficeJet Pro 8730|Ja|Ja
HP OfficeJet Pro 9010 series|Ja| 
HP ScanJet Pro 3500 fn1|Ja3| 
HP ScanJet Pro 4500 fn1|Ja| 
HP Smart Tank Plus 550 series|Ja| 
Kyocera ECOSYS M2035dn|Nein|Ja
Kyocera ECOSYS M2040dn|Ja|Ja
Kyocera ECOSYS M5521cdw|Ja|Ja
Kyocera ECOSYS M5526cdw|Ja| 
Lexmark CX317dn|Ja|Ja
Lexmark MB2236adw|Ja| 
Lexmark MC2535adwe|Ja| 
Lexmark MC3224adwe|Ja| 
Lexmark MC3326adwe|Ja| 
OKI-MC853|Ja| 
Panasonic KV-S1058Y|Nein|Ja
Pantum M6500W series|Ja| 
Ricoh MP C3003|Nein|Ja
Samsung M2070 Series|Nein|Ja
Samsung M267x 287x Series|Nein|Ja
Samsung M288x Series|Nein|Ja
Samsung M337x 387x 407x Series|Nein|Ja
Samsung SCX-3400 Series|Nein|Ja
SHARP MX-3060N|Ja| 
Xerox B205|Ja|Ja
Xerox B215|Ja| 
Xerox C235|Ja| 
Xerox VersaLink B405|Ja| 
Xerox WorkCentre 3025|Nein|Ja
