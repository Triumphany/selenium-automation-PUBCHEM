import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import os

@pytest.fixture()
def setup(request):  
    # Update the driver path if needed
    driver_path = r"C:\drivers\chromedriver-win64\chromedriver.exe"
    servj_obj = Service(driver_path)
    driver = webdriver.Chrome(service=servj_obj)
    wait = WebDriverWait(driver, 15)
    
    driver.get("https://pubchem.ncbi.nlm.nih.gov/")
    driver.maximize_window()
    
    # Attach driver and wait objects to the test class
    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.quit()