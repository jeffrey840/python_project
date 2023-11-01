import os
from selenium import webdriver

# Path to the geckodriver
geckodriver_path = "/Users/jeffreycabrera/.wdm/drivers/geckodriver/mac64/v0.33.0/geckodriver"

# Add geckodriver path to system PATH
os.environ["PATH"] += os.pathsep + os.path.dirname(geckodriver_path)

# Initialize the Firefox driver
browser = webdriver.Firefox()

# Navigate to Google
browser.get("https://www.google.com")

# Close the browser after a few seconds
import time
time.sleep(5)
browser.quit()
