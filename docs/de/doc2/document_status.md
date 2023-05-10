 mermaid
sequenceDiagram
  Upload->>Status: DocId von Upload erhalten?
  loop Status
      Status->>Status: Bis FinalStatus nicht Klassifizierung ist
  end
  Status->>Classify: FinalStatus ist Klassifizierung
	Classify->>Delete: Dokument mit DocId löschen

