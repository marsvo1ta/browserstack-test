from appium import webdriver

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


def test_one():
    assert 1==12
