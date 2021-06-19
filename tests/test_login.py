from pages.homepage import HomePage
import time

class LoginTests:
    def test_login_with_invalid_data(self, browser, invalid_test_data):
        browser.get("https://the-internet.herokuapp.com/")
        HomePage.form_authentication('', browser)
        HomePage.fill_login_form('', browser, invalid_test_data["username"], invalid_test_data["password"])
        
        if HomePage.messages == "Failure":
            logging.info("You used invalid credentials")
            assert "invalid" in HomePage.messages

    def test_login_with_valid_data(self, browser, valid_test_data):
        browser.get("https://the-internet.herokuapp.com/")
        HomePage.form_authentication('', browser)
        HomePage.fill_login_form('', browser, valid_test_data["username"], valid_test_data["password"])
        
        if HomePage.messages == "Success":
            logging.info("You used valid credentials")
            assert "logged" in HomePage.messages
