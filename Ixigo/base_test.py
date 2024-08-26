import selenium.webdriver as webdriver
import Ixigo.constants as consts
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class BaseTest(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(BaseTest, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def home_screen(self):
        self.get(consts.BASE_URL)


    def open_login_tab(self):
        login_btn = self.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/div[2]/button')
        login_btn.click()


