import re
import os
from jinja2 import Environment, FileSystemLoader

def process_text(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        # Check for question number and options
        if re.match(r'^\d+\.', line):
            line = re.sub(r'(\(\w\))', r'<span class="option">\1</span>', line)
            line = f'<span class="number">{line}</span>'
        # Check for answer letter
        elif re.match(r'^[A-E]\.', line):
            line = f'<span class="answer">{line}</span>'
        processed_lines.append(line)

    return '\n'.join(processed_lines)

def main():
    content = process_text('WC_final.txt')

    # Set up the environment to load the template
    env = Environment(loader=FileSystemLoader('templates'))

    # Load the template
    template = env.get_template('template.html')

    # Render the template with the processed content
    rendered_html = template.render(content=content)

    # Path for the output file
    output_file_path = 'output.html'

    # Check if the file exists and delete it
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # Write the rendered HTML to a new file
    with open(output_file_path, 'w') as html_file:
        html_file.write(rendered_html)

if __name__ == '__main__':
    main()
