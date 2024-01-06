# /mnt/data/json_file_parts_extraction_modular.py
import json
from pathlib import Path

# Purpose: Read JSON data from a file and extract the 'parts' content from items in the 'mapping' section, starting from a specified item.

def extract_parts_from_items_starting_at(file_path, start_at=2):
    """
    Extracts 'parts' content from items in the 'mapping' section, starting from the specified item.

    :param file_path: Path to the JSON file.
    :param start_at: Index to start extracting items from (default is 2 for the third item).
    :return: A list of 'parts' content for each item starting from 'start_at'.
    """
    file_path = Path(file_path)

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found at {file_path}")

    with open(file_path, 'r') as file:
        data = json.load(file)

    mapping_data = data.get("mapping", {})
    item_keys = list(mapping_data.keys())[start_at:]  # Start from the specified item

    parts_contents = []
    for key in item_keys:
        item = mapping_data[key]
        parts = item.get('message', {}).get('content', {}).get('parts', [])
        parts_contents.append(parts)

    return parts_contents

# Specify the JSON file path
json_file_path = 'biol.json'

# Extract and print the 'parts' content from items starting at the third item
parts_contents = extract_parts_from_items_starting_at(json_file_path, start_at=2)
for index, parts in enumerate(parts_contents, start=3):
    print(f"Item {index} parts:", parts, "\n")
