from selenium import webdriver

# Paths for Brave and ChromeDriver
driver_path = "/Users/jeffreycabrera/.wdm/drivers/chromedriver/mac64/118.0.5993.70/chromedriver-mac-arm64/chromedriver"
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Create a new instance of the Brave browser
browser = webdriver.Chrome()

# Navigate to a webpage
browser.get("https://www.google.com")



