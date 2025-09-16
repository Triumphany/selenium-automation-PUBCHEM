import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.upload_list_textfile import pubchem_home
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "uploadID_file")
os.makedirs(screenshots_loc, exist_ok=True)

file_loc = os.path.join(os.path.dirname(__file__), "..", "data_files")

@pytest.mark.usefixtures("setup")
class Test_uploadID_byFILE:
    def test_cid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        cid_file = os.path.abspath(os.path.join(file_loc, "cid_list.txt"))
        page.search_cid(cid_file)
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "cid_file.png"))
        
    def test_sid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        sid_file = os.path.abspath(os.path.join(file_loc, "sid_list.txt"))
        page.search_sid(sid_file)
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "sid_file.png"))

    def test_aid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        aid_file = os.path.abspath(os.path.join(file_loc, "aid_list.txt"))
        page.search_aid(aid_file)
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "aid_file.png"))

    def test_geneid(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        geneid_file = os.path.abspath(os.path.join(file_loc, "geneid_list.txt"))
        page.search_geneid(geneid_file)
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "geneid_file.png"))

    def test_protein(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        protein_file = os.path.abspath(os.path.join(file_loc, "protein_list.txt"))
        page.search_protein(protein_file)
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "protein_file.png"))

    def test_pathway(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        pathway_file = os.path.abspath(os.path.join(file_loc, "pathway_list.txt"))
        page.search_pathway(pathway_file)
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "pathway_file.png"))

    def test_pubmed(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        pubmed_file = os.path.abspath(os.path.join(file_loc, "pubmed_list.txt"))
        page.search_pubmed(pubmed_file)
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "pubmed_file.png"))

    def test_patent(self):
        page = pubchem_home(self.driver)
        page.click_upload_and_type()
        patent_file = os.path.abspath(os.path.join(file_loc, "patent_list.txt"))
        page.search_patent(patent_file)
        page.check_success_ORerror_message()
        page.submit_success_file()
        
        self.driver.save_screenshot(os.path.join(screenshots_loc, "patent_file.png"))


    
