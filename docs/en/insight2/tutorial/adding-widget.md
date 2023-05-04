---
title: Adding a widget
description:
tags:
  - Insight²
  - Widget
---

# Adding a widget

To add a widget, navigate to the `Widget manager` on the right sidebar. It will display the list of built-in widgets that can be added to the app. Use the search functionality to quickly find the widget that you want.



![Insight² - Tutorial - Adding a widget](/_images/insight2/tutorial/adding-widget/widget_in2.png)



## Drag and drop a widget
Let's add a `table` widget to the app to show the customer data from the query that we created in the previous steps.
To add a widget, drag and drop the widget to the canvas.

## Resize a widget
The widgets can be resized and repositioned within the canvas.



![Insight² - Tutorial - Adding a widget](/_images/insight2/tutorial/adding-widget/resize_in2.gif)



## Adding widgets to Modal
To add a widget to Modal, we need to trigger [Show modal action](/insight2/actions/actions/)


Before triggering `Show modal action` we need to add a modal widget to the canvas.


- Add a `modal widget` to the app
- Trigger the **Show modal action**
- Click on the canvas area for the `Widget manager` sidebar
- Navigate to the Widget manager on the right sidebar and Drag and drop a widget into the Modal



![Insight² - Tutorial - Adding a widget](/_images/insight2/tutorial/adding-widget/modal_in2.gif)



## Resize table columns
We can resize the column width using the resize handle of the column.



![Insight² - Tutorial - Adding a widget](/_images/insight2/tutorial/adding-widget/resize-table-column_in2.gif)



## Change widget properties
Click on the widget to open the inspect panel on right sidebar. Here you can change the properties of the widgets. Let's configure the table columns to display the customer data. The display order of columns can be changed by dragging icon near the column name.



![Insight² - Tutorial - Adding a widget](/_images/insight2/tutorial/adding-widget/inspect-panel_in2.gif)



## Connecting data with widget
Now we will connect the `data` object of the `fetch customers` query with the table. Click on the table widget to open the inspector on right sidebar. We can see that the data property of the table have an empty array as the value. The data field, like almost every other field on the editor supports single-line javascript code within double brackets. Variable suggestions will be shows as a dropdown while you type the code in the field.

Let's select `data` object of the 'postgresql' query.

` {{queries.postgresql1.data}}`

Since we have already run the query in previous step, the data will be immediately displayed in the table.



![Insight² - Tutorial - Adding a widget](/_images/insight2/tutorial/adding-widget/table-data_in2.png)



So far in this tutorial, we have connected to a PostgreSQL database and displayed the data on a table.


Read the widget reference of table [here](/insight2/widgets/table/) for more customizations such as server-side pagination, actions, editing data.
