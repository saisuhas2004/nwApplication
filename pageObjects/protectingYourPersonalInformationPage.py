from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


class protectingYourPersonalInformation:
    IAgree ="acceptedDataUsedStatement"  #Name
    IUnderstand = "acceptedTruthfullnessStatement"  # Name
    ContinueButton="//span[text()='Continue']"



    def __init__(self,driver):
        self.driver=driver

    def protectingYourPersonalInformation(self):
        sleep(5)
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(2)
        self.driver.find_element(By.NAME, protectingYourPersonalInformation.IAgree).click()
        self.driver.find_element(By.NAME, protectingYourPersonalInformation.IUnderstand).click()
        self.driver.find_element(By.XPATH, protectingYourPersonalInformation.ContinueButton).click()
        sleep(5)