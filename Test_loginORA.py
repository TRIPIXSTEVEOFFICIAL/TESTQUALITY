import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Main site ORANGEHRM
LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Fixture: setup, teardown and yields to open the site and closes after each test cases
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# TC01: Valid login
def test_login_valid_credentials(driver):
    driver.get(LOGIN_URL)
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    assert "dashboard" in driver.current_url

# TC02: Dashboard redirect check
def test_login_valid_dashboard_redirect(driver):
    driver.get(LOGIN_URL)
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    assert "dashboard" in driver.current_url

# TC03-TC08: Invalid login test cases
# Parametrize - to reduce redundancy
@pytest.mark.parametrize("username,password,description", [
    ("Admin", "wrongpass", "Valid username, invalid password"),
    ("wronguser", "admin123", "Invalid username, valid password"),
    ("wronguser", "wrongpass", "Invalid username and password"),
    ("", "", "Empty username and password"),
    ("", "admin123", "Empty username, valid password"),
    ("Admin", "", "Valid username, empty password")
])
def test_login_invalid_credentials(driver, username, password, description):
    driver.get(LOGIN_URL)
    time.sleep(3)

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    assert "dashboard" not in driver.current_url