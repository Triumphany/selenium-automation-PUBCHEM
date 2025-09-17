import pytest
from pages.element_properties import PubChem_Periodic_Table_Properties
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "element_properties")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_element_properties_selection:     
    def test_BY_value_attribute(self):
        page = PubChem_Periodic_Table_Properties(self.driver)
        page.click_periodicTABLE_button()
        values = ['GroupBlock', 'AtomicMass', 'StandardState', 'ElectronConfiguration', 'OxidationStates', 'Electronegativity', 'AtomicRadius', 'IonizationEnergy', 'ElectronAffinity', 'MeltingPoint', 'BoilingPoint', 'Density', 'YearDiscovered', 'None']
        for value in values:
            page.option_select_properties_byVALUEatrributes(value)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{value}.png"))

    def test_BY_visible_TEXT(self):
        page = PubChem_Periodic_Table_Properties(self.driver)
        page.click_periodicTABLE_button()
        texts = ['Chemical Group Block', 'Atomic Mass, u', 'Standard State', 'Electron Configuration', 'Oxidation States', 'Electronegativity (Pauling Scale)', 'Atomic Radius (van der Waals), pm', 'Ionization Energy, eV', 'Electron Affinity, eV', 'Melting Point, K', 'Boiling Point, K', 'Density, g/cm³', 'Year Discovered', 'None']
        for txt in texts:
            page.option_select_properties_byVISIBLE_TEXT(txt)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{txt}.png"))

    def test_BY_index(self):
        page = PubChem_Periodic_Table_Properties(self.driver)
        page.click_periodicTABLE_button()
        for index_no in range(0,14):
            page.option_select_properties_by_index(index_no)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{index_no}.png"))

    
