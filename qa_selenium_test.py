import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# WebDriver Setup
@pytest.fixture(scope="module")
def driver():
    # Initializing Chrome WebDriver
    options = Options()
    options.headless = False  # Set to True if you want to run in headless mode
    #serv_obj = Service("C:\\chromedriver.exe")
    #driver = webdriver.Chrome(service=serv_obj)
    #driver.maximize_window()
    service = Service("C:\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


# Test case searching for newyork in searchbbox
def test_search_for_new_york(driver):
    # Open the page
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    # ExplicitWait for the search input box to be visible
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))

    # Type "New York" into the search box
    search_box.clear()
    search_box.send_keys("New York")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr[role='row']")
    print(len(rows))

    # Validate the number of results (5 entries for "New York")
    assert len(rows) == 5, f"Expected 5 results, but found {len(rows)}"

    # Validate the total number of entries (should be 24 as per the page description)
    total_entries_text = driver.find_element(By.CSS_SELECTOR, "div[role='status']").text
    assert "24" in total_entries_text, f"Expected 24 total entries, but found {total_entries_text}"

    print("Test Passed: 5 search results for 'New York' out of 24 total entries.")