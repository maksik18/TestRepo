from pages.products_page import ProductsPage


def test_add_product_to_cart(logged_in):
    products_page = ProductsPage(logged_in)

    products_page.add_backpack()

    assert products_page.is_remove_backpack_displayed()
    assert products_page.cart_badge_text() == "1"


def test_remove_product_from_cart(logged_in):
    products_page = ProductsPage(logged_in)

    products_page.add_backpack()
    products_page.remove_backpack()

    assert products_page.is_add_backpack_displayed()