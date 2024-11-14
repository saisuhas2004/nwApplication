from time import sleep

from selenium.webdriver.common.by import By


class tellUsAboutYourself:
    doYouNeedCoverage ="//input[@name='isRequestingCoverage'][@value='true']"
    birthYear= "//input[@name='year']"
    sex="//input[@value='MALE']"
    saveAndContinue= "//span[text()='Save & continue']"

    def __init__(self, driver):
        self.driver = driver

    def tellUsAboutYourselfInformation(self):
        self.driver.find_element(By.XPATH, tellUsAboutYourself.doYouNeedCoverage).click()
        sleep(3)
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(3)
        self.driver.find_element(By.XPATH, tellUsAboutYourself.birthYear).send_keys("1980")
        self.driver.find_element(By.XPATH, tellUsAboutYourself.sex).click()
        self.driver.execute_script("scrollBy(0,200);")
        self.driver.find_element(By.XPATH, tellUsAboutYourself.saveAndContinue).click()
        sleep(5)
