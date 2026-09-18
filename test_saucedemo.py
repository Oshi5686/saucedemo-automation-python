import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_login():
    # 1. Initialize Chrome Browser
    driver = webdriver.Chrome()  # pylint: disable=not-callable
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)  # waits up to 10s for elements

    try:
        # 2. Open SauceDemo Website
        driver.get("https://www.saucedemo.com/")

        # 3. Enter Credentials and Login
        wait.until(EC.presence_of_element_located(
            (By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 4. Verify successful redirection to inventory page
        wait.until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url
        print("\n[SUCCESS] TC_LOGIN_01: Login Successful!")

        # 5. Add an item to cart (TC_CART_01)
        add_to_cart_btn = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_btn.click()

        # 6. Verify cart badge update (wait until badge actually appears)
        cart_badge = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert cart_badge.text == "1"
        print("[SUCCESS] TC_CART_01: Item added to cart successfully!")

    finally:
        # 7. Close Browser
        time.sleep(1)
        driver.quit()
