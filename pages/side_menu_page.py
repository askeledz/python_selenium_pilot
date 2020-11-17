from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSideMenuPage:

    OPEN_BTN = (By.CSS_SELECTOR, '[alt=\'Logo\']')
    CLOSE_BTN = (By.CSS_SELECTOR, '[alt=\'Close menu\']')

    def __init__(self, browser):
        self.browser = browser

    def open_menu(self):
        open_btn = self.browser.find_element(*self.OPEN_BTN)
        open_btn.click()

    def close_menu(self):
        close_btn = self.browser.find_element(*self.CLOSE_BTN)
        close_btn.click()

    @classmethod
    def APP_PICKER_BY_XPATH(cls, app_name):
        xpath = f"//div[@class='app']/nav[@class='navbar']/div[@class='app-drawer']//a[@href='#/{app_name}']"
        return (By.XPATH, xpath)

    def app_open(self, app_name):
        app_elem_btn = self.browser.find_element(*self.APP_PICKER_BY_XPATH(app_name))
        app_elem_btn.click()