import os
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up for the Brave browser
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Creating a new instance of the Brave browser
browser = webdriver.Chrome(options=chrome_options)


def download_image(image_url, folder_name, img_index, image_number):
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
    time.sleep(random.uniform(min_delay, max_delay))


images_dir = "downloaded_imagesV3"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

output_text_file = "compTia_sec+QuestionsV3.txt"

# Specify the correct file name containing the links
links_file_path = 'organized_links.txt'  # Replace with the actual path to your text file

# Function to handle both formats of links in the text file
def extract_link(line):
    if line.startswith('Question'):
        return line.split(': ')[1].strip()
    return line.strip()

# Reading links from the text file, handling both formats
with open(links_file_path, 'r') as f:
    links = [extract_link(line) for line in f if line.strip()]

with open(output_text_file, "w") as textfile:
    for index, link in enumerate(links):
        random_delay(0.9, 18.0)  # Random delay before each request
        browser.get(link)
        wait = WebDriverWait(browser, 10)
        try:
            header_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".discussion-header-container")))

            content_elements = header_container.find_elements(By.XPATH, "./*[not(contains(@class, 'discussion-meta-data'))]")
            for elem in content_elements:
                textfile.write(elem.text + "\n")

            images = header_container.find_elements(By.TAG_NAME, "img")
            for image_number, image in enumerate(images):
                image_url = image.get_attribute('src')
                img_name = download_image(image_url, images_dir, index, image_number)
                if img_name:
                    textfile.write(f"[Image {image_number + 1}] saved as {img_name}\n")

            textfile.write("\n\n")
        except Exception as e:
            textfile.write(f"Failed to process {link} due to {e}\n\n")

browser.quit()
