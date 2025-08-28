import time
import os
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from config import get_login_data
from event import Event

#CONFIGURATION

USER_DATA_PATH = r'C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data' 
chrome_options = uc.ChromeOptions()

chrome_options.add_argument(f'--user-data-dir={USER_DATA_PATH}')
chrome_options.add_argument('--profile-directory=Default') 
chrome_options.add_argument('--disable-blink-features=AutomationControlled')


class Brwsr:
# MAIN SCRIPT
    def __init__(self):
        print("Initializing driver with your REAL Chrome profile...")
        print("!!! Make sure all other Chrome windows are closed !!!")
        self.driver = uc.Chrome(options=chrome_options)
    def finish(self):
        if self.driver:
            self.driver.quit()
            print("Driver closed.")


    def is_auth_needed(self) -> bool:
        try:
            login_input = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        except NoSuchElementException as e:
            return False

        return True

    def authenticate(self):
        login_input = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="submitBtnLogin"]') 

        (login, password) = get_login_data()

        login_input.send_keys(login)
        time.sleep(1)
        password_input.send_keys(password)
        time.sleep(1)
        login_button.click()

    def open_timetable(self, url: str):
        try:
            print(f"Navigating to target site: {url}")
            self.driver.get(url)

            print("Page loaded. Simulating reading...")
            time.sleep(random.uniform(4, 7))

            print("\nScript paused. The browser now has full access to your cookies, sessions, and perfect fingerprint.")
            print("Try performing the actions that previously resulted in a block.")

            print("Checking if we're authorized")
            
            if self.is_auth_needed():
                self.authenticate()
            else:
                return
            
            time.sleep(random.uniform(2, 4))
            self.driver.get(url)
            time.sleep(random.uniform(2, 3))


        except Exception as e:
            print(f"\nAn error occurred: {e}")
            if "user data directory is already in use" in str(e).lower():
                print("\nLOCKING ERROR: You did not close all Google Chrome windows before running the script.")
            self.finish()

    def get_events_elems(self) -> list[WebElement]:
        elems = self.driver.find_elements(By.XPATH, '/html/body/div[2]/div[6]/div[2]/div/table/tbody/tr/td/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a')
        print("elems")
        print(elems)
        print("elems")
        return elems

    def extract_event(self, elem: WebElement) -> Event:
        date_elem = elem.find_element(By.XPATH, './/div[1]/div')
        data = date_elem.get_attribute("data-full") or " - "
        start, end = data.split("-")
        start = start.strip()
        end = end.strip()

        content_elem = elem.find_element(By.XPATH, './/div[1]')
        content = content_elem.text
        return Event(content)

def get_events(url: str):
    b = Brwsr()
    b.open_timetable(url)
    events_elems = b.get_events_elems()
    events = [b.extract_event(e) for e in events_elems]
    b.finish()
    return events

