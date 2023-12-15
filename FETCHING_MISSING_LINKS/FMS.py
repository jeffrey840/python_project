
import re
import os

# Function to extract total links expected from the file name
def extract_total_from_filename(filename):
    match = re.search(r'../google/Google Associate Cloud Engineer question/links_1-(\d+)', filename)
    return int(match.group(1)) if match else None

# Load the links from the file and the total expected links
filename = '../google/Google Associate Cloud Engineer question/links_1-255'
total_expected_links = extract_total_from_filename(filename)

with open(filename, 'r') as file:
    links = file.readlines()

# Sort the list of links to ensure they are in order
links = sorted(links, key=lambda x: int(re.search(r"question-(\d+)", x).group(1)))

# Regular expression to match the question numbers in the links
pattern = re.compile(r"question-(\d+)")

# Find missing question numbers
missing_numbers = []
last_number = 0  # Will hold the last number found to find missing ones up to total_expected_links
for i in range(len(links) - 1):
    current_match = pattern.search(links[i])
    next_match = pattern.search(links[i + 1])
    if current_match and next_match:
        current_number = int(current_match.group(1))
        next_number = int(next_match.group(1))
        if next_number != current_number + 1:
            missing_numbers.extend(range(current_number + 1, next_number))
    last_number = int(current_match.group(1))

# Add the remaining missing numbers if the last link's number is less than total_expected_links
if total_expected_links and last_number < total_expected_links:
    missing_numbers.extend(range(last_number + 1, total_expected_links + 1))

# Print out missing question numbers
print("Missing question numbers:")
for number in missing_numbers:
    print(number)

    # todo:  py file to find the search results from google to extract the links ,
    #  make a filter to return 3 search links from the
    # todo: google search from each missing number, you then want to save the missing links in a seperatae text file,
    #  to do this you want to use google ACE file to create a different saved images and text extraction data


