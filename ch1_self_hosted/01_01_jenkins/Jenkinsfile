pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID         = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY     = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION        = 'UPDATE_THIS_VALUE'
        STAGING_FUNCTION_NAME     = 'UPDATE_THIS_VALUE'
        STAGING_URL               = 'UPDATE_THIS_VALUE'
        PRODUCTION_FUNCTION_NAME  = 'UPDATE_THIS_VALUE'
        PRODUCTION_URL            = 'UPDATE_THIS_VALUE'
    }

    stages {
        stage('Requirements') {
            steps {
                sh('''
                    #!/bin/bash
                    python3 -m venv local
                    . ./local/bin/activate
                    make requirements
                ''')
            }
        }

        stage('Check') {
            parallel {
                stage('Check:Lint') {
                    steps {
                        sh('''
                            #!/bin/bash
                            . ./local/bin/activate
                            make check lint
                        ''')
                    }
                }

                stage('Check:Test') {
                    steps {
                        sh('''
                            #!/bin/bash
                            . ./local/bin/activate
                            make test
                        ''')
                    }
                }
            }
        }

        stage('Build') {
            steps {
                sh('''
                    #!/bin/bash
                    make build
                ''')
            }
        }

        stage('Deploy Staging') {
            steps {
                sh('''
                    #!/bin/bash
                    make deploy \
                        PLATFORM="Jenkins" \
                        FUNCTION=${STAGING_FUNCTION_NAME} \
                        VERSION=${GIT_COMMIT} \
                        BUILD_NUMBER=${BUILD_NUMBER}
                ''')
            }
        }

        stage('Test Staging') {
            steps {
                sh('''
                    #!/bin/bash
                    make testdeployment URL=${STAGING_URL} VERSION=${GIT_COMMIT}
                ''')
            }
        }

        stage('Deploy Production') {
            steps {
                sh('''
                    #!/bin/bash
                    make deploy \
                        PLATFORM="Jenkins" \
                        FUNCTION=${PRODUCTION_FUNCTION_NAME} \
                        VERSION=${GIT_COMMIT} \
                        BUILD_NUMBER=${BUILD_NUMBER}
                ''')
            }
        }

        stage('Test Production') {
            steps {
                sh('''
                    #!/bin/bash
                    make testdeployment URL=${PRODUCTION_URL} VERSION=${GIT_COMMIT}
                ''')
            }
        }
    }
    
    post {
        success {
            // Archive the lambda.zip file as an artifact
            archiveArtifacts artifacts: 'lambda.zip', allowEmptyArchive: false
    }
}
