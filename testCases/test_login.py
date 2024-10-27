import time
from webbrowser import Chrome

import pytest
from selenium import webdriver

import pageObjects
from pageObjects.LoginPage import LoginPage
from utilities.readPeoperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.debug("Test Case_01 HomePage Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        self.driver.close()

    def test_login(self,setup):
        self.logger.debug("Test Case_02 Login")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        #Create Object of Page object class
        self.lp = LoginPage(self.driver)
        time.sleep(20)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.logger.error("Test Case_02 Login ending")
        self.driver.save_screenshot(".\\screenshots\\"+"test_login_Page.png")
        self.driver.close()