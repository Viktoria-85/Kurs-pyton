
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self.driver = browser

    def click_checkout(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "#checkout")
        button.click()
