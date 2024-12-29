from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def validate_title(self):
        title = (By.ID, "main-title")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(title))
        element = self.driver.find_element(*title)
        print(f"Title text: {element.text}")
        assert element.is_displayed(), "Title not visible"
