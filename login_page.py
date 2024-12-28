from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):  # Especifica el tipo
        self.driver = driver
        self.button = (By.ID, "W0wltc")
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.submit_button = (By.NAME, "submit")

    def checkButton(self):
        self.driver.find_element(*self.button).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.submit()
