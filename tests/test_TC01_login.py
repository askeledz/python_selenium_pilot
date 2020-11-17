import pytest
import time
import json
from datetime import datetime

from pages.test_login_page import TestLoginPage
from pages.test_landing_page import TestLandingPage
from pages.test_page import TestPage
from pages.test_side_menu_page import TestSideMenuPage

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#CONFIG_PATH = 'tests/config.json'
CONFIG_PATH = 'config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
  if 'browser' not in config:
    raise Exception('The config file does not contain "browser"')
  elif config['browser'] not in SUPPORTED_BROWSERS:
    raise Exception(f'"{config["browser"]}" is not a supported browser')
  return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
  return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def config_username(config):
  return config['username']

@pytest.fixture(scope='session')
def config_password(config):
  return config['password']

@pytest.fixture(scope='session')
def config_url(config):
  return config['url']

@pytest.fixture
def browser(config_browser, config_wait_time):
  if config_browser == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
  elif config_browser == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  else:
    raise Exception(f'"{config_browser}" is not a supported browser')
  driver.implicitly_wait(config_wait_time)
  yield driver
  driver.quit()


def test_esp_login(browser, config_username, config_password, config_url):

    # Login
    login_page = TestLoginPage(browser)
    login_page.load(config_url)
    login_page.login(config_username, config_password)

    # Verify that  Landing page is loaded
    landing_page = TestLandingPage(browser)
    assert landing_page.app_count('wer') == 1
    assert landing_page.app_count('ewtyr') == 1
    assert landing_page.app_count('ery') == 1
    assert landing_page.app_count('eyry') == 1
    assert landing_page.app_count('eyr') == 1
    assert landing_page.app_count('ery') == 1

    #Open side menu
    side_menu_page = TestSideMenuPage(browser)
    side_menu_page.open_menu()
    side_menu_page.app_open('app/72')
    time.sleep(3)

    test_page = TestPage(browser)
    test_page.frame_switch_css('iframe')

    # current date and time

    NAME_SUFFIX = datetime.now().microsecond.__str__()

    test_page.case_form( "AS" + NAME_SUFFIX, 'asd', 'Asd', 'asdf')
    print("test")

