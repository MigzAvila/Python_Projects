import unittest
import time

import src.page as page

import tests.test_login as logintest

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
        logintest.test_block_user(self.driver)

    def test_standard_login(self):
        #Test normal user
        logintest.standard_user(self.driver)

    def test_glitch_login(self):
        #Test glitch user
        logintest.glitch_user(self.driver)

    def tearDown(self):
        """Invoked method after each test"""
        self.driver.close()

if __name__ == "__main__":
    unittest.main()











