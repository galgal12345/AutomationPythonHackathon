import time
from time import sleep

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from workflows import web_flows
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils.csv_reader import read_test_data_from_csv


@pytest.mark.usefixtures("my_web_starter", "my_web_before_method")
class TestWeb:

    @pytest.mark.parametrize("user_name, password,expected",
                             read_test_data_from_csv(r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\web.csv'))
    def test_login(self, user_name, password, expected):
        web_flows.login_flow(user_name, password)
        assert expected == web_flows.get_user_name_txt()

    @pytest.mark.parametrize("first_name,last_name,user_name,password,expected",
                             read_test_data_from_csv(r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\users.csv'))
    def test_register(self, first_name, last_name, user_name, password, expected):
        web_flows.register_flow(first_name, last_name, user_name, password)
        print(expected)
        assert web_flows.is_text_present(expected) is True
        # e = driver.find_element_by_xpath("//a[@href='/signup']")
        # e.click()
        # e.click()
        # driver.find_element_by_id("firstName").send_keys(first_name)
        # driver.find_element_by_id("lastName").send_keys(last_name)
        # driver.find_element_by_id("username").send_keys(user_name)
        # driver.find_element_by_id("password").send_keys(password)
        # driver.find_element_by_id("confirmPassword").send_keys(password)
        # driver.find_element_by_xpath("//span[text()='Sign Up']").click()
        # driver.find_element_by_id("username").send_keys(user_name)
        # driver.find_element_by_id("password").send_keys(password)
        # driver.find_element_by_xpath("//span[text()='Sign In']").click()
        # driver.find_element_by_xpath("//span[text()='Next']").click()
