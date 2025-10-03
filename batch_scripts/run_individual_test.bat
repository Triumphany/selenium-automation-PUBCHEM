@echo off
echo ========================================
echo    PubChem Framework - ALL INDIVIDUAL TESTS
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ========== RUNNING ALL TESTS INDIVIDUALLY ==========
echo.

echo [1/16] Running Homepage Buttons Test...
pytest tests/test_HOMEpage.py --html=reports/homepage_report.html --self-contained-html -v

echo [2/16] Running Periodic Table Elements Test...
pytest tests/test_periodicTABLE_elements.py --html=reports/periodic_elements_report.html --self-contained-html -v

echo [3/16] Running Density Plot Test...
pytest tests/test_density.py --html=reports/density_report.html --self-contained-html -v

echo [4/16] Running Electron Affinity Plot Test...
pytest tests/test_electron_affinity_plot.py --html=reports/electron_affinity_report.html --self-contained-html -v

echo [5/16] Running Electronegativity Chart Test...
pytest tests/test_electronegativity_chart.py --html=reports/electronegativity_report.html --self-contained-html -v

echo [6/16] Running Melting Point Plot Test...
pytest tests/test_melting_point.py --html=reports/melting_point_report.html --self-contained-html -v

echo [7/16] Running Search Functionality Test...
pytest tests/test_search.py --html=reports/search_report.html --self-contained-html -v

echo [8/16] Running Browse Data Options Test...
pytest tests/test_options_BRWOSERdata.py --html=reports/browse_data_report.html --self-contained-html -v

echo [9/16] Running Upload ID Input Test...
pytest tests/test_uploadID_input.py --html=reports/upload_input_report.html --self-contained-html -v

echo [10/16] Running Element Properties Test...
pytest tests/test_properties_selection.py --html=reports/properties_report.html --self-contained-html -v

echo [11/16] Running Draw Structure Buttons Test...
pytest tests/test_draw_structure_buttons.py --html=reports/draw_structure_report.html --self-contained-html -v

echo [12/16] Running Atomic Masses Chart Test...
pytest tests/test_atomicMASSES.py --html=reports/atomic_masses_report.html --self-contained-html -v

echo [13/16] Running Atomic Radius Chart Test...
pytest tests/test_atomicRadius.py --html=reports/atomic_radius_report.html --self-contained-html -v

echo [14/16] Running Boiling Point Plot Test...
pytest tests/test_boiling_point.py --html=reports/boiling_point_report.html --self-contained-html -v

echo [15/16] Running Upload ID by File Test...
pytest tests/test_uploadID_byFILE.py --html=reports/upload_file_report.html --self-contained-html -v

echo [16/16] Running Ionization Energy Plot Test...
pytest tests/test_ionization_plot.py --html=reports/ionization_report.html --self-contained-html -v

echo.
echo ========== ALL TESTS COMPLETED ==========
echo.
echo Individual reports generated in 'reports' folder:
echo - homepage_report.html
echo - periodic_elements_report.html
echo - density_report.html
echo - electron_affinity_report.html
echo - electronegativity_report.html
echo - melting_point_report.html
echo - search_report.html
echo - browse_data_report.html
echo - upload_input_report.html
echo - properties_report.html
echo - draw_structure_report.html
echo - atomic_masses_report.html
echo - atomic_radius_report.html
echo - boiling_point_report.html
echo - upload_file_report.html
echo - ionization_report.html
echo.
pause