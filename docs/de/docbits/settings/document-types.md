---
title: Dokumenttypen, Feld-Einstellungen und Profile
description: Hier finden Sie alle verfügbaren Dokumenttypen in DocBits (DOC²) wie Rechnung, Gutschrift, Lieferschein, Auftragsbestätigung und viele mehr.
date: "2021-10-29"
tags:
  - DocBits (DOC²)
  - Einstellungen
  - Dokumenttypen
  - Feld-Einstellungen
---

Im DocBits (DOC²) finden Sie das Menü "Einstellungen" in der oberen Leiste auf der "Startseite".

![DOC2 Dashboard Einstellungen](/_images/docbits/DOC2_Dashboard_Settings.png "DOC2 Dashboard Einstellungen")

Wenn Sie als Administrator bei DocBits (DOC²) angemeldet sind, finden Sie unter dem jeweiligen Dokumenttyp alle Felder, die extrahiert werden können.

Öffnen Sie das Menü "Dokumenttypen".

![DOC2 Dashboard Einstellungen Dokumenttypen](/_images/docbits/DOC2_Dashboard_Settings_Document Types.png "DOC2 Dashboard Einstellungen Dokumenttypen")

In der folgenden Übersicht finden Sie alle Standard-Dokumenttypen, die für Sie verfügbar sind:

![DOC2 Dokumenttypen](/_images/docbits/DOC2_Document Types.png "DOC2 Dokumenttypen")

Um zu sehen, welche Felder beispielsweise aus einer Rechnung extrahiert werden können, klicken Sie auf "Felder" für diesen Dokumenttyp.

![DOC2 Rechnungsfelder](/_images/docbits/DOC2_Invoice_Fields.png "DOC2 Rechnungsfelder")

### Feld-Einstellungen

Hier finden Sie alle Felder, die extrahiert werden können:

| RECHNUNGSDETAILS   | ZAHLUNGSDETAILS     |  MWST. & BETRÄGE    |  LIEFERANTENDETAILS |
|       :----:       |        :----:       |       :----:        |      :----:         |
| RECHNUNGSNUMMER    | IBAN                | WÄHRUNG             | ADRESSE             |
| RECHNUNGSDATUM     | ZAHLUNGSBEDINGUNGEN | NETTOBETRAG VOLL     | LIEFERANTENNAME     |
| LIEFERDATUM        |                     | NETTOBETRAG REDUZIERT  | LIEFERANTEN-ID           |
| BESTELLNUMMER      |                     | NETTOBETRAG FREI     | LIEFERANTEN-MWST          |
| BESTELLDATUM       |                     | STEUERBETRAG VOLL     |                     |
|                    |                     | STEUERBETRAG REDUZIERT  |                     |
|                    |                     | STEUERBETRAG FREI     |                     |
|                    |                     | MWST.-SATZ VOLL       |                     |
|                    |                     | MWST.-SATZ REDUZIERT    |                     |
|                    |                     | MWST.-SATZ FREI       |                     |
|                    |                     | GESAMT NETTOBETRAG    |                     |
|                    |                     | GESAMT STEUERBETRAG    |                     |
|                    |                     | GESAMTBETRAG        |                     |


Für jeden Punkt können Sie auch **FELD ERSTELLEN** wie Fracht, Porto oder jedes Feld mit einem Betrag erstellen, den Sie aus Ihren Rechnungen extrahieren möchten.

Für jedes Feld können Sie die folgenden Optionen aktivieren:

- ERFORDERLICH: Hier können Sie definieren, ob das Feld einen Wert enthalten muss, um fortzufahren.

- SCHREIBGESCHÜTZT: Hier können Sie definieren, ob ein Feld nur angezeigt, aber nicht bearbeitet werden kann.

- VERSTECKT: Hier können Sie definieren, ob ein Feld ausgeblendet oder in der Extraktionsansicht angezeigt werden soll.

- VALIDIERUNG ERFORDERLICH: Hier können Sie definieren, ob ein Feld immer manuell validiert werden muss, auch wenn es von DocBits (DOC²) zu 100% gelesen wurde.

- OCR und MATCH SCORE: Einstellung wie unten beschrieben, pro Feld.

- FORMEL: Erstellung einer Formel pro Feld.

![DOC2 Feld-Einstellungen](/_images/docbits/DOC2_field settings_fields.png "DOC2 Feld-Einstellungen")

Wenn alle Einstellungen vorgenommen wurden und gespeichert werden sollen, bestätigen Sie dies bitte mit der Schaltfläche "EINSTELLUNGEN SPEICHERN", sonst werden die Einstellungen nicht angewendet.

![DOC2 Feld-Einstellungen Speichern](/_images/docbits/DOC2_field settings_fields_save settings.png "DOC2 Feld-Einstellungen Speichern")

### ERKENNUNGSEINSTELLUNGEN

![DOC2 Feld-Einstellungen Erkennungseinstellungen](/_images/docbits/DOC2_field settings_recognition settings.png "DOC2 Feld-Einstellungen Erkennungseinstellungen")

**OCR:**

Hier können Sie die Empfindlichkeit der OCR (Optical Character Recognition) Funktion für alle Felder auf einmal einstellen. Dieser Wert bestimmt die Empfindlichkeit, mit der ein Feld rot markiert wird, wenn es nicht mit 100%iger Sicherheit extrahiert werden konnte (OCR-bezogen!).

**MATCH SCORE:**

Hier können Sie die Empfindlichkeit der MATCH SCORE Funktion für alle Felder auf einmal einstellen. Dieser Wert bestimmt ab wann ein Feld rot markiert wird, wenn DocBits (DOC²) das Feld nicht mit 100%iger Wahrscheinlichkeit extrahiert hat. In diesem Fall muss das Feld manuell validiert werden.

Die Schaltfläche "STANDARDEINSTELLUNGEN WIEDERHERSTELLEN" setzt beide Werte auf "50" zurück.

![DOC2 Feld-Einstellungen Erkennungseinstellungen Standardwerte](/_images/docbits/image-3.png "DOC2 Feld-Einstellungen Erkennungseinstellungen Standardwerte")

### PROFIL

Hier können Sie das Profil definieren, das verwendet werden soll. Entweder "Standard" oder "ZUGFeRD". Im Profil ZUGFeRD gibt es vorgegebene Felder, die für diesen Rechnungstyp obligatorisch sind. Wenn Sie nicht explizit ZUGFeRD verwenden, wählen Sie bitte "Standard".

![DOC2 Feld-Einstellungen Profil](/_images/docbits/DOC2_field settings_profile.png "DOC2 Feld-Einstellungen Profil")