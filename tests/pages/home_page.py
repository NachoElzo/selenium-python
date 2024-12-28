from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class HomePage:
    def __init__(self, driver=None):
        if not driver:
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            self.driver = Chrome(ChromeDriverManager().install(), options=options)
        else:
            self.driver = driver

    def go_to_login(self):
        title = (By.ID, "main-title")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(title))
        assert self.driver.find_element(*title).is_displayed(), "Title not visible"
