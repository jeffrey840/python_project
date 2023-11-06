import os
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up for the Brave browser as you have done previously.

def random_delay(min_delay, max_delay):
    time.sleep(random.uniform(min_delay, max_delay))

# Create a new instance of the Brave browser and other setup...

images_dir = "downloaded_images"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

output_text_file = "filtered_1-214.txt"

# Read links from a text file
with open('links_1-214.txt', 'r') as f:
    links = [line.strip() for line in f]

with open(output_text_file, "w") as textfile:
    for index, link in enumerate(links):
        # Random delay before each request
        random_delay(0.5, 3.0)  # Waits for a random time between 0.5 and 3.0 seconds

        browser.get(link)
        wait = WebDriverWait(browser, 10)
        header_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".discussion-header-container")))

        # ... (the rest of your code for fetching and writing content)

# Closing the browser after finishing
browser.quit()
