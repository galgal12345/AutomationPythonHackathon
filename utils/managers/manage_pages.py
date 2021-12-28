from page_objects.mobile import TvmCalcPage, CurrencyConverterPage, LoanCalcPage, CompoundInterestCalcPage
from page_objects.mobile.TvmCalcPage import TvmCalcPage
from page_objects.mobile.CurrencyConverterPage import CurrencyConverterPage
from page_objects.mobile.LoanCalcPage import LoanCalcPage
from page_objects.mobile.CompoundInterestCalcPage import CompoundInterestCalcPage
from page_objects.mobile.PayOffCalcPage import PayOffCalcPage
from page_objects.mobile.MainPage import MainPage


class ManagePages:
    tvm_calc_page: TvmCalcPage
    currency_converter_page: CurrencyConverterPage
    loan_calc_page: LoanCalcPage
    compound_interest_calc_page: CompoundInterestCalcPage
    pay_off_calc_page: PayOffCalcPage
    main_page: MainPage

    @classmethod
    def init_mobile_pages(cls, driver):
        cls.tvm_calc_page = TvmCalcPage(driver)
        cls.currency_converter_page = CurrencyConverterPage(driver)
        cls.loan_calc_page = LoanCalcPage(driver)
        cls.compound_interest_calc_page = CompoundInterestCalcPage(driver)
        cls.pay_off_calc_page = PayOffCalcPage(driver)
        cls.main_page = MainPage(driver)
