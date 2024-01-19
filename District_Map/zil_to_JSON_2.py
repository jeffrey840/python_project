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
    zipcodes = ["77099", "77036", "77074", "77096", "77025", "77054", "77051", "77031", "77071", "77035", "77045", "77048", "77047", "77053", "77489", "77477"]
    combined_data = []

    for zipcode in zipcodes:
        page = 1
        while True:
            data = fetch_zillow_listings_http(zipcode, page)
            if "error" not in data:
                combined_data.extend(data['props'])
                print(f"Data for {zipcode} (Page {page}) added to combined data.")

                if page < data['totalPages']:
                    page += 1
                    time.sleep(5)
                else:
                    break
            else:
                print(f"Error: {data['error']} Status Code: {data['status_code']} for {zipcode} (Page {page})")
                # Log the error to a log file
                with open('error_log.txt', 'a') as log_file:
                    log_file.write(f"Error: {data['error']} Status Code: {data['status_code']} for {zipcode} (Page {page})\n")
                # Continue to the next zipcode and start from the first page
                break  # Exit the loop and move to the next zipcode

    filename = "combined_9_zillow_listings.json"
    save_to_json(combined_data, filename)
    print(f"Combined data saved successfully to {filename}.")

if __name__ == "__main__":
    main()
