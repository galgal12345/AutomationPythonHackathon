from selenium.webdriver.common.by import By


class PayOffCalcPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cc_balance_edit_txt(self):
        return By.XPATH, "//*[@id='balanceInput']"

    def get_cc_interest_edit_txt(self):
        return By.XPATH, "//*[@id='interestInput']"

    def get_payment_per_month_edit_txt(self):
        return By.XPATH, "//*[@id='paymentInput']"

    def get_reset_btn(self):
        return By.XPATH, "//*[@text='RESET']"

    def get_calc_btn(self):
        return By.XPATH, "//*[@text='CALCULATE']"

    def get_result(self):
        return By.XPATH, "//*[@id='result']"

    def get_back_btn(self):
        return By.XPATH, "//*[@contentDescription='Navigate up']"
