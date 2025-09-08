import pytest
from pages.homePAGE import pubchem_home
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "Homepage_buttons")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_search_input: 
    def test_click_NIH(self):
        page = pubchem_home(self.driver)
        page.click_NIHhead
        self.driver.save_screenshot(os.path.join(screenshots_loc, f"NIHhead.png"))
        self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")  

    def test_click_PubChemLOGO(self):
        page = pubchem_home(self.driver)
        page.click_PubChemLOGO
        self.driver.save_screenshot(os.path.join(screenshots_loc, f"PubChemLOGO.png"))
        self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")

    def test_click_header_button(self):
        page = pubchem_home(self.driver)
        buttons = ['About', 'Docs', 'Submit', 'Contact']

        for button in buttons:
            page = pubchem_home(self.driver)
            page.click_header_buttons(button)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{button}.png"))
            self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")

    def test_search_suggestions(self):
        page = pubchem_home(self.driver)
        buttons = ['aspirin', 'EGFR', 'C9H8O4', '57-27-2', 'C1=CC=C(C=C1)C=O', 'InChI=1S/C3H6O/c1-3(2)4/h1-2H3']

        for button in buttons:
            page = pubchem_home(self.driver)
            page.click_search_suggestions(button)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{button}.png"))
            self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")

    def test_buttons_withBUTTONS(self):
        page = pubchem_home(self.driver)
        buttons = ['Draw Structure', 'Upload ID List'] 

        for button in buttons:
            page = pubchem_home(self.driver)
            page.click_buttons_withBUTTONS(button)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{button}.png"))
            self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")

    def test_buttons_withLINKS(self):
        page = pubchem_home(self.driver)
        buttons = ['Browse Data', 'Periodic Table']

        for button in buttons:
            page = pubchem_home(self.driver)
            page.click_buttons_withLINK(button)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{button}.png"))
            self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")

    def test_text_links(self):
        page = pubchem_home(self.driver)
        buttons = ['https://pubchemdocs.ncbi.nlm.nih.gov/statistics', '/source/', 'https://pubchemdocs.ncbi.nlm.nih.gov/about']

        for button in buttons:
            page = pubchem_home(self.driver)
            page.click_text_links(button)
            self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")

    def test_footerCOLUMN_links(self):
        page = pubchem_home(self.driver)
        buttons = ['Web Policies', 'FOIA', 'HHS Vulnerability Disclosure', 'Help', 'Accessibility', 'Careers']

        for button in buttons:
            page = pubchem_home(self.driver)
            page.click_footerCOLOUMN_links(button)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{button}.png"))
            self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")

    def test_footerROW_links(self):
        page = pubchem_home(self.driver)
        buttons = ['NLM', 'NIH', 'HHS', 'USA.gov']

        for button in buttons:
            page = pubchem_home(self.driver)
            page.click_footerROW_links(button)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{button}.png"))
            self.driver.get("https://pubchem.ncbi.nlm.nih.gov/")



