from selenium import webdriver
from pages.main_page import MainPage


def test_calculator_button():
    driver = webdriver.Chrome()
    page = MainPage(driver)
    page.open_calculator()
    page.set_delay("5")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    assert page.get_result("15")

    driver.quit()
