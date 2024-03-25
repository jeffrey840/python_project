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
specific_questions = [170, 182, 183, 194, 200, 201, 207, 210, 211, 212, 220, 224, 225, 226, 227, 228, 240, 241, 253, 264, 265, 277, 284, 285, 332, 351, 352, 353, 361, 366, 368, 378, 379, 380, 381, 383, 385, 386, 388, 389, 391, 392, 394, 397, 404, 405, 408, 409, 411, 414, 425, 430, 431, 432, 437, 438, 445, 446, 449, 450, 452, 465, 468, 474, 486, 487, 491, 497, 498, 499, 502, 503, 506, 509, 515, 520, 524, 525, 528, 529, 532, 533, 539, 540, 545, 546, 547, 550, 557, 560, 562, 567, 570, 576, 578, 582, 594, 595, 596, 601, 611, 618, 619, 620, 621, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 691, 692, 693, 694, 695, 696, 697, 698, 707, 711, 712, 713, 714, 715, 716, 717, 718, 725, 726, 727, 728, 729, 730, 731, 738, 739, 746, 747, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 789, 790, 791, 793, 795, 797, 802, 807, 808, 810, 811, 812, 813, 819, 820, 822, 826, 831, 833, 835, 837, 838, 839, 843, 845, 846]
def random_sleep(minimum=0.5, maximum=1.5):
    """Introduce a random delay between key presses."""
    time.sleep(random.uniform(minimum, maximum))

def google_search_and_save_links(queries, directory):
    """Perform Google searches and save the first result link to a file."""
    base_url = "https://www.google.com/search?q="
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, "links_specific_questions.txt")
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
    directory = "CompTIA_Security+"
    # Generate topics based on the specific question numbers
    topics = [f"sy0-601 question {i}" for i in specific_questions]
    google_search_and_save_links(topics, directory)
