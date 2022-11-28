from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage
from Pages.pageBase import pageBase

class Login(pageBase):
    signIn = (By.XPATH,"//input[@type='email']")
    password = (By.XPATH , "//input[@type='password']")
    login_button = (By.XPATH , "//button[text()='Login']")

    def __init__(self,driver):
        super().__init__(driver)


    def perform_login(self, username , passwrod):
        self.type(self.signIn , username)
        self.type(self.password , passwrod)
        self.do_click(self.login_button)
        assert self.driver.title == 'FDP'
        return HomePage(self.driver)
