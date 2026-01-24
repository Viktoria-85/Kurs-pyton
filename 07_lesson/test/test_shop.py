
from selenium.webdriver.common.by import By
from pages.shop import ShopPage
from pages.login import LoginPage
from pages.checkout import CheckoutPage


def test_shop():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    page = ShopPage(driver)
    page.click_button("#add-to-cart-sauce-labs-backpack")
    page.click_button("#add-to-cart-sauce-labs-bolt-t-shirt")
    page.click_button("#add-to-cart-sauce-labs-onesie")
    page = LoginPage(driver)
    page.input_password.send_keys("secret_sauce")
    page = CheckoutPage(driver)
    page.first_name.send_keys('Виктория')
    page.last_name.send_keys('Новикова')
    page.postal_code_field.send_keys("123456")
    page.button.click()


    total_element = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    assert total_element.text == "Total: $58.29"

    driver.quit()



