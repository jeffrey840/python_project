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

# Specify your driver and browser path here
driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path
# Add the path to your ChromeDriver
chrome_options.add_argument(f'--disable-gpu')
chrome_options.add_argument(f'--no-sandbox')
chrome_options.add_argument(f'--disable-dev-shm-usage')

# Include your specific question numbers here
specific_questions = [10, 11, 20, 21, 22, 23, 29, 54, 60, 180, 200, 202, 207, 210, 211, 215, 238, 244, 263, 301, 356, 389, 394, 398, 420, 470, 515, 517, 519, 520, 524, 528, 531, 538, 541, 554, 557, 565, 567, 608, 609, 612, 614, 622, 629, 631, 638, 639, 644, 645, 650, 654, 656, 657, 664, 698, 711, 717, 720, 721, 728, 737, 741, 742, 743, 748, 750]
def random_sleep(minimum=0.5, maximum=1.5):
    """Introduce a random delay between key presses."""
    time.sleep(random.uniform(minimum, maximum))

def google_search_and_save_links(queries, directory):
    """Perform Google searches and save the first result link to a file."""
    base_url = "https://www.google.com/search?q="
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, "run_2_links_specific_questions.txt")
    browser = webdriver.Chrome( options=chrome_options)
    try:
        with open(file_path, "a") as file:
            for query in queries:
                full_query = f"{query} site:examtopics.com"
                try:
                    browser.get(base_url + full_query)
                    # Adjust your XPath according to the actual page structure
                    xpath_to_select = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a'
                    element = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, xpath_to_select)))
                    link = element.get_attribute("href")
                    file.write(link + "\n")
                except TimeoutException as e:
                    logging.error(f"Timeout error with query: {query} - {str(e)}")
                    file.write(f"Error encountered with query: {query}\n")
                finally:
                    random_sleep(2,6)
    finally:
        browser.quit()


if __name__ == "__main__":
    directory = "CCNA"
    # Generate topics based on the specific question numbers
    topics = [f"Cisco 200-301 question {i} site: examtopics.com" for i in specific_questions]
    google_search_and_save_links(topics, directory)
