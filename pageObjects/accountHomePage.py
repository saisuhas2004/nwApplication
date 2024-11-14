from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


class accountHomePage:
    pickTheStateYouLiveInDropDown = "//*[@id='stateDropdown']"
    pickTheState = "//*[@id='stateDropdown__item--20']/span[text()='North Carolina']"
    startapplication="//button[text()='Start application']"
    ContinueButton = "fars-continue"
    menu = "//button//following::span[text()='Menu']"
    accountHomepageList="//a[text()='Account home']"



    def __init__(self,driver):
        self.driver=driver

    def selectStateOnAccountHomePage(self):
        sleep(3)
        self.driver.find_element(By.ID, accountHomePage.ContinueButton).click()
        sleep(8)
        self.driver.find_element(By.XPATH, accountHomePage.menu).click()
        self.driver.find_element(By.XPATH, accountHomePage.accountHomepageList).click()
        sleep(5)
        self.driver.find_element(By.XPATH, accountHomePage.pickTheStateYouLiveInDropDown).click()
        self.driver.find_element(By.XPATH, accountHomePage.pickTheState).click()
        self.driver.find_element(By.XPATH, accountHomePage.startapplication).click()

    def selectStateOnExistingAccountHomePage(self):
        sleep(5)
        self.driver.find_element(By.XPATH, accountHomePage.pickTheStateYouLiveInDropDown).click()
        sleep(1)
        # get  element
        element = self.driver.find_element(By.XPATH, accountHomePage.pickTheState)
        # create action chain object
        action = ActionChains(self.driver)
        # perform the operation
        action.move_to_element(element).click().perform()
        sleep(1)
        self.driver.find_element(By.XPATH, accountHomePage.startapplication).click()