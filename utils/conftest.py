import xml.etree.ElementTree as ET

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    match get_driver("Driver").lower():
        case 'web_driver':
            print()
        case 'android_driver':
            print()
        case 'rest_assured':
            print()
        case 'desktop':
            print()
        case 'electron':
            print()
        case _:
            driver = None
            print("Wrong input, unrecognized browser")

    match get_browser("Browser").lower():
        case 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        case 'edge':
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        case 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        case _:
            driver = None
            print("Wrong input, unrecognized browser")

    driver.maximize_window()
    driver.implicitly_wait(1)
    request.cls.driver = driver
    yield
    driver.quit()


def my_web_starter(self):
    print()


def my_appium_starter(self):
    print()


def my_api_starter(self):
    print()


def my_desktop_starter(self):
    print()


def my_electron_starter(self):
    print()


def get_browser(node_name):
    root = ET.parse('C:/Users/GIL/PycharmProjects/AutomationPythonHackathon/AaConfig_file/config.xml').getroot()
    return root.find(".//" + node_name).textdef


def get_driver(node_name):
    root = ET.parse('C:/Users/GIL/PycharmProjects/AutomationPythonHackathon/AaConfig_file/config.xml').getroot()
    return root.find(".//" + node_name).text
