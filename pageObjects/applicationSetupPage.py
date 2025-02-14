from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.methods_Mapping import pageMapper
from utilities.commonMethods import CommonMethods


class applicationSetupPage:
    Commonmethods = CommonMethods
    def __init__(self, driver):
        self.driver = driver

    def applicationSetupPageContinue(self):
        #sleep(5)
        applicationSetupPage.Commonmethods.test_timeouts_explicit_wait(self, pageMapper.CommonObjects.continuButton, "Xpath")
        self.driver.find_element(By.XPATH,pageMapper.CommonObjects.continuButton).click()
        #sleep(5)

