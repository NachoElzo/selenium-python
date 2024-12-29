import os
import pytest
from selenium import webdriver
from helpers.browser_options import get_chrome_options, get_firefox_options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Configurar el token de GitHub para superar el límite de la API
os.environ["GH_TOKEN"] = "TU_TOKEN_PERSONAL_AQUÍ"  # Reemplaza con tu token personal


# Fixture para Chrome
@pytest.fixture(scope="function")
def chrome_driver():
    options = get_chrome_options()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# Fixture para Firefox
@pytest.fixture(scope="function")
def firefox_driver():
    options = get_firefox_options()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()
