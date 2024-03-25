import re


def organize_links_by_questions_and_save(file_path1, file_path2, output_file_path):
    # Compile a regular expression pattern to extract question numbers and links
    pattern = re.compile(r'question-(\d+)')

    # Initialize a dictionary to store links or error messages keyed by question number
    questions_dict = {}

    # Function to process each line of the files
    def process_line(line):
        match = pattern.search(line)
        if match:
            question_number = int(match.group(1))
            questions_dict[question_number] = line.strip()

    # Read and process the first file
    with open(file_path1, 'r') as file1:
        for line in file1:
            process_line(line)

    # Read and process the second file
    with open(file_path2, 'r') as file2:
        for line in file2:
            process_line(line)

    # Sort the questions by their numbers and prepare the output
    sorted_questions = sorted(questions_dict.items())

    # Write the sorted list of links or error messages to the specified output file
    with open(output_file_path, 'w') as output_file:
        for question, link in sorted_questions:
            output_file.write(f"Question {question}: {link}\n")


# Example usage of the function
# Note: Replace these file paths with the actual paths to your input and output files
file_path1 = 'links_1-854.txt'
file_path2 = 'links_specific_questions.txt'
output_file_path = 'organized_links.txt'

# Uncomment and run the function with actual file paths to use it
organize_links_by_questions_and_save(file_path1, file_path2, output_file_path)
