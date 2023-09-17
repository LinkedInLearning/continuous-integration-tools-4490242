# 02_02 Codeship
> CloudBees CodeShip is a Software as a Service (SaaS) solution that empowers engineering teams to implement and optimize CI and CD in the cloud. It helps small and growing teams develop everything from simple web applications to modern microservice architectures to achieve fast, secure and frequent code delivery.

TODO: [End of free builds for CloudBees CodeShip #12758](https://github.com/checkstyle/checkstyle/issues/12758)

## Pricing
Plans under [Codeship Basic](https://www.cloudbees.com/codeship/features-pricing#basic-features):

- **Starter**: For the individual who wants to test and deploy with CodeShip.

    - $49/MO
    - Unlimited builds
    - 1 Concurrent Builds
    - 2 Parallel Test Pipelines


- **Essential**: For small teams looking to benefit from CI/CD for their projects.

    - $99/MO
    - Unlimited builds
    - 2 Concurrent Builds
    - 2 Parallel Test Pipelines

- **Power**: For larger teams working on bigger projects simultaneously.

    - $399/MO
    - Unlimited builds
    - 4 Concurrent Builds
    - 4 Parallel Test Pipelines

## Reccommended Resources

## Prequisites
Having the following items in place before starting this lab will help you have a smooth experience.

1. A [GitHub account](https://github.com/join) is required to host the code for the sample application. *NOTE: You need to be an admin for any repositories you want to integrate with Travis CI.*
2. A [Codeship account](https://app.codeship.com/).
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

## Configure your Travis CI account, repo connection, and project parameters
### 1. Set up your Travis CI account
### 2. Repo connection and project parameters
### Run the pipeline by creating the Travis configuration file
