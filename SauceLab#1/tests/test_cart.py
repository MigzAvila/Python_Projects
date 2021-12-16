from src.cart import Cart
# import Driver
from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def driver():
    """Setup method"""
    # Path to web Driver
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    url = "https://www.saucedemo.com/"
    driver.get(url)
    return driver


# Fixture function with module scope
@pytest.fixture(scope="module")
def username():
    """Setup method for each test"""
    # Username to swag website, change as needed
    username = 'standard_user'
    return username


# Fixture function with module scope
@pytest.fixture(scope="module")
def password():
    """Setup method for each test"""
    # Password to swag website
    password = "secret_sauce"
    return password


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
