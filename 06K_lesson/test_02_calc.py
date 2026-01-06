from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html ")


def test_calculator_button():

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()

    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()

    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()


    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    res = test_calculator_button(7, 8)
    assert res == 15























