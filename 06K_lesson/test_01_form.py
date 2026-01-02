import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def test_open_data_types_page():

    edge_options = Options()
    driver = webdriver.Edge(options=edge_options)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        assert "Data types" in driver.title or "Data types" in driver.page_source

        assert driver.find_element(By.ID, "first-name").is_displayed()
        assert driver.find_element(By.ID, "last-name").is_displayed()
        assert driver.find_element(By.CSS_SELECTOR, "button[type='submit']").is_displayed()

        print("✅ Страница успешно загружена в Edge")
        print(f"📄 Заголовок страницы: {driver.title}")
        print(f"🔗 Текущий URL: {driver.current_url}")

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])














