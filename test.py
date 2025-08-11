import logging
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

# Logging setup, doesn't overwrite existing files
logging.basicConfig(
    filename='test_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Helper functions
def log(level, msg):
    getattr(logging, level.lower())(msg)
    print(f"[{level}] {msg}")

def find_element(driver, locator, by=By.ID, retries=3, delay=1):
    """Find element with retries."""
    for i in range(retries):
        try:
            return driver.find_element(by, locator)
        except NoSuchElementException:
            log("WARNING", f"Element '{locator}' not found (attempt {i+1}/{retries})")
            time.sleep(delay)
    raise NoSuchElementException(f"Could not find element: {locator}")

def wait_for(driver, locator, by=By.ID, timeout=10, visible=True):
    """Wait until element is present or visible."""
    wait = WebDriverWait(driver, timeout)
    condition = EC.visibility_of_element_located if visible else EC.presence_of_element_located
    return wait.until(condition((by, locator)))

def click(driver, locator, by=By.ID, retries=3, delay=1):
    """Click element with retries."""
    for i in range(retries):
        try:
            el = find_element(driver, locator, by)
            el.click()
            log("INFO", f"Clicked on: {locator}")
            return
        except (ElementClickInterceptedException, NoSuchElementException) as e:
            log("WARNING", f"Click failed on '{locator}' (attempt {i+1}/{retries}): {e}")
            time.sleep(delay)
    raise Exception(f"Click failed on: {locator}")

def type_text(driver, locator, text, by=By.ID, retries=3, delay=1):
    """Type text into element with retries."""
    for i in range(retries):
        try:
            el = find_element(driver, locator, by)
            el.clear()
            el.send_keys(text)
            log("INFO", f"Typed '{text}' into: {locator}")
            return
        except NoSuchElementException as e:
            log("WARNING", f"Type failed on '{locator}' (attempt {i+1}/{retries}): {e}")
            time.sleep(delay)
    raise Exception(f"Type failed on: {locator}")

def verify_text(driver, locator, expected, by=By.ID, timeout=10):
    """Verify element text."""
    try:
        el = wait_for(driver, locator, by, timeout)
        actual = el.text
        if actual == expected:
            log("INFO", f"Text matched for '{locator}': '{expected}'")
            print("TEST PASSED")
        else:
            log("ERROR", f"Expected '{expected}' but got '{actual}' for '{locator}'")
            print("TEST FAILED")
    except TimeoutException as e:
        log("ERROR", f"Element '{locator}' not found in time: {e}")
        raise

# Test script
def test_webpage():
    driver = None
    try:
        driver = webdriver.Chrome()
        log("INFO", "Browser started successfully")

        webpage_url = os.path.join(os.path.dirname(__file__), "index.html")
        driver.get(webpage_url)
        log("INFO", f"Navigated to {webpage_url}")

        # Check title
        expected_title = "Test page wrong"
        if driver.title != expected_title:
            log("WARNING", f"Page title mismatch. Expected: '{expected_title}', Got: '{driver.title}'")
        else:
            log("INFO", "Page title is correct")

        # Test steps
        type_text(driver, "name", "Oliver Twist")
        type_text(driver, "email", "oliver@twist.com")
        click(driver, "submit-btn")

        expected_response = "Thank you, Oliver Twist! We'll contact you at oliver@twist.com."
        verify_text(driver, "result", expected_response)

    except Exception as e:
        log("ERROR", f"Test failed with error: {e}")
        print(f"TEST ERROR: {e}")

    finally:
        if driver:
            driver.quit()
            log("INFO", "Browser closed")

if __name__ == "__main__":
    test_webpage()
