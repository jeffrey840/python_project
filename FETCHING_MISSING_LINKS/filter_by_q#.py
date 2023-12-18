#
# import re
# import os
#
# file_path = '/Users/jeffreycabrera/PythonProject/FETCHING_MISSING_LINKS/GACE_missing_links/missing_links_Associate-Associate.txt'
#
# # Reading the links from the file
# with open(file_path, 'r') as file:
#     links = file.readlines()
#
# # Filter links and sort based on question number
# pattern = re.compile(r"question-(\d+)")
# filtered_sorted_links = sorted(
#     [link.strip() for link in links if "associate" in link.lower() and "professional" not in link.lower() and pattern.search(link)],
#     key=lambda x: int(pattern.search(x).group(1))
# )
#
# # Printing the sorted links
# for link in filtered_sorted_links:
#     print(link)
