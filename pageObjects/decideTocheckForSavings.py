from time import sleep

from selenium.webdriver.common.by import By
from pageObjects.methods_Mapping import pageMapper


class decideToCheckForSavings:
    taxFilingSize = "//input[@name='taxHouseholdSize']"
    IChooseNotToAnswer ="//input[@name='estimatedIncome'][@value='declined']"
    continueWithoutCheckingForSavingsOption="//input[@name='requestingFinancialAssistance'][@value='0']"



    def __init__(self, driver):
        self.driver = driver

    def enterApplicationTaxFilingInformation(self):
        sleep(5)
        self.driver.find_element(By.XPATH, decideToCheckForSavings.taxFilingSize).send_keys("1")
        self.driver.execute_script("scrollBy(0,400);")
        sleep(3)
        self.driver.find_element(By.XPATH, decideToCheckForSavings.IChooseNotToAnswer).click()
        sleep(2)
        self.driver.execute_script("scrollBy(0,400);")
        sleep(3)
        self.driver.find_element(By.XPATH, decideToCheckForSavings.continueWithoutCheckingForSavingsOption).click()
        sleep(2)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
        sleep(5)