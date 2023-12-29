import json
import re

def convert_to_latex(expression):
    # Replace '^' with LaTeX exponentiation
    expression = re.sub(r"\^(.*?) ", r"^{ \1 } ", expression)

    # Replace 'integrate' and other keywords as needed
    # Common Calculus Expressions and their LaTeX equivalents
    expression = expression.replace("integrate ", "\\int ")
    expression = expression.replace("^", "^")  # For exponentiation
    expression = expression.replace("sqrt", "\\sqrt")  # Square root
    expression = expression.replace("sin", "\\sin")  # Sine function
    expression = expression.replace("cos", "\\cos")  # Cosine function
    expression = expression.replace("tan", "\\tan")  # Tangent function
    expression = expression.replace("ln", "\\ln")  # Natural logarithm
    expression = expression.replace("log", "\\log")  # Logarithm
    expression = expression.replace("e^", "e^{")  # Exponential function
    expression = expression.replace("lim", "\\lim")  # Limit
    expression = expression.replace("->", "\\to ")  # Arrow for limits
    expression = expression.replace("pi", "\\pi")  # Pi
    expression = expression.replace("infinity", "\\infty")  # Infinity symbol
    expression = expression.replace("sum", "\\sum")  # Summation
    expression = expression.replace("integral", "\\int")  # Integral
    expression = expression.replace("dx", " \\, dx")  # Differential dx
    expression = expression.replace("dy", " \\, dy")  # Differential dy
    expression = expression.replace("dz", " \\, dz")  # Differential dz
    expression = expression.replace("dtheta", " \\, d\\theta")  # Differential dθ
    expression = expression.replace("'", "^\\prime ")  # Prime notation
    # Add more replacements as needed

    # Closing braces for functions that require them
    expression = expression.replace("{", " {")
    expression = expression.replace("}", "} ")

    return expression

def process_questions(data):
    for question in data.get("questions", []):
        question["question"] = convert_to_latex(question["question"])

        for key, option in question["options"].items():
            question["options"][key] = convert_to_latex(option)

        question["answer"] = convert_to_latex(question["answer"])

    return data

def process_json_file(input_file, output_file):
    with open(input_file, 'r') as file:
        original_data = json.load(file)
        processed_data = process_questions(original_data)

        with open(output_file, 'w') as output:
            json.dump(processed_data, output, indent=2)

# Replace 'original_data.json' and 'processed_data.json' with your file paths
process_json_file('sorted_data.json', 'processed_data.json')
