---

title: "Alle extrahierten Felder"
description: "Hier finden Sie alle extrahierten Felder von Rechnungsdetails, Berechnungsdetails und Empfängerdetails bis hin zu Lieferantendetails."
date: "2021-07-05"
tags:
  - KV²
  - Extrahierte Felder 
---

### 1 Rechnungsdetails

<table><tbody><tr><td><strong>Feldname</strong></td><td><strong>Beschreibung</strong></td></tr><tr><td>Rechnungsnummer</td><td>Manchmal gibt es mehrere Rechnungsnummern auf Rechnungen. Wählen Sie hier diejenige aus, die Sie extrahieren möchten.</td></tr><tr><td>Rechnungsdatum</td><td>Wählen Sie hier das Rechnungsdatum aus.</td></tr><tr><td>Bestellnummer</td><td>Manchmal gibt es mehrere Bestellnummern auf Rechnungen. Wählen Sie hier diejenige aus, die Sie extrahieren möchten.</td></tr><tr><td>Lieferdatum</td><td>Wählen Sie hier das Lieferdatum aus, sofern verfügbar. Wenn dies auf der Rechnung nicht sichtbar/notiert ist, lassen Sie dieses Feld leer.</td></tr><tr><td>Zahlungsbedingungen</td><td>Wählen Sie hier die Zahlungsbedingungen aus, sofern verfügbar.</td></tr><tr><td>Gesamtbetrag netto</td><td>Lassen Sie dieses Feld leer, es wird aus den Daten auf der Registerkarte "Berechnungsdetails" berechnet.</td></tr><tr><td>Gesamtbetrag MwSt.</td><td>Lassen Sie dieses Feld leer, es wird aus den Daten auf der Registerkarte "Berechnungsdetails" berechnet.</td></tr><tr><td>Gesamtbetrag</td><td>Wählen Sie hier den Gesamtbetrag aus.</td></tr><tr><td>Währung</td><td>Wählen Sie hier die Rechnungswährung, z.B. EUR/GBP.</td></tr><tr><td>Rechnungstyp</td><td>Wenn das Dokument eine Rechnung ist, sollte hier "Rechnung" ausgewählt werden. Wenn das Dokument eine Gutschrift ist, wählen Sie hier "Gutschrift".</td></tr></tbody></table>

### 2 Berechnungsdetails

<table><tbody><tr><td><strong>Feldname</strong></td><td><strong>Beschreibung</strong></td></tr><tr><td>MwSt.-Satz voll</td><td>Wenn es auf der Rechnung mehrere MwSt.-Sätze gibt, wählen Sie hier den höheren aus. Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr><tr><td>Nettobetrag voll</td><td>Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr><tr><td>MwSt.-Betrag voll</td><td>Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr><tr><td>MwSt.-Satz reduziert</td><td>Wenn es auf der Rechnung mehrere MwSt.-Sätze gibt, wählen Sie hier den niedrigeren aus. Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr><tr><td>Nettobetrag reduziert</td><td>Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr><tr><td>MwSt.-Betrag reduziert</td><td>Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr><tr><td>MwSt.-Satz befreit</td><td>Geben Sie hier für eine steuerfreie Rechnung 0 ein. Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr><tr><td>Nettobetrag befreit</td><td>Geben Sie hier für eine steuerfreie Rechnung den Gesamtbetrag ein. Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr><tr><td>MwSt.-Betrag befreit</td><td>Geben Sie hier für eine steuerfreie Rechnung 0 ein. Siehe Beispiel <a href="/kv2/how-to-deal-with-different-vat-amounts/">hier</a>.</td></tr></tbody></table>

### 3 Empfängerdetails

Diese Registerkarte wird nur benötigt, wenn Sie (mehrere) Tochtergesellschaften haben. In diesem Fall wählen Sie hier den entsprechenden Wert aus. Eine automatische Befüllung kann auf Basis der erkannten Empfänger-MwSt.-Nummer möglich sein.

Wenn es keine Tochtergesellschaften gibt, kann diese Registerkarte ignoriert oder auch in der Batch-Klassenkonfiguration ausgeblendet werden.

<table><tbody><tr><td>Empfängernamen</td><td></td></tr><tr><td>MwSt.-Nummer Empfänger</td><td></td></tr></tbody></table>

### 4 Lieferantendetails

Die Registerkarte Lieferantendetails zeigt alle Daten zum Lieferanten. Die meisten Felder werden hier automatisch aus der Fuzzy-Datenbank befüllt und können in diesem Bildschirm nicht bearbeitet werden. Nur die extrahierte MwSt.-Nummer und die Lieferanten-IBAN sollten überprüft und validiert werden.

<table><tbody><tr><td>Lieferanten-ID</td><td></td></tr><tr><td>Lieferantenname</td><td></td></tr><tr><td>Lieferantenstraße</td><td></td></tr><tr><td>Lieferanten-PLZ</td><td></td></tr><tr><td>Lieferantenstadt</td><td></td></tr><tr><td>Lieferantenland</td><td></td></tr><tr><td>Lieferanten-MwSt.-ID</td><td></td></tr><tr><td>Extrahierte MwSt.-Nummer</td><td>MwSt.-Nummer des Lieferanten, der die Rechnung sendet</td></tr><tr><td>Lieferanten-IBAN</td><td>IBAN des Lieferanten, wenn mehrere Werte verfügbar und erkannt sind, wählen Sie bitte den Hauptwert aus</td></tr><tr><td>Extrahierte IBAN</td><td></td></tr><tr><td>Lieferanten-Postfach</td><td></td></tr><tr><td>Lieferanten-Telefon</td><td></td></tr><tr><td>Lieferanten-E-Mail</td><td></td></tr><tr><td>Lieferanten-Webadresse</td><td></td></tr></tbody></table>

Bitte beachten Sie, dass einige Felder möglicherweise Einschränkungen wie eine begrenzte Anzahl von Zeichen haben. Diese Einschränkungen unterscheiden sich zwischen den einzelnen ERP-Systemen, und potenzielle Probleme beim Senden der Daten werden nicht durch das KV²-Plugin verursacht.