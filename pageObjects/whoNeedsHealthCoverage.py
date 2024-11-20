from time import sleep

from selenium.webdriver.common.by import By

from pageObjects.methods_Mapping import pageMapper
from utilities.commonMethods import CommonMethods

class whoNeedsHealthCoverage:
    Commonmethods = CommonMethods()
    noneOfTheseApplyToThePeopleInTheHouseHold="//input[@name='householdSituation'][@value='none']"
    dontHaveSSN = "//input[@name='doesnothavessn']"
    citizenshipYes = "//input[@name='allCitizenBoolean']"
    naturalizedNo= "//input[@name='naturalizedDerivedChoice'][@value='false']"
    applicationID ="//p[@class='ds-u-margin-y--2 ds-u-font-size--sm ds-u-color--muted']"

    def __init__(self, driver):
        self.driver = driver


    def whoNeedHealthCoverage(self):
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

    #Personal & household information
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(5)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
        sleep(5)

    #Household information
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.noneOfTheseApplyToThePeopleInTheHouseHold).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)


    #Help improve health care access
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(2)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
        sleep(5)

    #Consume's Race information
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(2)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)


    # Consume's information
        self.driver.execute_script("scrollBy(0,1300);")
        sleep(3)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

    # Consume' SSNs information
        ApplicationID = self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.applicationID)
        print(ApplicationID.text)
        whoNeedsHealthCoverage.Commonmethods.writeToTextFile(ApplicationID.text)

        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.dontHaveSSN).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

    #Citizenship & immigration status
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.citizenshipYes).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

    # naturalized
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.naturalizedNo ).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

