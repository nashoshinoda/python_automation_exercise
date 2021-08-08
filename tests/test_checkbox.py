import logging
from pytest import mark
from pages.checkbox import CheckBox

@mark.test_checkbox
class CheckboxTests:
    def test_select_first_checkbox(self, browser, url_to_test, get_screenshots_path):
        browser.get("{}/checkboxes".format(url_to_test))
        CheckBox.click_checkbox(self, browser)

        if CheckBox.checkboxes_clicked(self, browser, get_screenshots_path) == "Checked":
            logging.info("First checkbox checked")
            browser.implicitly_wait(15)

            assert "Checked" in CheckBox.checkboxes_clicked(self, browser, get_screenshots_path)
