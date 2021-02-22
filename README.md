# Robot Framework integration with AssertThat BDD & Cucumber Demo

https://github.com/robotframework/WebDemo was used as a base app for the demo

## Installation

```
pip install -r requirements.txt
```

## Starting demo application

```
python demoapp/server.py
```
After the demo application is started, it is be available in URL http://localhost:7272. 

## Downloading gherkin feature files from Jira

Update ASSERTTHAT_ACCESS_KEY and ASSERTTHAT_SECRET_KEY in `download_features.py` then run

```
python download_features.py
```

## Converting gherkin features to robot files

```
gherkin2robotframework login_tests/1-login.feature 
```

## Running tests
The test cases are located in the login_tests directory. They can be executed using the robot command:
```
robot login_tests
```

## Generating Cucucmber json report

To generate `cucumber.json` report based on Robot Framework `output.xml` run
```
python generate_report.py
```

## Uploading cucumber report to Jira

To uploadgenerated  `cucumber.json` update ASSERTTHAT_ACCESS_KEY and ASSERTTHAT_SECRET_KEY in `upload_report.py` then run
```
python upload_report.py
```

The following feature was uploaded to Jira in order to establish results linking

```
# language: en
Feature: Login

    A test suite with a single Gherkin style test.

    @AUTOMATED 
    Scenario: Valid Login
            Given browser is opened to login page
            When user "demo" logs in with password "mode"
            Then welcome page should be open
```
