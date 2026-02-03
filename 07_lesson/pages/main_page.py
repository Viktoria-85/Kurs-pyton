from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:


    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

    def open_calculator(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value: str):
        delay_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, text: str):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']")))
        button.click()

    def get_result(self, result):
        return  WebDriverWait(self.driver, 46).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), result))



