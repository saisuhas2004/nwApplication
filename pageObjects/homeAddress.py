from datetime import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pageObjects.methods_Mapping import pageMapper
from utilities.commonMethods import CommonMethods


class homeAddress:
    Commonmethods = CommonMethods
    streetName1="streetName1"#name
    homeAddressCity= "//*[@name='cityName']"
    stateDropdown ="//span[tex()='Select state']"
    pickAState="//span[text() = 'South Carolina']"
    zipcode="//*[@name='zipCode']"
    uspsRecord="//input[@name='geoAPIResult']"
    mailingAddressYes = "//input[@name='isHomeSameAsMailing']"
    phoneTypeHome = "//input[@name='primaryPhoneNumberType']"
    mailPreference = "//input[@name='communicationPreference'][@value='PAPER']"
    applicationHelpNo = "//input[@name='isAnyoneHelping'][@value='false']"
    otherStateDropdown="//*[@class='ds-c-dropdown__button ds-c-field']"

    def __init__(self, driver):
        self.driver = driver

    def homeAddressInfo(self, State):
        sleep(3)
        self.driver.find_element(By.NAME, homeAddress.streetName1).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.NAME, homeAddress.streetName1).send_keys(Keys.DELETE)
        self.driver.find_element(By.NAME, homeAddress.streetName1).send_keys(CommonMethods.readDataFromJson(self,State,"AddressLine"))
        sleep(3)

        homeAddress.Commonmethods.actionToMoveToElement(self,homeAddress.homeAddressCity)
        sleep(2)
        self.driver.find_element(By.XPATH, homeAddress.homeAddressCity).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, homeAddress.homeAddressCity).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, homeAddress.homeAddressCity).send_keys(CommonMethods.readDataFromJson(self,State,"City"))
        sleep(3)

        if State != 'NC':
            homeAddress.Commonmethods.actionToMoveToElement(self, homeAddress.otherStateDropdown)
            sleep(2)
            homeAddress.Commonmethods.actionToMoveToElement(self, CommonMethods.pickTheState(self,State))
            sleep(2)


        homeAddress.Commonmethods.actionToMoveToElement(self, homeAddress.zipcode)
        self.driver.find_element(By.XPATH, homeAddress.zipcode).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, homeAddress.zipcode).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, homeAddress.zipcode).send_keys(CommonMethods.readDataFromJson(self,State,"ZIPCode"))
        sleep(3)

        homeAddress.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(7)

        #USPS record
        homeAddress.Commonmethods.actionToMoveToElement(self, homeAddress.uspsRecord)
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
        homeAddress.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
        #self.driver.execute_script("scrollBy(0,1000);")
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






