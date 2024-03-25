import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# Paths for Brave and ChromeDriver
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

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create a new instance of the Brave browser using the specified options
    browser = webdriver.Chrome(options=chrome_options)

    # File to save the links
    file_path = os.path.join(directory, "links_2-300.txt")
    with open(file_path, "a") as file:
        for query in queries:
            try:
                # Navigate to Google
                browser.get(base_url)

                # Find the search input box
                search_box = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.NAME, "q"))
                )

                # Clear it if necessary, then type the query with delays
                search_box.clear()
                type_with_delay(search_box, query)
                search_box.send_keys(Keys.ENTER)

                # Wait for the search results to load and retrieve the link of the first search result
                xpath_to_select = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a'
                wait = WebDriverWait(browser, 10)
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_to_select)))

                # Get the href attribute of the first search result
                link = element.get_attribute("href")
                file.write(link + "\n")

            except TimeoutException:
                # Log the error and the query that caused it
                error_message = f"Error encountered with query: {query}\n"
                file.write(error_message)
                print(error_message)
            finally:
                # Introduce a random delay before the next search
                random_sleep(11, 14)

    browser.quit()


if __name__ == "__main__":
    directory = "CCNA"
    topics = ["Cisco 200-301 question {} site: examtopics.com".format(i) for i in range(2, 300)]
    google_search_and_save_links(topics, directory)
