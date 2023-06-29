---
title: IDM Geschäftskontextmodell 
description: In dieser Dokumentation finden Sie Informationen zur Erstellung neuer Dokumenttypen in IDM und deren Verbindung mit der entsprechenden Arbeitsumgebung in LN.
date: 2023-05-16
tags:
  - DocBits (DOC²)
  - Infor
  - IDM
  - LN

---
## Was ist Infor Document Management (IDM)?

Infor Document Management (IDM) ist eine Unternehmensanwendung zur Dokumentenverwaltung, die im Infor Operating Service-Portal bereitgestellt und integriert wird.

IDM ist eine von mehreren Infor-Anwendungen, die die Benutzeroberfläche von Infor Ming.leTM nutzen.

IDM ist ein zentrales Repository, in dem Sie Ihre allgemeinen Geschäftsregeln für die Erstellung, Speicherung und Verwaltung von Dokumenten - wie Rechnungen, Lieferantendokumente und Mitarbeiterdaten - verwalten können. Sie können die physischen Dateien anzeigen, bearbeiten, erstellen und speichern.

Sie können IDM mit DocBits (DOC²) erweitern. Es bietet Funktionen zur optischen Zeichenerkennung (OCR) und intelligenten Zeichenerkennung (ICR). Diese Werkzeuge ermöglichen umfassendere und verbesserte Prozesse zur Dokumentenerfassung.
Sie können Ihre Dokumente über einen Standard-Webbrowser scannen, verbinden und die Dokumente mit Ihrem Geschäftsprozess verbinden.
Mit IDM finden Sie die Dokumente, die Sie benötigen, und arbeiten immer mit der neuesten, vollständigsten Version eines Dokuments. Durch den kontextbezogenen Zugriff auf alle wichtigen Geschäftsinformationen automatisiert DocBits (DOC²) Ihre Dokumenten-Workflows durch die automatische Kategorisierung und den Abruf wichtiger Dokument-Metadaten weiter.


## Zugriff auf IDM

Greifen Sie über die IDM-URL auf die Anwendung zu.

Durch den Zugriff auf das System über diese URL stellen Sie sicher, dass die erforderlichen Bibliotheken beim Laden der Seite geladen werden. Andernfalls funktionieren einige Funktionen wie Verknüpfungen und Kontextfreigabe nicht ordnungsgemäß. Die IDM-URL wird Ihrem IDM-Administrator zur Verfügung gestellt.

Nach der Anmeldung können Sie über den App-Switcher im Infor Ming.le-Portal auf die Client-Anwendung zugreifen.

!["Document Management"](/_images/docbits/Infor/Infor-app-switcher.png)

### Control Center

Um auf das Control Center zuzugreifen, klicken Sie auf der Landing Page **Document Management** auf das Optionsmenü neben der Schaltfläche **+ Dokument hinzufügen** und wählen Sie **Control Center**.

!["Zugang Control Center"](/_images/docbits/Infor/Infor-control-center-button.png)
!["Control Center"](/_images/docbits/Infor/Infor_control-center.png)

Wenn Sie die Rolle `IDM-AdvancedUser` oder höher haben, können Sie diese Aktionen vom Kontrollzentrum aus durchführen:

1. Konfigurieren Sie den Export/Import. (siehe unten)

2. Synchronisieren Sie das Datenmodell. Durch diese Aktion können sich die Systeme selbst reparieren, indem sie das Datenmodell synchronisieren.

Alle weiteren Aktionen im Kontrollzentrum finden Sie im _Infor Document Management Administration Guide – Cloud Edition_. Diese Aktionen sind nur für Benutzer mit der Rolle `IDM-Administrator` verfügbar.

### Import/Export Konfiguration

!["Control Center Menü"](/_images/docbits/Infor/Infor-control-center-menue.png)

Über das Menü kann der Benutzer die Konfigurationsteile des Control Centers (Dokumenttypfilter, Ergebnisliste, Geschäftskontextmodell und ION-Konfiguration) mithilfe von XML-Dokumenten exportieren/importieren. 

Die XML-Dateien für alle gängigen Dokumenttypen können Sie hier herunterladen.

- Auftragsbestätigung: <a href="/_images/docbits/Infor/IDMconfiguration_OrderConfirmation.xml" download>IDMconfiguration_OrderConfirmation</a>
- Lieferschein: <a href="/_images/docbits/Infor/IDMconfiguration_DeliveryNote.xml" download>IDMconfiguration_DeliveryNote</a>
- Rechnung: <a href="/_images/docbits/Infor/IDMconfiguration_Invoice.xml" download>IDMconfiguration_Invoice</a>

Wenn Sie Infor LN als ERP verwenden, laden Sie auch diese xml-Dateien hoch:

- Auftragsbestätigung: <a href="/_images/docbits/Infor/IDMconfiguration_BusinessContext_OrderConfirmation.xml" download>IDMconfiguration_BusinessContext_OrderConfirmation</a>
- Lieferschein: <a href="/_images/docbits/Infor/IDMconfiguration_BusinessContext_DeliveryNote.xml" download>IDMconfiguration_BusinessContext_DeliveryNote</a>
- Lieferschein2: <a href="/_images/docbits/Infor/IDMconfiguration_BusinessContext_DeliveryNote2.xml" download>IDMconfiguration_BusinessContext_DeliveryNote2</a>
- Rechnung: <a href="/_images/docbits/Infor/IDMconfiguration_BusinessContext_Invoice.xml" download>IDMconfiguration_BusinessContext_Invoice</a>


