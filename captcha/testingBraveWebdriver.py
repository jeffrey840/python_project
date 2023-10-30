import time
from selenium import webdriver


# todo: when you are running the code make sure you have a brave application showing ,
#  else it will open in google chrome

# Paths for Brave and ChromeDriver
driver_path = "/Users/jeffreycabrera/.wdm/drivers/chromedriver/mac64/118.0.5993.70/chromedriver-mac-arm64/chromedriver"
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Create a new instance of the Brave browser using the specified options
browser = webdriver.Chrome(options=chrome_options)

# Navigate to a webpage
browser.get("https://www.google.com")

# Wait for 30 seconds
time.sleep(30)

# Close the browser
browser.quit()

