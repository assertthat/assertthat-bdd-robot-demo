import xmltodict
import re
import json

def get_status(robot_status):
    mapping = {
        'PASS': "passed",
        'FAIL': "failed",
    }
    return mapping.get(robot_status, "Invalid status")

def get_keyword(kw):
    if re.match(r"^Given.+", kw):
        return "Given "
    if re.match(r"^When.+", kw):
        return "When "
    if re.match(r"^Then.+", kw):
        return "Then "
    if re.match(r"^And.+", kw):
        return "And "

def strip_keyword(kw):
    return re.sub(r"^(Given|When|Then|And)\s", "", kw)


def populate_steps(kw, test):
    step = {}
    result = {}
    step['name'] = strip_keyword(kw['@name'])
    result['status'] = get_status(kw['status']['@status'])
    if kw['status']['@status'] == 'FAIL':
        result['error_message'] = test['status']['#text']
    step['result'] = result
    step['keyword'] = get_keyword(kw['@name'])
    step['line'] = 0
    step['match'] = {}
    return step


def populate_elements(test):
    element = {}
    steps = []
    element['name'] = test['@name']
    element['type'] = 'scenario'
    element['keyword'] = 'Scenario'
    try:
        for kw in test['kw']:
            steps.append(populate_steps(kw, test))
    except TypeError:
        # tests is not iterable
        steps.append(populate_steps(kw, test))
    element['steps'] = steps
    return element


def parse_test(tests, elements):
    try:
        for test in tests:
            elements.append(populate_elements(test))
    except TypeError:
        # tests is not iterable
        elements.append(populate_elements(tests))
    return elements


def parse_suites(suites):
    data = {}
    elements = []
    try:
        for suite in suites:
            data['elements'] = parse_test(suite['test'], elements)
    except TypeError:
        # suites is not iterable
        data['elements'] = parse_test(suites['test'], elements)
    return data


with open("output.xml", "r") as myfile:
    xml_input = myfile.read().replace('\n', '')

    all_data = xmltodict.parse(xml_input)['robot']
    report = []
    suite = all_data['suite']
    if 'suite' in suite:
        suite = all_data['suite']['suite']
    data = parse_suites(suite)
    for item in suite['metadata']['item']:
        if "Feature" == item['@name']:
            data['name'] =  item['#text']
    data['description'] = suite['doc']
    data['id'] = suite['@id']
    data['keyword'] = "Feature"
    data['uri'] = all_data['suite']['@source']
    report.append(data)
    with open("cucumber.json", "w") as outfile:
        json.dump(report, outfile)
