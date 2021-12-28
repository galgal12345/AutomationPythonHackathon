"""
conftest.py
"""

import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.listener import MyListener
from utils.manage_pages import ManagePages
from page_objects.web.login_page import LoginPage
from utils.common_ops import get_data
from applitools.selenium import Eyes, Target, BatchInfo, ClassicRunner

# WEB
driver: EventFiringWebDriver
wait: WebDriverWait
action = None
e_driver: WebDriver
# MOBILE
reportDirectory = 'reports'
reportFormat = 'xml'
dc = {}
testName = 'Untitled'

# API
url = 'https://api.chucknorris.io/jokes/'
header = {'Content-type': 'application/json'}

# ELECTRON
electron_app = "C:\\Automation\\Electrons\\Electron API Demos.exe"
edriver = "C:\\electrondriver.exe"


# PAGES
# Web


@pytest.fixture(scope='class')
def my_web_starter(request: FixtureRequest):
    global driver, wait, e_driver
    if get_data("Browser") == "chrome":
        e_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif get_data("Browser") == "edge":
        e_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif get_data("Browser") == "firefox":
        e_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        e_driver = None
        print("Wrong input, unrecognized browser")
    driver = EventFiringWebDriver(e_driver, MyListener())
    driver.maximize_window()
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = globals()['driver']
    wait = WebDriverWait(driver, 10)
    globals()['wait'] = wait
    ManagePages.init_web_pages(driver)
    yield driver
    # driver.quit()


@pytest.fixture(scope='function')
def my_web_before_method(request: FixtureRequest):
    global driver
    driver.get("http://localhost:4000")


@pytest.fixture(scope='class')
def my_mobile_starter(request):
    dc['reportDirectory'] = reportDirectory
    dc['reportFormat'] = reportFormat
    dc['testName'] = testName
    dc['udid'] = '16af5295'
    dc['appPackage'] = 'com.financial.calculator'
    dc['appActivity'] = '.FinancialCalculators'
    dc['platformName'] = 'android'
    driver = webdriver.Remote('http://localhost:4722/wd/hub', dc)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def my_api_starter(request):
    print()


@pytest.fixture(scope='class')
def my_desktop_starter(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def my_electron_starter(request):
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(name="runner", scope="session")
def runner_setup():
    """
    One test runner for all tests. Print test results in the end of execution.
    """
    runner = ClassicRunner()
    yield runner


@pytest.fixture(name="eyes")
def applitools_set_up(runner):
    global driver, e_driver
    eyes = Eyes(runner)
    eyes.api_key = "Y7YclUHy7uKAB110GYMAC9bTPBHimPnc3wUQ4UyPgBtRs110"
    eyes.open(e_driver, "Hack", "Dismiss test")
    yield eyes
