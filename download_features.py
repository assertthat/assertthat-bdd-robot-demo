from assertthat_bdd.jira_integration import JiraConnector

JiraConnector.download_features(
    # Jira project id e.g. 10001
    project_id='10000',
    # Optional can be supplied as environment variable ASSERTTHAT_ACCESS_KEY
    access_key='admin',
    # Optional can be supplied as environment variable ASSERTTHAT_SECRET_KEY
    secret_key='admin',

    jira_server_url='http://assertthat-jira.com/jira',
    # Optional - default ./features
    output_folder='./login_tests',
     tags='@robot',
    # Optional - all features downloaded by default - should be a valid JQL
    # jql = 'project = XX AND key in ('XXX-1')',
    # Optional - default automated (can be one of: manual/automated/both)
    # mode='both',
    # Optional - Detail the proxy with the specific scheme e.g.'10.10.10.10:1010'
    # proxy_uri='proxyip:port',
    # proxy_uri= 'proxy_uri',
    # Optional - user name which will be used for proxy authentication.*/
    # proxy_username='username',
    # Optional - password which will be used for proxy authentication.*/
    # proxy_password='password'
)