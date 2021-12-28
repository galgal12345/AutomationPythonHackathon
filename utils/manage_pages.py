from page_objects.web.create_bank_account_page import CreateBankAccountPage
from page_objects.web.login_page import LoginPage
from page_objects.web.notifications_page import NotificationsPage
from page_objects.web.sign_up_page import SignUpPage
from page_objects.web.main_page import MainPage


class ManagePages:
    lp: LoginPage
    su: SignUpPage
    mp: MainPage
    cba: CreateBankAccountPage
    np: NotificationsPage

    @classmethod
    def init_web_pages(cls, driver):
        cls.lp = LoginPage(driver)
        cls.su = SignUpPage(driver)
        cls.mp = MainPage(driver)
        cls.cba = CreateBankAccountPage(driver)
        cls.np = NotificationsPage(driver)
