from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

import testcases.conftest


def click(locator: tuple):
    testcases.conftest.wait.until(ec.element_to_be_clickable(locator)).click()


def set_text(locator: tuple, text):
    elem: WebElement = testcases.conftest.wait.until(ec.visibility_of_element_located(locator))
    elem.clear()
    elem.send_keys(text)
