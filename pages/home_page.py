from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class pubchem_home():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    #Common locators
    NIH_XPATH = (By.XPATH, "//div[contains(@class, 'main-width f-white')]/a")
    PubChem_LOGO_XPATH = (By.XPATH, "//h1[contains(@class, 'f-1')]/a")
    head_buttons_XPATH = (By.XPATH, "//a[contains(@class, 'button with-padding')]/span[text()]")
    search_suggestions_XPATH = (By.XPATH, "//a[contains(@class, 'p-xsm')]")
    buttons_withLINKS_XPATH = (By.XPATH, "//a[span[text()]]")
    buttons_withBUTTONS_XPATH = (By.XPATH, "//button[span[text()]]")
    text_links_XPATH = (By.XPATH, "//a[@href]")
    footerCOLUMN_links_XPATH = (By.XPATH, "//div[contains(@class, 'p-md-bottom')]/a[text()]")
    footerROW_links_XPATH = (By.XPATH, "//ul[contains(@id, 'org-links')]/li/a[text()]")

    

    #action
    def click_NIHhead(self):
        NIH_buttons = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'main-width f-white')]/a")))
        NIH_buttons.click()

    def click_PubChemLOGO(self):
        pubchem_buttons = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(@class, 'f-1')]/a")))
        pubchem_buttons.click()

    def click_header_buttons(self,name):
        header_buttons = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[contains(@class, 'button with-padding')]/span[text()='{name}']")))
        header_buttons.click()
        
    def click_search_suggestions(self,name):
        search_suggestions = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[contains(@class, 'p-xsm') and text()='{name}']")))
        search_suggestions.click()

    def click_buttons_withBUTTONS(self,name):
        buttons = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//button[span[text()='{name}']]")))
        buttons.click()

    def click_buttons_withLINK(self,name):
        buttons = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[span[text()='{name}']]")))
        buttons.click()

    def click_text_links(self,name):
        text_links_buttons = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{name}']")))
        text_links_buttons.click()

    def click_footerCOLOUMN_links(self,name):
        click_footerCOLOUMN_links = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class, 'p-md-bottom')]/a[text()='{name}']")))
        click_footerCOLOUMN_links.click()

    def click_footerROW_links(self,name):
        click_footerROW_links = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul[contains(@id, 'org-links')]/li/a[text()='{name}']")))
        click_footerROW_links.click()



