import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.uploadIDlist_input import pubchem_home
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "uploadID_input")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_uploadID_input:
    def test_cid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_cid("2244")
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "cid.png"))
        
    def test_sid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_sid("319306286")
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "sid.png"))

    def test_aid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_aid("450")
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "aid.png"))

    def test_geneid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_geneid("1956")
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "geneid.png"))

    def test_protein(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_protein("P40825")
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "protein.png"))

    def test_pathway(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_pathway("PWY-5340")
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "pathway.png"))

    def test_pubmed(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_aid("1234")
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "pubmed.png"))

    def test_patent(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_aid("CA-2272433-A1")
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "patent.png"))


    
