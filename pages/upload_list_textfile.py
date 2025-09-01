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
   


    upload_identi_files_area_XPATH = (By.XPATH, "//input[@id='id-list-upload']")
    success_upload_message_XPATH = (By.XPATH, "//h4[contains(@class, 'f-medium p-sm-bottom') and text()='SUCCESS']")
    invalid_file_message_XPATH = (By.XPATH, "//h4[contains(@class, 'f-medium p-sm-bottom') and text()='ERROR']")
    submit_uploadfile_button_XPATH = (By.XPATH, "//a[contains(@class, 'button bckg-primary with-padding') and text()='Search PubChem With This List']")

    #action
    #common for all to click the upload button from homepage
    def click_upload_and_type(self):
        upload_button = self.wait.until(EC.element_to_be_clickable(self.upload_id_list_XPATH))
        upload_button.click()

        select_type_button = self.wait.until(EC.element_to_be_clickable(self.choose_identifier_type_button_XPATH))
        select_type_button.click()

    #common success message after upload the file and before submission
    def check_success_ORerror_message(self):
        try:
            success_message = self.wait.until(EC.visibility_of_element_located(self.success_upload_message_XPATH)).text.strip()
            assert "SUCCESS" in success_message
            print("Valid format")

        except:
            error_message = self.wait.until(EC.visibility_of_element_located(self.invalid_file_message_XPATH)).text.strip()
            assert "ERROR" in error_message
            print("invalid format")

    #common submit after successfull upload
    def submit_success_file(self):
        submit_uploadfile_button = self.wait.until(EC.element_to_be_clickable(self.submit_uploadfile_button_XPATH))
        submit_uploadfile_button.click()


    def search_cid(self,name):
        cid_button = self.wait.until(EC.element_to_be_clickable(self.cid_button_XAPTH))
        cid_button.click()

        upload_identiFILES_area = self.wait.until(EC.element_to_be_clickable(self.upload_identi_files_area_XPATH))
        upload_identiFILES_area.clear()
        upload_identiFILES_area.send_keys(name)

    def search_sid(self,name):
        sid_button = self.wait.until(EC.element_to_be_clickable(self.sid_button_XPATH))
        sid_button.click()

        upload_identiFILES_area = self.wait.until(EC.element_to_be_clickable(self.upload_identi_files_area_XPATH))
        upload_identiFILES_area.clear()
        upload_identiFILES_area.send_keys(name)

    def search_aid(self,name):
        aid_button = self.wait.until(EC.element_to_be_clickable(self.aid_button_XPATH))
        aid_button.click()

        upload_identiFILES_area = self.wait.until(EC.element_to_be_clickable(self.upload_identi_files_area_XPATH))
        upload_identiFILES_area.clear()
        upload_identiFILES_area.send_keys(name)

    def search_geneid(self,name):
        geneid_button = self.wait.until(EC.element_to_be_clickable(self.geneid_button_XPATH))
        geneid_button.click()

        upload_identiFILES_area = self.wait.until(EC.element_to_be_clickable(self.upload_identi_files_area_XPATH))
        upload_identiFILES_area.clear()
        upload_identiFILES_area.send_keys(name)

    def search_protein(self,name):
        protein_button = self.wait.until(EC.element_to_be_clickable(self.protein_accession_button_XPATH))
        protein_button.click()

        upload_identiFILES_area = self.wait.until(EC.element_to_be_clickable(self.upload_identi_files_area_XPATH))
        upload_identiFILES_area.clear()
        upload_identiFILES_area.send_keys(name)

    def search_pathway(self,name):
        pathway_button = self.wait.until(EC.element_to_be_clickable(self.pathway_button_XPATH))
        pathway_button.click()

        upload_identiFILES_area = self.wait.until(EC.element_to_be_clickable(self.upload_identi_files_area_XPATH))
        upload_identiFILES_area.clear()
        upload_identiFILES_area.send_keys(name)

    def search_pubmed(self,name):
        pubmed_button = self.wait.until(EC.element_to_be_clickable(self.pubmed_button_XPATH))
        pubmed_button.click()

        upload_identiFILES_area = self.wait.until(EC.element_to_be_clickable(self.upload_identi_files_area_XPATH))
        upload_identiFILES_area.clear()
        upload_identiFILES_area.send_keys(name)

    def search_patent(self,name):
        patent_button = self.wait.until(EC.element_to_be_clickable(self.patent_button_XPATH))
        patent_button.click()

        upload_identiFILES_area = self.wait.until(EC.element_to_be_clickable(self.upload_identi_files_area_XPATH))
        upload_identiFILES_area.clear()
        upload_identiFILES_area.send_keys(name)
