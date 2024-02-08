# path/to/your_complete_script.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from lxml import etree
import time

def save_html(content, filename="original_page.html"):
    """Saves HTML content to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def prettify_html(input_file="original_page.html", output_file="pretty_page.html"):
    """Loads HTML from a file, prettifies it, and saves to another file."""
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Using lxml to parse and prettify the HTML
        parser = etree.HTMLParser()
        tree = etree.parse(input_file, parser)
        pretty_html = etree.tostring(tree, pretty_print=True, method="html").decode("utf-8")

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(pretty_html)

        print(f"Saved prettified HTML to {output_file}.")
    except Exception as e:
        print(f"An error occurred while prettifying HTML: {e}")


# Generate a random User-Agent
user_agent = UserAgent().random
print(f"Using User-Agent: {user_agent}")

chrome_options = Options()
chrome_options.add_argument(f"user-agent={user_agent}")

# Specify your own path to the ChromeDriver
driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
service = Service(executable_path=driver_path)
browser = webdriver.Chrome(service=service)

# Your target URL
url = "https://www.zillow.com/homes/for_sale/Houston-tx-77080/2_p"

try:
    browser.get(url)
    time.sleep(10)  # Adjust accordingly

    # Save the complete HTML content
    complete_html = browser.page_source
    save_html(complete_html, "original_page.html")

    # Optionally, you can also use BeautifulSoup to prettify and save HTML
    soup = BeautifulSoup(complete_html, "html.parser")
    pretty_html = soup.prettify()
    save_html(pretty_html, "pretty_page.html")

    # Instead, we'll use lxml to prettify the HTML as it provides a better structure for XPath testing
    prettify_html("original_page.html", "pretty_page.html")

finally:
    browser.quit()

# Note: After saving the pretty HTML, you can use the provided lxml methods to test your XPath expressions locally.
