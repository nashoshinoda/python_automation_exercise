import os
import json

def execute_tests(self):
    test_suite_list = json.load(open('./launch/test_suite.json'))

    for mark in test_suite_list:
        os.system('pytest -m "{}"'.format(mark["test_case_mark"]))
