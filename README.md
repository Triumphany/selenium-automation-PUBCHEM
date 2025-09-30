# selenium-automation-PUBCHEM

This project automates interactions with PubChem using Selenium. It includes parameterized POM (Page Object Model) definitions, data handling scripts, test cases, and utilities for logging and reporting.


## 🔎 Overview  
This project provides an automated framework for navigating and interacting with **PubChem** using Selenium.  
It follows the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and readability.  

The framework supports:  
* Automated browsing of PubChem data and element properties  
* Generating chemical property charts (atomic mass, radius, electronegativity, ionization energy, electron affinity)  
* Uploading workflows for ID lists and text files  
* Capturing reports, logs, and screenshots for every run  

The goal is to streamline repetitive research tasks, improve testing reliability, and enable faster data exploration within PubChem.  

---

## ✨ Features  

* Automated navigation and interaction with **PubChem**.  
* POM (Page Object Model) design for maintainability.  

## 📊 Charts and Property Pages Automated  
* Atomic mass charts  
* Atomic radius charts  
* Electronegativity charts  
* Electron affinity plots  
* Ionization energy plots  

## 🧪 Element Data Exploration  
* Periodic table elements  
* Element properties  
* Browse PubChem data  

## 📂 Upload Workflows  
* Upload ID list  
* Upload text files  

## 📝 Reporting  
* HTML reports  
* Logs  
* Screenshots  
---

## Prerequisites

- Python 3.x installed (≥ 3.8 recommended)  
- Chrome browser installed  
- Compatible ChromeDriver (matching Chrome version)  

---



## Folder Structure


```bash
 selenium-automation-PUBCHEM/
  │── data_files/       # user-uploaded input files
  │── excel_files/
  ├── pages/            # POM definitions for PubChem automation
  │   ├── atomic_mass_charts.py
  │   ├── atomic_radius_chart.py
  │   ├── browse_data.py
  │   ├── button_test_draw_structure.py
  │   ├── electronegativity_charts.py
  │   ├── elements_properties.py
  │   ├── home_page.py
  │   ├── periodic_table_elements.py
  │   ├── plot_boiling_point.py
  │   ├── plot_density.py
  │   ├── plot_electron_affinity.py
  │   ├── plot_ionization.py
  │   ├── plot_melting_point.py
  │   ├── search_pubchem.py
  │   ├── upload_id_list.py
  │   ├── upload_text_file.py
  │── reports/
  │   ├── html/
  │   ├── log/
  │── screenshots/
  │── tests/            # test cases (not expanded here)
  │── utils/
  │   ├── logger.py
  │── conftest.py
  │── requirements.txt
  │── README.md

```
## Installation

Clone the repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/Triumphany/selenium-automation-PUBCHEM.git

# Move into the project directory
cd selenium-automation-PUBCHEM

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

Execute the test suite with:

```bash
  pytest -v
  pytest -v tests/test_name.py --html=reports/html/name.html
```
* -v runs pytest in verbose mode
* HTML reports are stored in reports/html

