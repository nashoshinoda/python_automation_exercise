import logging
from pages.homepage import HomePage

class LoginTests:
    def test_login_with_invalid_data(self, browser, invalid_test_data):
        browser.get("https://the-internet.herokuapp.com/")
        HomePage.form_authentication('', browser)
        HomePage.fill_login_form('', browser, invalid_test_data["username"], invalid_test_data["password"])

        if HomePage.messages(self, browser) == "Failure":
            logging.info("You used invalid credentials")
            browser.implicitly_wait(10)

            assert "Failure" in HomePage.messages(self, browser)

    def test_login_with_valid_data(self, browser, valid_test_data):
        browser.get("https://the-internet.herokuapp.com/")
        HomePage.form_authentication('', browser)
        HomePage.fill_login_form('', browser, valid_test_data["username"], valid_test_data["password"])

        if HomePage.messages(self, browser) == "Success":
            logging.info("You used valid credentials")
            browser.implicitly_wait(10)

            assert "Success" in HomePage.messages(self, browser)
