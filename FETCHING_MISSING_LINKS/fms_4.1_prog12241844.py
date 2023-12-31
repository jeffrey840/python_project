import re
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def extract_total_from_filename(filename):
    match = re.search(r'../google/Google Professional Cloud Architect question/links_1-(\d+)', filename)
    return int(match.group(1)) if match else None

def load_and_sort_links(filename):
    with open(filename, 'r') as file:
        links = file.readlines()
    return sorted(links, key=lambda x: int(re.search(r"question-(\d+)", x).group(1)) if re.search(r"question-(\d+)", x) else 0)

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
        if current_match:
            last_number = int(current_match.group(1))
    if total_expected_links and last_number < total_expected_links:
        missing_numbers.extend(range(last_number + 1, total_expected_links + 1))
    return missing_numbers


def google_search_and_save_links(queries, directory):
    # Paths for Brave and ChromeDriver
    driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = brave_path

    # Create a new instance of the Brave browser using the specified options
    browser = webdriver.Chrome(options=chrome_options)

    xpaths = ['//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a',
              '//*[@id="rso"]/div[2]/div/div/div[1]/div/div/span/a']

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory created: {directory}")

    first_number = queries[0].split(" ")[1] if queries else "0"
    last_number = queries[-1].split(" ")[1] if queries else "0"
    file_path = os.path.join(directory, f"missing_links_{first_number}-{last_number}.txt")
    print(f"Creating file at: {file_path}")

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
                    if "professional" in link.lower() and "associate" not in link.lower():
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
    filename = '../google/Google Professional Cloud Architect question/links_1-279'
    total_expected_links = extract_total_from_filename(filename)
    links = load_and_sort_links(filename)
    missing_numbers = find_missing_numbers(links, total_expected_links)

    directory = "_GACE_links_DIR"
    queries = [f"Google Professional Cloud Architect question {i} examtopics" for i in missing_numbers]
    google_search_and_save_links(queries, directory)

def sort_and_save_filtered_links(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()

    # Debugging output to check the number of links read
    print(f"Number of links read: {len(links)}")

    # Filter links and sort based on question number
    pattern = re.compile(r"question-(\d+)")
    filtered_sorted_links = sorted(
        [link.strip() for link in links if "professional" in link.lower() and pattern.search(link)],
        key=lambda x: int(pattern.search(x).group(1))
    )

    # Debugging output to check the number of links after filtering
    print(f"Number of links after filtering: {len(filtered_sorted_links)}")

    with open(file_path, 'w') as file:
        for link in filtered_sorted_links:
            file.write(link + "\n")
    print(f"Filtered and sorted links saved to: {file_path}")


def read_and_process_links(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()

    unique_links = list(dict.fromkeys(links))

    with open(file_path, 'w') as file:
        for link in unique_links:
            file.write(link.strip() + "\n")
    print(f"Processed links (duplicates removed) saved to: {file_path}")

def main():
    filename = '../google/Google Professional Cloud Architect question/links_1-279'
    total_expected_links = extract_total_from_filename(filename)
    links = load_and_sort_links(filename)
    missing_numbers = find_missing_numbers(links, total_expected_links)

    directory = "_GACE_links_DIR"
    queries = [f"Google Professional Cloud Architect question {i} examtopics" for i in missing_numbers]
    google_search_and_save_links(queries, directory)

    file_path = os.path.join(directory, "missing_links_Professional-Professional.txt")
    sort_and_save_filtered_links(file_path)

    file_path = '/Users/jeffreycabrera/PythonProject/FETCHING_MISSING_LINKS/_GACE_links_DIR/missing_links_Professional-Professional.txt'
    if os.path.exists(file_path):
        read_and_process_links(file_path)
    else:
        print("File not found:", file_path)

if __name__ == "__main__":
    main()
