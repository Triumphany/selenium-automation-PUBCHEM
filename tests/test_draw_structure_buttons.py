import pytest
from pages.button_test_INdrawSTRUCTURE import pubchem_home
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "DRAW_STRUCTURE")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_DRAWstructure_buttons:     
    def test_click_DRAW_STRUCTURE(self):
        page = pubchem_home(self.driver)
        page.click_draw_structure()
        page.check_draw_structure_title()

        self.driver.save_screenshot(os.path.join(screenshots_loc, "check_draw_click.png"))

    def test_check_click_element(self):
        page = pubchem_home(self.driver)
        page.click_draw_structure()
        page.check_draw_structure_title()
        page.iframe_switch()
        ELEMENTS = ["H", "He", "Li", "Be", "Na", "Mg", "K", "Ca", "Rb", "Sr", "Cs", "Ba","B", "C", "N", "O", "F", "Ne",
    "Al", "Si", "P", "S", "Cl", "Ar",
    "Ga", "Ge", "As", "Se", "Br", "Kr",
    "In", "Sn", "Sb", "Te", "I", "Xe",
    "Tl", "Pb", "Bi", "Po", "At", "Rn"
]
        for element in ELEMENTS:
            page.check_click_element(element)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"element_{element}.png"))

    def test_check_click_buttons(self):
        page = pubchem_home(self.driver)
        page.click_draw_structure()
        page.check_draw_structure_title()
        page.iframe_switch()
        BUTTONS = [
    "new", "undo", "clean", "simplify", "del", "qry", "move", "rotate",
    "mirrorx", "mirrory", "single", "double", "triple", "up", "down",
    "any", "either", "wiggly", "sa", "da", "sd", "r3", "r4", "r5", "r6",
    "r7", "r8", "phenyl", "template", "plus", "minus", "radical", "ethyl",
    "propyl", "ipropyl", "butyl", "ibutyl", "sbutyl", "tbutyl", "cho",
    "co2h", "no2", "so3h", "misc", "d1", "d2", "d3", "export", "done",
    "hydrogen", "import"
]
        for button in BUTTONS:
            page.check_click_buttons(button)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"element_{button}.png"))
