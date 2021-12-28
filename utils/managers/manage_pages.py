from page_objects.desktop.calculator_page import Calculator_Page
from  page_objects.electron.apidemos_page import Apidemos_Page

class ManagePages:
    cl: Calculator_Page
    demo:Apidemos_Page
    @classmethod
    def init_desktop_page(cls, driver):
        cls.cl = Calculator_Page(driver)

    @classmethod
    def init_electron_page(cls, driver):
        cls.demo = Apidemos_Page(driver)

