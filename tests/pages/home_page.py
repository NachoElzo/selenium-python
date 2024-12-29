from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver  # Importa WebDriver


class HomePage:
    def __init__(
        self, driver: WebDriver  # Especifica el tipo 'WebDriver' de manera explícita
    ):
        self.driver = driver

    def go_to_login(self):
        self.driver.get("https://practice.expandtesting.com/#tools")
        title = (By.ID, "main-title")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(title))
        assert self.driver.find_element(*title).is_displayed(), "Title not visible"
