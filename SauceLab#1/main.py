import time
import src.page as page

import tests.test_login as login
import tests.test_cart as test_cart

# import Driver
from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def driver():
    """Setup method for each test"""
    # Path to web Driver
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    url = "https://www.saucedemo.com/"
    driver.get(url)
    return driver


def test_lock_login(driver):
    # Test lock user
    login.test_block_user(driver)
    driver.quit()


def test_standard_login(driver):
    # Test normal user
    login.test_standard_user(driver)
    driver.quit()


def test_glitch_login(driver):
    # Test glitch user
    login.test_glitch_user(driver)
    driver.quit()


def test_cart_normal(driver):
    # tests Item Added To Cart are present in cart page with normal user
    user = "standard_user"
    password = "secret_sauce"
    test_cart.test_cart(driver, user, password)
    driver.quit()


def test_cart_glitch(driver):
    # tests Item Added To Cart are present in cart page with glitch user
    user = "performance_glitch_user"
    password = "secret_sauce"
    test_cart.test_cart(driver, user, password)
    driver.quit()


def test_cart_normal_cart_page(driver):
    # tests Item Added To Cart are present in cart page
    user = "standard_user"
    password = "secret_sauce"
    test_cart.test_cart_page(driver, user, password)
    driver.quit()


def test_cart_glitch_cart_page(driver):
    # tests Item Added To Cart are present in cart page
    user = "performance_glitch_user"
    password = "secret_sauce"
    test_cart.test_cart_page(driver, user, password)
    driver.quit()


