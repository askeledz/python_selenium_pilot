from selenium.webdriver.common.by import By


class TestLandingPage:
    APP_PICKER = (By.CLASS_NAME, 'app-picker')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    @classmethod
    def APP_PICKER_BY_XPATH(cls, app_name):
        xpath = f"//div[@class='app']/div[@class='full-height main_container']//a[@href='#/{app_name}']/div[@class='app__name']"
        return (By.XPATH, xpath)

    @classmethod
    def APP_PICKER_BY_LINK_TEXT(cls, linktext):
        return (By.LINK_TEXT, linktext)

    def __init__(self, browser):
        self.browser = browser

    def app_count(self, linktext):
        phrase_results = self.browser.find_elements(*self.APP_PICKER_BY_LINK_TEXT(linktext))
        return len(phrase_results)

    def app_open(self, app_name):
        app_elem_btn = self.browser.find_element(*self.APP_PICKER_BY_XPATH(app_name))
        app_elem_btn.click()