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
                scm checkout
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Download features') {
            steps {
                //Download feature files
                assertthatBddFeatures(credentialsId: '10000', jql: '', tags: '@robot',  mode: 'automated', outputFolder: 'login_tests', projectId: '10000', proxyURI:'', proxyUsername: '',proxyPassword: '')
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

        stage('Generate report') {
            steps {
                bat 'python generate_report.py'
            }
        }

    }
    post{
        always{
                //Upload test results
                assertthatBddReport(credentialsId: '10000', jsonReportFolder: 'report', jsonReportIncludePattern: '**/*.json', projectId: '10000', runName: 'Robot test run', type: 'cucumber',proxyURI:'', proxyUsername: '',proxyPassword: '')
        }
    }
}