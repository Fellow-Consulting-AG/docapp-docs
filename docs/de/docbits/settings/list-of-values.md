---
title: "List of Values"
description: "Mit dieser Funktion können Sie verschiedene Listen oder Sätze verwandter Informationen erstellen und speichern, die zur Erstellung einer Dropdown-Box auf dem Validierungsbildschirm verwendet werden können."
date: "2023-06-23"
tags:
  - DocBits (DOC²)
  - Settings
  - List of Values
---

Mit dieser Funktion können Sie anhand einer Liste gültige Feldwerte festgelegen, um Validierungsfehler zu vermeiden. Synonyme können ebenfalls genutzt werden, um auf gültige Werte zu verweisen. Die Verwendung solcher Listen ist empfehlenswert, um mehr Kontrolle über exportierte Werte zu haben. 
Damit werden Dropdown-Boxen erstellt die auf dem Validierungsbildschirm zur Verfügung stehen.

Um eine Liste zu erstellen, navigieren Sie über das DocBits (DOC²) Dashboard zu den Einstellungen, wie unten gezeigt.

![Dashboard](/_images/docbits/einstellungen/list of values/dashboard_einstellungen.png)

Dokumentenverarbeitung → List of Values

![Einstellungen](/_images/docbits/einstellungen/list of values/einstellungen_list of values.png)

Auf diesem Bildschirm haben Sie Zugriff auf bestehende Listen sowie die Möglichkeit, neue Listen zu erstellen

![ListofValues](/_images/docbits/einstellungen/list of values/list of values_listen.png)

Wie kann diese Funktion für ein Feld in einem Layout aktiviert werden?

DocBits (DOC²) Dashboard → Einstellungen

![Dashboard](/_images/docbits/einstellungen/list of values/dashboard_einstellungen.png)

Globale Einstellungen → Dokumententypen

![Dokumententypen](/_images/docbits/einstellungen/list of values/einstellungen_dokumententypen.png)

Wählen Sie den Dokumenttyp aus, dem Sie auch die Werteliste hinzufügen möchten, und wählen Sie im Dokumenttyp das Feld aus, das die Werteliste auf dem Validierungsbildschirm enthalten soll.

Sobald Sie das Feld angeklickt haben, erscheint auf der linken Seite Ihres Bildschirms das folgende Menü.

![Properties](/_images/docbits/einstellungen/list of values/layout ersteller_select list of values.png)

Wählen Sie unten in der Dropdown-Box die entsprechende Liste von Werten aus, die Sie dem Feld zuordnen möchten, und speichern Sie die Änderungen.

![Speichern](/_images/docbits/einstellungen/list of values/ISO_Currency.png)

Mit Hilfe von verschiedenen Listen kann festgelegt werden, welche Werte für ein bestimmtes Feld gültig sind. Dadurch wird verhindert, dass eine ungültige Zeichenkette die Validierung des Feldes stört. Zum Beispiel beim Feld 'Währung': Die Werte sind 'EUR' und 'USD', aber der extrahierte Wert lautet 'U5D', der kein gültiger Wert ist. In diesem Fall wird DocBits (DOC²) den Benutzer auf den Fehler hinweisen und auf das richtige Feld verweisen. Eine zusätzliche Funktion der List of Values ist die Möglichkeit, Synonyme zu erstellen. Diese können als Indikatoren verwendet werden, um auf einen gültigen Wert zu verweisen. So kann zum Beispiel dem Wert 'USD' das Synonym 'U5D' zugeordnet werden. Wenn DocBits (DOC²) den Wert 'U5D' extrahiert, wird automatisch der Wert 'USD' aus der Liste eingesetzt. Die Verwendung dieser Funktion ist optional, aber empfehlenswert, um eine bessere Kontrolle darüber zu haben, welche Werte exportiert werden können.<br> Die Funktion kann im Layout-Ersteller aktiviert oder deaktiviert werden.