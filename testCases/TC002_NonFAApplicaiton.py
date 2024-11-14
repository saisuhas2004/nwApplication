import random
import time
from webbrowser import Chrome

import pytest
from selenium import webdriver

import pageObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.accountHomePage import accountHomePage
from pageObjects.homeAddress import homeAddress
from pageObjects.protectingYourPersonalInformationPage import protectingYourPersonalInformation
from pageObjects.tellUsAboutYourself import tellUsAboutYourself
from pageObjects.whoNeedsHealthCoverage import whoNeedsHealthCoverage
from pageObjects.yourMarketplaceApplicationPage import yourMarketPlaceApplicationPage
from pageObjects.applicationSetupPage import applicationSetupPage
from pageObjects.decideTocheckForSavings import decideToCheckForSavings
from pageObjects.kayak import kayakPage
from utilities.readPeoperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.commonMethods import CommonMethods
from utilities.writeToOracleDatabase import writeToOracleDB

class Test_002_NonFAApplicaiton:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    Commonmethods = CommonMethods()

    # number = random.randint(1000, 9999)
    # email = "MapchuWill" + str(number) + "@message-checker.appspotmail.com"
    # print(email)
    # Commonmethods.writeToTextFile(email)
    print("Email Retrived from Database")
    print(writeToOracleDB.readFromDatabase())



    def test_FAApplicaiton(self, setup):
        self.logger.debug("Test Case_01 HomePage Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        # start the application
        # accountHomePage.selectStateOnAccountHomePage(self)
        # protectingYourPersonalInformation.protectingYourPersonalInformation(self)
        # yourMarketPlaceApplicationPage.ContinueToApplication(self)
        self.logger.debug("Test Case_01 HomePage Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        LoginPage.closePopupOnLandingPage(self)
        LoginPage.clickOn_LoginLink(self)
        LoginPage.LoginWithExistingAccount_HealthCare(self, writeToOracleDB.readFromDatabase())

       #  # start the application
        accountHomePage.selectStateOnExistingAccountHomePage(self)
        protectingYourPersonalInformation.protectingYourPersonalInformation(self)
        yourMarketPlaceApplicationPage.continueYourMarketPlaceApplicationPage(self)
        applicationSetupPage.applicationSetupPageContinue(self)
       # #yourMarketPlaceApplicationPage.continueYourMarketPlaceApplicationPage(self)
        decideToCheckForSavings.enterApplicationTaxFilingInformation(self)
        tellUsAboutYourself.tellUsAboutYourselfInformation(self)
        homeAddress.homeAddressInfo(self)
        whoNeedsHealthCoverage.whoNeedHealthCoverage(self)







    # def test_Kayak_Flight_Price(self, setup):
    #     self.logger.debug("Test Case_02 Kayak Flight Price")
    #     self.driver = setup
    #     self.driver.get(self.baseKayakURL)
    #     act_title = self.driver.title
    #     print(act_title)
    #     kayakPage.search_Flights_On_Landing_Page(self)





