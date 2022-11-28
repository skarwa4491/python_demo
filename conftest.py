import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

@pytest.fixture(scope='class')
def init_browser(request):
    ch_driver = Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    ch_driver.maximize_window()
    ch_driver.get("https://msilpoc.fdpconnect.com/#/login")
    request.cls.driver = ch_driver
    yield
    time.sleep(15)

