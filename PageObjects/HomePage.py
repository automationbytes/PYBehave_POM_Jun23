import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:
    appLogo_webElement_classname = 'app_logo'
    filter_select_classname = '//select[@data-test="product_sort_container"]'
    openMenu_WebElement_id = 'react-burger-menu-btn'
    logOut_WebLink_id = 'logout_sidebar_link'

    def __init__(self,driver):
        self.driver =driver
#        self.driver = webdriver.Chrome()

    def verifyLogo(self):
        return self.driver.find_element(By.CLASS_NAME,self.appLogo_webElement_classname).is_displayed()

    def selectFilterDropdown(self,value):
        time.sleep(3)
        dropdown = Select(self.driver.find_element(By.XPATH,self.filter_select_classname))
        dropdown.select_by_visible_text(value)

    def clickLogout(self):
        self.driver.find_element(By.ID,self.openMenu_WebElement_id).click()
        self.driver.find_element(By.ID, self.logOut_WebLink_id).click()
