import selenium.webdriver as webdriver
import Ixigo.constants as consts
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from Ixigo.base_test import BaseTest

class FlightsTest(BaseTest):
    def __init__(self):
        super(FlightsTest, self).__init__()

    def select_flight_mode(self):
        trip_btn = self.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[2]/div/ul/li[2]/a')
        # print(trip_btn.is_selected())
        trip_btn.click()

    def enter_source(self, source):
        source_btn = self.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div')
        source_btn.click()

        source_field = self.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/input')
        source_field.send_keys(source)
        first_source = self.find_element(By.XPATH,'/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[3]/div[1]/li')
        first_source.click()

    def enter_destination(self,destination):
        dest_btn = self.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div')
        dest_btn.click()
        dest_field = self.find_element(By.CSS_SELECTOR, 'body > main > div.max-w-\[1240px\].m-auto.mainContainer > div.pt-30.mx-0.relative.px-20.xl\:px-0 > div.border-none.shadow-500.p-20.flex.flex-col.gap-10.rounded-20.bg-white.undefined > div.flex.gap-0\.5.cursor-pointer.h-\[60px\] > div.relative.flex.gap-0\.5.flex-1 > div.bg-charcoal-40.flex.items-center.relative.w-full.h-\[60px\].hover\:bg-neutral-subtle-over.border-b-4.border-blue-500 > div.w-full.flex.items-center.justify-between.relative.h-\[60px\].block.mt-15.pr-15.pl-\[25px\] > div > div > div.flex.flex-grow.items-center > input')
        dest_field.send_keys(destination)

        first_destination = self.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[2]/li')
        first_destination.click()

    def enter_date(self,date):
        select_date = self.find_element(By.CSS_SELECTOR, f'[aria-label="{date}"]')
        select_date.click()

    def select_adults(self,adults):
        select_adult = self.find_element(By.XPATH,f'/html/body/main/div[2]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[2]/div/button[{adults}]')
        select_adult.click()
        dont_btn = self.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[2]/button')
        dont_btn.click()

    def find(self):
        find_btn = self.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[3]/div[2]/button')
        find_btn.click()
        time.sleep(2)

    def add_hotels(self):

        try:
            hotel_checkbox = self.find_element(By.XPATH,
                                               '/html/body/main/div[2]/div[1]/div[3]/div[3]/div[2]/div/span/input')
            if hotel_checkbox:
                hotel_checkbox.click()
        except NoSuchElementException as e:
            print(e)



    def checking_all_sorting(self):
        for i in range(1, 5):
            sorting_btn = self.find_element(By.XPATH,
                                            f'/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/div[{i}]/span/input')
            # Capture data before sorting
            data_before_sorting = self.get_sorted_data()
            # print(data_before_sorting)

            # Click the sorting button
            time.sleep(2)
            sorting_btn.click()
            time.sleep(2)  # Wait for the sorting to be applied

            # Capture data after sorting
            data_after_sorting = self.get_sorted_data()
            print("-----------------------------------------------------")
            # print(data_after_sorting)
            # Assert that the data is sorted correctly
            try:
                assert data_after_sorting != data_before_sorting
                print(f"Test Case Passed: Sorting {i} worked correctly")
            except AssertionError:
                print(f"Test Case Failed: Sorting {i} did not work correctly")
                return False  # You can choose to fail the entire test if sorting fails

    def get_sorted_data(self):
        # Placeholder method to capture the data that needs to be sorted
        # Example: Grab data from a table, list, etc.
        # Replace the below with the actual logic to extract the data
        data_elements = self.find_elements(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[3]')  # Example XPath to data elements
        return [element.text for element in data_elements]  # Return the data as a list

    def sort_with_price(self):
        price_btn = self.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/div[1]/span/input')
        price_btn.click()

    def sort_with_shortest(self):
        fast_btn = self.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/div[2]/span/input')
        fast_btn.click()

    def changing_price_range(self,start,end):
        starting_price_loader = self.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/input[1]')
        starting_price_text = self.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div[3]')
        self.execute_script("arguments[0].innerHTML = arguments[1];", starting_price_text, start)
        # new_value = "New Value"
        self.execute_script(f"arguments[0].value = '{start}';", starting_price_loader)

        ending_price_loader = self.find_element(By.XPATH,
                                                  '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/input[2]')
        ending_price_text = self.find_element(By.XPATH,
                                                '/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/div/div[4]')
        self.execute_script("arguments[0].innerHTML = arguments[1];", ending_price_text, end)
        # new_value = "New Value"
        self.execute_script(f"arguments[0].value = '{end}';", ending_price_loader)

        try:
            assert starting_price_text.text == start
            print(f"Test Case Passed: Staring Price worked correctly")
        except AssertionError:
            print(f"Test Case Failed: Staring Price did not work correctly")
            return False

        try:
            assert ending_price_text.text == end
            print(f"Test Case Passed: Ending Price worked correctly")
        except AssertionError:
            print(f"Test Case Failed: Ending Price did not work correctly")
            return False

    def change_travellers(self,travellers):
        traveller_container = self.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div[1]/div[3]/div/div')
        traveller_container.click()

        traveller_selector = self.find_element(By.XPATH, f'/html/body/div[2]/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[2]/div/button[{travellers}]')
        traveller_selector.click()

        print(traveller_selector.get_attribute("innerHTML"))
        try:
            assert travellers == traveller_selector.get_attribute("innerHTML")
            print(f"Test Case Passed: Changing travellers worked correctly")
        except AssertionError:
            print(f"Test Case Failed: Changing travellers did not work correctly")
            return False

        done_btn = self.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/button')
        done_btn.click()
        # print(traveller_selector.get_attribute("innerHTML"))






