import src.page as page

def test_block_user(driver):
    # Test a locked user
    ProductsPage = page.LoginPage(driver).login("locked_out_user", "secret_sauce")
    assert ProductsPage == "Epic sadface: Sorry, this user has been locked out."

def standard_user(driver):
    # Test a locked user
    ProductsPage = page.LoginPage(driver).login("standard_user", "secret_sauce")
    assert ProductsPage.is_Login_Page()

def glitch_user(driver):
    # Test a locked user
    ProductsPage = page.LoginPage(driver).login("performance_glitch_user", "secret_sauce")
    assert ProductsPage.is_Login_Page()