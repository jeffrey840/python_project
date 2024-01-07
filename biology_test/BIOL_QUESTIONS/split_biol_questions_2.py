# # Read the content from the text file
# with open('text.txt', 'r') as file:
#     content = file.read()
#
# # Split the content into sections using the delimiter "________"
# sections = content.split("________\n")
#
#
# # Define function to save questions to a file
# def save_questions(questions, filename):
#     with open(filename, 'w') as file:
#         # Write "Hello World" at the beginning of the file
#         file.write("Hello World\n\n")
#         # Write the questions to the file
#         for question in questions:
#             file.write(question + "\n\n")
#             file.write("______")
#
#
# # Save the first 4 questions to '1_4_questions.txt'
# save_questions(sections[:4], '1_4_questions.txt')
#
# # Save questions 4-8 to '4_8_questions.txt'
# save_questions(sections[3:7], '4_8_questions.txt')

# ============

# Read the content from the text file
with open('text.txt', 'r') as file:
    content = file.read()

# Split the content into sections using the delimiter "________"
sections = content.split("________\n")


# Define function to save questions to a file
def save_questions(questions, filename):
    with open(filename, 'w') as file:
        # Write "Hello World" at the beginning of the file
        file.write("analyze and answer the following questions and return them as this json format \n\n")
        file.write(" do not explain teh answer just return the answer\n\n")
        file.write('''
    "Item 200 parts": {
        "content": " [complete question]"
    },
    "Item 201 parts": {
        "content": " [answer]"
    },
''')
        # Write the questions to the file
        for question in questions:
            file.write(question + "\n\n")
            file.write("______")
        # Add delimiter after each set of questions
        # file.write("________\n\n")


# Loop through sections in sets of 4 and save to respective files
for i in range(0, len(sections), 4):
    start_index = i
    end_index = min(i + 4, len(sections))
    filename = f'{start_index + 1}_{end_index}_questions.txt'
    save_questions(sections[start_index:end_index], filename)
