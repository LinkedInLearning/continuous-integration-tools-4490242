
## refs
-[Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/index.html)

## setup
- create account as needed
- create new project
- upload files to project 
  - from side menu, select Code -> Repository
  - select Edit -> WebIDE
  - drag files into side bar of editor window
  - right click gitlab-ci.yml and select "Rename..."
  - add a `.` at the beginning of the file name; `gitlab-ci.yml` should now be `.gitlab-ci.yml`.
  - select git icon with badge showing number of files added
  - enter commit message and select "Commit to 'main'"
  - Confirm committing files to the default branch
  - Switch back to repo tab

- side menu, select Build -> Pipelines

## environments
- side menu, Operate -> Environments -> Create environment
- For Production and Staging add name and URL
- 

## variables
- side menu, settings -> CI/CD. Next to "Variables" select **Expand**.
- select "Add variable"
- Add variable key "FUNCTION_NAME" and enter value for production function name.  Under type confirm "Variable (default)".  Under "Environment scope", select **Production**.  Uncheck "Protect variable".  Confirm "Expand variable reference" is selected.  Select "Add variable".  Repeat for staging FUNCTION_NAME.

## credentials
- note that GitLab CI/CD supports OpenID Connect (OIDC) to give your build and deployment jobs access to cloud credentials and services. [How do I configure OIDC for my cloud provider?](https://gitlab.com/help/ci/cloud_services/index#oidc-authorization-with-your-cloud-provider).  TODO: Add instructions later
- Add variable for AWS_DEFAULT_REGION.  uncheck "protect variable".
- Add variable for AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID.  uncheck "protect variable". check "mask variable".
- 

- run the pipeline
- 