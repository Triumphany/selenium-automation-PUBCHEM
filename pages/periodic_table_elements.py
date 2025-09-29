from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class pubchem_home():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = get_logger(self.__class__.__name__)

    #Common locators
    periodicTABLE_BUTTONS_XPATH = (By.XPATH, "//span[contains(@class, 'btn-text p-sm-top f-1') and text()='Periodic Table']")
    elements_button_common_XPATH = (By.XPATH, "//div[@data-tooltip='Symbol' and text()='']")
    close_button_forELEMNT_XPATH = (By.XPATH, "//button[contains(@class, 'mx-2 rounded-full')]")
    #action

    def click_periodic_table_button(self):
        button = self.wait.until(EC.visibility_of_element_located(self.periodicTABLE_BUTTONS_XPATH))
        button.click()
        self.logger.info(f"Periodic Table button : clicked")

    def click_elements(self,name):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@data-tooltip='Symbol' and text()='{name}']")))
        element.click()
        self.logger.info(f"{name} : clicked")

    def click_close_element_DIALOGUEbox(self):
        close_button = self.wait.until(EC.element_to_be_clickable(self.close_button_forELEMNT_XPATH))
        close_button.click()



