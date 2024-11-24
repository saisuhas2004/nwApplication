from time import sleep

from selenium.webdriver.common.by import By

from pageObjects.methods_Mapping import pageMapper
from utilities.commonMethods import CommonMethods


class currentCoverageAndSEP:
    Commonmethods = CommonMethods
    HRASEPNo = "//input[@name='hraOffersChoices'][@value='false']"
    adoptionSEP= "//*[@value='adoptedChild']"
    whoWasAdopted="//*[@name='whoWasAdopted']"
    month="//*[@name='month']"
    day="//*[@name='day']"
    year="//*[@name='year']"
    iAgree="//*[@name='terminateCoverageOtherMecFoundAgreementIndicator'][@value='true']"
    iAgreeToThisStatement ="//*[@name='changeInformationAgreementIndicator'][@value='true']"
    penaltyOfPerjuryAgreementIndicator="//*[@name='penaltyOfPerjuryAgreementIndicator'][@value='true']"
    signElectronically="//*[@name='applicationSignatureText']"
    signAndSubmitButton="//button/span[text()='Sign & submit']"
    viewEligibilityNotice="//button[@id='viewEligibility']"
    continueToEnrollment = "//button[@id='proceedToEnrollBtn']"
    applicationID="//p[text()='Application ID']"
    def __init__(self, driver):
        self.driver = driver

    #Current coverage & life changes
    def currentCoverage(self):
        #self.driver.execute_script("scrollBy(0,1000);")
        currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, currentCoverageAndSEP.applicationID)
        sleep(5)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
        sleep(5)

    #Special Enrollment Period eligibility
    def specialEnrollmentPeriodEligibility(self):
        sleep(3)
        currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.continuButton)
        #self.driver.execute_script("scrollBy(0,500);")
        sleep(3)
        #self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
        sleep(5)

        # Health Reimbursement Arrangement (HRA) offers
    def healthReimbursementArrangementHRAOffers(self):
        #self.driver.execute_script("scrollBy(0,500);")
        currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, currentCoverageAndSEP.HRASEPNo)
        sleep(3)
        self.driver.find_element(By.XPATH, currentCoverageAndSEP.HRASEPNo).click()
        currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
#        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        #SEP - Recent coverage changes
    def specialEnrollmentPage(self):

            #Recent coverage changes
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.noRadiobutton).click()
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
            sleep(5)

            # Upcoming coverage changes
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.noRadiobutton).click()
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
            sleep(5)


            # Life changes
            self.driver.find_element(By.XPATH, currentCoverageAndSEP.adoptionSEP).click()
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
            sleep(5)

            # Tell us about the new dependent
            self.driver.find_element(By.XPATH, currentCoverageAndSEP.whoWasAdopted).click()
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
            sleep(5)

            #Tell Us About The New Dependent
            self.driver.find_element(By.XPATH, currentCoverageAndSEP.month).send_keys("11")
            self.driver.find_element(By.XPATH, currentCoverageAndSEP.day).send_keys("01")
            self.driver.find_element(By.XPATH, currentCoverageAndSEP.year).send_keys("2024")
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
            sleep(5)

            #Voter Registration
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.NoSelection).click()
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
            sleep(5)

            # Review, sign, & submit
            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
            sleep(5)

            # Review your application
            #self.driver.execute_script("scrollBy(0,1000);")
            #sleep(5)
            #self.driver.execute_script("scrollBy(0,1200);")
            currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
            sleep(5)
#            self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
            sleep(5)

            #Read & agree to these statements
            self.driver.find_element(By.XPATH, currentCoverageAndSEP.iAgree).click()
            currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, currentCoverageAndSEP.iAgreeToThisStatement)
            #self.driver.execute_script("scrollBy(0,700);")
            sleep(3)
           # self.driver.find_element(By.XPATH, currentCoverageAndSEP.iAgreeToThisStatement).click()
            currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, pageMapper.CommonObjects.saveAndContinue)
            #self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
            sleep(5)

            # Sign & submit
            currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, currentCoverageAndSEP.penaltyOfPerjuryAgreementIndicator)
            #self.driver.find_element(By.XPATH, currentCoverageAndSEP.penaltyOfPerjuryAgreementIndicator).click()
            self.driver.find_element(By.XPATH, currentCoverageAndSEP.signElectronically).send_keys("JOYCE WATLINGTON")
            currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self,
                                                                      currentCoverageAndSEP.signAndSubmitButton)
            #self.driver.find_element(By.XPATH, currentCoverageAndSEP.signAndSubmitButton).click()
            sleep(30)

            #Eligibility results
            currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self,  currentCoverageAndSEP.viewEligibilityNotice)
            #self.driver.execute_script("scrollBy(0,700);")
            sleep(3)
           # self.driver.find_element(By.XPATH, currentCoverageAndSEP.viewEligibilityNotice).click()
            sleep(3)
            currentCoverageAndSEP.Commonmethods.actionToMoveToElement(self, currentCoverageAndSEP.continueToEnrollment)
            #self.driver.find_element(By.XPATH, currentCoverageAndSEP.continueToEnrollment).click()
            sleep(6)


















