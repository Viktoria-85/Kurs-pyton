from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(" http://uitestingplayground.com/ajax")


# нажать на синию плашку
ajax_button = driver.find_element(By.ID, "ajaxButton")
ajax_button.click()

# Дождаться появления результата
wait = WebDriverWait(driver, 15)
result_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content p")))

# Вывести текст
text = result_element.text
print(f"Data loaded with AJAX get request",'{text}')

driver.quit()





