
---
title: "TE² Tutorial: Step-by-Step Guide for Table Extraction with Ephesoft"
description: "Learn how to use the TE² Plugin for table extraction in Ephesoft with this step-by-step guide. Follow the instructions to get to the table view and optimize your data extraction process."
date: '2021-11-29'
tags:
  - TE²
  - Plugin
  - Ephesoft
  - Table Extraction
---

## TE² Tutorial: Step-by-Step Guide for Table Extraction with Ephesoft

If you've installed and configured the TE² Plugin, this tutorial will guide you through the steps to use it for table extraction in Ephesoft.

### Prerequisites

Before starting, make sure you've completed the [Installation & Configuration](/te2/install/) section for this Plugin.

### How To Use TE² Plugin

#### Step 1: Log-in

Log in to the Ephesoft Transact Software with your username and password.

![Ephesoft Login](/_images/docbits/login1Unbenannt.png)

After logging in, you'll see the menu on the left side with two modules: Administrator & Operator with their defined functions:

| Administrator | Operator |
| --- | --- |
| Batch Class Management | Batch List |
| Batch Instance Management | Review Validate |
| Folder Management | Web Scanner |
| System Configuration | Upload New Document |
| Report | |

#### Step 2: Upload Documents

Upload your documents through the Operator Module in “Upload Batch”.

![Upload Batch](/_images/docbits/step1_1.png)

Start the batch with the according batch class.

![Start Batch](/_images/docbits/startbatch.png)

Wait in the Administrator Module in “Batch Instance Management” for the batch to be processed and ready for validation.

![Batch Instance Management](/_images/docbits/Process3Unbenannt.png)

#### Step 3: Validate Header and Footer Fields

Select your Batch and in the list and click to open the batch in order to validate the header and footer fields.

![Open Batch](/_images/docbits/4-open-batchUnbenannt.png)

Now you will be redirected to the Ephesoft Validation Window. Besides the options Validate, Next Batch, Merge, Split and More you can find here the button to access the "Table" view.

![Ephesoft Validation Window](/_images/docbits/image-39-1024x541.png)

![Table View Button](/_images/docbits/image-40-1024x541.png)

#### Step 4: Access the Table View

There is a default schema in place which is used by default and can handle most of the Invoice/Table layouts. For certain Invoice/Table layouts, there are special (custom) layouts in place, and there could be more if there are any special needs within your organization.

The default schema can recognize values listed in the table below. If any field which is marked as required in the table below is missing, this row cannot be recognized as a valid row.

| Name | Type | Required |
| --- | --- | --- |
| POSITION | string | false |
| DESCRIPTION | string | true |
| ITEM_NUMBER | string | false |
| QUANTITY | number | true |
| UNIT_PRICE | currency | true |
| TOTAL_AMOUNT | currency | true |
| PURCHASE_ORDER | string | false |

![Default Schema Table](/_images/docbits/image-43-1024x732.png)

TE² plugin backend intelligence is executing and optimizing the data/table view, which can then be validated or corrected by the user if needed. Even if most tables are recognized and can be executed, there are some limitations in the technology, meaning that certain kinds of tables cannot be recognized.

The following characteristics are some reasons why tables cannot be extracted:

1. Multi-line tables.
2. Mixed separation of columns (grid and no grid mix).
3. Table grid overlapping.
4. Too much distance between the column headers and the actual lines.

In any case, tables will be analyzed by PolyDocs GmbH i. Gr. to determine the possibility and viability of the table extraction.

#### Examples

![Table Extraction Example 1](/_images/docbits/image-41-1024x727.png)

![Table Extraction Example 2](/_images/docbits/image-42-1024x648.png)

Follow these steps to optimize your data extraction process with the TE² Plugin in Ephesoft. For more information, visit our website or contact us today.
