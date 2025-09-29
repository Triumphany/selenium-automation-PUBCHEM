from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import re

class pubchem_home():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    #locators

    browserBUTTON_XPATH = (By.XPATH, "//span[text()='Browse Data']")
    selectCLASSIFICATION_ID = (By.ID, 'classification-select')

    #action
    def clickBROWSER_button(self):
        browserBUTTON_click = self.wait.until(EC.element_to_be_clickable(self.browserBUTTON_XPATH))
        browserBUTTON_click.click()

    def select_classification(self,name):
        select_elem = self.wait.until(EC.visibility_of_element_located(self.selectCLASSIFICATION_ID))
        select_classification_option_DISPLAY = Select(select_elem)
        select_classification_option_DISPLAY.select_by_value(name)

