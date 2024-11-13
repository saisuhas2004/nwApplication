from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.methods_Mapping import pageMapper


class applicationSetupPage:

    def __init__(self, driver):
        self.driver = driver

    def applicationSetupPageContinue(self):
        sleep(5)
        print(pageMapper.CommonObjects.continuButton)
        self.driver.find_element(By.XPATH,pageMapper.CommonObjects.continuButton).click()
        sleep(5)

