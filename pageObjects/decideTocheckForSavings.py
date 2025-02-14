from time import sleep

from selenium.webdriver.common.by import By
from pageObjects.methods_Mapping import pageMapper
from utilities.commonMethods import CommonMethods

class decideToCheckForSavings:
    Commonmethods = CommonMethods
    taxFilingSize = "//input[@name='taxHouseholdSize']"
    IChooseNotToAnswer ="//input[@name='estimatedIncome'][@value='declined']"
    incomeChooseLess64K = "//input[@name='estimatedIncome'][@value='less']"
    checkForAllSavingsOption = "//input[@name='requestingFinancialAssistance'][@value='1']"
    continueWithoutCheckingForSavingsOption="//input[@name='requestingFinancialAssistance'][@value='0']"



    def __init__(self, driver):
        self.driver = driver

    def enterApplicationTaxFilingInformation(self):
        #sleep(5)
        decideToCheckForSavings.Commonmethods.test_timeouts_explicit_wait(self, decideToCheckForSavings.taxFilingSize, "Xpath")
        self.driver.find_element(By.XPATH, decideToCheckForSavings.taxFilingSize).send_keys("1")
        #sleep(3)
        decideToCheckForSavings.Commonmethods.test_timeouts_explicit_wait(self, decideToCheckForSavings.IChooseNotToAnswer,
                                                                          "Xpath")
        CommonMethods.actionToMoveToElement(self, decideToCheckForSavings.IChooseNotToAnswer)
        #self.driver.execute_script("scrollBy(0,400);")
        #self.driver.find_element(By.XPATH, decideToCheckForSavings.IChooseNotToAnswer).click()
        # sleep(2)
        # self.driver.execute_script("scrollBy(0,400);")
        sleep(3)
        decideToCheckForSavings.Commonmethods.test_timeouts_explicit_wait(self,
                                                                          decideToCheckForSavings.continueWithoutCheckingForSavingsOption,
                                                                          "Xpath")
        CommonMethods.actionToMoveToElement(self, decideToCheckForSavings.continueWithoutCheckingForSavingsOption)
        #sleep(2)
        decideToCheckForSavings.Commonmethods.test_timeouts_explicit_wait(self,
                                                                          pageMapper.CommonObjects.continuButton,
                                                                          "Xpath")
        CommonMethods.actionToMoveToElement(self, pageMapper.CommonObjects.continuButton)
        #self.driver.find_element(By.XPATH, pageMapper.CommonObjects.continuButton).click()
        #sleep(5)

    def enterFAApplicationTaxFilingInformation(self):
        #sleep(5)
        decideToCheckForSavings.Commonmethods.test_timeouts_explicit_wait(self,
                                                                          decideToCheckForSavings.taxFilingSize,
                                                                          "Xpath")
        self.driver.find_element(By.XPATH, decideToCheckForSavings.taxFilingSize).send_keys("1")
        #sleep(3)
        CommonMethods.actionToMoveToElement(self, decideToCheckForSavings.incomeChooseLess64K)
        #sleep(3)
        CommonMethods.actionToMoveToElement(self, decideToCheckForSavings.checkForAllSavingsOption)
        #sleep(2)
        CommonMethods.actionToMoveToElement(self, pageMapper.CommonObjects.continuButton)
        #sleep(5)
