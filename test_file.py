import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Constants
URL = "https://console.upstash.com/auth/sign-in"
EMAIL = "atulbootcoding26@gmail.com"
PASSWORD = "Bootcoding12!@"  # dummy password for invalid login

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--headless')  # disable for debugging
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')  # bypass some bot detection

    # Start Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_invalid(driver):
    driver.get(URL)

    # Screenshot after loading
    driver.save_screenshot("01_login_page.png")

    # Enter email and password
    driver.find_element(By.NAME, "email").send_keys(EMAIL)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)

    # Wait and click login button
    wait = WebDriverWait(driver, 15)
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_btn.click()

    # Screenshot after clicking login
    driver.save_screenshot("02_after_click.png")

    # Wait until still on login page (invalid login)
    wait.until(EC.url_contains("sign-in"))

    driver.save_screenshot("03_dashboard.png")

    # Optional: check error message (if any)
    try:
        error = driver.find_element(By.CSS_SELECTOR, "p.text-destructive").text
        print(f"❌ Error message: {error}")
        assert "invalid" in error.lower()
    except:
        print("⚠️ Could not detect error message, but still on login page.")

    # Final assert
    #assert "sign-in" in driver.current_url.lower()
