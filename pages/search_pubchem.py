from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class pubchem_home():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    #locators

    search_input_XPATH = (By.XPATH, "//input[@type='text']")
    search_button_XPATH = (By.XPATH, "//button[@type='submit']")

    aspirin_smile_XPATH = (By.XPATH, "//*[@id='collection-results-container']/div/div/div[2]/ul/li/div/div/div[1]/div[2]/div[5]/div/span/span[2]/span")

    #action

    def search_input(self,name):
        search_input = self.wait.until(EC.element_to_be_clickable(self.search_input_XPATH))
        search_input.clear()
        search_input.send_keys(name)

    def search_click(self):
        search_click = self.wait.until(EC.element_to_be_clickable(self.search_button_XPATH))
        search_click.click()

    #assertion
    def check_assertion_search(self):
        aspirin_smile_text = self.wait.until(EC.visibility_of_element_located(self.aspirin_smile_XPATH)).text.strip()
        assert 'CC(=O)OC1=CC=CC=C1C(=O)O' in aspirin_smile_text