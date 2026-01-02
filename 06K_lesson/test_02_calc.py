import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_slow_calculator(browser):

    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Вводим значение 45 в поле задержки
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()


    wait = WebDriverWait(browser, 46)

    try:
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        screen_element = browser.find_element(By.CLASS_NAME, "screen")
        actual_result = screen_element.text

        assert actual_result == "15", f"Ожидался результат '15', но получен '{actual_result}'"
        print(f"✓ Результат '15' отобразился через 45 секунд")

    except TimeoutException:

        screen_element = browser.find_element(By.CLASS_NAME, "screen")
        actual_result = screen_element.text
        pytest.fail(f"Результат не появился за 45 секунд. Текущее значение на экране: '{actual_result}'")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

















