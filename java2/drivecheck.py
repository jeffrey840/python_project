from selenium import webdriver

# Path to the geckodriver executable
geckodriver_path = "/Users/jeffreycabrera/.wdm/drivers/geckodriver/mac64/v0.33.0/geckodriver"  # You can replace this with any other path from the list

browser = webdriver.Firefox(executable_path=geckodriver_path)
browser.get("https://www.google.com")

# Wait for a few seconds to see the browser
import time
time.sleep(5)

browser.quit()
