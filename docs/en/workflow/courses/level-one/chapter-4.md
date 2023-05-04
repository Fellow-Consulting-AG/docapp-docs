# Designing the Workflow

Now that we have an idea of what Nathan wants to automate, let's enumerate the steps he needs to take to achieve this:

1. Get the relevant data (order id, order status, order value, employee name) from the data warehouse
2. Filter the orders by their status (processing or booked)
3. Calculate the total value of all the booked orders
4. Notify the team members about the booked orders in the company's Discord channel
5. Insert the details about the processing orders in Airtable for follow-up
6. Schedule this workflow to run every Monday morning

Nathan's workflow involves sending data from the company's data warehouse to two external services: Discord and Airtable. In between, the data has to be wrangled with general functions (conditional filtering, calculation, scheduling).

n8n provides integrations for all these steps, so Nathan's workflow in n8n would look like this:

<figure><img src="assets/images/courses/level-one/chapter-two/Finished-workflow.png" alt="Finished workflow" style="width:100%"><figcaption align = "center"><i>Nathan's workflow</i></figcaption></figure>

You will build this workflow in 8 steps:

1. [Getting data from the data warehouse](/workflow/courses/level-one/chapter-5/chapter-5.1/)
2. [Inserting data into Airtable](/workflow/courses/level-one/chapter-5/chapter-5.2/)
3. [Filtering orders](/workflow/courses/level-one/chapter-5/chapter-5.3/)
4. [Setting values for processing orders](/workflow/courses/level-one/chapter-5/chapter-5.4/)
5. [Calculating booked orders](/workflow/courses/level-one/chapter-5/chapter-5.5/)
6. [Notifying the team](/workflow/courses/level-one/chapter-5/chapter-5.6/)
7. [Scheduling the workflow](/workflow/courses/level-one/chapter-5/chapter-5.7/)
8. [Activating and examining the workflow](/workflow/courses/level-one/chapter-5/chapter-5.8/)

To build this workflow, you will need credentials that are sent in the email from n8n when you sign up for this course. If you haven't signed up already, you can do it [here](https://n8n-community.typeform.com/to/PDEMrevI?typeform-source=127.0.0.1){:target="_blank" .external-link}. If you haven't received a confirmation email after signing up, [contact us](mailto:course@n8n.io).

<div style="text-align:center;">
	<button style="font-weight: 600;padding: 20px 46px;border-radius: 30px;color: #fff;background-color: #ff6d5a;border-color: #ff6d5a;border: 1px solid #ff6d5a;font-size: 14px;"><a href="/courses/level-one/chapter-5/chapter-5.1/" style="color: #fff;">Start building!</a></button>
</div>