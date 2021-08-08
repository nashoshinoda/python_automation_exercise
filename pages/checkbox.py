from datetime import datetime

date_time       = datetime.now()
date            = date_time.strftime("%b/%d/%Y %H:%M:%S")
screenshot_date = date_time.strftime("%m%d%Y-%H%M%S")

class CheckBox:
    def click_checkbox(self, browser):
        browser.find_element_by_css_selector('#checkboxes>input:first-child').click()
        browser.implicitly_wait(15)

    def checkboxes_clicked(self, browser, get_screenshots_path):
        checkboxes_container = browser.find_element_by_id('content')
        checkbox_checked     = browser.find_element_by_css_selector('#checkboxes>input:first-child[checked]')

        if checkbox_checked:
            checkboxes_container.screenshot('{}Checkboxes/CheckedMsg-{}.png'.format(get_screenshots_path, screenshot_date))
            return "Checked"
        else:
            checkboxes_container.screenshot('{}Checkboxes/NotCheckedMsg-{}.png'.format(get_screenshots_path, screenshot_date))
            return "Not checked"
