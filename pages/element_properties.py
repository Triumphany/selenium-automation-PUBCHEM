from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.logger import get_logger

class PubChem_Periodic_Table_Properties:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.logger = get_logger(self.__class__.__name__)

    #locators
    periodic_table_button_XPATH = (By.XPATH, "//span[contains(@class, 'btn-text p-sm-top f-1') and text()='Periodic Table']")
    properties_options_ID = (By.ID, "select-property")

    #actions
    def click_periodicTABLE_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.periodic_table_button_XPATH))
        button.click()
        self.logger.info("Periodic Table button clicked from HOMEPAGE. ")

    def option_select_properties_byVALUEatrributes(self,name):
        options_properties = self.wait.until(EC.element_to_be_clickable(self.properties_options_ID))
        options_selection = Select(options_properties)
        options_selection.select_by_value(f"{name}")
        self.logger.info(f"{name} : is selected. ")

    def option_select_properties_byVISIBLE_TEXT(self,name):
        options_properties = self.wait.until(EC.element_to_be_clickable(self.properties_options_ID))
        options_selection = Select(options_properties)
        options_selection.select_by_visible_text(f"{name}")
        self.logger.info(f"{name} : is selected. ")

    def option_select_properties_by_index(self,Index_no):
        options_properties = self.wait.until(EC.element_to_be_clickable(self.properties_options_ID))
        options_selection = Select(options_properties)
        options_selection.select_by_index(Index_no)
        self.logger.info(f"Index {Index_no} : is selected. ")
        