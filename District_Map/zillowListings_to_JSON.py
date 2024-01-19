import http.client
import json
import os
import time

def fetch_zillow_listings_http(zipcode, page=1):
    conn = http.client.HTTPSConnection("zillow-com1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "ff711f390emsh45c0fec2c0bc47fp18ac1djsn35accd7f9e03",
        'X-RapidAPI-Host': "zillow-com1.p.rapidapi.com"
    }
    path = f"/propertyExtendedSearch?location={zipcode}&page={page}&status_type=ForSale"

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
    zipcodes = ["77088", "77037", "77088", "77037", "77016", "77050", "77091", "77076", "77093", "77078", "77028", "77026", "77022", "77018", "77092", "77009", "77026", "77020", "77013", "77029"]

    combined_data = []
    for zipcode in zipcodes:
        page = 1
        while True:
            data = fetch_zillow_listings_http(zipcode, page)
            if "error" not in data:
                # Change 'listings' to 'props' here
                combined_data.extend(data['props'])
                print(f"Data for {zipcode} (Page {page}) added to combined data.")

                # Check if there are more pages to fetch
                if page < data['totalPages']:
                    page += 1
                    time.sleep(3)  # Wait for 3 seconds before fetching the next page
                else:
                    break  # Exit the loop if all pages are fetched
            else:
                print(f"Error: {data['error']} Status Code: {data['status_code']} for {zipcode} (Page {page})")
                break
    filename = "combined_2_zillow_listings.json"
    save_to_json(combined_data, filename)
    print(f"Combined data saved successfully to {filename}.")

if __name__ == "__main__":
    main()


# district 1 = 91 & 96
# district 2 88 & 37
