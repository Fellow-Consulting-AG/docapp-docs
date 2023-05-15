---
date: 2023-02-19
authors: [dajor,amnai2p,masadusman,FellowFellow,Bennse666,amierhaider,WingsOfCobra]
categories:
  - enhancement
  - bug
  - refactor
  - refactoring

---


## KV - App
- Importing models for AlchemyEncoder, ColumnValidationRules, DocumentTable, DocumentTableColumn, and DocumentType
- Refactored the code to separate the query execution and result processing into two functions.
- Initial release of the FellowPro IDP application
- Updated dependencies to fix security vulnerabilities
- Updated version of the application
- Updated version of the code
- Updated version of the FellowPro IDP application
- Refactored the OCR functionality to improve performance
- Modified the SELECT statement to include a DEFAULT org_id if the specified org_id is not found
- Removed redundant code
- Added two new fields to the 'fields' list
- Duplicate imports of authenticator and fellow2kv.extension
- Added a new 'deploy' job to the workflow that deploys the code to a production environment
- Added org_id to the SELECT statement and modified the WHERE clause to include the DEFAULT org_id if the specified org_id is not found
- Improved code formatting and indentation
- Removed a blank line in the __init__ method of the VersionHandler class
- Modified the code to enforce a list of values for a field
- Added import statement for sqlalchemy and enforced a list of values for CURRENCY field type


## API
- This code change adds a new preference key to the PREFERENCES_KEYS class for the layout builder module setting. This will allow the application to store and retrieve the user's preferred layout builder module type.
- Added a new enum value to FILTER_STATUS for workflow status
- An additional enum value was added to FILTER_STATUS.
- Added a new enum value to FILTER_STATUS for workflow processing
- Added a conditional statement to return an error response if the document is not valid.
- Updated version number to 2.2.439.1
- Updated the Fellow2KV library to version 2.2.439
- Updated the Fellow2KV library to version 2.2.451
- Updated version number to 2.2.450.1
- Updated the Fellow2KV library to version 2.2.435
- Updated version number to fix a bug in the login process
- Updated the Fellow2KV library to version 2.2.447
- Updated the Fellow2KV library to version 2.2.450
- Alter the column 'store_type' in the 'doc2light-stores' table to change the data type from ENUM to String.
- Changed the way the 'success' attribute is accessed in the 'check' dictionary from dot notation to bracket notation.
- Changed the way to access the 'success' attribute of the 'check' object from dot notation to bracket notation.
- Added a new store type for the Doc2 application.
- The code has been modified to use the create_trocr_task function instead of the process_trocr_fields.delay function. The rate_limit and concurrency options have been removed from the process_trocr_fields function.
- Added a condition to check if the 'validate' parameter is set to True before validating the extracted data. This allows for skipping validation if the parameter is set to False.
- Changed the validation check to only run if the 'validate' parameter is not set to False in the 'export_parameters' object of the transformed data.
- Changed the error message for invalid documents.
- Made changes to the trocr_client.send_task() method call to improve performance and reliability
- Refactored code for improved readability and maintainability
- Updated version of the application
- Added checks for document existence and user token validity before processing
- Added a new store type for the Doc2 application


## Web - App
- The code includes a mixin for storage management, but it should be using a cache instead.
- Modified a path in an SVG file.
- Converted the original SVG image to XML format.
- Changed the way the baseUrl is set to use the process.env.APP_VUE_DOC2_SERVICE_URL variable instead of hardcoding it.
- Ensured that the showConnectionFromField function is only called when allowAreaSelection is true.
- Modified the style properties of HTML elements to follow consistent naming conventions and adding proper indentation.
- Added a button to add a new user in the user settings page
- Changed the variable name from 'foo' to 'bar'
- The code includes an SVG image that is used in the project.
- Changed thead and tbody styles in the HTML table
- The code contains hardcoded values instead of using constants or configuration files.
- Modified the formBuilderConfigModel object to include a columns array and adding column properties to it.


## Changes from Developers
| code_change_description                                                                                                                                                                                               | author                   | github_labels        |   code_smell_rating |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|:---------------------|--------------------:|
| Importing models for AlchemyEncoder, ColumnValidationRules, DocumentTable, DocumentTableColumn, and DocumentType                                                                                                      | Amna                     | `enhancement`        |                   5 |
| Updated version of the code                                                                                                                                                                                           | Benedikt Liebs           | `bug, enhancement`   |                   8 |
| Added import statements for models module to use the classes defined in the module                                                                                                                                    | Lint Action              | `import, models`     |                   2 |
| Duplicate imports of authenticator and fellow2kv.extension                                                                                                                                                            | Muhammad Asad Usman Khan | `duplicate-imports`  |                   6 |
| Added a conditional statement to return an error response if the document is not valid.                                                                                                                               | Amna                     | `bug`                |                   6 |
| Updated the Fellow2KV library to version 2.2.435                                                                                                                                                                      | Benedikt Liebs           | `bug, enhancement`   |                   3 |
| The code has been modified to use the create_trocr_task function instead of the process_trocr_fields.delay function. The rate_limit and concurrency options have been removed from the process_trocr_fields function. | Benjamin Roder           | `refactor`           |                   6 |
| Changed the error message for invalid documents                                                                                                                                                                       | Muhammad Asad Usman Khan | `bug, documentation` |                   3 |
|                                                                                                                                                                                                                       | Syed Amier Haider Shah   |                      |                 nan |
| This change ensures that the showConnectionFromField function is only called when allowAreaSelection is true. This improves the code by reducing unnecessary function calls and improving performance.                | Anian Sollinger          | `performance`        |                   3 |