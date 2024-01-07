import json
from pathlib import Path

def extract_parts_from_items_starting_at(file_path, start_at=2):
    file_path = Path(file_path)

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found at {file_path}")

    with open(file_path, 'r') as file:
        data = json.load(file)

    mapping_data = data.get("mapping", {})
    item_keys = list(mapping_data.keys())[start_at:]

    parts_contents = []
    for key in item_keys:
        item = mapping_data[key]
        parts = item.get('message', {}).get('content', {}).get('parts', [])
        parts_contents.append(parts)

    return parts_contents

# Specify the JSON file path
json_file_path = 'biol.json'

# Extract the 'parts' content from items starting at the third item
parts_contents = extract_parts_from_items_starting_at(json_file_path, start_at=2)

# Specify the path for the output text file
output_file_path = 'output.txt'

# Write the output to a text file
with open(output_file_path, 'w') as file:
    for index, parts in enumerate(parts_contents, start=3):
        file.write(f"Item {index} parts: {parts}\n")

print(f"Data has been written to {output_file_path}")
