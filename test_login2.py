import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_positive_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(6)

    success_text = driver.find_element(By.TAG_NAME, "h1").text
    assert "Logged In Successfully" in success_text

def test_negative_username(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("wrongUser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(6)

    error_text = driver.find_element(By.ID, "error").text
    assert "Your username is invalid!" in error_text

def test_negative_password(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("wrongPassword")
    driver.find_element(By.ID, "submit").click()
    time.sleep(6)

    error_text = driver.find_element(By.ID, "error").text
    assert "Your password is invalid!" in error_text