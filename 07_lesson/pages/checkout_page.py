from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_user_data(self, fname, lname, post_code):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys(fname)
        first_name.click()

        last_name =self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys(lname)
        last_name.click()

        postal_code_field = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code_field.send_keys(post_code)

    def click_continue(self):
         button = self.driver.find_element(By.CSS_SELECTOR, "#continue")
         button.click()

    def get_total(self):
         return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
