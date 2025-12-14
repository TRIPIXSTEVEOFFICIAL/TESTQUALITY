import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()

def test_no_such_element(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(2)
    row2 = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    assert len(row2) >= 2

def test_element_not_interactable(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(2)
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    input2 = inputs[1]
    input2.clear()
    input2.send_keys("Sushi")
    save_buttons = driver.find_elements(By.XPATH, "//button[text()='Save']")
    save_buttons[-1].click()
    input2 = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")[1]
    assert input2.get_attribute("value") == "Sushi"

def test_invalid_element_state(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    driver.find_element(By.XPATH, "//button[text()='Edit']").click()
    input1 = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    input1.clear()
    input1.send_keys("Burger")
    assert input1.get_attribute("value") == "Burger"

def test_stale_element_reference(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    instructions = driver.find_element(By.ID, "instructions")
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(1)
    try:
        instructions.is_displayed()
        stale = False
    except:
        stale = True
    assert stale is True

def test_timeout_exception(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(2)
    row2 = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    assert len(row2) < 2