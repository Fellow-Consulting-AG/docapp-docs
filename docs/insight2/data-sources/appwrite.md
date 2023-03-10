---
title: Appwrite Database
description: 
tags:
  - Insight²
  - Data Sources
---

# Appwrite Database

Now build applications on top of your Appwrite database.

## Connection

Insight² connects to your Appwrite app using :
- **Host (API endpoint)**
- **Project ID**
- **Secret key**

You'll find the Secret key and other credentials on your Appwrite's project settings page. You may need to create a new key if you don't have one already.


You should also set scope for access of particular resource. Learn more about the **API keys and scopes** [here](https://appwrite.io/docs/keys).


To connect Appwrite datasource to your Insight² application, go to the data source manager on the left-sidebar and click on the `+` button. Select Appwrite from the list of available datasources, provide the credentials and click **Save**. It is recommended to the check the connection by clicking on 'Test connection' button to verify if the service account can access Appwrite from Insight² server.



![Insight² - Data source - Appwrite](/_images/insight2/datasource-reference/appwrite/appwrite-init_in2.gif)



## Querying Appwrite

After setting up the Appwrite datasource, you can click on the `+` button of the query manager at the bottom panel of the editor and select the Appwrite data source that you added in the previous step.



![Insight² - Data source - Appwrite](/_images/insight2/datasource-reference/appwrite/appwrite-query_in2.gif)



After selecting Appwrite datasource, select the operation that you want to perform on Appwrite database and click **Save** to save the query.

:::tip
Query results can be transformed using Transformations. Read our **Transformation documentation** [here](/insight2/tutorial/transformations/)
:::

## Supported operations

1.  **[List documents](#list-documents)**
2.  **[Get document](#get-document)**
3.  **[Update document](#update-document)**
4.  **[Delete document](#delete-document)**
5.  **[Bulk update using document id](#bulk-update-using-document-id)**

### List documents

This operation can be used to get a list of all the user documents.

#### Required parameters:

- **Collection ID:** You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/database#createCollection) or appwrite console. The value for collection ID field should be of `String` type.

#### Optional parameters:

- **Limit:** Maximum number of documents to return in response. By default will return maximum 25 results. Maximum of 100 results allowed per request. The Limit value should be of `integer` type.
- **Order fields:** Array of attributes used to sort results. The order field value should be an `array`.
- **Order types:** Array of order directions for sorting attribtues. Possible values are DESC for descending order, or ASC for ascending order. The order field value should be an `array`.
- **Field, Operator, and Value:** For filtering the results, you can enter a field(attribute) name, use appropriate operator from the dropdown and set a value.



![Insight² - Data source - Appwrite](/_images/insight2/datasource-reference/appwrite/appwrite_list.png)


### Get document

Use this operation to get a document from a collection by its unique ID.

#### Required parameters:

- **Collection ID:** You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/database#createCollection) or appwrite console. The value for collection ID should be of `String` type.

- **Document ID:** Enter the document ID of the document that you want to get. The document ID should be of `String` type.



![Insight² - Data source - Appwrite](/_images/insight2/datasource-reference/appwrite/appwrite_get.png)



### Add Document to Collection

Use this operation to create a new document in a collection.

#### Required parameters:

- **Collection ID:** You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/database#createCollection) or appwrite console. The collection ID should be of `String` type.

- **Body:** Enter the document data as JSON object.



![Insight² - Data source - Appwrite](/_images/insight2/datasource-reference/appwrite/appwrite_add.png)



### Update document

Use this operation to update a document.

#### Required parameters:

- **Collection ID:** You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/database#createCollection) or appwrite console. The value for collection ID should be of `String` type.

- **Document ID:** Enter the document ID of the document that you want to get. The document ID should be of `String` type.

- **Body:** Enter the document data as JSON object.



![Insight² - Data source - Appwrite](/_images/insight2/datasource-reference/appwrite/appwrite_update.png)



### Delete document

Use this operation for deleting a document in collection.

#### Required parameters:

- **Collection ID:** You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/database#createCollection) or appwrite console. The value for collection ID should be of `String` type.

- **Document ID:** Enter the document ID of the document that you want to get. The document ID should be of `String` type.



![Insight² - Data source - Appwrite](/_images/insight2/datasource-reference/appwrite/appwrite_delete.png)



### Bulk update using document id

Use this operation for bulk updating a documents in a collection.

#### Required parameters:

- **Collection ID:** You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/database#createCollection) or appwrite console. The value for collection ID should be of `String` type.

- **Key for document ID:**  Enter the key or attribute name that can be used to identify each record.

- **Records:** The array of objects that will contain the data for updating each record in the database
and these objects must contain a key value pair to point unique record in the database (key for document)



![Insight² - Data source - Appwrite](/_images/insight2/datasource-reference/appwrite/appwrite_bulk.png)

