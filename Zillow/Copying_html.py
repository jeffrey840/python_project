# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent
# import time
#
# # Generate a random User-Agent
# user_agent = UserAgent().random
# print(f"Using User-Agent: {user_agent}")
#
# chrome_options = Options()
# # Keep the browser window visible
# # chrome_options.add_argument("--headless")
# chrome_options.add_argument(f"user-agent={user_agent}")
#
# # Specify your own path to the ChromeDriver
# driver_path = "C:\\Users\\jeffr\\.cache\\selenium\\chromedriver\\win64\\118.0.5993.70\\chromedriver.exe"
# service = Service(executable_path=driver_path)
# browser = webdriver.Chrome(options=chrome_options)
#
# # Your target URL
# url = "https://www.zillow.com/homes/for_sale/Houston-tx-77080/2_p"
#
# try:
#     browser.get(url)
#     time.sleep(5000)  # Wait for the page to fully load
#     # Scroll down to the elementa
#     element = browser.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/ul/li[9]/div/div/script")
#     browser.execute_script("arguments[0].scrollIntoView();", element)
#     time.sleep(350)  # Wait for scrolling to complete
#
#     xpath = "/html/body"
#     element = browser.find_element("xpath", xpath)
#     content = element.get_attribute('innerHTML')
#
#
#
#     # Fetch the entire HTML of the page
#     html_content = browser.page_source
#
#     # Define the file path where you want to save the HTML content
#     file_path = "zillow_page.html"  # Adjust the path as necessary
#
#
#     # Save the HTML content to a file
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(html_content)
#     print(f"HTML content was successfully saved to: {file_path}")
#
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     browser.quit()
