from selenium.webdriver.chrome.webdriver import WebDriver


class SignUpPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_first_name(self):
        return self.driver.find_element_by_id("firstName")

    def input_last_name(self):
        return self.driver.find_element_by_id("lastName")

    def input_user_name(self):
        return self.driver.find_element_by_id("username")

    def input_password(self):
        return self.driver.find_element_by_id("password")

    def input_confirm_password(self):
        return self.driver.find_element_by_id("confirmPassword")

    def button_sign_up(self):
        return self.driver.find_element_by_xpath("//span[text()='Sign Up']")
