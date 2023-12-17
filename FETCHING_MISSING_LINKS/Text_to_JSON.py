

import json
import re

def convert_to_json_and_html(input_text_file):
    # Read the text file
    with open(input_text_file, 'r') as file:
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
    output_json_file = 'output_questions.json'
    with open(output_json_file, 'w') as output_file:
        output_file.write(json_data)

    # Create HTML content
    html_content = "<html><head><title>Google Cloud Engineer Questions</title></head><body>"

    # Loop through each question in the parsed JSON data
    for question_data in parsed_questions:
        html_content += "<div>"
        html_content += f"<h2>Question #{question_data['Question #']}</h2>"
        html_content += f"<p>{question_data['Content']}</p>"

        # Display options
        if 'Options' in question_data:
            html_content += "<ul>"
            for option in question_data['Options']:
                html_content += f"<li>{option}</li>"
            html_content += "</ul>"

        # Display image (if available)
        if 'Image' in question_data:
            html_content += f'<img src="{question_data["Image"]}" alt="Question Image"/>'

        html_content += "</div>"

    html_content += "</body></html>"

    # Write HTML content to a file
    output_html_file = 'output_questions.html'
    with open(output_html_file, 'w') as html_file:
        html_file.write(html_content)

    return output_json_file, output_html_file

# Example usage:
json_file_path, html_file_path = convert_to_json_and_html('/Users/jeffreycabrera/PythonProject/google/Google Associate Cloud Engineer question/Test_filtered-1-255.txt')
print(f"Conversion to JSON completed. JSON file created: {json_file_path}")
print(f"HTML generation completed. HTML file created: {html_file_path}")
