from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config import settings

Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = settings.driver_timeout):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: Locator, text: str) -> None:
        self.find(locator).send_keys(text)

    def is_displayed(self, locator: Locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False