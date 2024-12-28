from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class HomePage:
    def __init__(self, driver: WebDriver = None):
        options = Options()  # Crear una instancia de Options
        options.add_argument("--headless")  # Agregar el modo headless
        options.add_argument("--disable-gpu")  # Necesario para algunos sistemas
        options.add_argument("--no-sandbox")  # Mejora compatibilidad en CI
        options.add_argument("--disable-dev-shm-usage")  # Manejo de memoria compartida
        service = Service(ChromeDriverManager().install())  # Instalar el driver
        self.driver = driver if driver else Chrome(service=service, options=options)

    def go_to_login(self):
        # Localizador definido localmente dentro del método
        login_button = (
            By.ID,
            "W0wltc",  # Suponiendo que este es el ID correcto del botón
        )
        self.driver.find_element(*login_button).click()
