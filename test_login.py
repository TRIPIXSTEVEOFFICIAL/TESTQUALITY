import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)
    yield driver
    driver.quit()


# Will go to dashboard automatically
def test_valid_login(driver):
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)
    assert "dashboard" in driver.current_url.lower()


# Invalid login will not got to dashboard
@pytest.mark.parametrize("username,password", [
    ("Admin", "wrongpass"),
    ("wronguser", "admin123")
])
def test_invalid_login(driver, username, password):
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)
    assert "dashboard" not in driver.current_url.lower()