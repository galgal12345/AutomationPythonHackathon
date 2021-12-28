
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Calculator_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_tow(self):
        return self.driver.find_element_by_name("שתיים")

    def get_seven(self):
        return self.driver.find_element_by_name("שבע")

    def get_clear(self):
        return self.driver.find_element_by_name("נקה ערך")

    def get_equels(self):
        return self.driver.find_element_by_name("שווה")

    def get_multi(self):
        return self.driver.find_element_by_name("הכפל ב")

    def get_result(self):
        return self.driver.find_elements_by_xpath("//*[@AutomationId='CalculatorResults']")

    def get_result(self):
        # trim extra text and whitespace off of the display value
        return self.driver.find_element_by_xpath("//*[@AutomationId='CalculatorResults']").text.replace("Display is", "").strip()







