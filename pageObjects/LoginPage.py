import time
from time import sleep
import random
from utilities.writeToOracleDatabase import writeToOracleDB
from utilities.commonMethods import CommonMethods

from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    Commonmethods = CommonMethods
    sign_in_button_ID="signInButton_CustomDropdown_Btn"
    member_logIn_ID='1018124763'
    username_textbox_ID="username"
    password_texbox_ID="password"
    popup = "//img[contains(@src, 'svg-close-btn-white-1.svg')]"
    logIn = "//a[@class='hc-c-logged-out-links__link sl-c-login sl_swap']"
    loginTitle = "//title[contains(text(), 'HealthCare.gov')]"
    createAccount = "//a[text()='Create account']"

    # Create an account page
    pickTheStateYouLiveInDropDown = "//*[@id='dropdown--9__button-content']"
    pickTheState = "//*[@class='ds-c-dropdown__menu-container ds-c-field--medium']//li/span[text()='North Carolina']"
    firstName = "firstName"
    lastName = "lastName"
    emailAddress = "email"
    password = "Password"
    securityQuestionOneDropDown = "//*[@data-testid='securityQuestionOne']/span[1]"
    securityQuestionOne = "//span[text()='What is your favorite radio station?']"
    securityQuestionOneAns = "answer1"
    securityQuestionTwoDropDown = "//*[@data-testid='securityQuestionTwo']"
    securityQuestionTwo = "//span[text()='What was your favorite toy when you were a child?']"
    securityQuestionTwoAns = "answer2"
    securityQuestionThreeDropDown = "//*[@data-testid='securityQuestionThree']"
    securityQuestionThree = "//span[text()='What is your favorite cuisine?']"
    securityQuestionThreeAns = "answer3"
    iUnderstandCheckBox = "//*[@id='terms-checkbox']"
    createAccountButton = "//*[@id='create-account-button']"
    accountCreationMessage = "//h2[text()='Verify your email address to finish creating your account']"

    # https://message-checker.appspot.com/
    emailAddressTextbox = "address"
    checkMessageButton = "//button[text()='Check for messages']"
    checkMailInBox = "//a[@id='subject-0']"
    verifyMyEmailAddress = "//a/img[@alt='verify my email address']"

    # login
    loginButton = "//*[@data-testid='loginButton']"
    username = "Username"
    pasword = "Password"
    login = "login-button"

    #Homepage
    setUpLater = "//button[text()='Set up later']"
    manageYourSetting = "//a[text()='Manage account settings']"
    verifyNow = "//a[text()='Verify now']"
    birthMonth = "//*[@name='month']"
    birthDay = "//*[@name='day']"
    birthYear = "//*[@name='year']"
    streetAddress = "//*[@name='streetAddress']"
    city = "//*[@name='city']"
    zip = "//*[@name='zip']"
    phone = "//*[@name='phone']"
    termsAndConditions = "//*[@name='termsAndConditions']"
    continueButton = "//*[@id='create-account-button']"
    messageIdentityVerified = "//h1[text()='Identity verified']"
    expected_header = "Identity verified"


    def __init__(self,driver):
        self.driver=driver

    def closePopupOnLandingPage(self):
        self.driver.maximize_window()
        if len(self.driver.find_elements(By.XPATH, LoginPage.popup)) > 0:
            self.driver.find_elements(By.XPATH, LoginPage.popup).click()

    def clickOn_LoginLink(self):
        LoginPage.Commonmethods.page_is_loading(self)
        self.driver.find_element(By.XPATH, LoginPage.logIn).click()

    def createAccountLink(self):
        LoginPage.Commonmethods.page_is_loading(self)
        self.driver.find_element(By.XPATH, LoginPage.createAccount).click()

    def createAccount_pickTheStateYouLiveInDropDown(self):
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.pickTheStateYouLiveInDropDown,"Xpath")
        self.driver.find_element(By.XPATH, LoginPage.pickTheStateYouLiveInDropDown).click()

    def createAccountPickTheState(self):
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.pickTheState)

    def createAccountEnterFirstName(self, State):
        self.driver.find_element(By.NAME, LoginPage.firstName).send_keys(CommonMethods.readDataFromJson(self,State,"First_Name"))

    def createAccountEnterLastName(self, State):
        self.driver.find_element(By.NAME, LoginPage.lastName).send_keys(CommonMethods.readDataFromJson(self, State, "Last_Name"))

    def createAccountEnterEmail(self, email):
        self.driver.find_element(By.NAME, LoginPage.emailAddress).send_keys(email)


    def createAccountEnterPassword(self):
        self.driver.find_element(By.NAME, LoginPage.password).send_keys(CommonMethods.readDataFromJson(self, "", "Password"))

    def createAccountFirstSecurityQuestion(self):
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.securityQuestionOneDropDown,"Xpath")
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.securityQuestionOneDropDown)
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.securityQuestionOne)
        self.driver.find_element(By.NAME, LoginPage.securityQuestionOneAns).send_keys(CommonMethods.readDataFromJson(self, "", "SecurityOneAns"))

    def createAccountSecondSecurityQuestion(self):
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.securityQuestionTwoDropDown,"Xpath")
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.securityQuestionTwoDropDown)
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.securityQuestionTwo)
        self.driver.find_element(By.NAME, LoginPage.securityQuestionTwoAns).send_keys(CommonMethods.readDataFromJson(self, "", "SecurityTwoAns"))

    def createAccountThirdSecurityQuestion(self):
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.securityQuestionThreeDropDown,"Xpath")
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.securityQuestionThreeDropDown)
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.securityQuestionThree)
        self.driver.find_element(By.NAME, LoginPage.securityQuestionThreeAns).send_keys(CommonMethods.readDataFromJson(self, "", "SecurityThreeAns"))



    def createAccount_ClickOnCreateAccountButton(self):
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.iUnderstandCheckBox,"Xpath")
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.iUnderstandCheckBox)
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.createAccountButton, "Xpath")
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.createAccountButton)


    def createAccount_LogIntoAppSpotAccount(self,email):
        LoginPage.Commonmethods.page_is_loading(self)
        self.driver.find_element(By.NAME, LoginPage.emailAddressTextbox).send_keys(email)
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.checkMessageButton, "Xpath")
        self.driver.find_element(By.XPATH, LoginPage.checkMessageButton).click()
        LoginPage.Commonmethods.test_refresh_Button(self, LoginPage.checkMailInBox)
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.verifyMyEmailAddress,"Xpath")
        self.driver.find_element(By.XPATH, LoginPage.verifyMyEmailAddress).click()

    def createAccount_LoginIntoHealtCare(self, email, State):
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.loginButton,"Xpath")
        self.driver.find_element(By.XPATH, LoginPage.loginButton).click()
        #time.sleep(2)
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.username, "Name")
        self.driver.find_element(By.NAME, LoginPage.username).send_keys(email)
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.pasword, "Name")
        self.driver.find_element(By.NAME, LoginPage.pasword).send_keys(CommonMethods.readDataFromJson(self, "", "Password"))
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.login, "ID")
        self.driver.find_element(By.ID, LoginPage.login).click()
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.setUpLater,"Xpath")
        self.driver.find_element(By.XPATH, LoginPage.setUpLater).click()
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.manageYourSetting,"Xpath")
        self.driver.find_element(By.XPATH, LoginPage.manageYourSetting).click()
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.verifyNow,"Xpath")
        self.driver.find_element(By.XPATH, LoginPage.verifyNow).click()

        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.birthMonth,"Xpath")
        self.driver.find_element(By.XPATH, LoginPage.birthMonth).send_keys(CommonMethods.readDataFromJson(self,State,"Birth_Month"))
        self.driver.find_element(By.XPATH, LoginPage.birthDay).send_keys(CommonMethods.readDataFromJson(self,State,"Birth_Day"))
        self.driver.find_element(By.XPATH, LoginPage.birthYear).send_keys(CommonMethods.readDataFromJson(self,State,"Birth_Year"))

        self.driver.find_element(By.XPATH, LoginPage.streetAddress).send_keys(CommonMethods.readDataFromJson(self,State,"AddressLine1"))
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.city,"Xpath")
        LoginPage.Commonmethods.actionToMoveToElement(self,  LoginPage.city)


        self.driver.find_element(By.XPATH, LoginPage.city).send_keys(CommonMethods.readDataFromJson(self,State,"City"))
        self.driver.find_element(By.XPATH, LoginPage.zip).send_keys(CommonMethods.readDataFromJson(self,State,"ZIPCode"))

        self.driver.find_element(By.XPATH, LoginPage.phone).send_keys(CommonMethods.readDataFromJson(self,State,"PhoneNumber"))
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.termsAndConditions,"Xpath")
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.termsAndConditions)
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.continueButton,"Xpath")
        LoginPage.Commonmethods.actionToMoveToElement(self, LoginPage.continueButton)
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, "h1", "Tag")
        messageValue = self.driver.find_element(By.TAG_NAME, "h1")
        print(messageValue)
        time_string = time.asctime().replace(":", " ")
        self.driver.save_screenshot(
            "C:\\Users\\USER\\PycharmProjects\\nwApplication\\screenshots\\RIDPPage" + time_string + ".png")

    def setUserName(self,username):
        self. driver.find_element(By.ID, self.sign_in_button_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.member_logIn_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.username_textbox_ID).send_keys(username)
        time.sleep(10)
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_texbox_ID).send_keys(password)

    def LoginWithExistingAccount_HealthCare(self, registered_Email):
        #time.sleep(2)
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.username, "Name")
        self.driver.find_element(By.NAME, LoginPage.username).send_keys(registered_Email)
        self.driver.find_element(By.NAME, LoginPage.pasword).send_keys(CommonMethods.readDataFromJson(self, "", "Password"))
        LoginPage.Commonmethods.test_timeouts_explicit_wait(self, LoginPage.login, "ID")
        self.driver.find_element(By.ID, LoginPage.login).click()
        time.sleep(5)