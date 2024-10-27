import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class LoginPage:
    sign_in_button_ID="signInButton_CustomDropdown_Btn"
    member_logIn_ID='1018124763'
    username_textbox_ID="username"
    password_texbox_ID="password"



    def __init__(self,driver):
        self.driver=driver


    def setUserName(self,username):
        self. driver.find_element(By.ID, self.sign_in_button_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.member_logIn_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.username_textbox_ID).send_keys(username)
        time.sleep(10)
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_texbox_ID).send_keys(password)