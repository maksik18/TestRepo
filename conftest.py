import pytest
from pydantic_settings import BaseSettings
from selenium import webdriver

from pages.login_page import LoginPage


class Settings(BaseSettings):
    base_url: str
    username: str
    password: str

    class Config:
        env_file = ".env"


settings = Settings()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(settings.base_url)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in(driver):
    login_page = LoginPage(driver)

    login_page.login(
        settings.username,
        settings.password
    )

    yield driver