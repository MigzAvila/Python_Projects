import time
import unittest

from tests.test_login import User
import tests.test_cart as test_cart

#import Driver
from selenium import webdriver


class SauceLab(unittest.TestCase):
    """Sauce Lab testing login accounts, Cart Icon Increment and Verify Item Added To Cart"""

    def setUp(self):
        """Setup method for each test"""
        # Path to web Driver
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)

        self.URL = "https://www.saucedemo.com/"
        self.driver.get(self.URL)

    def test_lock_login(self):
        #Test lock user
        User(self.driver).block_user()

    def test_standard_login(self):
        #Test normal user
        User(self.driver).standard_user()

    def test_glitch_login(self):
        #Test glitch user
        User(self.driver).glitch_user()

    def test_cart_normal(self):
        # tests Item Added To Cart are present in cart page with normal user
        user = "standard_user"
        password = "secret_sauce"
        test_cart.test_cart(self.driver, user, password)

    def test_cart_glitch(self):
        # tests Item Added To Cart are present in cart page with glitch user
        user = "performance_glitch_user"
        password = "secret_sauce"
        test_cart.test_cart(self.driver, user, password)

    def test_cart_normal_cart_page(self):
        # tests Item Added To Cart are present in cart page
        user = "standard_user"
        password = "secret_sauce"
        test_cart.test_cart_page(self.driver, user, password)

    def test_cart_glitch_cart_page(self):
        # tests Item Added To Cart are present in cart page
        user = "performance_glitch_user"
        password = "secret_sauce"
        test_cart.test_cart_page(self.driver, user, password)

    def tearDown(self):
        """Invoked method after each test"""
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()











