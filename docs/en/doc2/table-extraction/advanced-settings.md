---
title: "Advanced settings for table extraction"
description: In DOC² there are various advanced settings to extract a table. On this page you will find a few examples of different table characteristics.
date: "2022-03-01"
tags:
  - Table
  - DOC²
  - Settings
---

In the table extraction view, you will find the menu item `Settings` in the upper action bar (make sure that the training mode is activated). If you click on the gear icon, a window will open in which you will find the `Advanced Settings`.

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_27_settings_icon.png){ loading=lazy }

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_28_advanced_settings_dropdown.png){ loading=lazy }

## Below functionalities are available in general settings:

#### Header row count

Here you can define the number of lines of a table header. For example, the table header line can be two lines:

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_29_header_row_example.png){ loading=lazy }

Accordingly, the value in "Header row count" is set to two:

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_30_header_row_settings.png){ loading=lazy }

Why is this needed? It might be that DOC² does not recognize the second line in the table header as header line. In this case, it incorrectly inserts it into the table as extracted value. This can be easily prevented with this function.

<ins>Example before</ins>:

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_31_example_before.png){ loading=lazy }

<ins>Example after</ins>:

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_32_example_after.png){ loading=lazy }


#### Move Extra Rows to

In this example, the item description in the table spans several rows, but you only need the first one. To extract only this and include it in the Description column, select `Move Extra Rows to` `Trash`.

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_33_move_extra_row_example.png){ loading=lazy }
![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_34_trash.png){ loading=lazy }

 After naming the columns and mapping them to position, you get the following result:

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_35_rows_to_trash.png){ loading=lazy }



## Below functionalities are available in the advanced settings:

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_36_advanced_settings.png){ loading=lazy }


#### Minimum grouped rows

Enter the minimum number of rows in your grouped column here.

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_37_m_grouped_rows_example.png){ loading=lazy }

In this table you see six rows of which only three are relevant for you. In the first two columns there are two criteria that have to be extracted separately. These will be your mapped columns all the other ones have to be trained as custom columns. <br> And this is how it works step by step:

Select the two [header rows](/doc2/table-extraction/advanced-settings/#header-row-count) as well as two minimum grouped rows as these should be grouped to one row.

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_38_settings.png){ loading=lazy }
![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_39_result1.png){ loading=lazy }

Also select the `Move extra rows to` `Trash` option to be able to train all the other columns as custom columns.

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_40_rows2trash.png){ loading=lazy }

Name first column Postition and group on that one.

![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_41_result.png){ loading=lazy }

After naming all the columns and training the values, this is your result:


![Advanced Settings](/_images/doc2/Table-Extraction/8-Advanced settings/Image_42_result2.png){ loading=lazy }



<!--

##### Maximum grouped rows

Enter the maximum number of rows in your grouped column here.

#### Distinct group columns

If you want only unique values for your grouped column, check the box here.

-->

#### Reverse grouping

If you want to combine all the rows above the grouped attribute, check the box here.

In this example, the table starts with a row that is above all other information but also needs to be extracted along with the information below it. It could be that DOC² extracts this row as an additional row and the grouping of the information, e.g. by position, does not work properly.

![Reverse Grouping](/_images/doc2/Table-Extraction/8-Advanced settings/Image_43_rev_grouping1.png){ loading=lazy }
![Reverse Grouping](/_images/doc2/Table-Extraction/8-Advanced settings/Image_44_rev_grouping2.png){ loading=lazy }

After grouping on net amount, checking the box, selecting the `Move extra rows to` `Trash` option

![Reverse Grouping](/_images/doc2/Table-Extraction/8-Advanced settings/Image_45_rev_grouping3_settings.png){ loading=lazy }

and naming all columns this is your result:

![Reverse Grouping](/_images/doc2/Table-Extraction/8-Advanced settings/Image_46_rev_grouping4_result.png){ loading=lazy }
<!--

#### Split Text

If you want to split the text exactly at the column separator, check the box here. -->
