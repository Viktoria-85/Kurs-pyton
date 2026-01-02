import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def browser():
    options = Options()
    # options.add_argument("--headless")  # раскомментировать для headless-режима
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_sauce_demo_total_price(browser):
    browser.get("https://www.saucedemo.com/")


    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()


    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))


    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:

        add_button_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        add_button = browser.find_element(By.XPATH, add_button_xpath)
        add_button.click()


    cart_icon = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()


    checkout_button = browser.find_element(By.ID, "checkout")
    checkout_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "first-name")))

    browser.find_element(By.ID, "first-name").send_keys("Виктория")
    browser.find_element(By.ID, "last-name").send_keys("Носикова")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()


    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

    total_element = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text

    total_amount = total_text.split("$")[1]

    assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получена ${total_amount}"



if __name__ == "__main__":
    pytest.main([__file__, "-v"])




