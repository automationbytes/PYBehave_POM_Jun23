from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    username_textbox_id = 'user-name'
    password_textbox_id = 'password'
    login_button_name = 'login-button'

    def __init__(self,driver):
        self.driver =driver
        #self.driver = webdriver.Chrome()

    def enterUserName(self,user):
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(user)

    def enterPassword(self,passwrd):
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(passwrd)

    def clickLogin(self):
        self.driver.find_element(By.NAME,self.login_button_name).click()