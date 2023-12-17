

import re
import json

# Read the text file
with open('/Users/jeffreycabrera/PythonProject/google/Google Associate Cloud Engineer question/Test_filtered-1-255.txt', 'r') as file:

    text = file.read()

# Split text into individual questions
questions = re.split(r'Actual exam question from Google', text)[1:]

# Process each question and extract details
parsed_questions = []
for i, question in enumerate(questions, start=1):
    q_data = {}
    q_data['Question #'] = i

    # Extracting question number and topic
    q_number_topic = re.search(r'Question #:\s(\d+)\s+Topic #:\s(\d+)', question)
    if q_number_topic:
        q_data['Question #'] = int(q_number_topic.group(1))
        q_data['Topic #'] = int(q_number_topic.group(2))

    # Extracting question content
    q_content = re.search(r'\[All Associate Cloud Engineer Questions\](.*?)Show Suggested Answer', question, re.DOTALL)
    if q_content:
        q_data['Content'] = q_content.group(1).strip()

    # Extracting question options
    options = re.findall(r'[A-Z]\.\s(.*?)(?=[A-Z]\.|Show Suggested Answer)', question, re.DOTALL)
    if options:
        q_data['Options'] = options

    # Extracting image details (if present)
    img_info = re.search(r'\[Image \d+\] saved as (.+\.png)', question)
    if img_info:
        q_data['Image'] = img_info.group(1)

    parsed_questions.append(q_data)

# Convert to JSON
json_data = json.dumps(parsed_questions, indent=4)

# Write JSON data to a file
with open('output_questions.json', 'w') as output_file:
    output_file.write(json_data)

print("Conversion to JSON completed.")

