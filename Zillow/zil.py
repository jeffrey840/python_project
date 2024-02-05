
from bs4 import BeautifulSoup as soup
import requests
import random

# Headers to mimic a legitimate browser request
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

with requests.session() as i:
    city = input("City To Search In: ") + "/"
    page = 1
    end_page = 10
    urlList = []
    requestList = []

    # Generate URLs for the first 10 pages of listings
    while page <= end_page:
        url = f"https://www.zillow.com/homes/for_sale/{city}{page}_p"
        urlList.append(url)
        page += 1

    # Make requests to each URL
    for url in urlList:
        request = i.get(url, headers=headers)
        requestList.append(request)

# Parse the HTML content of each request to extract listings
rawInfoList = [soup(request.content, "html.parser") for request in requestList]

# Initialize lists to hold the extracted information
addressList, priceList, linkList = [], [], []

# Extract address, price, and link information
for rawInfo in rawInfoList:
    addressList.extend([address.text for address in rawInfo.find_all("address")])
    priceList.extend([price.text for price in rawInfo.find_all(class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW")])
    linkList.extend([link["href"] for link in rawInfo.find_all(class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link", href=True)])

# Request details for each listing to extract HOA fees
requestList2 = [requests.get(link, headers=headers) for link in linkList]
listingInfoList = [soup(request.content, "html.parser") for request in requestList2]

# Extract HOA fee information using the recommended approach
finalHoaList = []

for listingInfo in listingInfoList:
    element_list = listingInfo.find_all(class_="Text-c11n-8-84-3__sc-aiai24-0")
    hoa = [element.text.strip() for element in element_list if "HOA fee" in element.text]
    if hoa:
        finalHoaList.append(hoa[0])  # Assuming the first matching element is the correct one
    else:
        finalHoaList.append("$0 annually HOA fee")

# Print the extracted HOA fees and listing links
print(finalHoaList)
print(linkList)


#     element_list = listingInfo.find_all(class_="Text-c11n-8-84-3__sc-aiai24-0")
#     for price in rawInfo.find_all(class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW"):