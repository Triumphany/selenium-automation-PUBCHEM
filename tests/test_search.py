import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.search_pubchem import pubchem_home
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "search")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_search_input:
    def test_aspirin(self):
        page = pubchem_home(self.driver)
        
        page.search_input("aspirin")
        page.search_click()
        page.check_assertion_search_smile()
        page.logger.info("Test test_aspirin passed")
        self.driver.save_screenshot(os.path.join(screenshots_loc, "aspirin.png"))
        

    def test_aspirin_id(self):
        page = pubchem_home(self.driver)
        
        page.search_input("2244")
        page.search_click()
        page.check_assertion_search_cid()
        page.logger.info("Test test_aspirin_id passed")
        self.driver.save_screenshot(os.path.join(screenshots_loc, "aspirin_id.png"))

    def test_aspirin_smile(self):
        page = pubchem_home(self.driver)
        
        page.search_input("CC(=O)OC1=CC=CC=C1C(=O)O")
        page.search_click()
        page.check_assertion_search_smile()
        page.logger.info("Test test_aspirin_smile passed")
        self.driver.save_screenshot(os.path.join(screenshots_loc, "smile.png"))

    def test_aspirin_inchl(self):
        page = pubchem_home(self.driver)
        
        page.search_input("InChI=1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)")
        page.search_click()
        page.check_assertion_search_smile()
        page.logger.info("Test test_aspirin_inchl passed")
        self.driver.save_screenshot(os.path.join(screenshots_loc, "inchl.png"))

    
