from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class pageBase:

    def __init__(self,driver):
        self.driver = driver

    def type(self,by_locator,text):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_click(self, by_loccator):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_loccator)).click()
