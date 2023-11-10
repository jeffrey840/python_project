import re

# Load the links from the file
with open('fileLinks.txt', 'r') as file:
    links = file.readlines()

# Sort the list of links to ensure they are in order
links = sorted(links)

# Regular expression to match the question numbers in the links
pattern = re.compile(r"question-(\d+)-discussion")

# Find missing question numbers
missing_numbers = []
for i in range(len(links) - 1):
    current_match = pattern.search(links[i])
    next_match = pattern.search(links[i + 1])
    if current_match and next_match:
        # Extract question numbers from current and next link
        current_number = int(current_match.group(1))
        next_number = int(next_match.group(1))
        # Check if the next question number is not the consecutive number
        if next_number != current_number + 1:
            # Add the range of missing numbers to the list
            missing_numbers.extend(range(current_number + 1, next_number))

# Print out missing question numbers
print("Missing question numbers:")
for number in missing_numbers:
    print(number)
