TODO: create a billing account as a prereq to the lab

# Resources
- [Cloud Build](https://cloud.google.com/build)
- [Substituting variable values](https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values)
- [Using user-defined variable substituions](https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions)
- [Google Cloud Build official builder images](https://github.com/GoogleCloudPlatform/cloud-builders#google-cloud-build-official-builder-images)
# create a project first (?)
# Implement the pipeline
- create a new project
- confirm new project is selected
- from the Google Cloud home page, serch for "cloud build" and select it in the search results
- Enable the cloud build API for your project
- enable billing for the project
- select billing account
- select cloud build -> dashboard
- select set upnbuild triggers
- add name  and description
- select create host connection
- under event, select "Repository event that invokes trigger Push to a branch"
- select repository -> connect new respository
- confirm "GitHub (Cloud Build GitHub App)" is selected; select continue
- select "Authorize Google Cloud Build"
- select "install google cloud build"
- select your username or organization, select "Only select repositories", select your the repo you created, select install.
- back in GCP UI, select the repository you just installed
- select check box next to "I understand that GitHub content for the selected repositories will be...", select "connect".
- Under Configuration, confirm Type is Autodetected
- select create
- next to trigger, select "RUN" -> RUN TRIGGER
- 

# add secrets
- from the google cloud home page, search for secret manager
- confirm your project is selected and enable the secret manager API
- On the secret manager home page, select create secret
- enter secret name and value.  under encryption, confirm "Google-managed encryption key" is selected.
- select create secret
- Repeat for AWS_SECRET_ACCESS_KEY
- grant Required IAM permissions
Grant the Secret Manager Secret Accessor (roles/secretmanager.secretAccessor) IAM role for the secret to the Cloud Build service account:

Open the Secret Manager page in the Google Cloud console:

Go to the Secret Manager page

Select the checkbox next to both secret names.

If it is not already open, click Show info panel to open the panel.

In the panel, under Permissions, click Add principal.

In the New principals textbox, enter the email address of your Cloud Build service account of the form PROJECT_NUMBER@cloudbuild.gserviceaccount.com. PROJECT_NUMBER is the project number of the project where you are running builds. You can find the project number in your Project settings page (three dots at top right of page, select project settings, locate project number)

In the Select a role drop-down box, select Secret Manager Secret Accessor.

Click Save.
216887157717@cloudbuild.gserviceaccount.com

# Or encrypt with KMS?
- from the google cloud home page, search for KMS
- on the Cloud Key Management Service (KMS) API  page, confirm your project is selected and enable the API
- do the whole key ring thing
  - create a key ring
  - add a key
  - encrypt the values
  - give cloud build permission to decrypt
  - update the cloud build config with the key and the encrypted values
  - 


- name: 'gcr.io/cloud-builders/gcloud'
  entrypoint: 'bash'
  args:
  - '-c'
  - |
    echo "Fetching AWS keys from Secret Manager"
    gcloud secrets versions access latest --secret=AWS_ACCESS_KEY_ID > /workspace/aws_access_key_id.txt
    gcloud secrets versions access latest --secret=AWS_SECRET_ACCESS_KEY > /workspace/aws_secret_access_key.txt

# Pricing
New customers get $300 in free credits to spend on Cloud Build. All customers get 2,500 build-minutes free per month, not charged against your credits. 


FREE Tier USD 0.00/minutes of build time Starting after: 0 minutes of build time/month

TIER 1 USD $0.006 /minutes of build time Starting after: 2.5K minutes of build time/month