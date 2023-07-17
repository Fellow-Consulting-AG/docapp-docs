---
title: Regex Manager
description: This feature by DocBits (DOC2) gives you an alternative to model classification as it allows you to write searchable regular expressions for a document type for classification and other purposes.
date: "2021-10-29"
tags:
  - DocBits (DOC²)
  - Settings
  - Document Types
  - Field Settings
  - Regex Manager
---

This feature by DocBits (DOC²) gives you an alternative to model classification as it allows you to write searchable regular expressions for a document type for classification and other purposes.

Document type: The Regex Manager allows you to write regular expressions and this regex will then be searched for in the document, if it finds a match to the regex of a defined document, it then classifies that document to the corresponding document type. For example, if you wrote a regular expression to find “Gutschrift”. If DocBits (DOC²) found this term in a document it would classify that document as a credit note.

Document origin: This lets DocBits (DOC²) know the country of origin of a document through regular expressions. For example, if a regular expression for a Spanish document contains the term “Factura”. If DocBits (DOC²) searched a document and found this term then it would know that the document is of Spanish origin and classify it as such.

## Accessing the Regex Manager

To find this feature in DocBits (DOC²), from your Dashboard, navigate to Settings → Global Settings → Document Types. Within each of the created document types, there is a “Regex” option.

![RegexManager](/_images/docbits/Settings/Document Types/image_10_regex_manager.png)

## Adding and Removing Regex

By clicking on “Regex” you will be taken to this menu, which displays the existing regex models that have been created as well as an “ADD” button for you to create new regex models.

![Add/RemoveRegex](/_images/docbits/Settings/Document Types/image_11_add_remove_regex.png)