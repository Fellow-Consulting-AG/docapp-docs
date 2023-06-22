---
title: "Group function to extract data from tables"
description: The group function is one of the most important feature to extract data form tables. Once a table has been extracted via Docbits (DOC²) and the columns have been mapped the obtained data can be grouped to get a structured result set of all extracted data.
date: "2022-02-24"
tags:
  - Tables
  - Table Extraction
  - Docbits (DOC²)
---

# Group function to extract data from tables

Once a table has been extracted via Docbits (DOC²) and the columns have been mapped ([Mapping of columns](/docbits/table-extraction/mapping-of-columns/)) the obtained data can be grouped to get a structured result set of all extracted data.

[Sign up for a 30 days free trail](https://app.polydocs.io){ .md-button .md-button--primary }

## What does this mean in detail?

All documents from order confirmations to invoices can vary enormously in complexity from company to company. For example, in documents, information may be presented in tables in some columns across multiple rows and in other columns across only one row.

As an example, you can see the German invoice below, where the information in column "Bezeichnung" extends over several lines (positions).

![Grouping Example](/_images/docbits/Table-Extraction/6-Group Function/Image_20_grouping_example.png){ loading=lazy }

At this point, another advantage of Docbits (DOC²) comes into play. It extracts the data in the first step 1 to 1. The result looks like this:

![Docbits (DOC²) Grouping Example](/_images/docbits/Table-Extraction/6-Group Function/Image_21_grouping_example_doc2.png){ loading=lazy }

BUT: Now there is the possibility to group data based on a specific column. That means in this case it can be grouped by the column "Position" as shown in the following video. This in turn groups the rows of the "Description" column into one row. So that at the end you get a structured overall picture of the export and the data can now be processed further.

If the grouping was created by mistake, it can be removed at any time, as also shown in the video.

The result of grouping looks like this:

![Grouping Result](/_images/docbits/Table-Extraction/6-Group Function/Image_22_grouping_result.png){ loading=lazy }