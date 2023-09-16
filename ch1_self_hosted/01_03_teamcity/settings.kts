import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.buildFeatures.perfmon
import jetbrains.buildServer.configs.kotlin.buildSteps.script
import jetbrains.buildServer.configs.kotlin.projectFeatures.githubIssues
import jetbrains.buildServer.configs.kotlin.triggers.vcs
import jetbrains.buildServer.configs.kotlin.vcs.GitVcsRoot

/*
The settings script is an entry point for defining a TeamCity
project hierarchy. The script should contain a single call to the
project() function with a Project instance or an init function as
an argument.

VcsRoots, BuildTypes, Templates, and subprojects can be
registered inside the project using the vcsRoot(), buildType(),
template(), and subProject() methods respectively.

To debug settings scripts in command-line, run the

    mvnDebug org.jetbrains.teamcity:teamcity-configs-maven-plugin:generate

command and attach your debugger to the port 8000.

To debug in IntelliJ Idea, open the 'Maven Projects' tool window (View
-> Tool Windows -> Maven Projects), find the generate task node
(Plugins -> teamcity-configs -> teamcity-configs:generate), the
'Debug' option is available in the context menu for the task.
*/

version = "2023.05"

project {

    vcsRoot(HttpsGithubComConsole6500teamcityCiCdGitRefsHeadsMain)

    buildType(Build)

    features {
        githubIssues {
            id = "PROJECT_EXT_2"
            displayName = "console6500/teamcity-ci-cd"
            repositoryURL = "https://github.com/console6500/teamcity-ci-cd"
            param("tokenId", "")
        }
    }
}

object Build : BuildType({
    name = "Build"

    enablePersonalBuilds = false
    artifactRules = "+:lambda.zip"
    maxRunningBuilds = 1
    publishArtifacts = PublishMode.SUCCESSFUL

    params {
        param("env.PRODUCTION_URL", "https://x2kwlkaff4pjobsjjtgl4ssdce0ceiof.lambda-url.us-east-2.on.aws/")
        param("env.STAGING_FUNCTION_NAME", "sample-application-staging")
        password("env.AWS_SECRET_ACCESS_KEY", "zxx629b65f16af5fd36e7d99513393750879f34b2c3a8513227b4686d3ed0e0d6f2c4081c41e0319c24775d03cbe80d301b", display = ParameterDisplay.HIDDEN, readOnly = true)
        password("env.AWS_ACCESS_KEY_ID", "zxx4d0e7d7c22921af9ea5cf855dc00d5344585f1e1d76bb021", display = ParameterDisplay.HIDDEN, readOnly = true)
        param("env.AWS_DEFAULT_REGION", "us-east-2")
        param("env.STAGING_URL", "https://nphukndnle4gm37v3bffyhdvri0dvzaz.lambda-url.us-east-2.on.aws/")
        param("env.PRODUCTION_FUNCTION_NAME", "sample-application-production")
    }

    vcs {
        root(HttpsGithubComConsole6500teamcityCiCdGitRefsHeadsMain)
    }

    steps {
        script {
            name = "Requirements"
            scriptContent = """
                python3 -m venv local
                . ./local/bin/activate
                make requirements
            """.trimIndent()
        }
        script {
            name = "Check"
            scriptContent = """
                . ./local/bin/activate
                make check lint test
            """.trimIndent()
        }
        script {
            name = "Build"
            scriptContent = "make build"
        }
        script {
            name = "Deploy Staging"
            scriptContent = """
                make deploy \
                	ENVIRONMENT="Staging" \
                	PLATFORM="TeamCity" \
                    FUNCTION=${'$'}{STAGING_FUNCTION_NAME} \
                    VERSION=${'$'}{BUILD_VCS_NUMBER} \
                    BUILD_NUMBER=${'$'}{BUILD_NUMBER}
            """.trimIndent()
        }
        script {
            name = "Test Staging"
            scriptContent = "make testdeployment URL=${'$'}{STAGING_URL}"
        }
        script {
            name = "Deploy Production"
            scriptContent = """
                make deploy \
                	ENVIRONMENT="Production" \
                	PLATFORM="TeamCity" \
                    FUNCTION=${'$'}{PRODUCTION_FUNCTION_NAME} \
                    VERSION=${'$'}{BUILD_VCS_NUMBER} \
                    BUILD_NUMBER=${'$'}{BUILD_NUMBER}
            """.trimIndent()
        }
        script {
            name = "Test Production"
            scriptContent = "make testdeployment URL=${'$'}{PRODUCTION_URL}"
        }
    }

    triggers {
        vcs {
        }
    }

    features {
        perfmon {
        }
    }
})

object HttpsGithubComConsole6500teamcityCiCdGitRefsHeadsMain : GitVcsRoot({
    name = "https://github.com/console6500/teamcity-ci-cd.git#refs/heads/main"
    url = "https://github.com/console6500/teamcity-ci-cd.git"
    branch = "refs/heads/main"
    branchSpec = "refs/heads/*"
})
