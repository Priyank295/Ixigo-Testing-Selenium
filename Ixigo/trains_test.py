from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from Ixigo.base_test import BaseTest

class TrainsTest(BaseTest):
    def __init__(self):
        super(TrainsTest, self).__init__()

    def select_trains_mode(self):
        trip_btn = self.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[2]/div/ul/li[3]/a')
        # print(trip_btn.is_selected())
        trip_btn.click()

    def select_origin(self,origin):
        origin_container = self.find_element(By.XPATH, '//*[@id="origin-destination-input"]/div[1]')
        origin_container.click()
        origin_field = self.find_element(By.XPATH, '//*[@id="origin-destination-input"]/div[1]/div/div/div/div[2]/input')
        origin_field.send_keys(origin)
        first_origin = self.find_element(By.XPATH, '/html/body/main/div[4]/div[1]/div[2]/div[3]/div/li[1]')
        first_origin.click()

    def select_destination(self,destination):
        destination_field = self.find_element(By.XPATH, '/html/body/main/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/input')
        destination_field.send_keys(destination)
        first_destination = self.find_element(By.XPATH, '/html/body/main/div[4]/div[1]/div[2]/div[3]/div/li[1]')
        first_destination.click()

    def select_date(self,date):
        select_date = self.find_element(By.CSS_SELECTOR, f'[aria-label="{date}"]')
        select_date.click()

    def find(self):
        search_btn = self.find_element(By.XPATH, '/html/body/main/div[4]/div[1]/div[2]/div[1]/button')
        search_btn.click()
        time.sleep(2)

    def checking_all_sorting(self):
        for i in range(1,5):
            sorting_btn = self.find_element(By.XPATH,f'//*[@id="content"]/div/div[2]/div[3]/div[1]/div[1]/div/nav/span[{i}]/span')
            sorting_btn.click()
            time.sleep(2)

