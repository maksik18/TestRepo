from pages.products_page import ProductsPage


def test_add_product(logged_in):

    products_page = ProductsPage(logged_in)

    products_page.add_backpack()

    assert products_page.is_remove_button_visible()

def test_remove_product(logged_in):
    products_page = ProductsPage(logged_in)

    products_page.add_backpack()
    products_page.remove_product()
