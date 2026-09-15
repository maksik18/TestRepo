from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    def add_backpack(self):
        self.click(self.ADD_BACKPACK)

    def is_remove_button_visible(self):
        return self.find(self.REMOVE_BACKPACK).is_displayed()

    def remove_product(self):
        self.click(self.REMOVE_BACKPACK)
