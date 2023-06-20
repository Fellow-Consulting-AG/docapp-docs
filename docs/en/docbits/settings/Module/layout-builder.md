title: "Layout Builder"
description: This module feature allows you to assign users and/or groups with the ability to approve a document before it can be exported.
date: "2023-05-23"
tags:
  - Docbits (DOC²)
  - Settings
  - Module
  - Layout Builder

## Layout Builder

### Accessing the Layout Manager

First of all, ensure that the Layout Manager feature is activated. This can be done by navigating to Settings > Document Processing > Module > Document Type and ensure that the Layout Builder slider is set too active as shown below.

![Access Layout Builder](/_images/docbits/Settings/Module/Layout Builder/Image 1 - Accessing Layout Manager.png)

After this is done you can access the Layout Manager via Settings > Document Types, once on this page you can select from the various document types you have created and either select “Edit Layout” as shown below

![Edit Layout](/_images/docbits/Settings/Module/Layout Builder/Image 2 - Edit Layout.png)

or if you have sub-document types within a created document type you can select “Document Sub Types” and select “Edit Layout” for the sub document type layout you wish to edit as shown below.

![Edit Sub Document Types](/_images/docbits/Settings/Module/Layout Builder/Image 3 - Doc Sub Types.png)

### Basics of the Layout Manager 

 After following the previous steps you will reach a page like the one shown below.

#### Uploading a document

In order to upload a document to the layout builder, simply navigate to the right on the screen 

![Upload Document](/_images/docbits/Settings/Module/Layout Builder/Image 4 - Uploading a Doc 1.png)

Click on the “Upload Documents” button or drag and drop your desired document into the provided area

![Upload Document](/_images/docbits/Settings/Module/Layout Builder/Image 5 - Uploading a Doc 2.png)

#### Groups

Groups can be created by selecting the following icon.

![Create Group](/_images/docbits/Settings/Module/Layout Builder/Image 6 - Groups 1.png)

Groups allow you to create different sections on a layout, this makes it easier to separate different groups of data or information to make a layout easier to follow. You can create a title for each group so that a user can know what information they will find in that group.

![Groups](/_images/docbits/Settings/Module/Layout Builder/Image 7 -  Groups 2.png)

#### Form Elements

![Form Elements](/_images/docbits/Settings/Module/Layout Builder/Image 8 - Form Elements.png)

These are a set of default fields that can be dragged and dropped into the layout builder and are available to you to create your desired layout. These include:

Text - This is a text box which creates a field in the layout that can have text entered into it once on the validation screen.

Label - This is a field that can be used to create uneditable text, this could be used to create sub-headings or any other desired uneditable text when on the validation screen.

Checkbox - This creates a boolean type field which can be checked or unchecked.

Multi Checkbox - This functions the same way as the “Checkbox” but can be used when the user knows they will be adding multiple checkboxes in one section.

Horizontal Separator - This creates a horizontal line on the layout that can be used to split up sections within a group on the layout.

Table of Checkboxes - This lets the user create a table of checkboxes consisting of custom  x- and y-axis values, eg. 

![Table of Checkboxes](/_images/docbits/Settings/Module/Layout Builder/Image 9 - Table of Checkboxes.png)

Button - This creates a clickable button on the validation screen within the layout that can be set to one of three functions, including: Export, Export mit Sonderwunsch or Reject.

 

#### Creating document specific fields

The user is able to create their own custom groups and fields for a document type, this can be done when originally creating a document type but also by selecting “Fields” when on the Document Types page in Settings.

![Fields](/_images/docbits/Settings/Module/Layout Builder/Image 10 - Blank Spaces 1.png)

#### Creating blank spaces

##### The 100 percent rule

![Blank Spaces](/_images/docbits/Settings/Module/Layout Builder/Image 11 - Blank Spaces 2.png)

In order to create the above space on the layout, a “Label” from the Form Elements must be used in a special way. The reason for this is that the Layout Manager operates according to a 100 space per line system in that 1 space represents 1 percent of a line, this means that fields can only take up 100 spaces per line as show below.

![Blank Spaces](/_images/docbits/Settings/Module/Layout Builder/Image 12 - Blank Spaces 3png.png)

This means that the user must build the layout line by line according to this rule. For example lets say you would like to add the fields “Name” and “Date” in the same line but would like the “Name” field to be larger. This can be done by dragging and dropping the “Text” field from the Field Elements drop down and naming each field “Name” and “Date” as shown.

![Blank Spaces](/_images/docbits/Settings/Module/Layout Builder/Image 13 - Blank Spaces 4.png)

The problem now exists that they are both the same size of 33 (this is the default size of all dragged and dropped fields) but you would like the “Name” field to be larger than the “Date” field and both fields should take up the entire line on the layout. Therefore, by following the 100 percent rule, you can set the “Name” and “Date” fields to any combination of 100 that you would desire. This of course depends on how large you would like each individual field but for the purpose of this example we will set the “Name” field to 70 and the “Date” field to 30, the results are:

![Blank Spaces](/_images/docbits/Settings/Module/Layout Builder/Image 14 - Blank Spaces 5.png)

This same rule applies to all fields in the Layout Manager.

##### Creating Blank Spaces

Now that this rule has been explained, creating blank spaces will make more sense. As previously mentioned, in order to create a blank space you have to use a “Label” from the Form Elements.

For example, let’s say that you would like to create a blank space between these two fields.

![Blank Spaces](/_images/docbits/Settings/Module/Layout Builder/Image 15 - Blank Spaces 6.png)

Step one is to drag and drop a “Label” between these two fields, once added you can click on the “Label” field you just added and on the left you will be presented with the properties of the field. Now, in the same way you would create or change the name of a field as shown previously, you will remove any name from the “Label” property like so

![Blank Spaces](/_images/docbits/Settings/Module/Layout Builder/Image 16 - Blank Spaces 7.png)

The result from doing this will then be

![Blank Spaces](/_images/docbits/Settings/Module/Layout Builder/Image 17 - Blank Spaces 8.png)

There is now a gap between the two fields. This gap can be extended or shortened according to the 100 percent rule discussed earlier, and with these functions you can create any desired layout.


#### Field Grouping

This feature allows you to group multiple fields together so that only one field from each group can be selected at a time on the validation screen.

![Field Grouping](/_images/docbits/Settings/Module/Layout Builder/Image 18 - Field Grouping.png)

For example, if you had multiple checkboxes all belonging to a group name “1” then only one checkbox from group “1” can be ticked on the validation screen.

 
#### KI Model Types

![KI Models](/_images/docbits/Settings/Module/Layout Builder/Image 19 - KI Models 1.png)

This dropdown gives you the choice of training a specific field according to a KI model. Possible options can be seen below.

![KI Models](docs/en/_images/docbits/Settings/Module/Layout Builder/Image 20 - KI Models 2.png)

KI model training can lead to more accurate extraction results on the validation screen.



