import os
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Paths for Brave Browser setup
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Creating a new instance of the Brave browser
browser = webdriver.Chrome(options=chrome_options)

def download_image(image_url, folder_name, img_index, image_number):
    # Validates the image URL and downloads the image, saving it with a specific file name
    if not image_url.startswith('http'):
        return None
    img_name = f'image_{img_index}_{image_number}.png'
    img_path = os.path.join(folder_name, img_name)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(img_path, 'wb') as file:
            file.write(response.content)
    return img_name

def random_delay(min_delay, max_delay):
    # Introduces a random delay between requests to simulate human behavior and avoid rate limiting
    time.sleep(random.uniform(min_delay, max_delay))

images_dir = "downloaded_images"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

output_text_file = "compTiaSecurity+.txt"

# Assuming 'links_1-255' is the name of your file containing the URLs
with open('CCNA/', 'r') as f:
    links = [line.strip() for line in f]

with open(output_text_file, "w") as textfile:
    for index, link in enumerate(links):
        random_delay(0.9, 18.0)
        browser.get(link)
        wait = WebDriverWait(browser, 10)
        header_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".discussion-header-container")))

        # Extracts and writes text content, excluding certain elements, to the output file
        content_elements = header_container.find_elements(By.XPATH, "./*[not(contains(@class, 'discussion-meta-data'))]")
        for elem in content_elements:
            textfile.write(elem.text + "\n")

        # Downloads images and writes their filenames to the output file
        images = header_container.find_elements(By.TAG_NAME, "img")
        for image_number, image in enumerate(images):
            image_url = image.get_attribute('src')
            img_name = download_image(image_url, images_dir, index, image_number)
            if img_name:
                textfile.write(f"[Image {image_number + 1}] saved as {img_name}\n")

        textfile.write("\n\n")

browser.quit()
