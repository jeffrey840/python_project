from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Paths for Brave
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Create a new instance of the Brave browser
browser = webdriver.Chrome(options=chrome_options)

# Array of links
links = [
    "https://www.examtopics.com/discussions/amazon/view/78580-exam-aws-certified-cloud-practitioner-topic-1-question-30/",
    "https://www.examtopics.com/discussions/amazon/view/17544-exam-aws-certified-cloud-practitioner-topic-1-question-31/",
    "https://www.examtopics.com/discussions/amazon/view/15943-exam-aws-certified-cloud-practitioner-topic-1-question-32/",
    "https://www.examtopics.com/discussions/amazon/view/78691-exam-aws-certified-cloud-practitioner-topic-1-question-33/",
    "https://www.examtopics.com/discussions/amazon/view/78423-exam-aws-certified-cloud-practitioner-topic-1-question-34/"
]

for link in links:
    # Navigate to the webpage
    browser.get(link)

    # Wait for the content to load using EC
    wait = WebDriverWait(browser, 10)
    content_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.sec-spacer.pt-50 > div > div:nth-child(5) > div > div.discussion-header-container")))
    content = content_element.text

    print(content)
    print("-------------------------------------------------------------")  # Separator for clarity

# Close the browser
browser.quit()
