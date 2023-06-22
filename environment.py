import allure
import logging
from selenium import webdriver

# Configure logging
logging.basicConfig(filename='logfile.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def before_all(context):
    logging.info("Before All")

def before_scenario(context, scenario):
    logging.info("Before Scenario")

def after_scenario(context, scenario):
    logging.info("After Scenario")

def before_step(context, step):
    logging.info("Before Step")

def after_step(context, step):
    logging.info("After Step")
    allure.attach(context.driver.get_screenshot_as_png(), name=step.name,
                  attachment_type=allure.attachment_type.PNG)
    if step.status == "failed":
        logging.error("Step failed: %s", step.name)
        context.driver.get_screenshot_as_png()
        context.driver.get_screenshot_as_file(step.name + ".png")

def after_all(context):
    logging.info("After All")
