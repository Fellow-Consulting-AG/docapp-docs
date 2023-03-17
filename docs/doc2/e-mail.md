---
title: "E-Mail"
date: "2021-10-22"
description: DOC² Email Import. If you want to import documents from your email inbox automatically, here are the steps you need to take.
tags:
  - E-Mail
  - Import
  - DOC²
---

### Folder Import

If you want to import documents from a specific email folder, here are the steps you need to take:

Your email folder could look like this.

![](/_images/doc2/email/AllImportOptions_Email_Folder.png)


Go to **SETTINGS** in the top bar and click on `Import`.

![](/_images/doc2/email/AllImportOptions_Email_1.png)

As you can see, there is no email account setup for the import yet.

![](/_images/doc2/email/AllImportOptions_Email_2.png)

Click on the `OFF` button to open the Email import settings.

The boxes for E-Mail and Password as well as the API Key might get automatically filled in with your login information for DOC², depending on your browser settings. Please empty the fields before continuing to enter the needed information for the E-Mail Import.

What you need to do is enter the protocol (IMAP or POP3), the encryption (SSL or TSL), server-name, port, a username (e.g. "incoming invoices") as well as the email address and password from which the documents are going to be imported from.

This example is for a google email account:

!!! note "Important due to changes made by Google"
		You now need to set up 2-Factor Authentication and create an App-Password which you have to use here to make sure that the E-Mail import will work.

After you have entered all required fields of your respective provider, save the data.

![](/_images/doc2/email/AllImportOptions_Email_3.png)

You can test the login by pressing the `TEST LOGIN` button. If all data is correct you will get the following feedback.

![](/_images/doc2/email/AllImportOptions_Email_4.png)


After you click the `IMPORT` button, the documents will be fetched from the mailbox and you will be taken directly to the Dashboard.

![](/_images/doc2/email/AllImportOptions_Email_6.png)


<!-- If you have made the right decision to also use our [Workflow² APP](https://docs.polydocs.io/workflow/), you will find the corresponding workflows [here](https://docs.polydocs.io/example/gmail-import/) to automatically import your documents from your e-mail inbox to DOC². -->




## Configuring Microsoft Email Services with OAuth2

### Register App on Azure AD

Follow the steps below to register an App to allow email ingestion in DOC² using OAuth2:<br>
:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }
**Note:** The permissions may require authorization from an administrator.
:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }

1\. Sign in to the Azure Portal using your credentials.



2\. From Azure services, locate and open Azure Active Directory (also known as Azure AD).

![](/_images/doc2/email/Azure-Active-Directory.png)



3\. Under the **Manage** section, select `App registrations`.

![](/_images/doc2/email/App-registrations.png)



4\. In the App registrations screen, click **+ New registration**.

![](/_images/doc2/email/App_new-registration.png)



5\. The **Register an application** screen displays. Enter the user-facing display name for the App in `Name`.



6\. Select one of the following account types depending on your needs:

 - **Accounts in any organizational directory (Any Azure AD directory – Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**

![](/_images/doc2/email/Register-an-application-screen.png)



7\. Leave the option **Redirect URI (optional)** as is.



8\. Click **Register** to complete the App registration. This will return you to the screen for the new App.

![](/_images/doc2/email/Register.png)



9\. In the App screen, locate the **Application (client) ID**. Copy it to be used when configuring email ingestion for DOC².

![](/_images/doc2/email/Application ID_copy-to-clipboard.png)



10\. From left panel, select **Certificates & secrets**:

![](/_images/doc2/email/Certificates-and-secrets.png)



11\. In the **Certificates & secrets** screen, click on `+ New client secret` button under **Client secrets** section:

![](/_images/doc2/email/New-client-secret.png)



12\. In the **Add a client secret** dialog box, click the `Add` button:

![](/_images/doc2/email/Add-a-client-secret_validity.png)

It is recommended to fill in a description to identify this secret among many (as of now the limit is 2 secrets per App).<br>
:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }
**Note:** Select this expiration date according to your company policy. Once expired, a new client secret will need to be created and specified for each email configuration where it was used previously.
:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }



13\. The newly generated client secret will be visible. Copy this client secret Value to be used when configuring email ingestion for DOC² 

![](/_images/doc2/email/client-secrets_value.png)

:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }
**Important:** Ensure that you have copied the client secret value as it will not display again once it is closed.
:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }



14\. Select **Authentication** on the left panel. This will present the **Authentication** screen on the right-hand side.

![](/_images/doc2/email/Authentication.png)



15\. In the **Advanced settings** section, click `Yes` for **Allow public client flows**.

![](/_images/doc2/email/Allow-public-client-flows.png)



16\. Click `Save` to confirm changes.

![](/_images/doc2/email/Advanced settings_save.png)



17\. Select **API permissions** on the left panel. This will present the API permissions screen.

![](/_images/doc2/email/API-permissions.png)



18\. By default the **User.Read** permission from **Microsoft Graph** is present, leave this as is.

![](/_images/doc2/email/API-permissions-name-user-read.png)

 :fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }
 **Note:** This is a required permission. 
 :fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }<br>
 If this permission is not available, then add the permission with the steps mentioned below for <br> `Mail.ReadWrite` permission.



 19\. Click **+ Add a permission**.This will open the **Request API permissions** panel.

![](/_images/doc2/email/Add-a-permission.png)
![](/_images/doc2/email/Microsoft-Graph.png)



20\. Click **Microsoft Graph**.



21\. From the two sub-categories, select **Delegated permissions**.
 
![](/_images/doc2/email/Delegated-permissions.png)



22\. Type `Mail.ReadWrite` in the search box. Select the Mail.ReadWrite checkbox for the permission.

![](/_images/doc2/email/Mail.ReadWrite_1.png)



23\. This will enable the `Add permissions` button at the bottom of the panel. Click `Add permissions`. This will add the **Mail.ReadWrite** permission to the list of **Configured permissions** for the App.

![](/_images/doc2/email/Mail.ReadWrite_2.png)



24\. :fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }
**Note:** Administrator permissions may be required. The administrator will have to authorize the App for using these permissions. 
:fontawesome-solid-triangle-exclamation:{ style="color: #EE0F0F" }<br>
Once authorized the granted status will be indicated as follows:

![](/_images/doc2/email/Configured-permissions.png)

This concludes the steps for App registration for DOC²  email ingestion using OAuth2.

