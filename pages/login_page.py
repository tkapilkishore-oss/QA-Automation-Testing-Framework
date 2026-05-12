from selenium.webdriver.common.by import By


class LoginPage:

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.TAG_NAME, "h3")

    def __init__(self, driver):
        self.driver = driver

    # Open Website
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    # Enter Username
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    # Enter Password
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    # Click Login
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # Get Error Message
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text