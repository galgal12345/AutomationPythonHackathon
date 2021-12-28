import pytest
import requests
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.common_ops import get_data
from utils.managers.listeners import EventListener
# ----------------------------------------
# WEB
from utils.managers.manage_pages import ManagePages

driver = None
action = None

# ----------------------------------------
# MOBILE
reportDirectory = get_data("Reports")
reportFormat = get_data("Xml")
dc = {}
testName = get_data("Untitled")

# ----------------------------------------
# API
url = 'https://api.chucknorris.io/jokes/'
header = {'Content-type': 'application/json'}

# ----------------------------------------
# ELECTRON
electron_app = "C:\\Automation\\Electrons\\Electron API Demos.exe"
edriver = "C:\\electrondriver.exe"


# ----------------------------------------

@pytest.fixture(scope='class')
def my_web_starter(request):
    if get_data("Browser") == "chrome":
        edriver = webdriver.Chrome(ChromeDriverManager().install())
    elif get_data("Browser") == "edge":
        edriver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif get_data("Browser") == "firefox":
        edriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        edriver = None
        print("Wrong input, unrecognized browser")

    edriver.get("https://www.google.com/")
    driver = EventFiringWebDriver(edriver, EventListener())
    driver.maximize_window()
    driver.implicitly_wait(1)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def my_mobile_starter(request):
    global pay_off_calc_page
    dc['reportDirectory'] = reportDirectory
    dc['reportFormat'] = reportFormat
    dc['testName'] = testName
    dc['udid'] = get_data("Udid")
    dc['appPackage'] = get_data('AppPackage')
    dc['appActivity'] = get_data('AppActivity')
    dc['platformName'] = get_data('PlatformName')
    edriver = webdriver.Remote(get_data("LocalHost"), dc)
    driver = EventFiringWebDriver(edriver, EventListener())
    globals()['driver'] = driver
    request.cls.driver = driver
    ManagePages.init_mobile_pages(driver)

    yield
    driver.quit()


@pytest.fixture(scope='class')
def my_api_starter(request):
    response = requests.get(url + 'categories')
    request.cls.action = response.json()


@pytest.fixture(scope='class')
def my_desktop_starter(request):
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    edriver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    driver = EventFiringWebDriver(edriver, EventListener())
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def my_electron_starter(request):
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    the_driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver = EventFiringWebDriver(the_driver, EventListener())
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()
