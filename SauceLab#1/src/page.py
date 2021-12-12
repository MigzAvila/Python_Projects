 # Import of Key for Enter
from selenium.webdriver.common.keys import Keys

# Used for Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import of TimoutException
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    # Constructor for basePage
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.err = (By.XPATH, "//div[@class='error-message-container error']/h3")
        self.title = (By.XPATH, "//span[@class='title']")


class LoginPage(BasePage):
    """Login Page class containing login and verify if a user is login """
    def login(self, username, password):
        # Inputs username input and its value
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)

        # Inputs the password and submit the credentials
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password,
                                                                                                            Keys.ENTER)

        # Verifies if there is an error
        try:
            # If Error, return error text
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.err)).text

        # If no error, login was successful and return an instance of this class
        except TimeoutException:
            return LoginPage(self.driver)

    # Checks if current Page is Login Page
    def is_Login_Page(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.title))
            return True
        except TimeoutException:
            return False


