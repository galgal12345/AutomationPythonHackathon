from selenium.webdriver.chrome.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def tab_mine(self):
        return self.driver.find_element_by_xpath("//span[text()='Mine']")

    def txt_user_name(self):
        return self.driver.find_element_by_xpath("//h6[@data-test='sidenav-username']")

    def input_user_name(self):
        return self.driver.find_element_by_id("username")

    def input_password(self):
        return self.driver.find_element_by_id("password")

    def input_confirm_password(self):
        return self.driver.find_element_by_id("confirmPassword")

    def button_sign_up(self):
        return self.driver.find_element_by_xpath("//span[text()='Sign Up']")
