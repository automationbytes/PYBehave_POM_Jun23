import allure
from behave import given, when, then,step
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(30)
driver.maximize_window()
hp = HomePage(driver)
lp = LoginPage(driver)

@given(u'the user launches the application')
def the_user_launches_the_application(context):
    context.driver = driver
    context.driver.get("https://www.saucedemo.com/")

@when(u'the user verifies the application is loaded')
def the_user_verifies_the_application_is_loaded(context):
    context.driver = driver
    logo = context.driver.find_element(By.CLASS_NAME,"login_logo").is_displayed()
    assert logo is True

@then(u'the user enters the valid credentials')
def the_user_enters_the_valid_credentials(context):
    context.driver =driver
    lp.enterUserName("standard_user")
    lp.enterPassword("secret_sauce")
    lp.clickLogin()

@given(u'the user is on home page')
def the_user_is_on_home_page(context):
    context.driver = driver
    assert hp.verifyLogo() is True


@then(u'the user filters high to low')
def the_user_filters_hightolow(context):
    context.driver = driver
    hp.selectFilterDropdown("Price (high to low)")

@given(u'the user logouts from the site')
def logout(context):
    context.driver =driver
    hp.clickLogout()

#
# def after_step(context, step):
#     if step.status == "failed":
#         Capture_Screensht(context)
#
# def Capture_Screensht(context):
#     context.driver = driver
#     allure.attach(context.driver.get_screenshot_as_png(), name=step.name, attachment_type=allure.attachment_type.PNG)
#

@then(u'the user filters "{filter}"')
def the_user_filters(context,filter):
    context.driver = driver
    hp.selectFilterDropdown(filter)

