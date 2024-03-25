import re


def organize_links_by_questions_and_save(file_path1, file_path2, output_file_path):
    # Compile a regular expression pattern to extract question numbers from links
    # This pattern now specifically looks for lines starting with "Question X:" format to ensure correct extraction
    pattern = re.compile(
        r'Question\s+(\d+):.*?(https://www\.examtopics\.com/discussions/cisco/view/\d+-exam-200-301-topic-1-question-\d+-discussion/)')

    # Initialize a dictionary to store links, keyed by question number
    questions_dict = {}

    # Function to process each line and extract question numbers and links
    def process_line(line):
        match = pattern.search(line)
        if match:
            question_number = int(match.group(1))
            question_link = match.group(2)  # Extract the link directly
            # Store the link using the extracted question number as key
            questions_dict[question_number] = question_link

    # Process the first file
    with open(file_path1, 'r') as file1:
        for line in file1:
            process_line(line)

    # Process the second file
    with open(file_path2, 'r') as file2:
        for line in file2:
            process_line(line)

    # Sort the questions by their numbers
    sorted_questions = sorted(questions_dict.items())

    # Write the sorted links to the output file, formatting each line uniformly
    with open(output_file_path, 'w') as output_file:
        for question, link in sorted_questions:
            output_file.write(f"Question {question}: {link}\n")


# Example paths (replace these with the actual paths to your files)
file_path1 = 'CCNA/organized_links_run1.txt'
file_path2 = 'CCNA/run_2_links_specific_questions.txt'
output_file_path = 'organized_final_output.txt'

# To use the function, uncomment the next line and replace the paths with your actual file paths
organize_links_by_questions_and_save(file_path1, file_path2, output_file_path)
