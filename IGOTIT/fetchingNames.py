


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


def type_with_delay(element, text, min_delay=0.05, max_delay=0.1):
    """Simulates typing into a web element with random delays between key presses."""
    for character in text:
        element.send_keys(character)
        random_sleep(min_delay, max_delay)


def google_search(names):
    """Perform Google searches and keep the search open."""
    base_url = "https://www.google.com/search?q="

    # Create a new instance of the Brave browser using the specified options
    browser = webdriver.Chrome(options=chrome_options)

    for name in names:
        try:
            # Navigate to Google
            browser.get(base_url)

            # Find the search input box
            search_box = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )

            # Clear it if necessary, then type the name with delays
            search_box.clear()
            type_with_delay(search_box, name + " Texas")
            search_box.send_keys(Keys.ENTER)

            # Introduce a delay to allow time for the user to interact with the search results
            input("Press Enter to continue to the next search...")

        except TimeoutException as e:
            print(f"Error encountered with name: {name}")
            print(e)

    browser.quit()


if __name__ == "__main__":
    names = ["Brenham Banner-Press", "Brownfield News", "The Brownsville Herald", "Brownwood Bulletin", "The Eagle", "Buffalo Express", "Burkburnett Informer Star", "Burnet Bulletin", "Citizens Gazette", "Burleson County Tribune", "The Cameron Herald", "The Canadian Record", "Canton Herald", "Van Zandt News", "The Canyon News", "Carrizo Springs Javelin", "The Panola Watchman", "Hill Country News Weekender", "Celina Record", "The Light and Champion"]



    google_search(names)

