from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.logger import get_logger

class PubChem_Periodic_Table_Ionization_Energy:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.logger = get_logger(self.__class__.__name__)

    #locators
    periodic_table_button_XPATH = (By.XPATH, "//span[contains(@class, 'btn-text p-sm-top f-1') and text()='Periodic Table']")
    ionization_link_XPATH = (By.XPATH, "//a[@href='/periodic-table/ionization-energy/']")
    selection_group_period_ID = (By.ID, "select-group-or-period")

    #actions
    def click_periodicTABLE_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.periodic_table_button_XPATH))
        button.click()
        self.logger.info("Periodic Table button clicked from HOMEPAGE. ")

    def click_link_and_switchWINDOW(self):
        atomic_masses_link = self.wait.until(EC.element_to_be_clickable(self.ionization_link_XPATH))
        link_url = atomic_masses_link.get_attribute("href")
        self.driver.switch_to.new_window('tab')
        self.driver.get(link_url)
        self.logger.info("Ionization Energy window : is opened. ")

    def option_selection_byVALUE(self,name):
        options_properties = self.wait.until(EC.element_to_be_clickable(self.selection_group_period_ID))
        options_selection = Select(options_properties)
        options_selection.select_by_value(f"{name}")
        self.logger.info(f"{name} : is selected. ")
        
    def option_selection_byTEXT(self,name):
        options_properties = self.wait.until(EC.element_to_be_clickable(self.selection_group_period_ID))
        options_selection = Select(options_properties)
        options_selection.select_by_visible_text(f"{name}")
        self.logger.info(f"{name} : is selected. ")

    def option_selection_byINDEX(self,name):
        options_properties = self.wait.until(EC.element_to_be_clickable(self.selection_group_period_ID))
        options_selection = Select(options_properties)
        options_selection.select_by_index(f"{name}")
        self.logger.info(f"{name} : is selected. ")