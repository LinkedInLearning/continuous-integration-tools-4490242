# 00_06 About the Exercise Files

Exercise files are available to help you following along with this course.  Use the exercise files to create the resources used in the course demonstrations.

The directory structure follows the course structure, with directories for each chapter and section.

## Prequisites
1. A [GitHub account](https://github.com/join) is needed to host the code for the sample application.
2. An [Amazon Web Services account](https://aws.amazon.com/free) is needed to deploy and host the sample application.

## Deploying the Sample Application
A sample application is included to use as a deployment target. The goal is to model the experimental pipeline with each CI tool and deploy updates to the sample application.

Use the provided [CloudFormation template](./sample-application.yml) and the following instructions to manually deploy the sample application in AWS.

### 1. Get the exercise files in place on your local system
1. Open the GitHub repo for this course and download the exercise files by selecting **Code -> Local -> Download ZIP**.  
2. Open the ZIP file and confirm the contents of the file are accessible.

### 2. Deploy the Sample Application
1. Log into your AWS account.  Select the search bar at the top of the page and enter **CloudFormation**.
1. On the CloudFormation homepage, select **Create stack**.  If the button includes a dropdown, select **With new resources (standard)**.
1. Under "Prerequisite - Prepare template", confirm that "Template is ready" is selected.
1. Under "Specify template", select **Upload a template file**.  Select **Chose file**.  Browse to the location where you opened the ZIP file.  Navigate to **ch0_introduction/00_06_about_the_exercise_files** and select **sample-application.yml**.  Select **Open**. Select **Next**.
1. Enter a name for the stack under "Stack name". *Note that the name should only include letters (A-Z and a-z), numbers (0-9), and dashes (-)*.  Select **Next**.
1. On the "Configure stack options" screen, keep all options as the default.  Scroll to the bottom of the page and select **Next**.
1.  On the "Review" screen, scroll to the bottom of the page and select the **checkbox** next to "I acknowledge that AWS CloudFormation might create IAM resources with custom names".  Select **Submit**.
1. Review the "Events" tab on the stack homepage until *CREATE_COMPLETE* is reported under the "Status" column for the Logical ID that matches your stack name.

### 3. Review the Deployed Sample Application and Lambda Functions
1.  On the stack homepage, select the "Outputs" column.  Make a note of the output key, value, and description for:

    - AwsAccessKeyId
    - AwsDefaultRegion
    - AwsSecretAccessKey
    - ProductionFunctionName
    - ProductionURL
    - StagingFunctionName
    - StagingURL

    These values will be needed to configure the experimental pipeline for each CI tool.

2.  To view the environments for the sample applicaiton, select the URL next to **ProductionURL** and  **StagingURL**. *Open each link in a new tab*.

3.  To view the lambda functions for the sample application, select the "Resources" tab on the stack homepage.  Under "Logical ID", locate **LambdaFunctionProduction** and **LambdaFunctionStaging**.  Select the link next to each resource in the "Physical ID" column.
