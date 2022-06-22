from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


desired_cap = {
    
    "browserstack.user" : "antonnemchynov_xdXhmt",
    "browserstack.key" : "g2w5qYhQYBnCukypqeks",
    "app" : "bs://a3026cfa929f43641848069d01d4d5b8246dc449",
    "device" : "Xiaomi Redmi Note 7",
    "os_version" : "9.0",
    "automationName" : "UiAutomator2",
    "project" : "First Python project", 
    "build" : "Python Android",
    "name" : "browserstack_test"
}


driver = webdriver.Remote('http://hub-cloud.browserstack.com/wd/hub',desired_capabilities=desired_cap)

def test_1():
    driver.find_element(MobileBy.ID, 'com.velvot.android:id/onBoardingCreateBtn')
    driver.quit()