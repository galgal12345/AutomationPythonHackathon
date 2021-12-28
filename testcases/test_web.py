import pickle
import time
from time import sleep

from applitools.common import DiffsFoundError
from proboscis import test
from pytest_dependency import depends

from extensions import ui_actions
from utils.manage_pages import ManagePages

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

    # @pytest.mark.parametrize("first_name,last_name,user_name,password,expected",
    #                          read_test_data_from_csv(r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\users.csv'))
    # def test_register(self, first_name, last_name, user_name, password, expected):
    #     web_flows.register_flow(first_name, last_name, user_name, password)
    #     print(expected)
    #     assert web_flows.is_text_present(expected) is True
    #     # e = driver.find_element_by_xpath("//a[@href='/signup']")
    #     # e.click()
    #     # e.click()
    #     # driver.find_element_by_id("firstName").send_keys(first_name)
    #     # driver.find_element_by_id("lastName").send_keys(last_name)
    #     # driver.find_element_by_id("username").send_keys(user_name)
    #     # driver.find_element_by_id("password").send_keys(password)
    #     # driver.find_element_by_id("confirmPassword").send_keys(password)
    #     # driver.find_element_by_xpath("//span[text()='Sign Up']").click()
    #     # driver.find_element_by_id("username").send_keys(user_name)
    #     # driver.find_element_by_id("password").send_keys(password)
    #     # driver.find_element_by_xpath("//span[text()='Sign In']").click()
    #     # driver.find_element_by_xpath("//span[text()='Next']").click()

    # @pytest.mark.parametrize("bank_name,routing_number,account_number,expected",
    #                          read_test_data_from_csv(
    #                              r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\bank_accounts.csv'))
    # def test_create_bank_account(self, bank_name, routing_number, account_number, expected):
    #     web_flows.go_to_bank_account_creation()
    #     web_flows.create_bank_account(bank_name, routing_number, account_number)
    #     assert ui_actions.get_element_text(ManagePages.mp.txt_bank_name(bank_name)) == bank_name

    # @pytest.mark.parametrize("contact_name,amount,note,action",
    #                          read_test_data_from_csv(
    #                              r'C:\Users\bizyb\PycharmProjects\project\DDTFiles\transactions.csv'))
    # def test_create_payment(self, contact_name, amount, note, action):
    #     balance_before = web_flows.get_account_balance()
    #     web_flows.create_new_transaction(contact_name, amount, note, action)
    #     balance_after = web_flows.get_account_balance()
    #     assert balance_before == balance_after + float(amount)

    @pytest.mark.usefixtures("eyes", "runner")
    def test_dismiss_notification(self, eyes, runner):
        web_flows.get_notifications_tab()
        eyes.check_window('Screen Shot before dismiss')
        web_flows.dismiss_notification("notification_name")
        eyes.check_window('Screen Shot after notification dismissed')
        eyes.close(False)
        try:
            runner.get_all_test_results(should_raise_exception=True)
        except DiffsFoundError:
            print("Test passed. changes have been founds!")
