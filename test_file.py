import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ---------- CONFIG (Hardcoded for simplicity) ----------
URL = "https://console.upstash.com/auth/sign-in"
EMAIL = "atulbootcoding26@gmail.com"         # Use dummy/test credentials
PASSWORD = "Bootcoding12!@"

# ---------- FIXTURE ----------
@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')  # Remove this line if you want to see the browser
    service = Service()  # You can specify chromedriver path if needed
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# ---------- TEST CASE ----------
def test_login_invalid(driver):
    driver.get(URL)

    # Locate email field and enter email
    driver.find_element(By.NAME, "email").send_keys(EMAIL)

    # Locate password field and enter password
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)

    # Click Log In button
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div/form/button").click()

    # Optional: Wait and check for error
    time.sleep(3)

    # You can assert based on actual error message or URL change
    assert "login" in driver.current_url.lower()  # Simplified assertion

    # Print result (just for demo)
    print("Test completed: Invalid login attempt")

