# 03_02 Azure Pipelines
Azure DevOps includes a complete set of hosted tools for application development with Pipelines as the main tool for building, testing, and deploying applications.

- [Azure Pipelines](https://azure.microsoft.com/en-us/products/devops/pipelines/)

## Recommended Resources
- [Azure DevOps for Beginners on LinkedIn Learning](https://www.linkedin.com/learning/azure-devops-for-beginners)


## Prerequisites
Having the following items in place before starting this lab will help you have a smooth experience.

1. A [GitHub account](https://github.com/join) is required to host the code for the sample application.
1. An [Amazon Web Services account](https://aws.amazon.com/free) is needed to deploy the sample application used for the deployment target.
1. The sample application should be in place before starting.  See [00_06 About the Exercise Files](../../ch0_introduction/00_06_about_the_exercise_files/README.md) for steps to deploy the sample application.
1. The exercise files for the course should be downloaded and accessible on your local system.

## Implement the Experimental Pipeline
To implement the experimental pipeline in TODO, you will need to create a GitHub repo, add the exercise files, and modify the files for your project if needed.

Next, you'll create the project that implements the pipeline.

And finally, you'll trigger the pipeline to deploy the sample application.

Before starting these steps, open the Output tab of the Cloudformation stack for the sample application.  You'll be referencing values displayed on that tab.

### 1. Create a GitHub repo for the sample application code
Because this course covers multiple tools, a dedicated repo is need for each tool to prevent unexpected deployments to the sample-application.

#### 1.1 Create a repo and upload the exercise files for this lesson
1. Create a new GitHub repo. Give the repo a name and description.  Please select **Public** for the repo visibility to simplify access.  Select the option to add a README file and select **Python** when adding a `.gitignore` file.
2. From ther repo home page, select **Add file -> Upload files**.
3. Select **choose your files** and browse to the exercise files for this lesson on your local system.
4. Select all of the files and then select **Open**.
5. After the files have been uploaded, enter a commit message and select **Commit changes**.

### 2. Configure TODO

## Additional Information




# resources
- [Specify jobs in your pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/phases)
- [Pricing for Azure DevOps](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)


- Create or log into your Azure DevOps account; https://learn.microsoft.com/en-us/azure/devops/user-guide/sign-up-invite-teammates?view=azure-devops
- create a new project
- choose public or private visibility
- select create
- from the menu on the left, select Repos
- add a .gitignore file for Python. select **Initialize**
- select **three dot menu** -> **upload files** -> **Browse...**
- select exercise files for this lesson.
- select **Committ**
- select **Set Up Build**
- select **variables** -> **new variable**
- add the name and value for each of the following parameters: (for AWS_ACCESS_KEY_D and AWS_SECRET_ACCESS_KEY select the option for "Keep this value secret".
  -   AWS_ACCESS_KEY_ID
  -   AWS_SECRET_ACCESS_KEY
  -   AWS_DEFAULT_REGION
  -   STAGING_FUNCTION_NAME
  -   STAGING_URL
  -   PRODUCTION_FUNCTION_NAME
  -   PRODUCTION_URL
    select the "+" for each additional varaible.
    when all variables are in place select **Save**.
- select **Save**
- to update or remove variables in the future, select the pipeline, select **Edit** and then select **Variables**.
- select **Run**


