from config import settings
from pages.login_page import LoginPage


def test_login_successful(driver):
    login_page = LoginPage(driver)

    login_page.login(settings.username, settings.password)

    assert "/inventory.html" in driver.current_url
    assert driver.title == "Swag Labs"