# conftest.py
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers.chrome_options import get_chrome_options


@pytest.fixture
def driver():
    # Configurar el navegador con las opciones definidas
    service = Service(ChromeDriverManager().install())
    options = get_chrome_options()
    driver = Chrome(service=service, options=options)
    yield driver
    driver.quit()
