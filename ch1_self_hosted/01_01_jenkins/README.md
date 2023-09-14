# 01_01 Jenkins
[Jenkins](https://www.jenkins.io/) is a self-hosted, open source automation server.

## Prequisites
1. A [GitHub account](https://github.com/join) is required to host the code for the sample application.
1. An [Amazon Web Services account](https://aws.amazon.com/free) is needed to deploy and host the Jenkins server and the sample application used for the deployment target.
1. The sample application should be in place before starting.  See [00_06 About the Exercise Files](../../ch0_introduction/00_06_about_the_exercise_files/README.md) for steps to deploy the sample application.
1. The exercise files for the course should be downloaded and accessible on your local system.

## Implement the Experimental Pipeline
### 1. Create a GitHub repo for the sample application code
1. Create a new GitHub repo.
1. From ther repo home page, select **Add file -> Upload files**.
1. Select **choose your files** and browse to the exercise files for this lesson on your local system.
1. Select all of the files and then select **Open**.
1. After the files have been uploaded, enter a commit message and select **Commit changes**.

### 2. Deploy the Jenkins server
1. Log into your AWS account.  Select the search bar at the top of the page and enter **CloudFormation**.
1. On the CloudFormation homepage, select **Create stack**.  If the button includes a dropdown, select **With new resources (standard)**.
1. Under "Prerequisite - Prepare template", confirm that "Template is ready" is selected.
1. Under "Specify template", select **Upload a template file**.  Select **Chose file**.  Browse to the exercise files for this lesson on your local system.  Select [`jenkins-cloudformation-template.yml`](./jenkins-cloudformation-template.yml).  Select **Open**. Select **Next**.
1. Enter a name for the stack under "Stack name"; `jenkins` is a good choice. *Note that the name should only include letters (A-Z and a-z), numbers (0-9), and dashes (-)*.  
1. Accept the defaults under "Parameters" and select **Next**.
1. On the "Configure stack options" screen, keep all options as the default.  Scroll to the bottom of the page and select **Next**.
1.  On the "Review" screen, scroll to the bottom of the page and select the **checkbox** next to "I acknowledge that AWS CloudFormation might create IAM resources with custom names".  Select **Submit**.
1. Review the "Events" tab on the stack homepage until *CREATE_COMPLETE* is reported under the "Status" column for the Logical ID that matches your stack name. *Note that it may take 5 to 10 minutes for the stack to report CREATE_COMPLETE*.
1.  On the stack homepage, select the "Outputs" column.  Make a note of the output key, value, and description for:
    - AdminPassword
    - URL

    These values will be needed to configure the Jenkins server

### 3. Configure the Jenkins Server
To configure the Jenkins server, you must connect to the server and retreive the initial admin password before logging into the web interface.

#### 3.1 Retreive the initial admin password
1.  On the stack homepage, select the "Resources" column.
2.  Locate "Server" in the Logical ID column and select the link next to it in the "Physical ID" column. *The link will be similar to like `i-0b3d8738c405979c8`*.  This will open a new tab displaying EC2 instance where the Jenkins server process is running.
3.  Open the instance summary page by selecting the linked ID under the "Instance ID" column.
4.  On the instance summary page, select **Connect**.
5.  On the "Connect to instance" page, select the **Session Manager** tab.  Select **Connect**.  This will open a new tab with a terminal session connected to the EC2 instance running the Jenkins server process.
6.  Run the command `sudo docker logs jenkins`.
7.  In the command output, locate the text "Please use the following password to proceed to installation:".  Copy the value beneath that line to your clipboard.  The intial admin password will be a string of numbers and letters similar to `3d4c1c14361a4526a8888bf527450b8a`.

#### 3.2 Login and complete the configuration
1. Go back to the CloudFormation browser tab and select the "Outputs" tab for the stack.  Open the link next to the "URL" key, preferably in a new browser tab.
2. On the "Unlock Jenkins" page, under "Administrator Password", paste the value that was retreived from the EC2 instance for the initial admin password.  Select **Continue**.
3. On the "Customize Jenkins" page, select **Install suggested plugins**.  Wait for the installation to complete.
4. TODO: Replace this with the "proceed as admin" option.  On the "create an admin account" page, create an admin account with a username, password, and email address.  *Note that the email address does not need to be valid but must have a name with `@` followed by a domain.*  Select **Next**.
5. On the "Instance Configuration" page, keep the value for "Jenkins URL" and select **Save and Finish**.
6. On the "Jenkins is ready!" page, select **Start using Jenkins**.

### 4. Create the pipeline
### 5. Run the pipeline
