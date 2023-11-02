from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

# todo: implement selenium base to this

proxies = [{'ip': '64.189.106.6', 'port': 3129}, {'ip': '149.62.183.209', 'port': 3128}, {'ip': '45.189.116.38', 'port': 999}, {'ip': '5.189.172.158', 'port': 3128}, {'ip': '43.156.103.153', 'port': 3128}, {'ip': '14.207.84.214', 'port': 8080}, {'ip': '200.30.138.54', 'port': 3128}, {'ip': '122.155.165.191', 'port': 3128}, {'ip': '45.174.76.22', 'port': 999}, {'ip': '190.239.221.234', 'port': 999}, {'ip': '143.47.244.130', 'port': 3128}, {'ip': '103.53.77.254', 'port': 28080}]


def download_image(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

import time

def extract_question_data(browser):
    # Extract the question text
    question_text = browser.find_element(By.CSS_SELECTOR, ".question-body .card-text").text

    # Extract the question options
    options_elements = browser.find_elements(By.CSS_SELECTOR, ".question-choices-container .multi-choice-item")
    options = [option.text for option in options_elements]

    # Extract the PNG images associated with the question
    img_elements = browser.find_elements(By.CSS_SELECTOR, ".question-body img.in-exam-image")
    img_urls = [img.get_attribute("src") for img in img_elements]

    # Get a timestamp for unique filenames
    timestamp = int(time.time())

    # Download the images
    saved_images = []
    for index, img_url in enumerate(img_urls):
        filename = f"image_{timestamp}_{index}.png"
        download_image(img_url, filename)
        saved_images.append(f"[Image {index + 1}] saved as {filename}")

    # Save the extracted information to a text file
    with open("output2.txt", "a") as file:  # Use "a" mode to append to the file for multiple pages
        file.write(question_text + "\n")
        file.write(saved_images[0] + "\n") if saved_images else None  # Write the first image
        for option in options:
            file.write(option + "\n")
        for img in saved_images[1:]:  # Write the rest of the images
            file.write(img + "\n")
        file.write("\n")  # Add a newline for separation between questions


from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_firefox_with_proxy(proxy_ip, proxy_port):
    firefox_options = FirefoxOptions()
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("network.proxy.type", 1)
    firefox_profile.set_preference("network.proxy.http", proxy_ip)
    firefox_profile.set_preference("network.proxy.http_port", proxy_port)
    firefox_profile.set_preference("network.proxy.ssl", proxy_ip)
    firefox_profile.set_preference("network.proxy.ssl_port", proxy_port)
    firefox_profile.update_preferences()
    return webdriver.Firefox(firefox_profile=firefox_profile, options=firefox_options, executable_path=GeckoDriverManager().install())

def get_brave_with_proxy(proxy_ip, proxy_port):
    brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = brave_path
    chrome_options.add_argument(f"--proxy-server={proxy_ip}:{proxy_port}")

    return webdriver.Chrome(options=chrome_options)

def google_search_and_click(queries):
    base_url = "https://www.google.com/search?q={}"

    # Ensure geckodriver is installed and set in the PATH
    # GeckoDriverManager().install()

    for query in queries:
        base_url = "https://www.google.com/search?q={}"
        for proxy in proxies:
            try:
                # Initialize the Firefox driver with the current proxy
                browser = get_brave_with_proxy(proxy['ip'], proxy['port'])

                # Navigate to the search query using Selenium
                browser.get(base_url.format(query))

                # Wait for the result to be clickable and then click it
                xpath_to_select = '/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/span/a'
                wait = WebDriverWait(browser, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_to_select)))
                element.click()

                # Wait for the content to load on the new page
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".question-body")))

                # Extract the question data
                extract_question_data(browser)

                # Close the browser and break out of the proxy loop
                browser.quit()
                break
            except Exception as e:
                print(f"Error using proxy {proxy['ip']}:{proxy['port']}. Trying next.")
                browser.quit()
                continue

if __name__ == "__main__":
    topics = ["aws cloud practitioner question {} examtopics".format(i) for i in range(29, 35)]
    google_search_and_click(topics)

# aws cloud practitioner question 3 examtopics
