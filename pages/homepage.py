from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

date_time       = datetime.now()
date            = date_time.strftime("%b/%d/%Y %H:%M:%S")
screenshot_date = date_time.strftime("%m%d%Y-%H%M%S")

class HomePage:
    def form_authentication(self, browser):
        browser.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()

    def fill_login_form(self, browser, username, password):
        browser.find_element(By.ID, 'username').send_keys(username)
        browser.find_element(By.ID, 'password').send_keys(password)
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def messages(self, browser, get_screenshots_path):
        message_box        = browser.find_element(By.ID, 'flash').get_attribute('class')
        msg_box_screenshot = browser.find_element(By.ID, 'flash')

        if message_box == "flash error":
            msg_box_screenshot.screenshot(f'{get_screenshots_path}Login/FailureMsg-{screenshot_date}.png')
            return "Failure"
        else:
            msg_box_screenshot.screenshot(f'{get_screenshots_path}Login/SuccessMsg-{screenshot_date}.png')
            return "Success"
