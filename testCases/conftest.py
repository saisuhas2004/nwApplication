from selenium import    webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("launching Chrome Browser")
    elif browser == 'firefox':
         driver=webdriver.Firefox()
         print("launching Firefox Browser")
    return driver


def pytest_addoption(parser):  #This will get the value from CLI/Hooks
   parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to set up method
    return request.config.getoption("--browser")