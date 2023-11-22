# 04_03 Bitbucket Pipelines
Bitbucket Pipelines is a continuous integration and continuous delivery (CI/CD) service built into Bitbucket.

## Recommended Resources
- [Build, test, and deploy with Pipelines](https://support.atlassian.com/bitbucket-cloud/docs/build-test-and-deploy-with-pipelines/): The official Bitbucket Pipelines documenation.
- [Bitbucket Pipelines configuration reference](https://support.atlassian.com/bitbucket-cloud/docs/bitbucket-pipelines-configuration-reference/)
- [Set up and monitor Bitbucket Deployments](https://support.atlassian.com/bitbucket-cloud/docs/set-up-and-monitor-bitbucket-deployments/)


## Prerequisites
Having the following items in place before starting this lab will help you have a smooth experience.

1. [Atlassian and Bitbucket accounts](https://bitbucket.org/product) are required to host the code for the sample application.
2. An [Amazon Web Services account](https://aws.amazon.com/free/) is needed to deploy the sample application used for the deployment target.
3. The sample application should be in place before starting. See [00_06 About the Exercise Files](../../ch0_introduction/00_06_about_the_exercise_files/README.md) for steps to deploy the sample application.
4. The exercise files for the course should be downloaded and accessible on your local system.

## Implement the Experimental Pipeline
To implement the experimental pipeline in Bitbucket Pipelines, you will need to create a Bitbucket repo, add the exercise files, and configure the pipeline settings.

Before starting these steps, open the Output tab of the Cloudformation stack for the sample application. You'll be referencing values displayed on that tab.

### 1. Create a Bitbucket Repository
1. Log into your Bitbucket account and select the **Repositories** tab.  Then select **Create repository**.
1. Next to "Project name" select **"Select project"** and choose "**Create new project"**.  Enter a name for the project.
2. Next to **"Repository name"**, enter a name for the repo.
3. Determine the desired access level and select or deselect the checkbox next to **"Private repository"**.
4. For **"Default branch name"**, enter **`main`**.
5. For **"Include .gitignore?"**, confirm that **"Yes (recommneded)"** is selected.
6. Expand the "Advanced settings" menu and next to "Language", select **Python**.
7. Select "Create repository"

### 2. Add the Exercise Files
https://support.atlassian.com/bitbucket-cloud/docs/clone-a-git-repository/


### 3. Configure the Pipeline Settings

# add an SSH key
- select top right cog icon -> "Personal Bitbucket settings"
- select "SSH keys"
- If you need to create a key follow the steps to [configure SSH and two-step verification](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/).
- select "Add key"
- Next to "Label", enter a label for they key. paste the contents of your public into the "Key" field.  Select **Add key**.
- go back to the repo and clone it to your local system


# back in the repo
- select "Clone" from the top right
- copy the git clone command to the clipboard.

# local system
- from a terminal, run the clone command on your local system
- cd into the directory where the repo was cloned
- copy the exercise files from this lesson into the repo
- commit the files and push them to the repo

        git add .
        git commit -m "Adding exercise files"
        git push

# add project parameters
- In the web UI, select "Repository settings -> Settings".
- Toggle the switch next to "Enable Pipelines".
- select "Repository variables"
- Enter the name and value for each of the following project parameters.  For the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY, select "Secured".
-
