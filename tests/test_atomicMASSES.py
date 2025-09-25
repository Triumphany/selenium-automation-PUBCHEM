import pytest
from pages.atomic_mass_charts import PubChem_Periodic_Table_Properties
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "AtomicMasses_chart")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_element_atomic_masses_selection:     
    def test_BY_value_attribute(self):
        page = PubChem_Periodic_Table_Properties(self.driver)
        page.click_periodicTABLE_button()
        page.click_link_and_switchWINDOW()
        values = ['all', 'period_1', 'period_2', 'period_3', 'period_4', 'period_5', 'period_6', 'period_7', 'group_1', 'group_2', 'group_3', 'group_4', 'group_5', 'group_6', 'group_7', 'group_8', 'group_9', 'group_10', 'group_11', 'group_12', 'group_13', 'group_14', 'group_15', 'group_16', 'group_17', 'group_18']
        for value in values:
            page.option_selection_byVALUE(value)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{value}.png"))

    def test_BY_visible_TEXT(self):
        page = PubChem_Periodic_Table_Properties(self.driver)
        page.click_periodicTABLE_button()
        page.click_link_and_switchWINDOW()
        texts = ['All Elements', 
                 'Period 1 (Atomic Numbers: 1, 2)', 
                 'Period 2 (Atomic Numbers: 3, 4, 5, 6, 7, 8, 9, 10)', 
                 'Period 3 (Atomic Numbers: 11, 12, 13, 14, 15, 16, 17, 18)', 
                 'Period 4 (Atomic Numbers: 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)', 
                 'Period 5 (Atomic Numbers: 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54)', 
                 'Period 6 (Atomic Numbers: 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86)', 
                 'Period 7 (Atomic Numbers: 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118)', 
                 'Group 1 (Atomic Numbers: 1, 3, 11, 19, 37, 55, 87)', 
                 'Group 2 (Atomic Numbers: 4, 12, 20, 38, 56, 88)', 
                 'Group 3 (Atomic Numbers: 21, 39, 71, 103)', 
                 'Group 4 (Atomic Numbers: 22, 40, 72, 104)', 
                 'Group 5 (Atomic Numbers: 23, 41, 73, 105)', 
                 'Group 6 (Atomic Numbers: 24, 42, 74, 106)', 
                 'Group 7 (Atomic Numbers: 25, 43, 75, 107)', 
                 'Group 8 (Atomic Numbers: 26, 44, 76, 108)', 
                 'Group 9 (Atomic Numbers: 27, 45, 77, 109)', 
                 'Group 10 (Atomic Numbers: 28, 46, 78, 110)', 
                 'Group 11 (Atomic Numbers: 29, 47, 79, 111)', 
                 'Group 12 (Atomic Numbers: 30, 48, 80, 112)', 
                 'Group 13 (Atomic Numbers: 5, 13, 31, 49, 81, 113)', 
                 'Group 14 (Atomic Numbers: 6, 14, 32, 50, 82, 114)', 
                 'Group 15 (Atomic Numbers: 7, 15, 33, 51, 83, 115)', 
                 'Group 16 (Atomic Numbers: 8, 16, 34, 52, 84, 116)', 
                 'Group 17 (Atomic Numbers: 9, 17, 35, 53, 85, 117)', 
                 'Group 18 (Atomic Numbers: 2, 10, 18, 36, 54, 86, 118)']
        for txt in texts:
            page.option_selection_byTEXT(txt)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{txt}.png"))

    def test_BY_index(self):
        page = PubChem_Periodic_Table_Properties(self.driver)
        page.click_periodicTABLE_button()
        page.click_link_and_switchWINDOW()
        for index_no in range(0,25):
            page.option_selection_byINDEX(index_no)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{index_no}.png"))
    
