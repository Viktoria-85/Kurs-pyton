# from pydoc import browse

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(" https://www.saucedemo.com/")

def test_shop_element():
    user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
    user_name.send_keys("standard_user")

    input_password = driver.find_element(By.CSS_SELECTOR, "#password")
    input_password.send_keys("secret_sauce")

    button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    button.click()

    button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    button.click()

    button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    button.click()

    button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    button.click()

    button = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    button.click()

    button = driver.find_element(By.CSS_SELECTOR, "#checkout")
    button.click()

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys('Виктория')
    first_name.click()

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys('Новикова')
    last_name.click()

    button = driver.find_element(By.CSS_SELECTOR, "#continue")
    button.click()

    postal_code_field = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code_field.send_keys("123456")

    driver.quit()
















