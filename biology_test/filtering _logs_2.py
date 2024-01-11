import json

def all_items_text_to_json(input_text_file, output_json_file):
    """
    Reads all items from a text file, structures them into a JSON object with nested structure, and saves them to a JSON file.

    :param input_text_file: Path to the input text file.
    :param output_json_file: Path to the output JSON file.
    """
    data = {}

    with open(input_text_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith('Item'):
            key, content = line.split(':', 1)
            # Process the content to be a list or another suitable structure
            processed_content = content.strip().strip('[]').replace("'", "").replace("\\n", "\n").strip()
            # Store the content in a nested structure, like a list
            data[key.strip()] = {"content": processed_content}

    with open(output_json_file, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"All items' JSON data with nested structure has been written to {output_json_file}")

# Specify the input text file and output JSON file paths
input_text_file = 'output.txt'
output_json_file = 'all_items_nested_output.json'

# Convert all items' text data to JSON with nested structure and save it
all_items_text_to_json(input_text_file, output_json_file)
