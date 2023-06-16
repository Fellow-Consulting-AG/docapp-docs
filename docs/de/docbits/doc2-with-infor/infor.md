---
title: "Docbits (Doc²) - Infor-Anwendungsfälle"
description: Hier finden Sie verschiedene Anwendungsfälle, wie Prozesse Ihrer verschiedenen Dokumenttypen aussehen und in Infor integriert werden.
date: "2023-05-16"
tags:
  - Docbits (Doc²)
  - PO Abgleich
  - Infor LN
  - Infor M3
  - Anwendungsfälle
---

## Effizientes Dokumentenmanagement mit Docbits (Doc²) und Infor

Docbits (Doc²) ist eine leistungsstarke Dokumentenmanagementlösung, mit der Sie Ihre Arbeitsabläufe in der Dokumentenverarbeitung optimieren können. Durch die nahtlose Integration mit Infor LN und Infor M3 kann Docbits (Doc²) Ihnen helfen, Ihre Dokumente effizient und genau zu verwalten. Hier sind einige der Anwendungsfälle, bei denen Docbits (Doc²) Ihnen helfen kann:


### Einfache Rechnungsverarbeitung

Dies ist der häufigste Anwendungsfall für Docbits (Doc²). Mit seinen fortschrittlichen OCR-Funktionen kann Docbits (Doc²) relevante Informationen aus Rechnungen extrahieren und zur weiteren Verarbeitung an Infor senden.
Und so funktioniert es:

``` mermaid
graph TD
  A[Start] --> B{Rechnung?};
  Infor[Infor] --> |Validierung von Stammdaten| C;
  B -->|Ja| C[Kopfdatenfelder extrahieren];
  C -->|Optional| T[Tabellenfelder];
  T -->C;
  C --> D[An Infor senden];
  D --> E;
  B ---->|Nein| E[Ende];
```

Mit Docbits (Doc²) können Sie mehr tun

``` mermaid
graph TD
  A[Start] --> B{Rechnung?};
  B -->|Ja| C[Extraktion];
  C -->|Optional| T[Tabellenauszug];
  T -->C;
  Infor[Infor] --> |Validierung von Stammdaten| C;
  C --> D[In ZUGFeRD umwandeln];
  D --> F[An Infor senden];
  F --> Z;
  B ---->|Nein| Z[Ende];
```

### Rechnung und Lieferschein

``` mermaid
graph TD
  A[Start] --> B{Klassifizierung?};
  B -->|Rechnung| Extraktion[Extraktion];
  B -->|Lieferschein| Extraktion;
  Extraktion -->|Optional| T[Tabellenauszug];
  T -->Extraktion;
  Infor --> |Validierung von Stammdaten| Extraktion;
  Extraktion --> ION[Infor ION & IDM];
  B -->|Sonst| G[Nur OCR];
  G -->IDM[PDF an Infor IDM senden];
  IDM --> Infor;
  ION --> Infor;
  Infor --> Ende[Ende];

```

### Rechnung und Bestellungen inkl. PO Abgleich und ZUGFeRD und Bestellung-X

``` mermaid
graph TD
  A[Start] --> B{Klassifizierung?};
  B -->|Rechnung| Extraktion[Extraktion];
  B -->|Lieferschein| Extraktion;
  B ---->|Auftragsbestätigung| Extraktion;
  Extraktion -->T[Tabellenfelder];
  T -->Extraktion;
  Extraktion ---> D[In ZUGFeRD umwandeln];
  Extraktion --> PO;
  D --> F[PDF an Infor IDM + ION senden];
  F --> Infor;
  PO --> |Bestellung bestätigen|Infor;
  B -->|Sonst| G[Nur OCR];
  G -->H[PDF an Infor IDM senden];
  H --> Infor[Infor];
  Infor[Infor] --> |Auftragsbestätigung|PO[PO Abgleich];
  Infor[Infor] --> |Validierung von Stammdaten| Extraktion;
  PO --> Bestellung-X[Bestellung-X];
  Extraktion --> Bestellung-X;
  Infor --> Bestellung-X;
  Bestellung-X --> Lieferant[Lieferant];
  Lieferant --> Ende;
  Infor --> Ende;

```

# Infor ION API hinzufügen

<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube-nocookie.com/embed/N64jzntUMao" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Hinzufügen von Verbindungspunkten in Infor OS

<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube-nocookie.com/embed/ZMVqpRRkv48" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Hinzufügen von Verbindungspunkten in Infor OS

<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube-nocookie.com/embed/sYST3GLn1IY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>





# Auftragsbestätigung

<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube-nocookie.com/embed/fkJrEDuG5Nw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Lieferschein

<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube-nocookie.com/embed/4KsliipUFx8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Rechnung

<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube-nocookie.com/embed/k9z586vsLZs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
