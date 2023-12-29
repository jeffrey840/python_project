import json

def sort_questions_by_number(data):
    if "questions" in data and isinstance(data["questions"], list):
        def sort_key(item):
            num = item.get("number")
            return (isinstance(num, int), num)

        sorted_questions = sorted(data["questions"], key=sort_key)
        data["questions"] = sorted_questions
        return data
    else:
        return None

def sort_questions_in_file(input_file, output_file):
    with open(input_file, 'r') as file:
        original_data = json.load(file)
        sorted_data = sort_questions_by_number(original_data)

        if sorted_data:
            with open(output_file, 'w') as output:
                json.dump(sorted_data, output, indent=2)
            print(f"Sorted JSON data written to '{output_file}'")
        else:
            print("Invalid JSON format or missing 'questions' field.")

# Replace 'original_data.json' and 'sorted_data.json' with your file paths
sort_questions_in_file('original_data.json', 'sorted_data.json')
