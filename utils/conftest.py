import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.common_ops import get_browser

# WEB
driver = None
action = None

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


@pytest.fixture(scope='class')
def my_web_starter(request):
    if get_browser("Browser") == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif get_browser("Browser") == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif get_browser("Browser") == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = None
        print("Wrong input, unrecognized browser")

    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(1)
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


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
