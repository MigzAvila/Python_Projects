# Used for Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import of TimeoutException
from selenium.common.exceptions import TimeoutException

# Class
class Product(object):
    def __init__(self, driver):
        self.driver = driver
        # counter to verify all added items match the value in cart icon
        self.counter = 0
        # Adds all process product
        self.process_product = []
        self.page = (By.XPATH, "//span[@class='title']")

    # returns the path of the product
    def product_path(self, product):
        return (By.XPATH, f"//div[@class='inventory_item_name'][text()='{product}']/../../../div[@class='pricebar']/button[contains(@class, 'btn_primary')]")

    # finds all product available and adds them to cart
    def find_product(self, products):
        # check of the page is product pages
        if self.is_product_page() == "Wrong Page":
            return "Wrong Page"

        # loops each object to be added in cart
        for product in products:
            # Check if product is available in page
            try:
                # finds the product
                product_item = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.product_path(product)))
                product_item.click()

                # increments the counter as the product was added to cart and appends it to process product
                self.counter += 1
                self.process_product.append(product)

            # error, product item was not found
            except TimeoutException:
                print(f"Error, could not process {product}.")
        if self.counter == len(products):
            return "Passed"
        else:
            return self.process_product

    def is_product_page(self):
        # check if current page is product pages
        try:
            # Returns pages title "Product"
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.page)).text

        # error, currently in wrong page
        except TimeoutException:
            return "Wrong Page"
