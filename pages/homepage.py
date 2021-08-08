from datetime import datetime

date_time       = datetime.now()
date            = date_time.strftime("%b/%d/%Y %H:%M:%S")
screenshot_date = date_time.strftime("%m%d%Y-%H%M%S")

class HomePage:
    def form_authentication(self, browser):
        browser.find_element_by_css_selector('a[href="/login"]').click()

    def fill_login_form(self, browser, username, password):
        browser.find_element_by_id('username').send_keys(username)
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_css_selector('button[type="submit"]').click()

    def messages(self, browser, get_screenshots_path):
        message_box        = browser.find_element_by_id('flash').get_attribute('class')
        msg_box_screenshot = browser.find_element_by_id('flash')

        if message_box == "flash error":
            msg_box_screenshot.screenshot('{}Login/FailureMsg-{}.png'.format(get_screenshots_path, screenshot_date))
            return "Failure"
        else:
            msg_box_screenshot.screenshot('{}Login/SuccessMsg-{}.png'.format(get_screenshots_path, screenshot_date))
            return "Success"
