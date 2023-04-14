---
title: Privileges with DOC²
description: A explanation of the groups & privileges of DOC²
tags:
- DOC²
- Groups
- Privileges
---
# Admins
The first user of DOC² is the default organization admin.

## Privileges
Organisation admins are able to access the settings in DOC².
They are allowed to configure:

- Company information
- Groups, users and permissions
- Integration (API-Key and SSO Settings)
- Document types
- Import methods
- OCR settings
- Classification and Extraction
- Master Data Lookup
- List of Values
- Export settings
- Modules


## User management
Admins can add new users to the organization.  
They can also grant a user admin privileges, there is no limit on how many users are allowed to be admins.<br>  
Every admin can revoke a user's admin rights.

# Groups
## What is a Group?
A group is a set of users that can be granted specific permissions for one or multiple document types.  
The groups can be created, changed and deleted by the organization admins. Every organization admin has the rights to do this.  
If no group is configured all privileges are granted to the users within the organization.

## Groups and Privileges management
Groups are managed in DOC² under SETTINGS > Groups, Users and Permissions > Groups and Permissions

![](/_images/security/groups-and-permissions.png)

### DOC² group user management  
The Organization admin can add users to the groups.
![doc2 group user management](/_images/security/group-user.png)

### DOC² group permission management
The organization admin can set the group permissions.
![doc2 group permission management](/_images/security/group-permissions.png)

## Group permissions
When creating a group, you can specify what privileges the users have for each document type.  

The different types of Privileges are:

- View
- Update
- Delete
- First Approval
- Second Approval 

### View 
If a user doesn't have the view permission, the document type will not be shown to him on the dashboard.  

### Update
Exporting documents is only possible if the user has the update permission.

### Delete
Permission to delete documents.

### First Approval
Permission to grant the first approval, if configured.

### Second Approval
Permission to grant the second approval, if configured.



