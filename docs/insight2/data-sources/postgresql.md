---
title: PostgreSQL
description: 
tags:
  - Insight²
  - Data Sources
---

# PostgreSQL

Insight² can connect to PostgreSQL databases to read and write data.

## Connection

Please make sure the host/ip of the database is accessible from your VPC if you have self-hosted Insight. If you are using Insight² cloud, please whitelist our IP.

To add a new PostgreSQL database, click on the `+` button on data sources panel at the left-bottom corner of the app editor. Select PostgreSQL from the modal that pops up.

Insight² requires the following to connect to your PostgreSQL database.

- **Host**
- **Port**
- **Username**
- **Password**

It is recommended to create a new PostgreSQL database user so that you can control the access levels of Insight.



![Insight² - Data source - PostgreSQL](/_images/insight2/datasource-reference/postgresql/pgconnect.png)



Click on **Test connection** button to verify if the credentials are correct and that the database is accessible to Insight² server. Click on **Save** button to save the data source.

## Querying PostgreSQL

Click on `+` button of the query manager at the bottom panel of the editor and select the database added in the previous step as the data source. PostgreSQL query editor has two modes, SQL & GUI. **[SQL mode](/docs/data-sources/postgresql#sql-mode)** can be used to write raw SQL queries and **[GUI mode](/docs/data-sources/postgresql#gui-mode)** can be used to query your PostgreSQL database without writing queries.

#### SQL mode

Select SQL mode from the dropdown and enter the query in the editor. Click on the `run` button to run the query.

**NOTE**: Query should be saved before running.



![Insight² - Data source - PostgreSQL](/_images/insight2/datasource-reference/postgresql/pg-sql.png)



#### GUI mode

Select GUI mode from the dropdown and then choose the operation **Bulk update using primary key**. Enter the **Table** name and **Primary key column** name. Now, in the editor enter the **records** in the form of an array of objects.

Click on the `run` button to run the query. **NOTE**: Query should be saved before running.



![Insight² - Data source - PostgreSQL](/_images/insight2/datasource-reference/postgresql/pg-gui.png)


:::tip
Query results can be transformed using transformations. Read our transformations documentation to see how: **[link](/docs/tutorial/transformations)**
:::