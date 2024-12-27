# Selenium Test for Table Search Demo using pytest

This Python script uses pytest and Selenium WebDriver to test the Table Search functionality on the Selenium Playground site. The test checks if searching for "New York" returns exactly 5 search results out of a total of 24 entries.
Approach
1.	Setup the WebDriver: The pytest fixture sets up the Selenium WebDriver (using Chrome in this test case). The driver navigates to the Table Search Demo page.
2.	Search for "New York": The test locates the search input box, types "New York" into it, and submits the search query.
3.	Validation: After the results are updated:
o	It checks that exactly 5 rows are returned in the search results.
o	It also verifies that the total number of entries on the page is 24.
4.	Assertions: The test asserts these conditions, and if they fail, pytest will report the error.
Requirements
•	Python 3.x
•	pytest
•	Selenium
•	WebDriver (ChromeDriver for Chrome browser)
Setup Instructions
1.	Install Python Dependencies: If you haven't installed pytest and selenium, you can do so using pip:
“pip install pytest selenium”
2.	Download WebDriver: To interact with the browser, download the ChromeDriver that matches version of Chrome.
3.	Give the Chromedriverpath  in Service.
4.	Running the Tests: To run the test, navigate to the directory where the script is located and run:
                    ‘Pytest qa_selenium_test.py’
This will execute the test and output the results. If the test passes, you should see something like:
 

If the assertions fail, pytest will show an error message with the details of the failure.












# Code:
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
