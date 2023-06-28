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

![Dashboard](/_images/docbits/einstellungen/module/doc scan/Dashboard-Dokument-scannen.png)

As your scanner is not installed yet, you’ll get the following message

![Software nicht gefunden](/_images/docbits/einstellungen/module/doc scan/Scanner Software herunterladen.png)

:fontawesome-solid-circle-info:{ style="color: #0F17E4" } <br>
Je nachdem, welches Betriebssystem Sie verwenden, klicken Sie zum Herunterladen auf die entsprechende Schaltfläche. Die Installationsdatei ist nur auf englisch verfügbar.


Öffnen Sie die Installationsdatei und Sie werden folgendes sehen

![Welcome](/_images/docbits/einstellungen/module/doc scan/Install doc2scan.png)

Klicken Sie auf `Continue`, akzeptieren Sie die Software-Lizenzvereinbarung mit `Continue` sowie `Agree` und fahren Sie mit der Installation der Software fort.<br> 
:fontawesome-solid-circle-info:{ style="color: #0F17E4" } Für die Installation dieser Software werden 33,6 MB Speicherplatz benötigt.<br> 
Sie können den Speicherort ändern, bevor Sie im nächsten Schritt auf `Install` klicken.

Sobald der folgende Bildschirm angezeigt wird, sind Sie fast fertig.

![](/_images/docbits/einstellungen/module/doc scan/Install doc2scan-installation-completed-successfully.png)

Open web browser to test if the app works by entering: <https://local.polydocs.io:12500/> <br>
If you see this message on the screen, you must first configure some settings in your FritzBox network settings if you are using one.

![](/_images/docbits/einstellungen/module/doc scan/browser_FritzBox.png)

Alle Informationen finden Sie **[hier](https://docs.polydocs.io/doc2/modules/doc-scan/#fritzbox-network-settings)**.

Wenn Sie diesen Bildschirm sehen, können Sie auf `Doc2` klicken.

![](/_images/docbits/einstellungen/module/doc scan/browser_bereit-fuer-doc2scan.png)

Sie werden zur Docbits (DOC²)-Anmeldeseite weitergeleitet, wo Sie Ihre Anmeldedaten eingeben können, um auf Ihr Dashboard zuzugreifen.

![Anmelden](/_images/docbits/einstellungen/module/doc scan/docbits-doc2-anmeldeseite-browser.png)

Alles, was Sie jetzt noch tun müssen, ist, Doc Scan in den Einstellungen unter Module zu aktivieren.

![](/_images/docbits/einstellungen/module/doc scan/docbits-doc2-einstellungen-module-docscan.png)

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




[Deutsche Übersetzung bald verfügbar](https://en.docs.fellowpro.com/docbits/settings/module/doc-scan/)