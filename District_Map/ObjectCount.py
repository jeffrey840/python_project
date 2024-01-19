
import json

def count_objects(json_path):
    # Load the JSON data from the file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Count the number of objects in the array
    object_count = len(data)

    return object_count


# combined_8_zillow_listings.json = 1550
# combined_8.1_zillow_listings.json = 997

# Example usage with your.json as the path
json_path = 'combined_8.1_zillow_listings.json'
result = count_objects(json_path)

print(f'Total number of objects in the array: {result}')

