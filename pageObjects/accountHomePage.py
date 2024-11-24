from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from utilities.commonMethods import CommonMethods


class accountHomePage:
    pickTheStateYouLiveInDropDown = "//*[@id='stateDropdown']"
    startapplication="//button[text()='Start application']"
    ContinueButton = "fars-continue"
    menu = "//button//following::span[text()='Menu']"
    accountHomepageList="//a[text()='Account home']"
    viewAllApplications ="//a[text()='View all applications']"
    applyOrRenewButton ="//button[text()='Apply or renew']"


    def __init__(self,driver):
        self.driver=driver

    def selectStateOnAccountHomePage(self, State):
        sleep(3)
        self.driver.find_element(By.ID, accountHomePage.ContinueButton).click()
        sleep(8)
        self.driver.find_element(By.XPATH, accountHomePage.menu).click()
        self.driver.find_element(By.XPATH, accountHomePage.accountHomepageList).click()
        sleep(5)
        self.driver.find_element(By.XPATH, accountHomePage.pickTheStateYouLiveInDropDown).click()
        self.driver.find_element(By.XPATH, CommonMethods.pickTheState(self,State)).click()
        self.driver.find_element(By.XPATH, accountHomePage.startapplication).click()

    def selectStateOnExistingAccountHomePage(self, State):
        sleep(5)

        if len(self.driver.find_elements(By.XPATH, accountHomePage.viewAllApplications)) > 0:
            self.driver.find_element(By.XPATH, accountHomePage.viewAllApplications).click()
        sleep(5)
        self.driver.find_element(By.XPATH, accountHomePage.pickTheStateYouLiveInDropDown).click()
        sleep(1)
        # get  element
        element = self.driver.find_element(By.XPATH, CommonMethods.pickTheState(self,State))
        # create action chain object
        action = ActionChains(self.driver)
        # perform the operation
        action.move_to_element(element).click().perform()
        sleep(1)
        if len(self.driver.find_elements(By.XPATH, accountHomePage.startapplication)) > 0:
            self.driver.find_element(By.XPATH, accountHomePage.startapplication).click()
        else:
            self.driver.find_element(By.XPATH, accountHomePage.applyOrRenewButton).click()
