# Define the range of file numbers
file_numbers = range(1, 6)  # This will create a sequence from 1 to 15

# Open the merged file in write mode
with open('merged-1_5.txt', 'w') as merged_file:
    # Iterate through each file number
    for num in file_numbers:
        # Construct the file name
        file_name = f'text_file_{num}.txt'

        # Open the individual file in read mode
        with open(file_name, 'r') as individual_file:
            # Read the content and write it to the merged file
            merged_file.write(individual_file.read())
            # Optionally, add a newline between files if needed
            merged_file.write('\n')
