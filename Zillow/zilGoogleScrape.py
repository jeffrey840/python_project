from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from fake_useragent import UserAgent
import time

# Generate a random User-Agent
user_agent = UserAgent().random
print(f"Using User-Agent: {user_agent}")

chrome_options = Options()
# Uncomment the next line if you wish to run Chrome in headless mode
# chrome_options.add_argument("--headless")
chrome_options.add_argument(f"user-agent={user_agent}")

# Specify your own path to the ChromeDriver
driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
service = Service(executable_path=driver_path)
browser = webdriver.Chrome(options=chrome_options)

# Your target URL
url = "https://www.zillow.com/homes/for_sale/Houston-tx-77080/2_p/"

try:
    browser.get(url)
    # Adjust the sleep time or use WebDriverWait for more robust waiting
    time.sleep(10)  # Wait for the page to fully load

    # Scroll down to the element
    element = browser.find_element("xpath", "/html/body")
    browser.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(10)  # Wait for scrolling to complete

    # Your target XPath
    xpath = "/html/body"
    element = browser.find_element("xpath", xpath)
    content = element.get_attribute('innerHTML')

    if content:
        print("Content was successfully retrieved. Here's the full content:")
        print(content)  # Print the full content
    else:
        print("No content found at the specified XPath.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    browser.quit()
