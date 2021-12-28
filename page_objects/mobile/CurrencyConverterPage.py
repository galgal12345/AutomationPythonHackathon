from selenium.webdriver.common.by import By


class CurrencyConverterPage:
    def __init__(self, driver):
        self.driver = driver

    def get_rate_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='exchRateInput']")

    def get_amount_edit_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@id='amountInput']")

    def get_big_red_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@text='3 USD = 150 ILS']")

    def get_small_red_txt(self):
        return self.driver.find_element(By.XPATH, "//*[@text='3 ILS = 0.06 USD']")

    def get_graph_img(self):
        return self.driver.find_element(By.XPATH, "//*[@id='exChart']")

    def get_back_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@contentDescription='Navigate up']")
