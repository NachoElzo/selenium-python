from pages.home_page import HomePage


def test_home_page_firefox(firefox_driver):
    f_home_page = HomePage(firefox_driver)  # Usamos firefox_driver aquí
    f_home_page.driver.get("https://practice.expandtesting.com/")
    f_home_page.validate_title()


def test_home_page_chrome(chrome_driver):
    home_page = HomePage(chrome_driver)  # Usamos chrome_driver aquí
    home_page.driver.get("https://practice.expandtesting.com/")
    home_page.validate_title()
