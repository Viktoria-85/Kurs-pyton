from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def add_to_cart(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        button.click()

        button = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        button.click()

        button = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        button.click()

    def click_cart(self):
        button =self.driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        button.click()
