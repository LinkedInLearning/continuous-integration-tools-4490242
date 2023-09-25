# resources
- [Specify jobs in your pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/phases)


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