Sie können die Dateien wie folgt importieren:

### Verwendung der Registerkarte `Importieren`

1. Navigieren Sie zu **Control Center** > **Verwaltung** > **Import / Export** und wählen Sie dort die Registerkarte **Importieren**.
2. Klicken Sie auf den **Ordner** und suchen Sie nach der zuvor heruntergeladenen XML-Datei und wählen Sie `Importieren`. Eine Dateivalidierung wird durchgeführt. Es werden nur XML-Dateien akzeptiert, die vom Exporteur erstellt wurden. Wenn die Validierung fehlschlägt, bleibt die Datei **XML Importieren** deaktiviert.
3. Ist der Import der Konfiguration erfolgreich, wird Ihnen dies oben rechts angezeigt.
<!-- 3. Beim Hochladen der Konfigurationsdatei wird eine Importvorschau angezeigt, die einige oder alle dieser Teile enthält:
    <table>
    <tr>
        <td style="max-width: 100%; white-space: nowrap">Document Types and Value Sets</td>
        <td style="max-width: 100%; white-space: nowrap">The list of document types and value sets to be imported.</td>
    </tr>
    <tr>
        <td>Document Type Filter</td>
        <td>A list of document types that is displayed for the user when importing this configuration.</td>
    </tr>
    <tr>
        <td>Result List</td>
        <td>Result list configuration to be imported.</td>
    </tr>
    <tr>
        <td>Business Context Models</td>
        <td>Business context model configuration to be imported.</td>
    </tr>
    <tr>
        <td>ION</td>
        <td>ION configuration to be imported.</td>
    </tr>
    </table>
4. You can collapse or expand each part to see possible warnings or information:
   + :fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" } Warning - yellow sign: The warning sign does not disable **Import XML file**. We recommend that you go through all warning messages before starting the importer. This could be due to these situations:
    + Some configuration parts already exist in the repository that might be overwritten, for example, Result List.
    + Some configuration parts already exist in the repository that might be lost, for example, Document Type Filter.
   + :fontawesome-solid-info:{ style="color: #eee20e" } Information - blue sign: The information sign does not disable Import XML file. It is usually displayed in these situations:
    + If some parts cannot be imported, for example, Items.
    + If some existing parts are merged with new ones from the XML file, for example, Result List.
   + A green OK sign with no message required.
5. Click **Import XML file** to run the importer. When the import is finished, a report window is displayed with an information table that summarizes the status of the import. If any error occurs during the import, the error message informs the user what went wrong.

When the import is successful, **Import XML file** is disabled. -->

So sehen die allgemeinen Informationen und Attribute in IDM unter dem entsprechenden Dokumenttyp aus:

**Auftragsbestätigung**

![](/_images/docbits/Infor/IDM_dokumenttyp_auftragsbestätigung_dokumenttyp.png)
![](/_images/docbits/Infor/IDM_dokumenttyp_auftragsbestätigung_attribute.png)

**Lieferschein**

![](/_images/docbits/Infor/IDM_dokumenttyp_lieferschein_dokumenttyp.png)
![](/_images/docbits/Infor/IDM_dokumenttyp_lieferschein_attribute.png)

**Rechnung**

![](/_images/docbits/Infor/IDM_dokumenttyp_rechnung_dokumenttyp.png)
![](/_images/docbits/Infor/IDM_dokumenttyp_rechnung_attribute.png)

Wenn Sie den Menüpunkt **Geschäftskontextmodell** öffnen
![](/_images/docbits/Infor/IDM_geschäftskontextmodell.png)
finden Sie hier die Informationen wie folgt:

**Auftragsbestätigung**

![](/_images/docbits/Infor/IDM_geschäftskontextmodell_auftragsbestätigung.png)
```oc
/ORDER_CONFIRMATION[@MDS_EntityType = "{entityType}" AND @MDS_id1 = "{id1}"]
```

**Lieferschein**

![](/_images/docbits/Infor/IDM_geschäftskontextmodell_lieferschein.png)
```dn
/DELIVERY_NOTE[@MDS_EntityType = "{entityType}" AND @MDS_id1 = "{id1}"]
```

![](/_images/docbits/Infor/IDM_geschäftskontextmodell_lieferschein2.png)
```dn2
/DELIVERY_NOTE[@Delivery_Note_Id="{id3}"]
```

**Rechnung**

![](/_images/docbits/Infor/IDM_geschäftskontextmodell_rechnung.png)
```inv
/LN_SupplierInvoice[@MDS_EntityType = "{entityType}" AND @MDS_id1 = "{id1}"]
```

All diese Schritte verbinden alle Dokumente von IDM mit der entsprechenden Workbench in LN, wo sie auch angezeigt werden. Und so sieht es in LN aus:

**Auftragsbestätigung**

![](/_images/docbits/Infor/LN_Order_Order Confirmation.png)

**Lieferschein**

![](/_images/docbits/Infor/LN_Workbench Order volume_Delivery Note.png)

**Rechnung**

![](/_images/docbits/Infor/LN_Workbench Accounts Payable Processing_Invoice.png)
