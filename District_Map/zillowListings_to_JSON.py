import requests
import json
import os
import time

def fetch_zillow_listings(zipcode, page=1):
    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
    querystring = {"location": zipcode, "page": page}  # Include page parameter
    headers = {
        "X-RapidAPI-Key": "206a0782demsh5a1d5a242226a6dp1f6b6cjsnf08b18ac4dfa",
        "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data for {zipcode}", "status_code": response.status_code}

def save_to_json(data, filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(dir_path, filename)

    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    zipcodes = ["77091", "77096"]  # Add more zip codes as needed
    for zipcode in zipcodes:
        page = 1
        while True:
            data = fetch_zillow_listings(zipcode, page)
            if "error" not in data:
                filename = f"zillow_listings_{zipcode}_page{page}.json"
                save_to_json(data, filename)
                print(f"Data for {zipcode} (Page {page}) saved successfully.")
                # Check if there are more pages to fetch
                if page < data['totalPages']:
                    page += 1
                    time.sleep(3)  # Wait for 3 seconds before fetching the next page
                else:
                    break  # Exit the loop if all pages are fetched
            else:
                print(f"Error: {data['error']} Status Code: {data['status_code']} for {zipcode} (Page {page})")
                break

if __name__ == "__main__":
    main()
