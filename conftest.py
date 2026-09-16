from pathlib import Path

import pytest
from selenium import webdriver

from config import settings
from pages.login_page import LoginPage


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    if settings.headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(settings.driver_timeout)
    driver.get(settings.base_url)

    yield driver

    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        artifacts_dir = Path("artifacts") / request.node.name
        artifacts_dir.mkdir(parents=True, exist_ok=True)
        driver.save_screenshot(artifacts_dir / "failure.png")

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, f"rep_{call.when}", outcome.get_result())


@pytest.fixture
def logged_in(driver):
    login_page = LoginPage(driver)
    login_page.login(settings.username, settings.password)
    yield driver