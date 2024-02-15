import re

def parse_questions(input_file_path):
    """
    Parses the input file containing questions and their corresponding images,
    including "../" in the image src path as required.
    """
    questions = []
    with open(input_file_path, 'r') as file:
        question = {}
        for line in file:
            if line.startswith('Actual exam question'):
                if question:
                    questions.append(question)
                    question = {}
                question['text'] = line.strip()
            elif line.strip().startswith('[Image'):
                match = re.search(r'\[Image \d+\] saved as (.+?)\.png', line.strip())
                if match:
                    image_name = match.group(1)
                    # Include "../" in the image src path
                    question.setdefault('images', []).append(f"../CompTIA/downloaded_imagesV2/{image_name}.png")
            else:
                question['text'] += f"\n{line.strip()}"
        if question:  # Add the last question
            questions.append(question)
    return questions


def generate_html(questions, output_file_path):
    """
    Generates an HTML file displaying the questions and their images,
    including "../" in the image src path as required.
    """
    html_content = '<html><head><title>Exam Questions</title></head><body>'
    for question in questions:
        html_content += f"<div><p>{question['text']}</p>"
        for image_path in question.get('images', []):
            # Ensure the "../" prefix is included in the img src attribute
            html_content += f'<img src="{image_path}" style="max-width:100%;height:auto;"><br>'
        html_content += "</div><hr>"
    html_content += '</body></html>'

    with open(output_file_path, 'w') as file:
        file.write(html_content)


# Example usage
input_file_path = 'test_questio.txt'  # Update this path
output_file_path = 'output.html'
questions = parse_questions(input_file_path)
generate_html(questions, output_file_path)
