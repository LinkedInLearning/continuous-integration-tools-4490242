# reqs
- [Bitbucket Pipelines configuration reference](https://support.atlassian.com/bitbucket-cloud/docs/bitbucket-pipelines-configuration-reference/)
- [Set up and monitor Bitbucket Deployments](https://support.atlassian.com/bitbucket-cloud/docs/set-up-and-monitor-bitbucket-deployments/)


# steps
- create an Atlassian account if needed
- create a prjoject
- "WORKSPACE REPOSITORIES ARE GROUPED INTO PROJECTS. Give your new project a name. You can change this later from this project's settings."
- from Bitbucket home page, select "Create -> Repository"
- Next to "Project name" select "Select project" and choose "Create new project".  enter a name for the project.
- Next to "Repository name", enter a name for the repo.
- Determine the desired access level and select or deselect the checkbox nect to "Private repository".
- "Include a README?" = NO
- "Default branch name" = main
- "Include .gitignore?" = "Yes (recommneded)"
- select "Create repository"

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