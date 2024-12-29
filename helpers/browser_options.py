from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_chrome_options():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    return options


def get_firefox_options():
    options = FirefoxOptions()
    options.add_argument("--headless")  # Opcional, elimina si quieres interfaz gráfica
    options.add_argument("--disable-gpu")  # Opcional
    return options
