# /Users/jeffreycabrera/PythonProject/FETCHING_MISSING_LINKS/FMS_V5.py

import re
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Function to extract total links expected from the file name
def extract_total_from_filename(filename):
    match = re.search(r'../google/Google Associate Cloud Engineer question/links_1-(\d+)', filename)
    return int(match.group(1)) if match else None

# Function to load and sort the links from a file
def load_and_sort_links(filename):
    with open(filename, 'r') as file:
        links = file.readlines()
    return sorted(links, key=lambda x: int(re.search(r"question-(\d+)", x).group(1)))

# Function to find missing question numbers
def find_missing_numbers(links, total_expected_links):
    pattern = re.compile(r"question-(\d+)")
    missing_numbers = []
    last_number = 0
    for i in range(len(links) - 1):
        current_match = pattern.search(links[i])
        next_match = pattern.search(links[i + 1])
        if current_match and next_match:
            current_number = int(current_match.group(1))
            next_number = int(next_match.group(1))
            if next_number != current_number + 1:
                missing_numbers.extend(range(current_number + 1, next_number))
        last_number = int(current_match.group(1))
    if total_expected_links and last_number < total_expected_links:
        missing_numbers.extend(range(last_number + 1, total_expected_links + 1))
    return missing_numbers





# Function to perform Google search and save the first three links
def google_search_and_save_links(queries, directory):
    # Paths for Brave and ChromeDriver
    driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = brave_path

    # Create a new instance of the Brave browser using the specified options
    browser = webdriver.Chrome(options=chrome_options)

    # XPaths for the first three search results
    xpaths = [
        '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a',
        '//*[@id="rso"]/div[2]/div/div/div[1]/div/div/span/a',
    ]

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # File to save the links
    first_number = queries[0].split(" ")[1] if queries else "0"
    last_number = queries[-1].split(" ")[1] if queries else "0"
    file_path = os.path.join(directory, f"missing_links_{first_number}-{last_number}.txt")

    with open(file_path, "a") as file:
        for query in queries:
            try:
                # Perform the Google search
                base_url = "https://www.google.com/search?q={}"
                browser.get(base_url.format(query))

                # Retrieve links
                wait = WebDriverWait(browser, 10)
                retrieved_links = []
                for xpath in xpaths:
                    try:
                        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                        link = element.get_attribute("href")
                        retrieved_links.append(link)
                    except TimeoutException:
                        continue

                # Filter and save links
                for link in retrieved_links:
                    if "associate" in link.lower() and "professional" not in link.lower():
                        file.write(link + "\n")
                        print(link)

            except TimeoutException:
                error_message = f"Error encountered with query: {query}\n"
                file.write(error_message)
                print(error_message)
            finally:
                random_sleep()

    browser.quit()

def random_sleep(minimum=3, maximum=7):
    """Introduce a random delay between requests."""
    time.sleep(random.uniform(minimum, maximum))

if __name__ == "__main__":
    filename = '../google/Google Associate Cloud Engineer question/links_1-255'
    total_expected_links = extract_total_from_filename(filename)
    links = load_and_sort_links(filename)
    missing_numbers = find_missing_numbers(links, total_expected_links)

    directory = "GACE_missing_links"
    queries = [f"Google Associate Cloud Engineer question {i} examtopics" for i in missing_numbers]
    google_search_and_save_links(queries, directory)


def sort_and_save_filtered_links(file_path):
    # Reading the links from the file
    with open(file_path, 'r') as file:
        links = file.readlines()

    # Removing duplicates while preserving order
    unique_links = list(dict.fromkeys(links))

    # Filter links and sort based on question number
    pattern = re.compile(r"question-(\d+)")
    filtered_sorted_links = sorted(
        [link.strip() for link in unique_links if "associate" in link.lower() and "professional" not in link.lower() and pattern.search(link)],
        key=lambda x: int(pattern.search(x).group(1))
    )

    # Saving the sorted links back into the file
    with open(file_path, 'w') as file:
        for link in filtered_sorted_links:
            file.write(link + "\n")

def main():
    filename = '../google/Google Associate Cloud Engineer question/links_1-255'
    total_expected_links = extract_total_from_filename(filename)
    links = load_and_sort_links(filename)
    missing_numbers = find_missing_numbers(links, total_expected_links)

    directory = "GACE_missing_links"
    queries = [f"Google Associate Cloud Engineer question {i} examtopics" for i in missing_numbers]
    google_search_and_save_links(queries, directory)

    file_path = os.path.join(directory, "missing_links_Associate-Associate.txt")
    sort_and_save_filtered_links(file_path)

if __name__ == "__main__":
    main()
