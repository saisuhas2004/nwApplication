from datetime import time

from selenium.webdriver.common.by import By
from pageObjects.methods_Mapping import pageMapper


class homeAddress:

    streetName1="streetName1"#name
    uspsRecord="//input[@name='geoAPIResult']"
    mailingAddressYes = "//input[@name='isHomeSameAsMailing']"
    phoneTypeHome = "//input[@name='primaryPhoneNumberType']"
    mailPreference = "//input[@name='communicationPreference']"
    applicationHelpNo = "//input[@name='isAnyoneHelping']"

    def __init__(self, driver):
        self.driver = driver

    def homeAddressInfo(self):
        self.driver.find_element(By.NAME, homeAddress.streetName1).send_keys("905 S GARNETT ST")
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        time(5)

        #USPS record
        self.driver.find_element(By.XPATH, homeAddress.streetName1).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        time(5)

        #Mailing address
        self.driver.find_element(By.XPATH, homeAddress.phoneTypeHome).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        time(5)

        #Contact information
        self.driver.find_element(By.XPATH, homeAddress.mailingAddressYes).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        time(5)

        #Preferred language
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        time(5)

        #Contact preferences
        self.driver.find_element(By.XPATH, homeAddress.mailPreference).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        time(5)

        #Application help
        self.driver.find_element(By.XPATH, homeAddress.applicationHelpNo).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        time(5)






