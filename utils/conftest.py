import xml.etree.ElementTree as ET

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    match  get_data("Browser").lower():
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


def get_data(node_name):
    root = ET.parse('C:/Users/GIL/PycharmProjects/AutomationPythonHackathon/AaConfig_fileconfig.xml').getroot()
    return root.find(".//" + node_name).text
