import func
from global_func import *
import global_func
import sys
import json
import subprocess
import logger
file = 'test.json'
log = logger.log


def generate_test_case(file):

    cmd_line = 'java -jar "graphwalker-cli-4.0.1.jar" offline -m ' + file + ' "random(edge_coverage(100))"'
    output = subprocess.check_output(cmd_line, shell=True)

    test_case = str(output)
    test_case = test_case[3:-2]
    test_case = test_case.replace("\\r\\n", "")
    test_case = test_case.replace('"currentElementName":"', "")
    test_case = test_case.replace('"', "")
    test_case = test_case[:-4]
    test_case = test_case.split("}{")
    print(test_case)

    set_execution_status('started')

    execute_test_case(test_case)

    end_of_test_case()

    return


def execute_test_case(test_case):
    for function in test_case:
        method_to_call = getattr(func, function)
        method_to_call()
    return


def end_of_test_case():
    if get_execution_status() != "fail":
        log.info("Test case ended with verdict: Pass")
        func.close_browser()
        sys.exit(1)

    else:
        log.log(35, "Test case ended with verdict: Fail")
        func.close_browser()
        sys.exit(1)


generate_test_case(file)