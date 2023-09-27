
## refs
- [Variables](https://docs.github.com/en/actions/learn-github-actions/variables)
- [Pricing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)

- create a repo per the usual and upload files

- create environments (?!)
- Settings -> Environments -> New environment
  - Name = Staging
  - Under "Environment variables" select "Add variable"
  - enter FUNCTION_NAME and value for staging function name
  - enter URL and value for staging URL
  - select Environments -> New environment and repeat for Production environment, adding FUNCTION_NAME and URL with their corresponding values
- Add AWS credentials. Left menu, select "Secrets and variables"-> Actions
- Select "New repository secret"
- Add name and values for AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID
- select "variables" tab adn then "New repository variable"
- enter AWS_DEFAULT_REGION for name and the correseponding value for your project
- 
- 
- add the project parameters as environment variables and secrets
- move the workflow file `pipeline.yml` to `./.github/workflows`
- commit the file
- 