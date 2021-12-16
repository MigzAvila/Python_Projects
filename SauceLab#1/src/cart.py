import src.page as page
from src.product import Product

# Used for Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import of TimeoutException
from selenium.common.exceptions import TimeoutException


# Class to check cart status, add products
class Cart(object):
    """Cart class containing increment verification and cart status (is cart empty), item present in cart page, etc. """

    def __init__(self, driver):
        self.driver = driver
        self.page_path = (By.XPATH, "//div[@class= 'shopping_cart_container']/a")
        self.page = (By.XPATH, "//span[@class= 'title']")
        self.process_product = []
        self.counter = 0
        self.cart_icon = (By.XPATH, "//span[@class= 'shopping_cart_badge']")

    # returns the path of the item in cart
    def item_path(self, product):
        return (By.XPATH, f"//div[@class='inventory_item_name'][text()='{product}']")

    # Process login and preforms Add item to cart
    def increment_cart(self, username, password, products):
        if self.cart_status() != 0:
            return "Cart is not empty"

        products_page = page.LoginPage(self.driver).login(username, password)
        products_page.is_Login_Page()

        # Adds all found product in products
        click_product = Product(self.driver)
        return click_product.find_product(products)

    def cart_status(self):
        # Verifies if the cart is empty or items added
        try:
            # return items values
            return WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.cart_icon)).text

        # error, the cart is empty, thus returning 0
        except TimeoutException:
            return 0

    # Check items with item added
    def cart_items(self, username, password, products):
        # check if current page is product pages
        products_page = page.LoginPage(self.driver).login(username, password)
        products_page.is_Login_Page()

        # Adds all found product in products to cart
        click_product = Product(self.driver)
        # gets a list of item that were successfully added to cart
        products_added = click_product.find_product(products)

        # goes to cart page
        self.go_to_cart_page()
        if self.is_cart_page() != "YOUR CART":
            return "Wrong Page"

        # checks if items added to cart are visible in cart page
        return self.check_items_in_cart(products_added)

    def go_to_cart_page(self):
        try:
            # finds the cart icon and goes to cart page
            cart = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.page_path))
            cart.click()

        # error, link not found
        except TimeoutException:
            return "Could not click page"

    def check_items_in_cart(self, products):
        # loops each object and checks it is present in cart page
        for product in products:
            # Check if product is available in page
            try:
                # finds the product
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.item_path(product)))

                # increments the counter as the product is visible in cart page
                self.counter += 1
                self.process_product.append(product)

            # error, product item was not found
            except TimeoutException:
                print(f"Error, did not find {product}.")

        #  checks if items added to cart are all visible in cart page
        if self.counter == len(products):
            return "Passed"
        else:
            return f"Only {self.counter} were processed out of {len(products)}: {self.process_product}"

    def is_cart_page(self):
        # check if current page is product pages
        try:
            # Returns pages title "Product"
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.page)).text

        # error, currently in wrong page
        except TimeoutException:
            return "Wrong Page"
