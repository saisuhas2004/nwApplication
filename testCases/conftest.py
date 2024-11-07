from selenium import    webdriver
import pytest
from pytest_metadata.plugin import metadata_key
from platform import python_version


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("launching Chrome Browser")
    elif browser == 'firefox':
         driver=webdriver.Firefox()
         print("launching Firefox Browser")
    else:
        driver = webdriver.Ie()
        print("launching Internet Explorer Browser")

    return driver


def pytest_addoption(parser):  #This will get the value from CLI/Hooks
   parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to set up method
    return request.config.getoption("--browser")

########### Pytest HTML Report ###############

def pytest_html_report_title(report):
#modifying the title of html report
	report.title = "Regression Automation Report"

# it is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "Hybrid Framework Practice",
        "Module Name": "Customers",
        "Automation Engineer": "Pavan"
    }

# it is hook for delete/modify Environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)
