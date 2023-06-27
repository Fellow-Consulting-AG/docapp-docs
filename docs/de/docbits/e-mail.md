---
title: "E-Mail Import in Docbits (DOC²)"
date: "2021-10-25"
description: Erfahren Sie, wie Sie Dokumente automatisch aus Ihrem E-Mail-Posteingang in Docbits (DOC²) importieren können. Dies kann über verschiedene Protokolle erfolgen.
tags:
  - E-Mail
  - Import
  - Docbits (DOC²)
---

### So importieren Sie Dokumente aus einem bestimmten E-Mail-Ordner:

Wenn Sie es leid sind, Dokumente manuell aus Ihrem E-Mail-Posteingang zu importieren, hat Docbits (DOC²) die Lösung für Sie. Mit unserer E-Mail-Importfunktion können Sie den Prozess automatisieren und Zeit sparen.<br> Und so geht's:

Rufen Sie das Einstellungsmenü auf und wählen Sie "Import".

![Import auswählen](/_images/docbits/import/Einstellungen_Import.png "Import auswählen")

Scrollen Sie zum Ende der Seite und wählen Sie die Schaltfläche + HINZUFÜGEN, um einen neuen E-Mail-Import zu erstellen.

![Import hinzufügen](/_images/docbits/import/Email-Import-hinzufuegen.png "Import hinzufügen")

Nachdem Sie auf + HINZUFÜGEN geklickt haben, öffnet sich folgendes Fenster

![Eintrag erstellen](/_images/docbits/import/Email-neuen-eintrag-erstellen.png "Eintrag erstellen")

Hier können Sie auswählen, welches Protokoll Sie wünschen:

![Protokoll](/_images/docbits/import/Email-Protokoll.png "Protokoll")

### **IMAP** 
Hier müssen Sie nur die erforderlichen Informationen zu Ihrem E-Mail-Anbieter, zur Verschlüsselung (SSL oder TSL), zum Servernamen, zum Port, zum Benutzernamen (z.B. "Eingangsrechnungen"), zur E-Mail-Adresse, zum Passwort sowie zum E-Mail-Ordner eingeben.

![IMAP](/_images/docbits/import/Email-Protokoll-IMAP.png "IMAP")

### **POP3**
Hier müssen Sie nur die erforderlichen Informationen für Ihren E-Mail-Anbieter, die Verschlüsselung, den Servernamen, den Port, den Benutzernamen (z.B. "Eingangsrechnungen"), die E-Mail-Adresse und das Passwort eingeben.

![POP3](/_images/docbits/import/Email-Protokoll-POP3.png "POP3")


Der API-Key ist automatisch mit Ihren Anmeldedaten für Docbits (DOC²) hinterlegt und gefüllt. 

Nachdem Sie alle erforderlichen Felder Ihres jeweiligen Anbieters eingegeben haben, speichern Sie die Daten.

Dieses Beispiel ist für ein Google-E-Mail-Konto:

!!! note "Wichtig aufgrund von Änderungen bei Google"
		Sie müssen jetzt die Zwei-Faktor-Authentifizierung einrichten und ein App-Passwort erstellen, das Sie hier verwenden müssen, um sicherzustellen, dass der E-Mail-Import funktioniert.


### **OAuth Office365**
Hier müssen Sie nur (falls eine angelegt) die gewünschte Unterorganisation wählen und auf `AUTHENTIFIZIEREN` klicken

![OAuth Office365](/_images/docbits/import/Email-Protokoll-OAuthOffice365.png "OAuth Office365")

Sie werden auf diese Microsoft-Seite weitergeleitet und müssen einen Code eingeben.

![Microsoft Code](/_images/docbits/import/Microsoft-Code-eingeben.png "Microsoft Code")

Diesen Code finden Sie, wenn Sie zurück auf den Tab Docbits (DOC²) gehen.<br> Der Code wird dort wie folgt angezeigt. Kopieren Sie den Code indem Sie auf den markierten Button klicken und fügen Sie diesen auf der Microsoft-Seite ein und bestätigen Sie mit einem Klick auf `Weiter`.

![DOC2App Code](/_images/docbits/import/Microsoft-Authentifizierungscode-kopieren.png "DOC2App Code")
![Microsoft Code](/_images/docbits/import/Microsoft-Code-einfuegen.png "Microsoft Code")


Danach müssen Sie Ihre eigenen Microsoft-Anmeldedaten eingeben oder diese mit einem Doppelklick bestätigen.

![Mit Doppelklick bestaetigen](/_images/docbits/import/Microsoft-Email-mit-Doppelklick-bestaetigen.png "Mit Doppelklick bestaetigen")

Bestätigen Sie die Anmeldung im nächsten Schritt erneut mit `Weiter`.

![Anmeldung bestaetigen](/_images/docbits/import/Mircosoft-DOC2App-Email-Import-anmelden.png "Anmeldung bestaetigen")
![Anmeldung schliessen](/_images/docbits/import/Microsoft-DOC2App-Email-Import-Anmelderbestaetigung.png "Anmeldung schliessen")

Nachdem die Anmeldung erfolgreich durchgeführt wurde und Sie den Microsoft Tab geschlossen haben, bestätigen Sie diese in Docbits (DOC²) mit einem Klick auf `AUTHENTIFIZIERUNG ABSCHLIESSEN`. 

![Abschliessen](/_images/docbits/import/DOC2App-Authentifizierung-abschliessen.png "Abschliessen")

Die Details des zum Import gewünschten E-Mail Ordners können Sie dann hier eingeben

![Details DOC2App](/_images/docbits/import/DOC2App-Auswahl-nach-Authentifizierung.png "Details DOC2App")

Ein Beispiel finden Sie hier:

![Beispiel](/_images/docbits/import/DOC2App_Beispiel_Ordner-Email.png "Beispiel")

Speichern Sie die Daten und testen Sie die Anmeldung, um sicherzustellen, dass alles korrekt funktioniert.

![Test](/_images/docbits/import/OAuth-Verbindung-testen.png "Test")

Nachdem Sie auf die Schaltfläche `IMPORTIEREN` geklickt haben, werden die Dokumente aus dem Postfach abgerufen und Sie gelangen direkt zum Dashboard.

Solange der Schieberiegler auf ON steht werden neue Dokumente aus angegebenem E-Mail Ordner abgerufen und importiert.

![ON_OFF](/_images/docbits/import/Schieberiegler_on-off.png "ON_OFF")



<!-- ### Bringen Sie Ihr Dokumentenmanagement mit Workflow² auf das nächste Level

Wenn Sie Ihr Dokumentenmanagement auf die nächste Stufe heben möchten, sollten Sie den Einsatz unserer Workflow²-App in Betracht ziehen. Mit Workflow² können Sie Ihre Dokumenten-Workflows automatisieren und noch mehr Zeit sparen. Sehen Sie sich unseren [Gmail-Import-Workflow](https://de.docs.fellowpro.com/example/gmail-import/) an, um zu erfahren, wie Sie Ihre Dokumente automatisch aus Ihrem E-Mail-Posteingang in Docbits (DOC²) importieren können.

Beginnen Sie noch heute mit Docbits (DOC²) und Workflow², Ihren Dokumentenmanagementprozess zu optimieren! -->