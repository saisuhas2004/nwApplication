from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

from utilities.commonMethods import CommonMethods


class yourMarketPlaceApplicationPage:
    Commonmethods = CommonMethods

    ContinueToApplication ="//span[text()='Continue to application']"





    def __init__(self,driver):
        self.driver=driver

    def continueYourMarketPlaceApplicationPage(self):
        sleep(3)
        self.driver.execute_script("scrollBy(0,500);")
        yourMarketPlaceApplicationPage.Commonmethods.test_timeouts_explicit_wait(self, yourMarketPlaceApplicationPage.ContinueToApplication, "Xpath")
        self.driver.find_element(By.XPATH, yourMarketPlaceApplicationPage.ContinueToApplication).click()

