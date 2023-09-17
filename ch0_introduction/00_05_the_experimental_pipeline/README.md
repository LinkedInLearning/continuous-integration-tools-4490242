# 00_05 The Experimental Pipeline
As we explore CICD tools, it's helpful to have a sample pipeline to work with. We'll be configuring a pipeline that builds, tests, and deploys a web application. Our application is a Python script that serves JSON data over a simple API.

TODO: Add an image for reference

## Pipeline Steps
The pipeline will have seven steps.  Each step must be successful for any following steps to be initiated.

1. Requirements: Install any tools or libraries needed to test, build, and deploy the application.

2. Check: Lint the code and run integration tests.

3. Build: Package the code into a deployable artifact.

4. Deploy Staging: Deploy the code to the staging environment.

5. Test Staging: Test the staging environment.  A successful test will allow the production deployment to proceed.

6. Deploy Production: Deploy the code to the production environment.

7. Test Production: Test the production environment to confirm the application has been deployed successfully.