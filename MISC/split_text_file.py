def split_text_file(file_path, max_word_count):
    # Read the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Text to be added at the beginning of each file
    additional_text = """given teh following text provide several interesting topic to write a paper about, For instance, if you picked the criminal justice system in Texas, you can pick the death penalty in Texas and discuss the pros and cons of it (again using at least 2 outside resources not including your text).\n\n"""

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
split_text_file('govt_ch3.txt', 1400)  # Replace 'path_to_your_file.txt' with your file path and 900 with your desired word limit per file


# For this assignment, you will need to read chapter 3 in your text. What I am looking for in this assignment is for you to become the instructor for chapter 3 and do a power point presentation that would help others learn the important facts about chapter 3 (as well as why this is important). You need to have at least 10 slides (i.e- ten important facts) and a final slide that summarizes the chapter overall.