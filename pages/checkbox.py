from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

date_time       = datetime.now()
date            = date_time.strftime("%b/%d/%Y %H:%M:%S")
screenshot_date = date_time.strftime("%m%d%Y-%H%M%S")

class CheckBox:
    def click_checkbox(self, browser):
        browser.find_element(By.CSS_SELECTOR, '#checkboxes>input:first-child').click()
        browser.implicitly_wait(15)

    def checkboxes_clicked(self, browser, get_screenshots_path):
        checkboxes_container = browser.find_element(By.ID, 'content')
        checkbox_checked     = browser.find_element(By.CSS_SELECTOR, '#checkboxes>input:first-child[checked]')

        if checkbox_checked:
            checkboxes_container.screenshot(f'{get_screenshots_path}Checkboxes/CheckedMsg-{screenshot_date}.png')
            return "Checked"
        else:
            checkboxes_container.screenshot('{get_screenshots_path}Checkboxes/NotCheckedMsg-{screenshot_date}.png')
            return "Not checked"
