# /mnt/data/json_file_parts_extraction.py
import json
from pathlib import Path

# Purpose: Read JSON data from a file and extract the 'parts' content from the second item in the 'mapping' section.

def extract_parts_from_second_item(file_path):
    # Ensure the file path is a Path object
    file_path = Path(file_path)

    # Check if the file exists
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found at {file_path}")

    # Read JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Navigate to the 'mapping' key
    mapping_data = data.get("mapping", {})

    # Extract the second item from 'mapping'
    second_item_key = list(mapping_data.keys())[2]  # Get the key of the second item
    second_item = mapping_data[second_item_key]  # Access the second item using its key

    # Extract 'parts' content
    parts = second_item.get('message', {}).get('content', {}).get('parts', [])

    return parts

# Specify the JSON file path
json_file_path = 'biol.json'

# Extract and print the 'parts' content from the second item in 'mapping'
parts_content = extract_parts_from_second_item(json_file_path)
print(parts_content)
