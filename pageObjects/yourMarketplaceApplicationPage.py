from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


class yourMarketPlaceApplicationPage:


    ContinueToApplication ="//span[text()='Continue to application']"





    def __init__(self,driver):
        self.driver=driver

    def continueYourMarketPlaceApplicationPage(self):
        sleep(5)
        self.driver.execute_script("scrollBy(0,500);")
        sleep(2)
        self.driver.find_element(By.XPATH, yourMarketPlaceApplicationPage.ContinueToApplication).click()
        sleep(5)
