pipeline {
    agent any
    options {
        // This is required if you want to clean before build
        skipDefaultCheckout(true)
    }
    stages {
       stage('Checkout') {
            steps {
                // Clean before build
                cleanWs()
                //Download feature files
                checkout scm
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Download features') {
            steps {
                //Download feature files
                assertthatBddFeatures(jiraServerUrl: 'http://assertthat-jira.com/jira', credentialsId: '10000', jql: '', tags: '@robot',  mode: 'automated', outputFolder: 'login_tests', projectId: '10000', proxyURI:'', proxyUsername: '',proxyPassword: '')
            }
        }
        stage('Convert Features into Robot') {
            steps {
                bat 'gherkin2robotframework login_tests/1-login.feature'
            }
        }

        stage('Run tests') {
            steps {
                bat 'robot login_tests'
            }
        }

    }
    post{
        always{
                //Generate report
                bat 'python generate_report.py'
                //Upload test results
                assertthatBddReport(jiraServerUrl: 'http://assertthat-jira.com/jira', credentialsId: '10000', jsonReportFolder: './', jsonReportIncludePattern: '**/*.json', projectId: '10000', runName: 'Robot test run', type: 'cucumber',proxyURI:'', proxyUsername: '',proxyPassword: '')
        }
    }
}