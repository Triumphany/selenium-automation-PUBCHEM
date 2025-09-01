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

    upload_id_list_XPATH = (By.XPATH, "//*[@id='main-content']/div[1]/div/div[2]/div/div[5]/div/div[2]/button")
    choose_identifier_type_button_XPATH = (By.XPATH, "//div[contains(@class,'p-sm-left p-sm-right ellipsis') and text()='Compound, e.g. CID like 2244']")

    cid_button_XAPTH = (By.XPATH, "//span[contains(text(), 'Compound, e.g. CID like 2244')]")
    sid_button_XPATH = (By.XPATH, "//span[contains(text(), 'Substance, e.g. SID like 319306286')]")
    aid_button_XPATH = (By.XPATH, "//span[contains(text(), 'BioAssay, e.g. AID like 450')]")
    geneid_button_XPATH = (By.XPATH, "//span[contains(text(), 'Gene, e.g. GENEID like 1956')]")
    protein_accession_button_XPATH = (By.XPATH, "//span[contains(text(), 'Protein, e.g. protein accession like P40825')]")
    pathway_button_XPATH = (By.XPATH, "//span[contains(text(), 'Pathway, e.g. pathway accession like PWY-5340')]")
    pubmed_button_XPATH = (By.XPATH, "//span[contains(text(), 'PubMed, e.g. PMID like 1234')]")
    patent_button_XPATH = (By.XPATH, "//span[contains(text(), 'Patent, e.g. patent publication number like CA-2272433-A1")
   


    enter_identifiers_XPATH = (By.XPATH, "//input[@id='identifier-list']")
    search_identifires_button_XPATH = (By.XPATH, "//button[@type='submit' and @value='Submit']")

    #action

    def click_upload_and_type(self):
        upload_button = self.wait.until(EC.element_to_be_clickable(self.upload_id_list_XPATH))
        upload_button.click()

        select_type_button = self.wait.until(EC.element_to_be_clickable(self.choose_identifier_type_button_XPATH))
        select_type_button.click()

    def search_cid(self,name):
        cid_button = self.wait.until(EC.element_to_be_clickable(self.cid_button_XAPTH))
        cid_button.click()

        enter_identifier_button = self.wait.until(EC.element_to_be_clickable(self.enter_identifiers_XPATH))
        enter_identifier_button.clear()
        enter_identifier_button.send_keys(name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.search_identifires_button_XPATH))
        search_button.click()

    def search_sid(self,name):
        sid_button = self.wait.until(EC.element_to_be_clickable(self.sid_button_XPATH))
        sid_button.click()

        enter_identifier_button = self.wait.until(EC.element_to_be_clickable(self.enter_identifiers_XPATH))
        enter_identifier_button.clear()
        enter_identifier_button.send_keys(name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.search_identifires_button_XPATH))
        search_button.click()

    def search_aid(self,name):
        aid_button = self.wait.until(EC.element_to_be_clickable(self.aid_button_XPATH))
        aid_button.click()

        enter_identifier_button = self.wait.until(EC.element_to_be_clickable(self.enter_identifiers_XPATH))
        enter_identifier_button.clear()
        enter_identifier_button.send_keys(name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.search_identifires_button_XPATH))
        search_button.click()

    def search_geneid(self,name):
        geneid_button = self.wait.until(EC.element_to_be_clickable(self.geneid_button_XPATH))
        geneid_button.click()

        enter_identifier_button = self.wait.until(EC.element_to_be_clickable(self.enter_identifiers_XPATH))
        enter_identifier_button.clear()
        enter_identifier_button.send_keys(name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.search_identifires_button_XPATH))
        search_button.click()

    def search_protein(self,name):
        protein_button = self.wait.until(EC.element_to_be_clickable(self.protein_accession_button_XPATH))
        protein_button.click()

        enter_identifier_button = self.wait.until(EC.element_to_be_clickable(self.enter_identifiers_XPATH))
        enter_identifier_button.clear()
        enter_identifier_button.send_keys(name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.search_identifires_button_XPATH))
        search_button.click()

    def search_pathway(self,name):
        pathway_button = self.wait.until(EC.element_to_be_clickable(self.pathway_button_XPATH))
        pathway_button.click()

        enter_identifier_button = self.wait.until(EC.element_to_be_clickable(self.enter_identifiers_XPATH))
        enter_identifier_button.clear()
        enter_identifier_button.send_keys(name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.search_identifires_button_XPATH))
        search_button.click()

    def search_pubmed(self,name):
        pubmed_button = self.wait.until(EC.element_to_be_clickable(self.pubmed_button_XPATH))
        pubmed_button.click()

        enter_identifier_button = self.wait.until(EC.element_to_be_clickable(self.enter_identifiers_XPATH))
        enter_identifier_button.clear()
        enter_identifier_button.send_keys(name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.search_identifires_button_XPATH))
        search_button.click()

    def search_patent(self,name):
        patent_button = self.wait.until(EC.element_to_be_clickable(self.patent_button_XPATH))
        patent_button.click()

        enter_identifier_button = self.wait.until(EC.element_to_be_clickable(self.enter_identifiers_XPATH))
        enter_identifier_button.clear()
        enter_identifier_button.send_keys(name)

        search_button = self.wait.until(EC.element_to_be_clickable(self.search_identifires_button_XPATH))
        search_button.click()