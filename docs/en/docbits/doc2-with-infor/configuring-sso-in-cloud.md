---
title: "Configuring SSO in Infor Cloud"
date: "2021-10-14"
description: This is a step by step guide how to configure SSO in Infor Cloud. Starting with the prerequisites, getting access to the cloud and checking it to add a new service provider.
tags:
  - Infor
  - SSO
  - Cloud
  - new service provider
---

# Configuring SSO in Infor Cloud

## Step by step guide

### **Prerequisites**

<table><tbody><tr><td><strong>Required Information</strong></td><td><strong>Description</strong></td></tr><tr><td>Login Details to Cloud</td><td>Credentials are mandatory for accessing the Infor Cloud environment.<br>The user should have the roles "Infor-SystemAdministrator" and "UserAdmin".</td></tr><tr><td>Config Admin Details (Docbits (DOC²))</td><td>You should have received an email from FellowPro AG with the login details for the Docbits (DOC²) SSO Settings page.<br><br>You will need login and password.<br></td></tr><tr><td>Certificate</td><td>You can download the certificate in Docbits (DOC²) under SSO Service Provider Settings</td></tr></tbody></table>

**1\. Get access to the Cloud and check your access**

URL starts with [https://mingle-portal.eu1.inforcloudsuite.com/<TENANT\_NAME](https://mingle-portal.eu1.inforcloudsuite.com/)\> followed by your personal extension

![](/_images/docbits/infor-signin-1024x520.png){ loading=lazy }

a) Choose the option Cloud Identities and use your login details

![](/_images/docbits/LogIn-infor-1024x640.png){ loading=lazy }

b) After login you will have access to the Infor Cloud. In this case we enter this page, but on the burger menu you will find access to all application.

![](/_images/docbits/Welcome-to-infor-Ming.le_-1024x585.png){ loading=lazy }

![](/_images/docbits/infor_Burger-Menu-1024x586.png){ loading=lazy }

**2\. Open User Management for adding new Service Provider**

On the right hand side of the bar menu, you will find the user menu and there you can access the user management

![](/_images/docbits/infor_User-Management-1024x548.png){ loading=lazy }

a) Then you need to select in the left hand side menu the option **Security Administration** and **Service Provider**.

![](/_images/docbits/infor_Service-Provider-1024x523.png){ loading=lazy }

b. You will see this window with the Service Providers.

![](/_images/docbits/infor_Service-Provider_2-1-1024x479.png){ loading=lazy }

c. Now click on the “+” sign and add our Docbits (DOC²) as Service Provider. (View step 4)

![](/_images/docbits/infor6.png){ loading=lazy }

**3\. Access the SSO SERVICE PROVIDER SETTINGS in Docbits (DOC²)**

a) Log in on URL [https://app.polydocs.io/](https://app.polydocs.io/) with the login details you received from us.

b) Go to SETTINGS (on top bar) and choose SSO Settings down at the bottom of the list.

Here you will find all the information you need for the following steps

c) Download the certificate

![](/_images/docbits/DOC2_SSO-Service-Provider-Settings-1024x640.png){ loading=lazy }

**4\. Filling the Service Provider with the help of SSO Service Provider Settings in Docbits (DOC²)**

![](/_images/docbits/infor_Service-Provider_3-1024x891.png)

<table><tbody><tr><td><strong>Field</strong></td><td><strong>Value</strong></td></tr><tr><td><strong>Application Type</strong></td><td>DEFAULT_SAML</td></tr><tr><td><strong>Display Name</strong></td><td>Docbits (DOC²)</td></tr><tr><td><strong>Entity ID</strong></td><td>See Entity ID under SSO SERVICE SETTINGS</td></tr><tr><td><strong>SSO Endpoint</strong></td><td>Copy the SSO URL from SSO SERVICE SETTINGS and paste it in the <strong>SSO Endpoint </strong>field.</td></tr><tr><td><strong>SLO Endpoint</strong></td><td>Copy SLO URL from SSO SERVICE SETTINGS and paste it in the <strong>SLO Endpoint </strong>field.</td></tr><tr><td><strong>Signing Certificate</strong></td><td>Upload the appropriate .cer file you have downloaded in step 3c) from SSO SERVICE SETTINGS</td></tr><tr><td><strong>Name ID Format and Mapping</strong></td><td>emailaddress</td></tr></tbody></table>

![](/_images/docbits/infor_Service-Provider_completed-956x1024.png)

a) When you have filled out everything remember to save it with the disk icon above Application Type

b) Then, enter the service provider Docbits (DOC²) again.

c) Click on view the Identity Provider Information underneath.

![](/_images/docbits/infor_Identity-Provider-Information-copy-1024x559.png){ loading=lazy }

![](/_images/docbits/infor_Identity-Provider-Information-806x1024.png){ loading=lazy }

d) Export the **SAML METADATA.**

File looks like this: ServiceProviderSAMLMetadata\_10\_20\_2021.xml

**5\. Import the SAML METADATA in the SSO Settings.**

Go to IDENTITY SERVICE PROVIDER SETTINGS, enter your Tenant ID (e.g. FELLOWCONSULTING\_DEV and underneath that line you see Upload file and the IMPORT Button, where you need to upload the previously exported SAML METADATA file.

a) Click on IMPORT an then choose the METADATA file that you have already downloaded from the SSO SERVICE PROVIDER SETTINGS

b) Click on CONFIGURE

![](/_images/docbits/DOC2_identity-service-provider-settings_completed-1024x316.png){ loading=lazy }

This part is successfully completed when you see the following popup

![](/_images/docbits/DOC2_File-successfully-saved.png){ loading=lazy }

**6\. Add new Application in infor Ming.le**

a) got to Admin settings and

![](/_images/docbits/infor_Admin-Settings_Manage-Applications-1024x528.png){ loading=lazy }

b) click on ADD APPLICATION top right

![](/_images/docbits/infor_Add-Application.png){ loading=lazy }

c) fill out all fields like on following picture but with your own SSO Url, don't forget to choose icon and click on SAVE

![](/_images/docbits/infor_Add-New-Application.png){ loading=lazy }

**And now the last step:**

- Log out of Docbits (DOC²).
- Go back to the burger menu in infor and select the icon you just created.
- And you are already on the dashboard of Docbits (DOC²).

![](/_images/docbits/Sign-in-over-SSO-1024x640.png){ loading=lazy }