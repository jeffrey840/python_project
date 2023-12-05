


import re

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

content = process_text('WC_final.txt')



from jinja2 import Environment, FileSystemLoader

# Set up the environment to load the template
env = Environment(loader=FileSystemLoader('templates'))

# Load the template
template = env.get_template('template.html')

# Render the template with the processed content
rendered_html = template.render(content=content)

# Write the rendered HTML to a file
with open('output.html', 'w') as html_file:
    html_file.write(rendered_html)




