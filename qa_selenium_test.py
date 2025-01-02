import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Test configuration
URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
SEARCH_QUERY = "New York"
EXPECTED_ENTRIES = 5

def setup_browser():
    """Set up the browser driver with options."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def test_search_functionality():
    """Test to validate the search functionality on Selenium Playground."""
    # Setup browser
    driver = setup_browser()
    try:
        # Navigate to the URL
        driver.get(URL)

        # Locate the search input box
        search_box = driver.find_element(By.XPATH, "//input[@type='search']")

        # Enter the search query
        search_box.send_keys(SEARCH_QUERY)

        # Wait briefly for the search results to filter (implicit wait recommended)
        driver.implicitly_wait(2)

        # Validate the number of visible rows
        rows = driver.find_elements(By.XPATH, "//table[@id='example']//tr/td[3]")
        visible_rows = [row for row in rows if row.is_displayed()]

        # Assert the expected number of results
        assert len(visible_rows) == EXPECTED_ENTRIES, (
            f"Expected {EXPECTED_ENTRIES} entries but found {len(visible_rows)}."
        )


    finally:
        # Quit the browser
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "--disable-warnings", __file__])

