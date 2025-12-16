import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# FIXTURE 
# Handles browser setup and teardown
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window() 
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    yield driver
    driver.quit()

# VALID LOGIN TEST CASES 

# TC01: Valid username and valid password
def test_login_valid_credentials(driver):
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)
    assert "dashboard" in driver.current_url, "Valid login failed: Did not redirect to dashboard"

# TC02: Valid credentials should stay on the dashboard page
def test_login_valid_dashboard_redirect(driver):
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)
    assert "dashboard" in driver.current_url, "Dashboard redirect failed after valid login"

#  INVALID LOGIN TEST CASES 

# Using parametrization to cover multiple invalid login scenarios
@pytest.mark.parametrize("username,password,description", [
    ("Admin", "wrongpass", "Valid username, invalid password"),        
    ("wronguser", "admin123", "Invalid username, valid password"),     
    ("wronguser", "wrongpass", "Invalid username and password"),    
    ("", "", "Empty username and password"),                      
    ("", "admin123", "Empty username, valid password"),              
    ("Admin", "", "Valid username, empty password")                  
])
def test_login_invalid_credentials(driver, username, password, description):

    if username:
        driver.find_element(By.NAME, "username").send_keys(username)
    if password:
        driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)
    assert "dashboard" not in driver.current_url, f"Invalid login passed: {description}"