def split_text_file(file_path, max_word_count):
    # Read the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Count total words
    words = text.split()
    total_words = len(words)
    print(f"Total words in the file: {total_words}")

    # Split the file into chunks
    for i in range(0, total_words, max_word_count):
        chunk = ' '.join(words[i:i + max_word_count])
        with open(f'text_file_{i//max_word_count + 1}.txt', 'w') as new_file:
            new_file.write(chunk)
        print(f"Text file {i//max_word_count + 1} split complete.")

# Usage
split_text_file('govt_ch1.txt', 700)  # Replace 'path_to_your_file.txt' with your file path and 500 with your desired word limit per file
