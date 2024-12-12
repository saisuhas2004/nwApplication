from time import sleep

from selenium.webdriver.common.by import By

from pageObjects.methods_Mapping import pageMapper
from utilities.commonMethods import CommonMethods

class whoNeedsHealthCoverage:
    Commonmethods = CommonMethods
    noneOfTheseApplyToThePeopleInTheHouseHold="//input[@name='householdSituation'][@value='none']"
    dontHaveSSN = "//input[@name='doesnothavessn']"
    citizenshipYes = "//input[@name='allCitizenBoolean']"
    naturalizedNo= "//input[@name='naturalizedDerivedChoice'][@value='false']"
    applicationID ="//p[@class='ds-u-margin-y--2 ds-u-font-size--sm ds-u-color--muted']"
    single ="//input[@value='UNMARRIED']"
    willFileAFederalIncomeTaxReturn="//*[@name='filingTaxes'][@value='true']"
    claimAnyDependent="//*[@name='claimsDependent'][@value='false']"
    willSomeOneClamAsDependent="//*[@name='claimedAsADependent'][@value='false']"
    parentsAndCaretakerRelatives ="//*[@name='ParentCaretakerRelativeStatusQuestion'][@value='none']"
    medicaidOrCHIPCoverageEnding="//*[@name='hadMedicaidEnded'][@value='none']"
    medicaidOrCHIPDenial="//*[@name='hadMedicaidDenied'][@value='none']"
    #Income Page
    addIncome="//button[text()='Add income']"
    selectIncomeType="//button/span[text()='Select income type']"
    job="//button/span[text()='Job (like salary, wages, commissions, or tips)']"
    employerName ="//*[@name='employerName']"
    incomeAmount="//*[@name='incomeAmount']"
    addIncomeButton="//button[text()='Add']"
    expectedToBeAboutThisAmount ="//*[@name='isEstimateAccurate'][@value='true']"


    def __init__(self, driver):
        self.driver = driver


    def whoNeedHealthCoverage(self):
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

    #Personal & household information
        #self.driver.execute_script("scrollBy(0,1000);")
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.continuButton)
        sleep(5)


    #Household information
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.noneOfTheseApplyToThePeopleInTheHouseHold).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)


    #Help improve health care access

        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.continuButton)
        sleep(5)

    #Consume's Race information

        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
        sleep(5)


    # Consume's information
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
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

    def whoNeedHealthCoverageFAApplication(self):
        # Who needs health coverage?
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        # Personal & household information
        # self.driver.execute_script("scrollBy(0,1000);")
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.continuButton)
        sleep(5)

        #Marital status
        self.driver.find_element(By.XPATH,whoNeedsHealthCoverage.single).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        # Household information
       # self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.single).click()

        # Household tax returns
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, whoNeedsHealthCoverage.willFileAFederalIncomeTaxReturn)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, whoNeedsHealthCoverage.claimAnyDependent)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, whoNeedsHealthCoverage.willSomeOneClamAsDependent)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self,
                                                                   pageMapper.CommonObjects.saveAndContinue)
        sleep(5)

        # Parents & caretaker relatives
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self,
                                                                   whoNeedsHealthCoverage.parentsAndCaretakerRelatives)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self,
                                                                   pageMapper.CommonObjects.saveAndContinue)
        sleep(5)

        # Household information
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.noneOfTheseApplyToThePeopleInTheHouseHold).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        # Help improve health care access
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.continuButton)
        sleep(5)

        # Consume's Race information

        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
        sleep(5)

        # Consume's information

        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
        sleep(5)

        # Consume' SSNs information
        ApplicationID = self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.applicationID)
        print(ApplicationID.text)
        whoNeedsHealthCoverage.Commonmethods.writeToTextFile(ApplicationID.text)

        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.dontHaveSSN).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        # Citizenship & immigration status
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.citizenshipYes).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        # naturalized
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.naturalizedNo).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        # Disabilities & help with activities
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
        sleep(5)

        #Medicaid or CHIP coverage ending
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, whoNeedsHealthCoverage.medicaidOrCHIPCoverageEnding)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
        sleep(5)

        # Recent Medicaid or CHIP denial
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self,
                                                                   whoNeedsHealthCoverage.medicaidOrCHIPDenial)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
        sleep(5)

        #Household income
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.continuButton)
        sleep(5)

        #'s income for this month
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, whoNeedsHealthCoverage.selectIncomeType)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, whoNeedsHealthCoverage.job)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, whoNeedsHealthCoverage.employerName)
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.employerName).send_keys("ABC Limited")
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.incomeAmount).send_keys("30000")
        self.driver.find_element(By.XPATH, whoNeedsHealthCoverage.addIncomeButton).click()
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)

        #estimated income for next year
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, whoNeedsHealthCoverage.expectedToBeAboutThisAmount)
        whoNeedsHealthCoverage.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)




