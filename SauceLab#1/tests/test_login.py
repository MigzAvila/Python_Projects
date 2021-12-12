import src.page as page


class User(object):
    def __init__(self, driver):
        self.driver = driver

    def block_user(self):
        # Test a locked user
        ProductsPage = page.LoginPage(self.driver).login("locked_out_user", "secret_sauce")
        assert ProductsPage == "Epic sadface: Sorry, this user has been locked out."

    def standard_user(self):
        # Test a standard user
        ProductsPage = page.LoginPage(self.driver).login("standard_user", "secret_sauce")
        assert ProductsPage.is_Login_Page()

    def glitch_user(self):
        # Test a glitch user
        ProductsPage = page.LoginPage(self.driver).login("performance_glitch_user", "secret_sauce")
        assert ProductsPage.is_Login_Page()
