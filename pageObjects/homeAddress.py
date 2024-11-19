from datetime import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.methods_Mapping import pageMapper


class homeAddress:

    streetName1="streetName1"#name
    uspsRecord="//input[@name='geoAPIResult']"
    mailingAddressYes = "//input[@name='isHomeSameAsMailing']"
    phoneTypeHome = "//input[@name='primaryPhoneNumberType']"
    mailPreference = "//input[@name='communicationPreference'][@value='PAPER']"
    applicationHelpNo = "//input[@name='isAnyoneHelping'][@value='false']"

    def __init__(self, driver):
        self.driver = driver

    def homeAddressInfo(self):
        sleep(3)
        self.driver.find_element(By.NAME, homeAddress.streetName1).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.NAME, homeAddress.streetName1).send_keys(Keys.DELETE)
        self.driver.find_element(By.NAME, homeAddress.streetName1).send_keys("905 S GARNETT ST")
        sleep(3)
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(5)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(7)

        #USPS record
        self.driver.find_element(By.XPATH, homeAddress.uspsRecord).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        #Mailing address
        self.driver.find_element(By.XPATH, homeAddress.mailingAddressYes).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)



        # Contact information
        self.driver.find_element(By.XPATH, homeAddress.phoneTypeHome).click()
        sleep(2)
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(3)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)



        #Preferred language
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        #Contact preferences
        self.driver.find_element(By.XPATH, homeAddress.mailPreference).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        #Application help
        self.driver.find_element(By.XPATH, homeAddress.applicationHelpNo).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)






