import re
from time import sleep


from pytest_check import check
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.methods_Mapping import pageMapper


class planComparePage:
    startButton = "//a[text()='Start']"
    skipButton ="//*[text()='Skip']"
    nextButton ="//button[text()='Next']"
    seeAllPlans = "//button[text()='See all plans']"
    enrollButton ="//*[text()='Enroll']"
    selectThisPlan ="//button[text()='Select this plan']"
    noCompleteHealthPlanEnrollment="// *[ @ value = 'no']"
    conformPlanChoice ="//*[text()='Confirm plan choices']"
    yourAlmostDone ="//h1[@id='page-heading']"


    def __init__(self, driver):
        self.driver = driver

       # You’re eligible to enroll in Marketplace coverage
        # Current coverage & life changes
    def eligibleToEnroll(self):
        self.driver.find_element(By.XPATH, planComparePage.startButton).click()
        sleep(5)

        #Report a tobacco
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.NoFalse).click()
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        # #Get an estimate of your total health care costs for the year
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(3)
        self.driver.find_element(By.XPATH, pageMapper.CommonObjects.saveAndContinue).click()
        sleep(5)

        #See if your doctors, facilities & drugs are covered
        self.driver.find_element(By.XPATH, planComparePage.skipButton).click()
        sleep(5)

        #Help comparing plans
        self.driver.find_element(By.XPATH, planComparePage.nextButton).click()
        sleep(2)
        self.driver.find_element(By.XPATH, planComparePage.seeAllPlans).click()
        sleep(5)

        #Pick a health plan
        sleep(5)
        self.driver.execute_script("scrollBy(0,600);")
        #self.driver.find_element(By.XPATH, planComparePage.enrollButton).select_by_index(0).click()
        sleep(5)
       # self.driver.execute_script("scrollBy(0,900);")
        elements =self.driver.find_elements(By.XPATH, planComparePage.enrollButton)
        # Index of the element you want to click (index 0)
        index_to_click = 0
       # elements[index_to_click].click()
        # create action chain object
        action = ActionChains(self.driver)
        # perform the operation
        action.move_to_element(elements[index_to_click]).click().perform()


        #Health plan selection
        sleep(5)
        self.driver.execute_script("scrollBy(0,1200);")
        sleep(2)
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(2)
        self.driver.find_element(By.XPATH, planComparePage.selectThisPlan).click()

        # Review your health plan choices
        sleep(6)
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(2)
        self.driver.execute_script("scrollBy(0,1000);")
        sleep(2)
        self.driver.find_element(By.XPATH, planComparePage.noCompleteHealthPlanEnrollment).click()
        self.driver.find_element(By.XPATH, planComparePage.conformPlanChoice).click()
        sleep(18)
        get_url =self.driver.current_url
        Application_ID = re.sub('[^0-9]', '', get_url)
        print("Application ID==" + Application_ID)

        #You're almost done
        self.driver.save_screenshot("C:/Users/USER/PycharmProjects/nwApplication/ApplicationID_"+Application_ID+"_PlanComparePage.png")
        message = self.driver.find_element(By.XPATH, planComparePage.yourAlmostDone)
        print(message.text)








