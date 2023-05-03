import json
from datetime import datetime
from pytest import fixture
from selenium import webdriver

environment_file = json.load(open("./resources/environment.json"))


def pytest_configure(config):
    """
    `Description:`
    Create a log file, if log_file is not mentioned in *.ini file, for every time a test it's being executed.

    `Parameters:`
    `config:` The pytest config object.
    """
    if not config.option.log_file:
        config.option.log_file = (
            environment_file["reports"]["logs"]
            + "TEST-"
            + datetime.now().strftime("%m%d%Y-%H%M%S")
            + ".log"
        )


@fixture(scope="session")
def browser():
    """
    `Description:`
    Make Chromedriver accesible to this project. We can also add browser options with variable chrome_options.

    `Return:`
    `driver:` Selenium Webdriver Object.
    """
    options = (
        webdriver.ChromeOptions()
    )  # If you want to implement a Chrome option, just add second parameter chrome_options=optionsin line 33 .
    options.add_argument(
        "--headless"
    )  # Execute the tests without open the window browser.
    driver = webdriver.Chrome(
        environment_file["webdrivers"]["chrome"]["path"], options=options
    )
    driver.maximize_window()  # Maximize window in every execution.

    yield driver

    driver.quit()

    return driver


@fixture(scope="session")
def url_to_test():
    web_url = environment_file["url_to_test"]

    return web_url


@fixture
def invalid_test_data():
    invalid_test_user = {
        "username": environment_file["test_credentials"]["invalid_user"]["username"],
        "password": environment_file["test_credentials"]["invalid_user"]["password"],
    }

    return invalid_test_user


@fixture
def valid_test_data():
    valid_test_user = {
        "username": environment_file["test_credentials"]["valid_user"]["username"],
        "password": environment_file["test_credentials"]["valid_user"]["password"],
    }

    return valid_test_user


@fixture
def get_screenshots_path():
    screenshot_path = environment_file["reports"]["screenshots"]

    return screenshot_path
