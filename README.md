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
This will execute the test and output the results.


If the assertions fail, pytest will show an error message with the details of the failure.


