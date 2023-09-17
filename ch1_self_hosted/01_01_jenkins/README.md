# 01_01 Jenkins
[Jenkins](https://www.jenkins.io/) is a self-hosted, open source automation server.

## Reccommended Resources
- [Jenkins User Documentation](https://www.jenkins.io/doc/)
- [LinkedIn Learning: Learning Jenkins](https://www.linkedin.com/learning/learning-jenkins-14423877)
- [LinkedIn Learning: Running Jenkins on AWS](https://www.linkedin.com/learning/running-jenkins-on-aws-8591136)
- [LinkedIn Learning: Jenkins Essential Training](https://www.linkedin.com/learning/jenkins-essential-training-17420152)

## Prequisites
Having the following items in place before starting this lab will help you have a smooth experience.

1. A [GitHub account](https://github.com/join) is required to host the code for the sample application.
2. An [Amazon Web Services account](https://aws.amazon.com/free) is needed to deploy and host the Jenkins server and the sample application used for the deployment target.
3. The sample application should be in place before starting.  See [00_06 About the Exercise Files](../../ch0_introduction/00_06_about_the_exercise_files/README.md) for steps to deploy the sample application.
4. The exercise files for the course should be downloaded and accessible on your local system.

## Deploy the Jenkins server
### 1. Create an AWS CloudFormation Stack using the provided template
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

### 2. Configure the Jenkins Server
To configure the Jenkins server, you must connect to the server and retreive the initial admin password before logging into the web interface.

#### 2.1 Retreive the initial admin password
1.  On the stack homepage, select the "Resources" column.
2.  Locate "Server" in the Logical ID column and select the link next to it in the "Physical ID" column. *The link will be similar to like `i-0b3d8738c405979c8`*.  This will open a new tab displaying EC2 instance where the Jenkins server process is running.
3.  Open the instance summary page by selecting the linked ID under the "Instance ID" column.
4.  On the instance summary page, select **Connect**.
5.  On the "Connect to instance" page, select the **Session Manager** tab.  Select **Connect**.  This will open a new tab with a terminal session connected to the EC2 instance running the Jenkins server process.
6.  Run the command `sudo docker logs jenkins`.
7.  In the command output, locate the text "Please use the following password to proceed to installation:".  Copy the value beneath that line to your clipboard.  The intial admin password will be a string of numbers and letters similar to `3d4c1c14361a4526a8888bf527450b8a`.

#### 2.2 Login and complete the configuration
1. Go back to the CloudFormation browser tab and select the "Outputs" tab for the stack.  Open the link next to the "URL" key, preferably in a new browser tab.
2. On the "Unlock Jenkins" page, under "Administrator Password", paste the value that was retreived from the EC2 instance for the initial admin password.  Select **Continue**.
3. On the "Customize Jenkins" page, select **Install suggested plugins**.  Wait for the installation to complete.
4. On the "create an admin account" page, create an admin account with a username, password, and email address.  *Note that the email address does not need to be valid but must have a name with `@` followed by a domain.*  Select **Next**.
5. On the "Instance Configuration" page, keep the value for "Jenkins URL" and select **Save and Finish**.
6. On the "Jenkins is ready!" page, select **Start using Jenkins**.

## Implement the Experimental Pipeline
To implement the experimental pipeline in Jenkins, you will need to create a GitHub repo, add the exercise files, and modify the files for your project.

Then you'll add the service account credentials to Jenkins.  Next, you'll create the project that implements the pipeline.

And finally, you'll trigger the pipeline to deploy the sample applicaiton.

Before starting these steps, open the Output tab of the Clouformation stack for the sameple application.  You'll be referencing values displayed on that tab.

### 1. Create a GitHub repo for the sample application code
Because this course covers multiple tools, a dedicated repo is need for each tool to prevent unexpected deployments to the sample-application.

#### 1.1 Create a repo and upload the exercise files for this lesson
1. Create a new GitHub repo. Give the repo a name and description.  Please select **Public** for the repo visibility to simplify access.  Select the option to add a README file and select **Python** when adding a `.gitignore` file.
2. From ther repo home page, select **Add file -> Upload files**.
3. Select **choose your files** and browse to the exercise files for this lesson on your local system.
4. Select all of the files and then select **Open**.
5. After the files have been uploaded, enter a commit message and select **Commit changes**.

#### 1.2 Update the files for your project
1. From the root of your GitHub repo, select `Jenkinsfile`.
2. Select the pencil icon to edit the file.
3. Find all occurrences of `UPDATE_THIS_VALUE` in the file and replace the text with the correct value for your project. All information can be found on the **Outputs** tab for the sample application stack in the CloudFormation console. Specfically, you'll need to update the following lines under `environment` and commit the updated file:

        environment {
            ...
            AWS_DEFAULT_REGION        = 'UPDATE_THIS_VALUE'
            STAGING_FUNCTION_NAME     = 'UPDATE_THIS_VALUE'
            STAGING_URL               = 'UPDATE_THIS_VALUE'
            PRODUCTION_FUNCTION_NAME  = 'UPDATE_THIS_VALUE'
            PRODUCTION_URL            = 'UPDATE_THIS_VALUE'
        }


### 2. Configure credentials and create the pipeline project

#### 2.1 Configure credentials
1. Log into your Jenkins server.  Select **Manage Jenkins -> Credentials -> System *(under "Stores scoped to Jenkins")* -> Global credentials (unrestricted) -> Add Credentials**
2. Under "Kind", select **Secret text**.
3. Under "Secret", enter the value for `AwsAccessKeyId`.
4. Under "ID", enter **AWS_ACCESS_KEY_ID**.
5. Select **Create**.
6. Select **Add Credentials**.
7. Under "Kind", select **Secret text**.
3. Under "Secret", enter the value for `AwsSecretAccessKey`.
4. Under "ID", enter **AWS_SECRET_ACCESS_KEY**.
5. Select **Create**.

#### 2.1 Create the pipeline project
1. Select **Dashboard -> +New Item**.
2. Under "Enter an item name", enter **Experimental Pipeline**.
3. Select **Pipeline** and then select **OK**.
4. Scroll down to the "Pipeline" section on the configuration papge.  Under "Definition", select **Pipeline script from SCM**.
5. Under "SCM", select **Git**.
6. Under "Repositories -> Repository URL", enter the URL for your GitHub repo.  Find this value from the home page of your repo by selecting **Code -> HTTPS** and then selecting the stacked squares icon to copy the URL to your system's clipboard.
7. Under "Branches to build -> Branch Specifier", change "master" to **main**.
8. Confirm that under "Script Path", the value is `Jenkinsfile`.
9. Select **Save**.

### 3. Run the pipeline
1. From the "Experimental Pipeline" home page, select **Build Now**.
2. Allow the build to complete.
3. If any errors are encountered, hover over the stage where the error was encoutered and select **Logs**.  Review the errors and make corrections as needed.  Consider reviewing the configuration steps for the credentials and the pipeline project.  If you are not able to resolve the errors, please post a question on LinkinedIn Learning in the course Q&A section.
4. Open the URLs for the sample application's staging and production environments.  For both environments, confirm that the deployment platform is "Jenkins" and the build number matches the last successful build number.

[[Next: 01_02 Bamboo](../01_02_bamboo/README.md)]
