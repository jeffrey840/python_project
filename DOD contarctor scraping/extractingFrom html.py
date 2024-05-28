from bs4 import BeautifulSoup

# Sample HTML data
html_content = """

"""

# Create a soup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all 'a' tags since they contain the names
names = [a.get_text() for a in soup.find_all('a')]

# Write the names to a file
with open("B_contractors_list.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Names have been saved to 'contractors_list.txt'")