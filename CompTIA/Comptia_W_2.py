import os
import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Paths for Brave and ChromeDriver (recommend externalizing these configurations)
driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

def random_sleep(minimum=0.5, maximum=1.5):
    """Introduce a random delay between key presses."""
    time.sleep(random.uniform(minimum, maximum))

def type_with_delay(element, text, min_delay=0.1, max_delay=0.5):
    """Simulates typing into a web element with random delays between key presses."""
    for character in text:
        element.send_keys(character)
        random_sleep(min_delay, max_delay)

def google_search_and_save_links(queries, directory):
    """Perform Google searches and save the first result link to a file."""
    base_url = "https://www.google.com/search?q="
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, "links_00-00.txt")
    browser = None
    try:
        browser = webdriver.Chrome(options=chrome_options)
        with open(file_path, "a") as file:
            for query in queries:
                try:
                    browser.get(base_url)
                    search_box = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.NAME, "q")))
                    search_box.clear()
                    type_with_delay(search_box, query)
                    search_box.send_keys(Keys.ENTER)

                    xpath_to_select = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a'
                    element = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, xpath_to_select)))
                    link = element.get_attribute("href")
                    file.write(link + "\n")
                except TimeoutException as e:
                    logging.error(f"Timeout error with query: {query} - {str(e)}")
                    file.write(f"Error encountered with query: {query}\n")
                except Exception as e:
                    logging.error(f"General error with query: {query} - {str(e)}")
                finally:
                    random_sleep(2, 6)
    finally:
        if browser is not None:
            browser.quit()

if __name__ == "__main__":
    directory = "CompTIA_Security+"
    topics = [f"sy0-601 question {i} site: examtopics.com" for i in range(00, 00)]
    google_search_and_save_links(topics, directory)
