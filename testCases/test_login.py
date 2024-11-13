import random
import time
from webbrowser import Chrome

import pytest
from selenium import webdriver

import pageObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.accountHomePage import accountHomePage
from pageObjects.protectingYourPersonalInformationPage import protectingYourPersonalInformation
from pageObjects.yourMarketplaceApplicationPage import yourMarketPlaceApplicationPage
from pageObjects.applicationSetupPage import applicationSetupPage
from pageObjects.decideTocheckForSavings import decideToCheckForSavings
from pageObjects.kayak import kayakPage
from utilities.readPeoperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.commonMethods import CommonMethods

class Test_001_NewAccountRegistration:
    baseURL=ReadConfig.getApplicationURL()
    baseAppSpotURL = ReadConfig.getAppSpotURL()
    baseKayakURL = ReadConfig.getKayakURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    Commonmethods = CommonMethods()

    number = random.randint(1000, 9999)
    email = "MapchuWill" + str(number) + "@message-checker.appspotmail.com"
    print(email)
    Commonmethods.writeToTextFile(email)
    registered_Email="testwilli9181@message-checker.appspotmail.com"


    # def test_ApplicationCreation(self,setup):
    #     self.logger.debug("Test Case_01 HomePage Title")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #     print(act_title)
    #     LoginPage.closePopupOnLandingPage(self)
    #     LoginPage.clickOn_LoginLink(self)
    #     LoginPage.createAccountLink(self)
    #     LoginPage.createAccount_pickTheStateYouLiveInDropDown(self)
    #     LoginPage.createAccountPickTheState(self)
    #     LoginPage.createAccountEnterFirstName(self)
    #     LoginPage.createAccountEnterLastName(self)
    #     LoginPage.createAccountEnterEmail(self, self.email)
    #     LoginPage.createAccountEnterPassword(self)
    #     LoginPage.createAccountFirstSecurityQuestion(self)
    #     LoginPage.createAccountSecondSecurityQuestion(self)
    #     LoginPage.createAccountThirdSecurityQuestion(self)
    #     LoginPage.createAccount_ClickOnCreateAccountButton(self)
    #     self.driver.get(self.baseAppSpotURL)
    #     LoginPage.createAccount_LogIntoAppSpotAccount(self, self.email)
    #     LoginPage.createAccount_LoginIntoHealtCare(self, self.email)
    #
    # # start the application
    #     accountHomePage.selectStateOnAccountHomePage(self)
    #     protectingYourPersonalInformation.protectingYourPersonalInformation(self)
    #     yourMarketPlaceApplicationPage.ContinueToApplication(self)

    def test_homePage_AccountRegistration(self, setup):
        self.logger.debug("Test Case_01 HomePage Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        LoginPage.closePopupOnLandingPage(self)
        LoginPage.clickOn_LoginLink(self)
        LoginPage.LoginWithExistingAccount_HealthCare(self, self.registered_Email)

        # start the application
        accountHomePage.selectStateOnExistingAccountHomePage(self)
        protectingYourPersonalInformation.protectingYourPersonalInformation(self)
        yourMarketPlaceApplicationPage.continueYourMarketPlaceApplicationPage(self)
        applicationSetupPage.applicationSetupPageContinue(self)
       # yourMarketPlaceApplicationPage.continueYourMarketPlaceApplicationPage(self)
        decideToCheckForSavings.enterApplicationTaxFilingInformation(self)







    # def test_Kayak_Flight_Price(self, setup):
    #     self.logger.debug("Test Case_02 Kayak Flight Price")
    #     self.driver = setup
    #     self.driver.get(self.baseKayakURL)
    #     act_title = self.driver.title
    #     print(act_title)
    #     kayakPage.search_Flights_On_Landing_Page(self)





