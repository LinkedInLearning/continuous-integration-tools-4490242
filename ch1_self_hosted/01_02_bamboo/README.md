# 01_02 Bamboo
[Bamboo](https://www.atlassian.com/software/bamboo) is a self-hosted, continuous integration and delivery tool developed by Atlassian, the makers of popular software including Jira and Confluence among others.

## Reccommended Reading
- [Understanding the Bamboo CI Server](https://confluence.atlassian.com/bamboo/understanding-the-bamboo-ci-server-289277285.html)
- [Configuring plans](https://confluence.atlassian.com/bamboo/configuring-plans-289276853.html)
- [Configuring tasks](https://confluence.atlassian.com/bamboo/configuring-tasks-289277036.html)
- [Configuring jobs](https://confluence.atlassian.com/bamboo/creating-a-plan-289276868.html)

## Prequisites
1. A [GitHub account](https://github.com/join) is required to host the code for the sample application.
1. An [Atlassian account](https://id.atlassian.com/signup) is required to request a license for the demo server.
2. An [Amazon Web Services account](https://aws.amazon.com/free) is needed to deploy and host the Bamboo server and the sample application used for the deployment target.
3. The sample application should be in place before starting.  See [00_06 About the Exercise Files](../../ch0_introduction/00_06_about_the_exercise_files/README.md) for steps to deploy the sample application.

## Implement the Experimental Pipeline
### 1. Create a GitHub repo for the sample application code
1. Create a new GitHub repo.
1. From ther repo home page, select **Add file -> Upload files**.
1. Select **choose your files** and browse to the exercise files for this lesson on your local system.
1. Select all of the files and then select **Open**.
1. After the files have been uploaded, enter a commit message and select **Commit changes**.
 
### 2. Deploy the Bamboo server
1. Log into your AWS account.  Select the search bar at the top of the page and enter **CloudFormation**.
1. On the CloudFormation homepage, select **Create stack**.  If the button includes a dropdown, select **With new resources (standard)**.
1. Under "Prerequisite - Prepare template", confirm that "Template is ready" is selected.
1. Under "Specify template", select **Upload a template file**.  Select **Chose file**.  Browse to the exercise files for this lesson on your local system.  Select [`bamboo-cloudformation-template.yml`](./bamboo-cloudformation-template.yml).  Select **Open**. Select **Next**.
1. Enter a name for the stack under "Stack name"; `bamboo` is a good choice. *Note that the name should only include letters (A-Z and a-z), numbers (0-9), and dashes (-)*.  
1. Accept the defaults under "Parameters" and select **Next**.
1. On the "Configure stack options" screen, keep all options as the default.  Scroll to the bottom of the page and select **Next**.
1.  On the "Review" screen, scroll to the bottom of the page and select the **checkbox** next to "I acknowledge that AWS CloudFormation might create IAM resources with custom names".  Select **Submit**.
1. Review the "Events" tab on the stack homepage until *CREATE_COMPLETE* is reported under the "Status" column for the Logical ID that matches your stack name. *Note that it may take 5 to 10 minutes for the stack to report CREATE_COMPLETE*.
1.  On the stack homepage, select the "Outputs" column.  Open the value for the key "URL" in a new tab.

### 3. Configure the Bamboo server
To configure the Bamboo server, you need to create and enter an evalutation license, disable the embedded database check, and add a local agent.

#### 3.1 Create and enter an evaluation license
1. On the "Welcome to Bamboo Data Center", select **Generate a Bamboo Data Center license**. *Note that the text for this link is very small and located under the "License key" form.
2. If needed, log into your Atlassian account when prompted.
3. On the "New Trial License" page, confirm the product is "Bamboo" and the license type is "Bamboo (Data Center)".  Enter a value for "Organization" and select **Generate License**.
4. Highlight the value in the "License Key" field and copy it to your system clipboard.  Go back to the tab with the Bamboo setup wizard.
5. Paste the key into the "License key" form.  Select **Continue**.
6. On the "Configure instance" page, keep all the values as default, scroll to the bottom of the page and select **Continue**.
7. On the "Configure database" page, under "Database type", select **H2**. *Note that this option selects an embedded database which is for evaluation purposes and is not intended for production use*. Select **Continue**.
8. On the "Import data" page, confirm that "Create a new Bamboo home" is selected and select **Continue**.  Stand by for the database to be configured.
9. On the "Create admin" page, enter the details for your admin account and select **Finish**.  Stand by for the installation to complete.

#### 3.2 Disable notifications
This step prevents Bamboo from creating notificaitons about the server running with an embedded database or agents running on the primary server.

1. Once the installation is complete, select the cog on the top, far right of the page.  Select **Overview**.
2. Scroll to the bottom of that page and select **Troubleshooting and support tools** from the menu on the left.
3. On the far right under "Notifications", select the dropdown menu and select "Don't show any notifications".

#### 3.3 Disable sign-ups
This step prevents others from creating accounts on your Bamboo server without your permission.

1. Once the installation is complete, select the cog on the top, far right of the page.  Select **Overview**.
2. From the menu on the left, select **Security Settings**.
3. On the bottom of the "Security and permission" page, select **Edit**.
4. Under "Change global security and permission properties", remove the selection next to "Enable signup?".
5. At the bottom of the page, Select **Save**.

#### 3.3 Add a local agent
1. Select the cog on the top, far right of the page.  Select **Agents**.
2. Select **Add local agent**.
3. Enter a name and description for the agent, perhaps `agent1`.
4. In the top menu bar of the page, select **My Bamboo**.

### 4. Create the pipeline
### 5. Run the pipeline


