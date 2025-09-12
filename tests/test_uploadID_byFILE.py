import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.upload_list_textfile import pubchem_home
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "uploadID_file")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_uploadID_byFILE:
    def test_cid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_cid("H:/selenium/pubchem/framework/data_files/cid_list.txt")
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "cid_file.png"))
        
    def test_sid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_sid("H:/selenium/pubchem/framework/data_files/sid_list.txt")
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "sid_file.png"))

    def test_aid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_aid("H:/selenium/pubchem/framework/data_files/aid_list.txt")
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "aid_file.png"))

    def test_geneid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_geneid("H:/selenium/pubchem/framework/data_files/geneid_list.txt")
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "geneid_file.png"))

    def test_protein(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_protein("H:/selenium/pubchem/framework/data_files/protein_list.txt")
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "protein_file.png"))

    def test_pathway(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_pathway("H:/selenium/pubchem/framework/data_files/pathway_list.txt")
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "pathway_file.png"))

    def test_pubmed(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_pubmed("H:/selenium/pubchem/framework/data_files/pubmed_list.txt")
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "pubmed_file.png"))

    def test_patent(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        page.search_patent("H:/selenium/pubchem/framework/data_files/patent_list.txt")
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "patent_file.png"))


    
