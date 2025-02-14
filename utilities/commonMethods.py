import json
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CommonMethods:



    def writeToTextFile(email):
        with open(
            'C:\\Users\\USER\\PycharmProjects\\behaveHealthCareGov\\features\\resources\\RIDP_Accounts.txt'
            ,'a') as file:
         file.write(email + '\n')
         print("***New Email ID added to text file***")
         file.close()

    def __init__(self, driver):
        self.driver = driver

    def actionToMoveToElement(self, WebElement):
         # create action chain object
        element = self.driver.find_element(By.XPATH, WebElement)
        action = ActionChains(self.driver)
        # perform the operation
        action.move_to_element(element).click().perform()

    def readDataFromJson(self,State, dataField):
        myJsonfile = open("C:\\Users\\USER\\PycharmProjects\\nwApplication\\testData\\test_Data.json", 'r')
        jsonData = myJsonfile.read()
        jsonElement= State+dataField
        # Parse the data
        obj = json.loads(jsonData)
        return str(obj[0][jsonElement])

    def pickTheStateLocator(self, State):
        thisdict = {
            "NC": "North Carolina",
            "SC": "South Carolina",
            "FL": "Florida",
            "TX": "Texas",
            "DE": "Delaware"
        }
        return thisdict.get(State)

    def pickTheState(self, State):
        stateValue = CommonMethods.pickTheStateLocator(self, State)
        pickState = "//span[text()='" + stateValue + "']"
        print("pick the state value" + pickState)
        return pickState

    def page_is_loading(self):
        while True:
            x = self.driver.execute_script("return document.readyState")
            if x == "complete":
                print("Page Loaded")
                return True
            else:
                yield False
    def test_timeouts_explicit_wait(self, xpath, xpathType):

        match xpathType:
            case "Xpath":
                # Define Fluent Wait (polling every 500 milliseconds and ignoring NoSuchElementException)
                wait = WebDriverWait(self.driver, 10, poll_frequency=0.5, ignored_exceptions=[TimeoutException])
                # Use the wait to wait for an element to be present
                element = wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
            case "Name":
                # Define Fluent Wait (polling every 500 milliseconds and ignoring NoSuchElementException)
                wait = WebDriverWait(self.driver, 10, poll_frequency=0.5, ignored_exceptions=[TimeoutException])
                # Use the wait to wait for an element to be present
                element = wait.until(expected_conditions.presence_of_element_located((By.NAME, xpath)))
            case "ID":
                # Define Fluent Wait (polling every 500 milliseconds and ignoring NoSuchElementException)
                wait = WebDriverWait(self.driver, 10, poll_frequency=0.5, ignored_exceptions=[TimeoutException])
                # Use the wait to wait for an element to be present
                element = wait.until(expected_conditions.presence_of_element_located((By.ID, xpath)))
            case "Tag":
                # Define Fluent Wait (polling every 500 milliseconds and ignoring NoSuchElementException)
                wait = WebDriverWait(self.driver, 10, poll_frequency=0.5, ignored_exceptions=[TimeoutException])
                # Use the wait to wait for an element to be present
                element = wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, xpath)))
        # Perform actions with the element
        #element.send_keys("text")

    def test_refresh_Button(self, xpath):
        # Define Fluent Wait (polling every 500 milliseconds and ignoring NoSuchElementException)
            for i in range(10):
                sleep(2)
                self.driver.refresh()
                if len(self.driver.find_elements(By.XPATH, xpath)) > 0:
                    break

            if len(self.driver.find_elements(By.XPATH, xpath)) > 0:
                self.driver.find_element(By.XPATH, xpath).click()
            else:
                print("Email is not triggered in Inbox. Stop the test")
                exit()






