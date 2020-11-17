from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLoginPage:

    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'submit-btn')

    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

    def login(self, usr, pas):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        login_btn = self.browser.find_element(*self.LOGIN_BTN)
        username_input.send_keys(usr)
        password_input.send_keys(pas)
        login_btn.click()
