---
title: "Einschränkungen des KV²-Plugins"
description: "Das KV²-Plugin hat einige kleine Einschränkungen bei der korrekten Extraktion von Header- und Footer-Feldern. In dieser Dokumentation finden Sie eine Liste mit den wichtigsten Einschränkungen, dem Grund dafür und der vorgeschlagenen 'Lösung' für den Benutzer."
date: "2021-11-05"
tags:
  - KV²
  - Plugin
  - Ephesoft
  - Einschränkungen
---

**Version: 1.0.11**

Das KV²-Plugin hat einige kleine Einschränkungen bei der korrekten Extraktion von Header- und Footer-Feldern. In dieser Dokumentation finden Sie eine Liste mit den wichtigsten Einschränkungen, dem Grund dafür und der vorgeschlagenen "Lösung" für den Benutzer.

## 1. Verarbeitung von mehreren Seiten

**Beschreibung der Einschränkung**

Für diesen Fall verwenden wir das Beispiel mit Rechnungen. Das KV²-Plugin ist in der Lage, selbst zu lernen und sich von verschiedenen Dokumententypen zu trainieren, was auch bedeutet, dass verschiedene Lieferantenrechnungsvorlagen trainiert werden.

Das Hauptproblem hierbei ist, wenn ein "trainierter" Lieferant Rechnungen mit einer oder mehreren Seiten hat. Der Grund dafür ist, dass die Extraktion fehlschlagen kann, auch wenn der Lieferant bereits vom Benutzer "trainiert" wurde, wenn die trainierten Extraktionsregeln auf einer anderen Seite präsentiert werden. Siehe Prozess unten:

![Screenshot-2021-11-05-at-12.25.17](/assets/images/Screenshot-2021-11-05-at-12.25.17.png)

a) Der Benutzer hat den Lieferanten "Banana" mit einer Rechnung mit nur einer Seite trainiert. Das bedeutet, dass die Extraktionsregeln auf der ersten Seite bestimmt werden. Insbesondere Felder wie andere benutzerdefinierte Felder, die möglicherweise nicht auf der ersten Seite erscheinen, werden bei anderen mehrseitigen Beispielen ein Problem darstellen.

![Screenshot-2021-11-05-at-12.30.41](/assets/images/Screenshot-2021-11-05-at-12.30.41.png)

b) Das zweite Szenario ist, wenn derselbe Lieferant "Banana" eine Rechnung mit mehr als einer Seite gesendet hat. Zuvor wurden die Extraktionsregeln für die Felder für Seite eins bestimmt. Aber insbesondere für zusätzliche benutzerdefinierte Felder werden diese auf einer völlig anderen Seite präsentiert.

**Vorgeschlagene Lösung für den Benutzer**

Wenn ein solcher Fall auftritt, muss der Benutzer diese Einschränkung berücksichtigen. Das bedeutet, dass der Benutzer das zweite Szenario (und zukünftige Szenarien) unabhängig "neu lernen" muss. Wenn weitere Probleme auftreten, kann der Benutzer uns über die verfügbare Feedback-Funktion auf dem 5. Tab (Validierungsbildschirm) informieren.