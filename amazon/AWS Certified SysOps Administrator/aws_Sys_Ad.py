import os
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up for the Brave browser as you have done previously.
# Assuming you have set up the Brave browser setup code above.
# Paths for Brave
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Create a new instance of the Brave browser
browser = webdriver.Chrome(options=chrome_options)

# Function to download images and return the file name
def download_image(image_url, folder_name, img_index, image_number):
    # Check if the image URL is valid
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

# Create image directory if not exists
images_dir = "downloaded_images3"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Prepare to write to the text file
output_text_file = "filtered_165-385.txt"

# Read links from a text file
with open('links_1-385', 'r') as f:
    links = [line.strip() for line in f]

# Write header content and images to the text file
with open(output_text_file, "w") as textfile:
    for index, link in enumerate(links):
        # Random delay before each request
        random_delay(0.9, 18.0)  # Waits for a random time between 0.5 and 3.0 seconds
        # Navigate to the webpage
        browser.get(link)
        # Wait for the discussion header container to load
        wait = WebDriverWait(browser, 10)
        header_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".discussion-header-container")))

        # Write text content to the file, excluding the metadata and disclaimer
        # Fetch only the question content or other information you want to include before fetching images
        content_elements = header_container.find_elements(By.XPATH, "./*[not(contains(@class, 'discussion-meta-data'))]")

        for elem in content_elements:
            textfile.write(elem.text + "\n")

        # Find and download images, and write their info
        images = header_container.find_elements(By.TAG_NAME, "img")
        for image_number, image in enumerate(images):
            image_url = image.get_attribute('src')
            img_name = download_image(image_url, images_dir, index, image_number)
            if img_name:
                textfile.write(f"[Image {image_number + 1}] saved as {img_name}\n")

        textfile.write("\n\n")  # Extra spacing between discussions

# Reminder to include the brave browser teardown code here
browser.quit()
