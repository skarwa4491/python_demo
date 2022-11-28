from selenium.webdriver.common.by import By

from Pages.pageBase import pageBase


class HomePage(pageBase):
    hs_code_classify = (By.XPATH , "//div[text()='HS code Clasify']")

    def __init__(self,driver):
        super().__init__(driver)


    def click_hs_code_classify(self):
        self.do_click(self.hs_code_classify)

