# 03_01 AWS CodePipeline and CodeBuild
CodePipeline and CodeBuild are tools for implementing CI/CD in Amazon Web Services.

- With [CodePipeline](https://aws.amazon.com/codepipeline), developers can model the stages of their pipeline and the actions that need to be taken in each stage.
- [CodeBuild](https://aws.amazon.com/codebuild) provides an on-demand build service that can be used with CodePipeline to implement the steps needed to build, deliver, and deploy code.

## Recommended Resources
- [DevOps with AWS on LinkedIn Learning](https://www.linkedin.com/learning/devops-with-aws): Covers AWS automation services including CodeBuild and CodePipeline.

## Prerequisites
Having the following items in place before starting this lab will help you have a smooth experience.

1. A [GitHub account](https://github.com/join) is required to host the code for the sample application.
1. An [Amazon Web Services account](https://aws.amazon.com/free) is needed to deploy the sample application used for the deployment target.
1. The sample application should be in place before starting.  See [00_06 About the Exercise Files](../../ch0_introduction/00_06_about_the_exercise_files/README.md) for steps to deploy the sample application.
1. The exercise files for the course should be downloaded and accessible on your local system.

## Implement the Experimental Pipeline
To implement the experimental pipeline in AWS CodePipeline and CodeBuild, you will need to create a GitHub repo, add the exercise files, and modify the files for your project if needed.

Next, you'll create the project that implements the pipeline.

And finally, you'll trigger the pipeline to deploy the sample application.

Before starting these steps, open the Output tab of the Cloudformation stack for the sample application.  You'll be referencing values displayed on that tab.

### 1. Create a GitHub repo for the sample application code
Because this course covers multiple tools, a dedicated repo is need for each tool to prevent unexpected deployments to the sample-application.

1. Create a new GitHub repo. Give the repo a name and description.  Please select **Public** for the repo visibility to simplify access.  Select the option to add a README file and select **Python** when adding a `.gitignore` file.
2. From the repo home page, select **Add file -> Upload files**.
3. Select **choose your files** and browse to the exercise files for this lesson on your local system.
4. Select all of the files and then select **Open**.
5. After the files have been uploaded, enter a commit message and select **Commit changes**.

### 2. Configure AWS CodePipeline and CodeBuild

#### 2.1 Create the pipeline configuration for the staging environment
1. In the AWS console, open the **CodePipeline** console.
2. Select **Create pipeline**.
3. For "Pipeline name", enter **sample-application**.
4. Confirm that the following are selected under "Service role":

    - **New service role**
    - **Allow AWS CodePipeline to create a service role so it can be used with this new pipeline**

    Select **Next**.

5. Under "Source provider", select **GitHub (Version 2)**.  Select **Connect to GitHub**.
6. A new window should open.  For the "Connection name", enter your GitHub user name. *Note: This is not a requirement.  Its only suggested since this connection can be reused.  Naming the connection after  the GitHub account makes the connection easier to identify if you use it again.*

    Select **Connect to GitHub**.

7. Select **Install a new app**.  You will be redirected to GitHub.
8. On the "Install AWS Connector for GitHub" screen, select your GitHub user name. *Note: If you have two-factor authentication enable, you may be required to reauthenticate.*
9. Under "Repository access", select **All repositories** then select **Save**.
10. After being redirected back to AWS, select **Connect**.
11. Back in the CodePipeline configuration, under "Repository name", search for the repository you created for this lesson.  Under "Branch name", enter **main**.  Confirm **Start the pipeline on source code change** and **CodePipeline default** are selected.  Then select **Next**.
12. Add a build stage - Under "Build provider", select **AWS CodeBuild**.  Confirm "Region" is the same as the region where your sample application is deployed.  Select **Create project**.
13. In the new window that opens, enter **sample-application** for the project name.

    Select the checkbox next to **Restrict number of concurrent builds this project can start**.

    Under "Environment", confirm "Managed image" is selected.  For "Operating System", select **Amazon Linux**.  For "Runtime(s)", select **Standard** and for "Image" select the most recent image for **aws/codebuild/amazonlinux2-x86_64-standard:X.Y**.

    Under "Service role", select **New service role**.  Enter a role name, perhaps **codebuild-sample-application-service-role**.

    Confirm **Use a buildspec file** is selected under "Build specifications".

    Scroll to the bottom of the form and select **Continue to CodePipeline**.

14. Under "Environment variables", select **Add environment variable**.  Add values for the staging environment's function name and URL.  For example:

        - Name=FUNCTION_NAME, Value=sample-application-staging
        - Name=URL, Value=<URL for your sample application staging environment>

    Select **Next**.

15. Add a deploy stage - Select **Skip deploy stage**. Select **Skip**.  *Note: This is required because we can't select CodeBuild as a "Deploy provider" in this stage of the pipeline during pipeline creation.  We'll add the production deployment manually once the pipeline is in place.*
16. Review the configuration and select **Create pipeline**.

Once the pipeline is created, it will start to run.  The "Source" stage will likely pass but the "Build" stage will fail because permissions are not in place for CodeBuild to update the sample-application Lambda environments.

#### 2.2 Add permissions to the CodeBuild role
1. Open the IAM console and select **Roles**.  Select the role you created for CodeBuild.
2. Select **Add permissions -> Attach policies**.
3. Under "Filter by Type" select **Customer managed**.  Select the role that begins with the name you used for the sample application's CloudFormation stack.  Then select **Add permissions**.
4. Go back to the CodePipeline console.  Select the `sample-application` pipeline and select **Release change -> Release**.  This will trigger a new run of the pipeline.
5. Wait for the pipeline to complete.  Confirm that the run completed successfully.  If you encounter any errors, review the configuration for the CodeBuild project and confirm the policy has been correctly attached to the role in use by CodeBuild.

#### 2.2 Add a "Deploy" pipeline stage for production
1. From the pipeline view of the `sample-applicaiton` pipeline, select **Edit**.
2. Under "Edit: Build", select **+ Add stage**.
3. Enter "Production" for the stage name and select **Add stage**.
4. Under "Edit: Production", select **+ Add action group**.
5. Under "Action name", enter **deploy-production**.

    For "Action provider", select **AWS CodeBuild**.  Confirm the region is where the sample application is deployed.

    Under "Input artifacts", select **SourceArtifact**.

    Under "Project name", select the same CodeBuild project created during the staging configuration.

    Under "Environment variables", select **Add environment variable**.  Add values for the staging environment's function name and URL.  For example:

        - Name=FUNCTION_NAME, Value=sample-application-staging
        - Name=URL, Value=<URL for your sample application staging environment>

    Select **Done**.

6. Select **Save -> Save**.
7. From the pipeline view, select **Release change -> Release**. *Note: you can also trigger the pipeline by pushing an update to the repo.*
8. Wait for the pipeline to complete.  Confirm that the run completed successfully.  If you encounter any errors, review the configuration for the CodeBuild project and confirm the policy has been correctly attached to the role in use by CodeBuild.


## Additional Information
- [Build specification reference for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)
- [CodeBuild environment variables](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html)
- [CodeBuild pricing](https://aws.amazon.com/codebuild/pricing/)
- [CodePipeline pricing](https://aws.amazon.com/codepipeline/pricing/)

[Next: 03_02 Azure Pipelines](../03_02_azure_pipelines/README.md)
