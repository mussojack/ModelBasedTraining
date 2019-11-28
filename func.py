from selenium import webdriver
from global_func import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
global driver
executionstatus = None
log = logger.log


def close_browser():
    global driver
    driver.quit()
    return


def v_Start():
    global driver
    driver = webdriver.Chrome('C:/ModelBasedTraining/drivers/chromedriver')
    return


def e_OpenGoogle():
    global driver
    driver.get("https://www.google.org")
    return


def v_GoogleOpened():
    global driver
    WebDriverWait(driver, 10)
    try:
        assert "Google" in driver.title
    except:
        fail_test_case()
    return


def e_OpenTestscoutsHomePageWithLink():
    global driver
    log.info("[ACT] Open Testscouts Homepage through its link")
    driver.get("http://testscouts.se/")
    return


def e_OpenTestscoutsHomePageWithButton():
    global driver
    log.info("[ACT] Open Testscouts Homepage through the current sites button")
    button = driver.find_element_by_id("menu-item-2928")
    button.click()
    return


def v_TestscoutsHomePage():
    global driver
    WebDriverWait(driver, 10)
    try:
        log.info("[VS] Verifying that we are at the homepage")
        assert "Testscout AB | Vi älskar test!Testscout AB | Vi älskar test!" in driver.title
    except:
        fail_test_case('Homepage')
    return


def e_OpenTestscoutsOffersWithLink():
    global driver
    log.info("[ACT] Open Testscouts Offers page through its link")
    driver.get("http://testscouts.se/erbjudanden/")
    return


def e_OpenTestscoutsOffersWithButton():
    global driver
    log.info("[ACT] Open Testscouts Offers page through the current site button")
    button = driver.find_element_by_id("menu-item-2935")
    button.click()
    return


def v_TestscoutsOffers():
    global driver
    WebDriverWait(driver, 10)
    try:
        log.info("[VS] Verifying that we are at the offers page")
        assert "Erbjudanden | Testscout ABTestscout AB" in driver.title
    except:
        fail_test_case('Offers page')
    return


def e_OpenTestscoutsWorkWithUsWithLink():
    global driver
    log.info("[ACT] Open Testscouts Work With Us page through its link")
    driver.get("http://testscouts.se/jobb-hos-oss/")
    return


def e_OpenTestscoutsWorkWithUsWithButton():
    global driver
    log.info("[ACT] Open Testscouts Work With Us page through the current sites button")
    button = driver.find_element_by_id("menu-item-2936")
    button.click()
    return


def v_TestscoutsWorkWithUs():
    global driver
    WebDriverWait(driver, 10)
    try:
        log.info("[VS] Verifying that we are at the Work With Us page")
        assert "Jobba hos oss | Testscout ABTestscout AB" in driver.title
    except:
        fail_test_case('Work With Us page')
    return


def e_OpenTestscoutsAboutWithLink():
    global driver
    log.info("[ACT] Open Testscouts About page through its link")
    driver.get("http://testscouts.se/om-oss/")
    return


def e_OpenTestscoutsAboutWithButton():
    global driver
    log.info("[ACT] Open Testscouts About page through the current sites button")
    button = driver.find_element_by_id("menu-item-2956")
    button.click()
    return


def v_TestscoutsAbout():
    global driver
    WebDriverWait(driver, 10)
    try:
        log.info("[VS] Verifying that we are at the About page")
        assert "Om Test Scouts | Testscout ABTestscout AB" in driver.title
    except:
        fail_test_case('About page')
    return



def e_OpenTestscoutsWeHireWithLink():
    global driver
    log.info("[ACT] Open Testscouts We Hire through its link")
    driver.get("http://testscouts.se/jobb-hos-oss/")
    return


def e_OpenTestscoutsWeHireWithButton():
    global driver
    log.info("[ACT] Open Testscouts We Hire through the current sites button")
    button = driver.find_element_by_id("header-controls-right")
    button.click()
    return


def v_TestscoutsWeHire():
    global driver
    WebDriverWait(driver, 10)
    try:
        log.info("[VS] Verifying that we are at the We Hire page")
        assert "Jobba hos oss | Testscout ABTestscout AB" in driver.title
    except:
        fail_test_case('We Hire page')
    return


