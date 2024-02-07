from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
driver_path = "path_to_your_chromedriver"
service = Service(executable_path=driver_path)
browser = webdriver.Chrome(options=chrome_options)

# Apply selenium-stealth to make the Selenium-driven Chrome more undetectable
stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# Your target URL
url = "https://www.zillow.com/homes/for_sale/Houston/2_p/"

try:
    browser.get(url)
    # Adjust the sleep time as necessary to ensure the page loads completely
    time.sleep(10)

    # Your target XPath
    xpath = "/html"
    element = browser.find_element("xpath", xpath)
    content = element.get_attribute('innerHTML')

    if content:
        print("Content was successfully retrieved. Here's a snippet:")
        print(content[:200])  # Print a snippet to verify
    else:
        print("No content found at the specified XPath.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    browser.quit()
