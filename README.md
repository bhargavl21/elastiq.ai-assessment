## Selenium Search Functionality Test

This project contains a Python script to automate testing of the search functionality on the Selenium Playground Table Search Demo. The script searches for "New York" and verifies the results using assertions within the pytest framework.

### Overview

  * Tests search functionality on Selenium Playground Table Search Demo
  * Uses Python and Selenium WebDriver to interact with the webpage
  * Structured using pytest for simplicity and maintainability

### Prerequisites

**Software Requirements:**

  * Python 3.8 or later
  * Google Chrome browser (latest version)

**Python Modules:**

  * selenium
  * pytest
  * webdriver-manager

### Environment Setup

1.  **Install Python:**

    Ensure Python 3.8 or later is installed. Download it from the official Python website: [https://www.python.org/downloads/](https://www.google.com/url?sa=E&source=gmail&q=https://www.python.org/downloads/)

    Verify installation by running:

    ```bash
    python3 --version
    ```

2.  **Install Google Chrome:**

    Download the latest version of Google Chrome from the official website: [https://www.google.com/chrome/](https://www.google.com/url?sa=E&source=gmail&q=https://www.google.com/chrome/)

3.  **Install Python Modules:**

    Open a terminal and run:

    ```bash
    pip install selenium pytest webdriver-manager
    ```

4.  **Clone or Download the Script:**

    Download the script file `qa_selenium_test.py` to your local machine.

### Running the Test

1.  **Open Terminal or Command Prompt:**

    Navigate to the directory where the script is saved.

2.  **Execute the Script:**

    Run the test with pytest:

    ```bash
    pytest qa_selenium_test.py
    ```

3.  **View Results:**

    The test results will be displayed in the terminal. A success message indicates a passing test; error details will be shown for any failures.

### Notes

  * **Headless Mode:** The script runs in headless mode by default, meaning the browser UI will not be visible. To disable headless mode, remove the `--headless` argument in the `setup_browser` function.
  * **Debugging:** If you encounter issues, ensure all dependencies are installed correctly and that your Chrome browser is up-to-date.
  * **Customization:** You can update the `SEARCH_QUERY`, and `EXPECTED_ENTRIES` constants within the script to test different scenarios.
