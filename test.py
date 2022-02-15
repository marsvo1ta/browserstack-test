from appium import webdriver

desired_cap = {
    # Set your access credentials
    "browserstack.user" : "antonnemchynov_xdXhmt",
    "browserstack.key" : "g2w5qYhQYBnCukypqeks",

    # Set URL of the application under test
    "app" : "bs://af95ca5ac0ff178d7df7bf0770cd80bfd7db2564",

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

driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)

driver.swipe(100,100,100,500)

def test_one():
    assert 1==12