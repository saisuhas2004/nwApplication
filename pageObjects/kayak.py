from time import sleep

import keyboard
from keyboard import press

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class kayakPage:
    title_Homepage="//title"
    flight_clickOnTab = "//div[text()='Flights']"
    select_origin_City="//input[@aria-label='Flight origin input']"
    select_Destination_City = "//input[@aria-label='Flight destination input']"
    startDate_EnterDate = "//div[@aria-label='Start date']/descendant::span"
    EndDate_EnterDate = "//div[@aria-label='End date']/descendant::span"
    search_button = "//*[@class='A_8a-icon']"
    price_list = "//*[@class='f8F1-price-text']"

    def __init__(self, driver):
        self.driver = driver

    def search_Flights_On_Landing_Page(self):
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        sleep(10)
        actions = ActionChains(self.driver)
        #self.driver.find_element(By.XPATH, kayakPage.flight_clickOnTab).click()
        # self.driver.find_element(By.XPATH, kayakPage.select_origin_City).send_keys(Keys.BACK_SPACE)
        # self.driver.find_element(By.XPATH, kayakPage.select_origin_City).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, kayakPage.select_origin_City).send_keys("Charlotte(CLT)")
        keyboard.press_and_release('enter')
        # actions.send_keys(Keys.ENTER)
        # actions.perform()
        sleep(10)
        self.driver.find_element(By.XPATH, kayakPage.select_origin_City).send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, kayakPage.select_Destination_City).send_keys("Chennai(MAA)")
        keyboard.press_and_release('enter')
        self.driver.find_element(By.XPATH,  kayakPage.select_Destination_City).send_keys(Keys.TAB)
        sleep(5)
        self.driver.find_element(By.XPATH, kayakPage.search_button).click()
        sleep(10)
