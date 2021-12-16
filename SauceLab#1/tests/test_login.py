import src.page as page
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


def test_block_user(driver):
    # Test a locked user
    ProductsPage = page.LoginPage(driver).login("locked_out_user", "secret_sauce")
    assert ProductsPage == "Epic sadface: Sorry, this user has been locked out."


def test_standard_user(driver):
    # Test a standard user
    ProductsPage = page.LoginPage(driver).login("standard_user", "secret_sauce")
    assert ProductsPage.is_Login_Page()


def test_glitch_user(driver):
    # Test a glitch user
    ProductsPage = page.LoginPage(driver).login("performance_glitch_user", "secret_sauce")
    assert ProductsPage.is_Login_Page()
