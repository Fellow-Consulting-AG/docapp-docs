---
title: Privileges with DocBits (Doc²)
description: A explanation of the groups & privileges of DocBits (Doc²)
tags:
- DocBits (Doc²)
- Groups
- Privileges
---
# Admins
The first user of DocBits (Doc²) is the default organization admin.

## Privileges
Organisation admins are able to access the settings in DocBits (Doc²).
They are allowed to configure:

- document types
- general settings
- ocr settings
- company information
- modules
- users
- groups & roles
- import methods
- export settings
- filter regexes
- master data validation
- SSO settings

## User management
Admins can add new users to the organization.
They can also grant a user admin privileges, there is no limit on how many users are allowed to be admins.
Every admin can revoke a user's admin rights.

# Groups
## What is a Group?
A group is a set of users that can be granted specific permissions for one or multiple document types.
The groups can be created, changed and deleted by the organization admins. Every organization admin has the rights to do this.
If no group is configured all privileges are granted to the users within the organization.

## Groups and Priveleges management
Groups are managed in DocBits (Doc²) under Settings -> Groups & Roles

### DocBits (Doc²) group user mangement
The Organization admin can add users to the groups.
![doc2 group user mangement](/_images/security/group-user.png)

### DocBits (Doc²) group permission mangement
The Organization admin can set the group permissions.
![doc2 group permission mangement](/_images/security/group-permissions.png)

## Group permissions
When creating a group, you can specify what privileges the users have for each document type.

The different types of Privileges are:

- view
- update
- delete
- approve
- second approval

### View
If a user doesn't have the view permission, the document type will not be shown to him on the dashboard.

### Update
Exporting documents is only possible if the user has the update permission.

### Delete
Permission to delete documents

### Approve
Permission to approve documents

### Second Approval
Permission to grant the second approval if configured



