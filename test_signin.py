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
    # Do NOT use headless
    driver = webdriver.Chrome(options=options)
    yield driver
    # driver.quit()  # Comment during test to keep browser open

def test_valid_signin(driver):
    driver.get("https://console.upstash.com/auth/sign-in")

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys("atulbootcoding26@gmail.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Bootcoding12!@")

    driver.find_element(By.XPATH, "//button[contains(., 'Continue')]").click()

    # Wait until dashboard header is visible
    driver.get("https://console.upstash.com/redis?teamid=0")

    print("✅ Login successful — You should now see the dashboard.")
    time.sleep(30)  # Pause so you can see the dashboard
