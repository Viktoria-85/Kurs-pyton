from selenium import webdriver
from pages.shop_page import ShopPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage


def test_shop_click_button():
    driver = webdriver.Firefox()
    page = LoginPage(driver)
    page.open_shop()
    page.enter_user_name("standard_user")
    page.enter_password("secret_sauce")
    page.click_login()
    shop_page = ShopPage(driver)
    shop_page.add_to_cart()
    shop_page.click_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_user_data("Виктория","Новикова", "1234")
    checkout_page.click_continue()

    assert checkout_page.get_total() == "Total: $58.29"

    driver.quit()


