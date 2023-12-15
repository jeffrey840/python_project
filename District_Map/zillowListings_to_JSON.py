# /mnt/data/zillow_listings.py
import requests
import json

def fetch_zillow_listings():
    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
    querystring = {"location":"77080"}
    headers = {
        "X-RapidAPI-Key": "206a0782demsh5a1d5a242226a6dp1f6b6cjsnf08b18ac4dfa",
        "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

import os

def save_to_json(data, filename):
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Create a full path by joining the directory path and filename
    full_path = os.path.join(dir_path, filename)

    # Save the file
    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    data = fetch_zillow_listings()
    if "error" not in data:
        save_to_json(data, 'zillow_listings.json')
        print("Data saved successfully.")
    else:
        print(f"Error: {data['error']} Status Code: {data['status_code']}")

if __name__ == "__main__":
    main()
