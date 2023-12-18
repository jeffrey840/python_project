import re
import json

def parse_questions_from_text(text):
    # Updated pattern with optional image capture
    pattern = re.compile(
        r"Question #:\s*(\d+)\s*"
        r"Topic #:\s*\d+\s*"
        r"\[All Associate Cloud Engineer Questions\]\s*"
        r"(.*?)\s*"
        r"A\.\s*(.*?)\s*"
        r"B\.\s*(.*?)\s*"
        r"C\.\s*(.*?)\s*"
        r"D\.\s*(.*?)\s*"
        r"Show Suggested Answer\s*"
        r"(?:\[Image \d+\] saved as (.*?)\s*\n)?", re.DOTALL)

    questions = []
    for match in pattern.finditer(text):
        question_data = {
            "Question #": match.group(1),
            "Question": match.group(2).strip(),
            "Options": {
                "A": match.group(3).strip(),
                "B": match.group(4).strip(),
                "C": match.group(5).strip(),
                "D": match.group(6).strip(),
            },
            "Image": match.group(7).strip() if match.group(7) else None
        }
        questions.append(question_data)
    return questions


def generate_html(questions):
    html = "<html><head><title>Exam Questions</title></head><body>"
    html += "<h1>Google's Associate Cloud Engineer Exam Questions</h1>"

    for question in questions:
        html += f"<div><h2>Question {question['Question #']}</h2>"
        html += f"<p>{question['Question']}</p>"
        html += "<ul>"
        for option, answer in question['Options'].items():
            html += f"<li>{option}: {answer}</li>"
        html += "</ul>"
        if question.get("Image"):  # Add image tag if image is present
            html += f"<img src='{question['Image']}' alt='Image for Question {question['Question #']}'>"
        html += "</div>"

    html += "</body></html>"
    return html

def main(file_path):
    # Read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Parse the questions
    questions = parse_questions_from_text(text)

    # Convert to JSON
    json_data = json.dumps(questions, indent=4)

    # Generate HTML content
    html_content = generate_html(questions)

    # Write JSON data to a file
    with open('questions.json', 'w') as json_file:
        json_file.write(json_data)

    # Write HTML content to a file
    with open('questions.html', 'w') as html_file:
        html_file.write(html_content)

    print("JSON and HTML files have been created.")

# The file path for your text file
file_path = '/Users/jeffreycabrera/PythonProject/google/Google Associate Cloud Engineer question/Test_filtered-1-255.txt'
main(file_path)
