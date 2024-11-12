import time
from time import sleep
import random
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
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
    iUnderstandCheckBox = "terms-checkbox"
    createAccountButton = "create-account-button"
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
        sleep(10)
        self.driver.find_element(By.XPATH, LoginPage.logIn).click()

    def createAccountLink(self):
        sleep(5)
        self.driver.find_element(By.XPATH, LoginPage.createAccount).click()

    def createAccount_pickTheStateYouLiveInDropDown(self):
        sleep(7)
        self.driver.find_element(By.XPATH, LoginPage.pickTheStateYouLiveInDropDown).click()

    def createAccountPickTheState(self):
        sleep(3)
        # get  element
        element = self.driver.find_element(By.XPATH, LoginPage.pickTheState)
        # create action chain object
        action = ActionChains(self.driver)
        # perform the operation
        action.move_to_element(element).click().perform()


    def createAccountEnterFirstName(self):
        sleep(2)
        self.driver.find_element(By.NAME, LoginPage.firstName).send_keys("JOYCE")

    def createAccountEnterLastName(self):
        sleep(2)
        self.driver.find_element(By.NAME, LoginPage.lastName).send_keys("WATLINGTON")

    def createAccountEnterEmail(self, email):

        self.driver.find_element(By.NAME, LoginPage.emailAddress).send_keys(email)


    def createAccountEnterPassword(self):
        sleep(2)
        self.driver.find_element(By.NAME, LoginPage.password).send_keys("Test123#")

    def createAccountFirstSecurityQuestion(self):
        sleep(3)
        # to scroll try use the following command
        self.driver.execute_script("scrollBy(0,1000);")
        time.sleep(3)
        self.driver.find_element(By.XPATH, LoginPage.securityQuestionOneDropDown).click()
        self.driver.find_element(By.XPATH, LoginPage.securityQuestionOne).click()
        self.driver.find_element(By.NAME, LoginPage.securityQuestionOneAns).send_keys("Station")

    def createAccountSecondSecurityQuestion(self):
        sleep(2)
        self.driver.find_element(By.XPATH, LoginPage.securityQuestionTwoDropDown).click()
        self.driver.find_element(By.XPATH, LoginPage.securityQuestionTwo).click()
        self.driver.find_element(By.NAME, LoginPage.securityQuestionTwoAns).send_keys("Child")

    def createAccountThirdSecurityQuestion(self):
        sleep(2)
        self.driver.find_element(By.XPATH, LoginPage.securityQuestionThreeDropDown).click()
        self.driver.find_element(By.XPATH, LoginPage.securityQuestionThree).click()
        self.driver.find_element(By.NAME, LoginPage.securityQuestionThreeAns).send_keys("cuisine")
        sleep(3)
        # to scroll try use the following command
        self.driver.execute_script("scrollBy(0,500);")
        time.sleep(3)



    def createAccount_ClickOnCreateAccountButton(self):
        self.driver.find_element(By.ID, LoginPage.iUnderstandCheckBox).click()
        self.driver.find_element(By.ID, LoginPage.createAccountButton).click()
        time.sleep(4)

    def createAccount_LogIntoAppSpotAccount(self,email):
        time.sleep(3)
        self.driver.find_element(By.NAME, LoginPage.emailAddressTextbox).send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, LoginPage.checkMessageButton).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, LoginPage.checkMailInBox).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, LoginPage.verifyMyEmailAddress).click()

    def createAccount_LoginIntoHealtCare(self, email):
        time.sleep(3)
        self.driver.find_element(By.XPATH, LoginPage.loginButton).click()
        time.sleep(2)
        self.driver.find_element(By.NAME, LoginPage.username).send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.NAME, LoginPage.pasword).send_keys("Test123#")
        time.sleep(1)
        self.driver.find_element(By.ID, LoginPage.login).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, LoginPage.setUpLater).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, LoginPage.manageYourSetting).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, LoginPage.verifyNow).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, LoginPage.birthMonth).send_keys("06")
        self.driver.find_element(By.XPATH, LoginPage.birthDay).send_keys("27")
        self.driver.find_element(By.XPATH, LoginPage.birthYear).send_keys("1951")
        time.sleep(1)
        self.driver.find_element(By.XPATH, LoginPage.streetAddress).send_keys("RR 9 BOX 126")
        time.sleep(1)
        self.driver.execute_script("scrollBy(0,800);")
        time.sleep(3)
        self.driver.find_element(By.XPATH, LoginPage.city).send_keys("HENDERSON")
        self.driver.find_element(By.XPATH, LoginPage.zip).send_keys("27536")

        self.driver.find_element(By.XPATH, LoginPage.phone).send_keys("9106944250")
        self.driver.find_element(By.XPATH, LoginPage.termsAndConditions).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, LoginPage.continueButton).click()
        time.sleep(2)
        messageValue = self.driver.find_element(By.TAG_NAME, "h1")
        print(messageValue)








    def setUserName(self,username):
        self. driver.find_element(By.ID, self.sign_in_button_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.member_logIn_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.username_textbox_ID).send_keys(username)
        time.sleep(10)
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_texbox_ID).send_keys(password)