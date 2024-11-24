import json

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


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
            "SC": "South Carolina"
        }
        return thisdict.get(State)

    def pickTheState(self, State):
        stateValue = CommonMethods.pickTheStateLocator(self, State)
        pickState = "//span[text()='" + stateValue + "']"
        print("pick the state value" + pickState)
        return pickState


