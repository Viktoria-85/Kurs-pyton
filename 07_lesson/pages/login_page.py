from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage:


    def __init__(self, driver):
        self.driver = driver
        self.driver.maximizewindow()
        self.wait = WebDriverWait(self.driver, 10)

# открыть браузер
    def open_shop(self):
        self.driver.get("https://www.saucedemo.com/")

    # ввод логина
    def enter_user_name(self):
        user_name = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        user_name.send_keys("standard_user")

    # ввод пароля
    def enter_password(self):
        input_password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        input_password.send_keys("secret_sauce")

    def clik_login(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "#login-button")
        button.click()

