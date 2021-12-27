from page_objects.web.login_page import LoginPage
from page_objects.web.sign_up_page import SignUpPage
from page_objects.web.main_page import MainPage


class ManagePages:
    lp: LoginPage
    su: SignUpPage
    mp: MainPage

    @classmethod
    def init_web_pages(cls, driver):
        cls.lp = LoginPage(driver)
        cls.su = SignUpPage(driver)
        cls.mp = MainPage(driver)
