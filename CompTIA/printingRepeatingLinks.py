

import re


def analyze_links_for_repeating_numbers(file_path):
    # Compile a regular expression pattern to extract numerical IDs from the URLs
    url_number_pattern = re.compile(r'/view/(\d+)-exam')

    # Initialize a dictionary to count occurrences of each number
    number_occurrences = {}

    # Read and process the file
    with open(file_path, 'r') as file:
        for line in file:
            matches = url_number_pattern.findall(line)
            for number in matches:
                if number in number_occurrences:
                    number_occurrences[number] += 1
                else:
                    number_occurrences[number] = 1

    # Find and print repeating numbers
    repeating_numbers = [number for number, count in number_occurrences.items() if count > 1]

    if repeating_numbers:
        print("Repeating numbers in URLs:", repeating_numbers)
    else:
        print("No repeating numbers found.")


# Example usage
# Note: Replace the placeholder path with the actual path to your text file
file_path = 'CompTIA_Security+/organized_links.txt'

# This function call is for demonstration. Replace the file_path with your actual file path to execute.
analyze_links_for_repeating_numbers(file_path)
