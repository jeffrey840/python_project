from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver
driver_path = '/path/to/chromedriver'  # Update this to the path of your ChromeDriver
browser = webdriver.Chrome(executable_path=driver_path)

# Define the queries and the result positions you want to click
searches = {
    "python mdn": 1,       # Click the first result
    "python libraries": 2  # Click the second result
}

for query, position in searches.items():
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the results page to load and display the results.
    time.sleep(2)  # A more robust solution would be to use WebDriverWait

    # Click the desired search result
    results = browser.find_elements(By.CSS_SELECTOR, 'h3')
    results[position - 1].click()

    # Wait a bit before the next search
    time.sleep(2)

# Note: You might want to close the browser once done or keep it open based on your needs.
# browser.quit()
