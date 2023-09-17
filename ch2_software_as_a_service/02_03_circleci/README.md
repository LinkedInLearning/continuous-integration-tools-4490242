# 02_03 CircleCI

## Reccommended Resources
- [Quickstart guide](https://circleci.com/docs/getting-started/)

## Prequisites
Having the following items in place before starting this lab will help you have a smooth experience.

1. A [GitHub account](https://github.com/join) is required to host the code for the sample application. *NOTE: You may need to be an admin for any repositories you want to integrate with CircleCI.*
2. A [CircleCI account](https://circleci.com/signup/).
3. An [Amazon Web Services account](https://aws.amazon.com/free) is needed to deploy and host the sample application used for the deployment target.
4. The sample application should be in place before starting.  See [00_06 About the Exercise Files](../../ch0_introduction/00_06_about_the_exercise_files/README.md) for steps to deploy the sample application.
5. The exercise files for the course should be downloaded and accessible on your local system.

## Create a GitHub repo for the sample application code
Because this course covers multiple tools, a dedicated repo is need for each tool to prevent unexpected deployments to the sample-application.

1. Create a new GitHub repo. Give the repo a name and description.  Please select **Public** for the repo visibility to simplify access.  Select the option to add a README file and select **Python** when adding a `.gitignore` file.
2. From ther repo home page, select **Add file -> Upload files**.
3. Select **choose your files** and browse to the exercise files for this lesson on your local system.
4. Select all of the files and then select **Open**.
5. After the files have been uploaded, enter a commit message and select **Commit changes**.

## Configure your CircleCI account, repo connection, and project parameters
### 1. Set up your CircleCI account
Follow the directions to [sign up and try CircleCI](https://circleci.com/docs/first-steps/) to create your account.

CircleCI supports GitHub, Bitbucket, and GitLab projects.  This lab focuses on the GitHub integration.

Once you have your account in place, proceed to set up a connection to the repo where the exercise files are stored and setting up the project parameters.

### 2. Repo connection and project parameters
#### 2.1 Connect to GitHub repo
1. Log into your CircleCI account and, from the meno on the left-hand side of the page, select **Projects**.
2. Locate the repo you created to store the exercise files and select the **Set Up Project** button next to it.  *Note: If you've already set up the project, select the three dots next to "Unfollow Project" and select **Project Settings**. Proceed to **Configure project parameters** below).*
3. 

#### 2.2 Configure project paramters


### Run the pipeline by creating the CircleCI configuration file


- Starter workflows
- Very competitive pricing with generous limits
- [AWS CLI orb](https://circleci.com/developer/orbs/orb/circleci/aws-cli#usage-install_aws_cli)
- error messages can be checked via AI ("no code or proprietary data shared")
