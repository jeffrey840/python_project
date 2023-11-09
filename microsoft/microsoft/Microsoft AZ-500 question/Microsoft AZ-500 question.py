





# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Paths for Brave and ChromeDriver
# driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
# brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = brave_path

# def random_sleep(minimum=5, maximum=15):
#     time.sleep(random.uniform(minimum, maximum))

# def google_search_and_save_links(queries):
#     base_url = "https://www.google.com/search?q={}"

#     # Create a new instance of the Brave browser using the specified options
#     browser = webdriver.Chrome(options=chrome_options)

#     # File to save the links
#     with open("links_115-460.txt", "a") as file:
#         for query in queries:
#             # Navigate to the search query using Selenium
#             browser.get(base_url.format(query))

#             # Wait for the search results to load and retrieve the link of the first search result
#             xpath_to_select = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a'
#             wait = WebDriverWait(browser, 10)
#             element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_to_select)))

#             # Get the href attribute of the first search result
#             link = element.get_attribute("href")
#             file.write(link + "\n")

#             # Introduce a random delay before the next search
#             random_sleep()

#     browser.quit()

# if __name__ == "__main__":
#     topics = [" AZ-500 question {} examtopics".format(i) for i in range(115, 460)]
#     google_search_and_save_links(topics)


# ============
# ===========


import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Paths for Brave and ChromeDriver
driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

def random_sleep(minimum=3, maximum=7):
    """Introduce a random delay between requests."""
    time.sleep(random.uniform(minimum, maximum))

def google_search_and_save_links(queries):
    """Perform Google searches and save the first result link to a file."""
    base_url = "https://www.google.com/search?q={}"

    # Create a new instance of the Brave browser using the specified options
    browser = webdriver.Chrome(options=chrome_options)

    # File to save the links
    with open("links_115-460.txt", "a") as file:
        for query in queries:
            try:
                # Navigate to the search query using Selenium
                browser.get(base_url.format(query))

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
                random_sleep()

    browser.quit()

if __name__ == "__main__":
    topics = [" AZ-500 question {} examtopics".format(i) for i in range(115, 460)]
    google_search_and_save_links(topics)