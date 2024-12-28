# Selenium mac python setup

1. install python or pipenv
2. install selenium for python [here](https://pypi.org/project/selenium/)
   - install selenium: `pip install -U selenium`
3. handy commands for selenium
   - show selenium settings: `pip show selenium`
   - check selenium is not broken `pip check selenium`
   - uninstall selenium `pip uninstall selenium`
4. install pytest not requiered but complements for ci/cd and validations:
   - install pytest:`pip install pytest`
5. install ChromeDriverManager for driver configs `pip install webdriver-manager`
6. create a `__init__.py` file in your page and test folder main path of yor project for importing modules
7. functions and test files sould be named ading first test\_
8. install webdriver manager for handling multiple browsers in pip commands: `pip install selenium pytest webdriver-manager`
9. create a pytest.ini for project configurations
10. hide `__pychache__` file extensions
    - in mac press cmd + ,
    - search for files.exclude
    - add the pattern \*\*/**pycache**

- execute example `pytest tests/specs/test_home_page.py`
  -add
