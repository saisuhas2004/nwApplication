from time import sleep

from selenium.webdriver.common.by import By

from pageObjects.methods_Mapping import pageMapper


class whoNeedsHealthCoverage:
    noneOfTheseApplyToThePeopleInTheHouseHold="//input[@name='householdSituation']"
    dontHaveSSN = "//input[@name='doesnothavessn']"
    citizenshipYes = "//input[@name='allCitizenBoolean']"
    naturalizedNo= "//input[@name='naturalizedDerivedChoice']"

    def __init__(self, driver):
        self.driver = driver


    def whoNeedHealthCoverage(self):
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

    #Personal & household information
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
        sleep(5)

    #Household information
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.noneOfTheseApplyToThePeopleInTheHouseHold).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)


    #Help improve health care access
        self.driver.execute_script("scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
        sleep(5)

    #Consume's Race information
        self.driver.execute_script("scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

    # Consume's information
        self.driver.execute_script("scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

    # Consume' SSNs information
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

