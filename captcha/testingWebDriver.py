import webbrowser
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def google_search_and_click(queries):
    base_url = "https://www.google.com/search?q={}"

    # Ensure geckodriver is installed and set in the PATH
    GeckoDriverManager().install()

    # Initialize the Firefox driver
    browser = webdriver.Firefox()

    for query in queries:
        # Navigate to the search query using Selenium (instead of webbrowser)
        browser.get(base_url.format(query))

        # Wait for the result to be clickable and then click it
        xpath_to_select = '/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/span/a'
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_to_select)))
        element.click()

if __name__ == "__main__":
    topics = ["oracle 1z0-808 question {} exam topics".format(i) for i in range(1, 4)]
    google_search_and_click(topics)
