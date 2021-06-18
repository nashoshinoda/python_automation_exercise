class HomePage:
    def form_authentication(self, browser):
        form_link = browser.find_element_by_css_selector('a[href="/login"]').click()

    
    def fill_login_form(self, browser, username, password):
        username_field = browser.find_element_by_id('username').send_keys(username)
        password_field = browser.find_element_by_id('password').send_keys(password)
        login_btn      = browser.find_element_by_css_selector('button[type="submit"]').click()
        
    def messages(self, browser):
        message_box   = browser.find_element_by_id('flash').text

        if message_box == "You logged into a secure area!":
            return "Success"
        else:
            return "Failure"
