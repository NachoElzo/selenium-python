import pytest
from pages.home_page import HomePage  # Asegúrate de que la importación esté bien


def test_home_page(driver):
    # Usar el fixture 'driver' y pasarlo a la clase HomePage
    home_page = HomePage(driver)
    home_page.go_to_login()  # Llamar al método
