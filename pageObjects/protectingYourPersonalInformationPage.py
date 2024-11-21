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
        sleep(5)
        protectingYourPersonalInformation.Commonmethods.actionToMoveToElement(self, protectingYourPersonalInformation.IAgree)
        sleep(1)
        protectingYourPersonalInformation.Commonmethods.actionToMoveToElement(self, protectingYourPersonalInformation.IUnderstand)
        protectingYourPersonalInformation.Commonmethods.actionToMoveToElement(self, protectingYourPersonalInformation.ContinueButton)
        sleep(5)