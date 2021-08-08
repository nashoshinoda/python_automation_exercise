import logging
from pytest import mark
from pages.homepage import HomePage

@mark.test_login
class LoginTests:
    def test_login_with_invalid_data(self, browser, url_to_test, invalid_test_data, get_screenshots_path):
        browser.get(url_to_test)
        HomePage.form_authentication(self, browser)
        HomePage.fill_login_form(self, browser, invalid_test_data["username"], invalid_test_data["password"])

        if HomePage.messages(self, browser, get_screenshots_path) == "Failure":
            logging.info("You used invalid credentials")
            browser.implicitly_wait(10)

            assert "Failure" in HomePage.messages(self, browser, get_screenshots_path)

    def test_login_with_valid_data(self, browser, url_to_test, valid_test_data, get_screenshots_path):
        browser.get(url_to_test)
        HomePage.form_authentication(self, browser)
        HomePage.fill_login_form(self, browser, valid_test_data["username"], valid_test_data["password"])

        if HomePage.messages(self, browser, get_screenshots_path) == "Success":
            logging.info("You used valid credentials")
            browser.implicitly_wait(10)

            assert "Success" in HomePage.messages(self, browser, get_screenshots_path)
