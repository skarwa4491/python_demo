from Pages.loginPage import Login
from Test.testBase import testBase

class Tests(testBase):

    def test_sample_1(self):
        login = Login(self.driver)
        home = login.perform_login("msil2022@gmail.com","123456789")
        home.click_hs_code_classify()

