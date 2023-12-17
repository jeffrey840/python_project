

import re
import json

# Read the text file
with open('your_text_file.txt', 'r') as file:
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

    parsed_questions.append(q_data)

# Convert to JSON
json_data = json.dumps(parsed_questions, indent=4)

# Write JSON data to a file
with open('output_questions.json', 'w') as output_file:
    output_file.write(json_data)

print("Conversion to JSON completed.")



