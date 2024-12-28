from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage  # Ajusta la ruta según tu estructura


def test_login():
    # Configuración de Chrome con opciones headless
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())

    # Inicializar el driver con opciones configuradas
    driver = Chrome(service=service, options=options)

    # Crear una instancia de HomePage y realizar acciones
    homePage = HomePage(driver)
    driver.get("https://www.google.com")
    homePage.go_to_login()

    # Cerrar el navegador
    driver.close()
