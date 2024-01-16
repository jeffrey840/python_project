


import http.client
import json
import os
import time

def fetch_zillow_listings_http(zipcode, page=1):
    conn = http.client.HTTPSConnection("zillow-com1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "206a0782demsh5a1d5a242226a6dp1f6b6cjsnf08b18ac4dfa",
        'X-RapidAPI-Host': "zillow-com1.p.rapidapi.com"
    }
    path = f"/propertyExtendedSearch?location={zipcode}&page={page}&status_type=ForRent"

    conn.request("GET", path, headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")

    try:
        json_data = json.loads(data)
        return json_data
    except json.JSONDecodeError as e:
        return {"error": f"Failed to decode JSON data: {str(e)}", "status_code": res.status}

def save_to_json(data, filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(dir_path, filename)

    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    zipcodes = ["77091", "77096", "77080"]  # Add more zip codes as needed
    for zipcode in zipcodes:
        page = 1
        while True:
            data = fetch_zillow_listings_http(zipcode, page)
            if "error" not in data:
                filename = f"zillow_listings_{zipcode}_page{page}_forRent.json"
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

