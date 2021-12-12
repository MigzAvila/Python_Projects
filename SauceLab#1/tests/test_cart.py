from src.cart import Cart


def test_cart(driver, username, password):
    # test if cart number matches to item add in the page
    user = Cart(driver)
    product = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Bike Light",
        "Sauce Labs Fleece Jacket"
    ]
    assert user.increment_cart(username, password, product) == "Passed"


def test_cart_page(driver, username, password):
    # test if items added to cart are all visible in cart page
    user = Cart(driver)
    product = [
        "Sauce Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Bike Light",
        "Sauce Labs Fleece Jacket"
    ]
    assert user.cart_items(username, password, product) == "Passed"
