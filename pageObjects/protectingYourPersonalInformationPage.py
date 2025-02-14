from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

from utilities.commonMethods import CommonMethods


class protectingYourPersonalInformation:
    Commonmethods = CommonMethods
    IAgree ="//*[@name='acceptedDataUsedStatement']"  #Name
    IUnderstand = "//*[@name='acceptedTruthfullnessStatement']"  # Name
    ContinueButton="//span[text()='Continue']"



    def __init__(self,driver):
        self.driver=driver

    def protectingYourPersonalInformation(self):
        protectingYourPersonalInformation.Commonmethods.test_timeouts_explicit_wait(self, protectingYourPersonalInformation.IAgree, "Xpath")
        protectingYourPersonalInformation.Commonmethods.actionToMoveToElement(self, protectingYourPersonalInformation.IAgree)
        protectingYourPersonalInformation.Commonmethods.test_timeouts_explicit_wait(self,
                                                                                    protectingYourPersonalInformation.IUnderstand,
                                                                                    "Xpath")
        protectingYourPersonalInformation.Commonmethods.actionToMoveToElement(self, protectingYourPersonalInformation.IUnderstand)
        protectingYourPersonalInformation.Commonmethods.actionToMoveToElement(self, protectingYourPersonalInformation.ContinueButton)
