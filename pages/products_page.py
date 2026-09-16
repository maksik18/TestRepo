from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack(self) -> None:
        self.click(self.ADD_BACKPACK)

    def remove_backpack(self) -> None:
        self.click(self.REMOVE_BACKPACK)

    def is_remove_backpack_displayed(self) -> bool:
        return self.is_displayed(self.REMOVE_BACKPACK)

    def is_add_backpack_displayed(self) -> bool:
        return self.is_displayed(self.ADD_BACKPACK)

    def cart_badge_text(self) -> str:
        return self.find(self.SHOPPING_CART_BADGE).text