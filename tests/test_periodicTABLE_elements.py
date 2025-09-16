import pytest
from pages.periodicTABLE_elements import pubchem_home
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "PeriodicTable_elements")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_periodicTABLE_buttons: 
    def test_click_elements_ofPERIODICtable(self):
        elements = [
  "H","He",
  "Li","Be","B","C","N","O","F","Ne",
  "Na","Mg","Al","Si","P","S","Cl","Ar",
  "K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
  "Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe",
  "Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu",
  "Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn",
  "Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr",
  "Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"
]
        page = pubchem_home(self.driver)
        page.click_periodic_table_button()
        for element in elements:
            page.click_elements(element)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{element}.png"))
            page.click_close_element_DIALOGUEbox()
         

    



