from bs4 import BeautifulSoup as soup
import requests
import random

# Custom headers including a dynamically generated user-agent
headers = {
    'authority': 'www.zillow.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' + str(random.randint(1, 1000)),
}

# Target URL
url = "https://www.zillow.com/homes/for_sale/Houston-tx-77080/2_p"

# Make the request with custom headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    page_soup = soup(response.text, 'html.parser')
    # Process the page with BeautifulSoup or your scraping logic here
    print("Request successful, process the response...")
else:
    print(f"Failed to fetch the page, status code: {response.status_code}")

# Note: This script makes a direct request and is suitable for static pages.
# For dynamic content or interaction, consider integrating with Selenium or similar.
