# SauceDemo Test Automation (Python + Selenium + Pytest)

An automated UI testing suite for the [SauceDemo](https://www.saucedemo.com/) e-commerce website, built using Python, Selenium WebDriver, and Pytest.

##  Key Features Automated
- **TC_LOGIN_01:** Validates user login functionality and URL redirection to the inventory page.
- **TC_CART_01:** Validates adding an item to the shopping cart and verifies the cart badge updates correctly.

##  Tech Stack
- **Language:** Python 3.11
- **Automation Tool:** Selenium WebDriver 4.x
- **Testing Framework:** Pytest
- **Design Pattern:** Explicit Waits with Expected Conditions (no hardcoded `time.sleep`, for reliable and non-flaky tests)

##  Project Structure
```
saucedemo-automation-python/
└── test_saucedemo.py   # Login + Add to Cart test flow
```

##  How to Run Tests Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Oshi5686/saucedemo-automation-python.git
   cd saucedemo-automation-python
   ```

2. **Install dependencies**
   ```bash
   pip install selenium pytest
   ```

3. **Run the tests**
   ```bash
   pytest test_saucedemo.py -s
   ```

##  Sample Output
```
test_saucedemo.py
[SUCCESS] TC_LOGIN_01: Login Successful!
[SUCCESS] TC_CART_01: Item added to cart successfully!
.
========================== 1 passed in 9.66s ==========================
```
