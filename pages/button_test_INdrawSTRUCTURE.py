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
    draw_structure_button_XPATH = (By.XPATH, "//button[contains(@class, 'button has-icon-top')]")
    DRAW_STRUCTURE_tile_XPATH = (By.XPATH, "//div[contains(@id, 'input-options-icon-title') and text()='Draw Structure']")
    elements_button_XPATH = (By.XPATH, "//td[@id='']")
    iframe_XPATH = (By.XPATH, "//iframe[contains(@src, '/edit3/index.html')]")

    #action
    def click_draw_structure(self):
        draw_structure_button = self.wait.until(EC.element_to_be_clickable(self.draw_structure_button_XPATH))
        draw_structure_button.click()

    def check_draw_structure_title(self):
        draw_structure_title_locate = self.wait.until(EC.visibility_of_element_located(self.DRAW_STRUCTURE_tile_XPATH))
        DRAW_STRUCTURE_title = draw_structure_title_locate.text
        assert "DRAW STRUCTURE" in DRAW_STRUCTURE_title

    def iframe_switch(self):
        iframe = self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.iframe_XPATH))

    def check_click_element(self,element_symbol):
        click_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//td[@id='{element_symbol}']")))
        click_element.click()

    def check_click_buttons(self,name):
        click_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//td[@id='{name}']")))
        click_element.click()
        

    
