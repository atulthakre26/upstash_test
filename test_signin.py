import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    yield driver
    # driver.quit()  # Keep open for debugging

def test_valid_signin(driver):
    driver.get("https://console.upstash.com/auth/sign-in")

    # Wait for email field and input
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys("atulbootcoding26@gmail.com")

    # Input password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Bootcoding12!@")

    # Click continue
    driver.find_element(By.XPATH, "//button[contains(., 'Continue')]").click()

    # ✅ Wait for URL to change to dashboard
    WebDriverWait(driver, 15).until(
        lambda d: "redis?teamid=" in d.current_url
    )

    # ✅ Optionally confirm with an element on dashboard
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Create Database')]"))
    )

    print("✅ Login successful — Dashboard loaded.")
    time.sleep(10)
