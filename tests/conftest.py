import logging
from datetime import datetime
from pytest import fixture
from selenium import webdriver

def pytest_configure(config):
    '''
    `Description:`
    Create a log file, if log_file is not mentioned in *.ini file, for every time a test it's being executed.

    `Parameters:`
    `config:` The pytest config object.
    '''
    if not config.option.log_file:
        timestamp              = datetime.now().strftime("%m%d%Y-%H%M%S")
        config.option.log_file = './reports/log/TEST-' + timestamp + '.log'

@fixture(scope="session")
def browser():
    '''
    `Description:`
    Make Chromedriver accesible to this project. We can also add browser options with variable chrome_options.

    `Return:`
    `driver:` Selenium Webdriver Object.
    '''
    options = webdriver.ChromeOptions()  # If you want to implement a Chrome option, just add second parameter chrome_options=optionsin line 33 .
    options.add_argument('--headless')   # Execute the tests without open the window browser.
    driver = webdriver.Chrome('./resources/chromedriver.exe', options=options)
    driver.maximize_window()

    yield driver

    driver.quit()

    return driver

@fixture
def invalid_test_data():
    invalid_test_user = {
        "username": "wronguser",
        "password": "wrongpassword"
    }

    return invalid_test_user

@fixture
def valid_test_data():
    valid_test_user = {
        "username": "tomsmith",
        "password": "SuperSecretPassword!"
    }

    return valid_test_user
