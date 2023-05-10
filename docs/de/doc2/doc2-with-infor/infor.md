 mermaid
graph LR
  A[Start] --> B{Rechnung?};
  Infor[Infor] --> |Master Data Validation| C;
  B -->|Ja| C[Extrahieren von Kopffeldern];
  C -->|Optional| T[Tabellenfelder];
  T -->C;
  C --> D[An Infor senden];
  D --> E;
  B ---->|Nein| E[Ende];
