import logger

log = logger.log


def fail_test_case(page):
    set_execution_status('fail')
    log.log(35, 'Failed to verify ' + page)
    return


def get_execution_status():
    return execution_status


def set_execution_status(status):
    global execution_status
    execution_status = status
    return


def end_of_test_case():

    return
