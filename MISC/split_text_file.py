def split_text_file(file_path, max_word_count):
    # Read the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Text to be added at the beginning of each file
    additional_text = """given the following text provide only important facts that were mentioned in the text. Also return a small keyword in the text so that i can find it later \n\n"""

    # Count total words
    words = text.split()
    total_words = len(words)
    print(f"Total words in the file: {total_words}")

    file_counter = 1

    # Split the file into chunks
    for i in range(0, total_words, max_word_count):
        chunk = ' '.join(words[i:i + max_word_count])

        # Prepend additional text to the chunk
        chunk = additional_text + chunk

        with open(f'text_file_{file_counter}.txt', 'w') as new_file:
            new_file.write(chunk)

        print(f"Text file {file_counter} split complete.")
        file_counter += 1

# Usage
split_text_file('Unit_2/govt_ch7.txt', 900)  # Replace 'path_to_your_file.txt' with your file path and 900 with your desired word limit per file

