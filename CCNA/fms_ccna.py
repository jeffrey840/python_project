import re

# todo: thsiswiill extracy eth numbers from teh txt file thta i s missing numbers


def find_missing_questions_from_file(file_path):


    # Open and read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Regular expression to match question numbers in URLs and error messages
    question_number_pattern = re.compile(r'question-(\d+)')

    # Extract all question numbers from the lines
    question_numbers = [
        int(match)
        for line in lines
        for match in question_number_pattern.findall(line)
    ]

    if not question_numbers:
        return "No question numbers found."

    # Determine the range of question numbers
    min_question = min(question_numbers)
    max_question = max(question_numbers)

    # Identify missing numbers in the sequence
    full_range = set(range(min_question, max_question + 1))
    missing_questions = list(full_range - set(question_numbers))

    # Return the missing question numbers sorted
    return sorted(missing_questions)


# Specify the path to the text file
file_path = 'CCNA/links_1-100.txt' # Replace with the actual path

# Call the function with the path to your text file
# Note: We won't actually run this line because we don't have a real file path specified
# missing_questions_from_file = find_missing_questions_from_file(file_path)
# print(missing_questions_from_file)

# For demonstration purposes, we'll just show the modified function
# find_missing_questions_from_file
missing_questions_from_file = find_missing_questions_from_file(file_path)
print(missing_questions_from_file)