from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Ensure geckodriver is installed and set in the PATH
GeckoDriverManager().install()

# Initialize the Firefox driver without specifying the executable_path
browser = webdriver.Firefox()

# Navigate to Google
browser.get("https://www.google.com")

# Find the search box, type a query, and submit
search_box = browser.find_element('q')
search_box.send_keys('Hello, Selenium!')
search_box.submit()

# Wait for a bit to see the results
import time
time.sleep(3)

# Close the browser
browser.quit()
