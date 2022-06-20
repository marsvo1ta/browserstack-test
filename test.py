from appium import webdriver
from appiumbase import BaseCase


desired_cap = {
    # Set your access credentials
    "browserstack.user" : "antonnemchynov_xdXhmt",
    "browserstack.key" : "g2w5qYhQYBnCukypqeks",

    # Set URL of the application under test
    "app" : "bs://a3026cfa929f43641848069d01d4d5b8246dc449",

    # Specify device and os_version for testing
    "device" : "Xiaomi Redmi Note 7",
    "os_version" : "9.0",
    "device" : "Samsung Galaxy S8 Plus",
    "os_version" : "9.0",
    "automationName" : "UiAutomator2",
    
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "Python Android",
    "name" : "first_test"
}


def test_two():
    assert 1==1

def test_bro():
    driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap)
    driver.quit()
