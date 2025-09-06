import pytest
from pages.browseDATA import pubchem_home
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

screenshots_loc = os.path.join(os.path.dirname(__file__), "..", "screenshots", "options")
os.makedirs(screenshots_loc, exist_ok=True)

@pytest.mark.usefixtures("setup")
class Test_search_input:     
    def test_click_DRAW_STRUCTURE(self):
        page = pubchem_home(self.driver)
        page.clickBROWSER_button()
        values = [
    "78", "124", "86", "130", "104", "114", "113", "2", "87", "84", "95", "110", "98", "111", "102", "99",
    "132", "105", "81", "123", "78", "89", "90", "91", "83", "133", "121", "131", "107", "92", "16", "28",
    "20", "117", "6", "25", "3", "18", "118", "96", "23", "7", "100", "4", "59", "8", "5", "24", "22", "14",
    "17", "15", "54", "115", "1", "134", "116", "93", "112", "109", "101", "122", "106", "135", "120", "80",
    "125", "72", "126", "127", "128", "129", "88", "108", "79", "58", "119"
]
        
        #if want to use by select_by_visible_text
        classifications = [
    "Baker Lab, Chemistry Department, The University of North Carolina at Chapel Hill: CCS Classification - Baker Lab",
    "CAMEO Chemicals: CAMEO Chemical Reactivity Classification",
    "Catalogue of Life (COL): Catalogue of Life (COL)",
    "CCSbase: CCSbase Classification",
    "Cell Line Ontology (CLO): Cell Line Ontology",
    "Cell Ontology (CL): Cell Ontology (CL)",
    "ChEBI: ChEBI Ontology",
    "ChEMBL: ChEMBL Protein Target Tree",
    "ChemIDplus: ChemIDplus Chemical Information Classification",
    "Collaborative Drug Discovery, Inc.: CDD Classification Tree",
    "Consumer Product Information Database (CPID): Consumer Products Category Classification",
    "Consumer Product Information Database (CPID): Household Products Classification",
    "Cooperative Patent Classification (CPC): Cooperative Patent Classification (CPC)",
    "Drug Enforcement Administration (DEA): DEA Drug and Chemical Classification",
    "EPA Chemical and Products Database (CPDat): EPA CPDat Classification",
    "EPA Chemicals under the TSCA: EPA TSCA Classification",
    "EPA DSSTox: CompTox Chemicals Dashboard Chemical Lists",
    "EPA Safer Choice: EPA Safer Chemical Ingredients Classification",
    "EPA Substance Registry Services: EPA SRS List Classification",
    "FDA Pharm Classes: FDA Pharmacological Classification",
    "Gene Ontology (GO): Biological Process",
    "Gene Ontology (GO): Cellular Component",
    "Gene Ontology (GO): Molecular Function",
    "GHS Classification (UNECE): GHS Classification",
    "Glycan Naming and Subsumption Ontology (GNOme): GNOme",
    "Haz-Map, Information on Hazardous Chemicals and Occupational Diseases: Haz-Map Classification",
    "Integrated Taxonomic Information System (ITIS): Integrated Taxonomic Information System (ITIS)",
    "International Agency for Research on Cancer (IARC): IARC Classification",
    "IUPHAR/BPS Guide to PHARMACOLOGY: Guide to Pharmacology Target Classification",
    "KEGG: Anatomical Therapeutic Chemical (ATC) classification",
    "KEGG: Animal drugs in Japan",
    "KEGG: Antiinfectives",
    "KEGG: Antimicrobials Abbreviations",
    "KEGG: Bioactive peptides",
    "KEGG: Classification of Japanese OTC drugs",
    "KEGG: Compounds with biological roles",
    "KEGG: Crude drugs",
    "KEGG: Drug Classes",
    "KEGG: Drug Groups",
    "KEGG: Drugs listed in the Japanese Pharmacopoeia",
    "KEGG: Endocrine disrupting compounds",
    "KEGG: Glycosides",
    "KEGG: Lipids",
    "KEGG: Natural toxins",
    "KEGG: Pesticides",
    "KEGG: Phytochemical compounds",
    "KEGG: Risk category of Japanese OTC drugs",
    "KEGG: Target-based classification of drugs",
    "KEGG: Therapeutic category of drugs in Japan",
    "KEGG: Traditional Chinese Medicine in Japan",
    "KEGG: USP drug classification",
    "LIPID MAPS: Lipid Classification",
    "LOTUS - the natural products occurrence database: LOTUS Tree",
    "Medical Subject Headings (MeSH): MeSH Tree",
    "MolGenie: MolGenie Organic Chemistry Ontology",
    "National Drug Code (NDC) Directory: FDA Drug Type and Pharmacologic Classification",
    "NCBI Taxonomy: Taxonomy",
    "NCI Thesaurus (NCIt): NCI Thesaurus",
    "NIST Synthetic Polymer MALDI Recipes Database: NIST Synthetic Polymer Classification",
    "NORMAN Suspect List Exchange: NORMAN Suspect List Exchange Classification",
    "Pistoia Alliance DataFAIRy Bioassay Pilot: Pistoia Classification Tree",
    "PubChem: Aggregated CCS Classification",
    "PubChem: Chemicals in PubChem from Regulatory Sources",
    "PubChem: PFAS and Fluorinated Compounds in PubChem",
    "PubChem: PubChem BioAssay Classification",
    "PubChem: PubChem Cell TOC",
    "PubChem: PubChem Compound TOC",
    "PubChem: PubChem Gene TOC",
    "PubChem: PubChem Pathway TOC",
    "PubChem: PubChem Protein TOC",
    "PubChem: PubChem Taxonomy TOC",
    "Swiss Institute of Bioinformatics ENZYME: Enzyme Classification",
    "The Natural Products Atlas: The Natural Products Atlas Classification",
    "WHO Anatomical Therapeutic Chemical (ATC) Classification: ATC Classification",
    "WIPO: International Patent Classification",
    "World Register of Marine Species (WoRMS): Biota"
]

        for option in values:
            page = pubchem_home(self.driver)
            page.select_classification(option)
            self.driver.save_screenshot(os.path.join(screenshots_loc, f"{option}.png"))