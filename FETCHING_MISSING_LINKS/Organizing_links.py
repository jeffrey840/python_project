# def read_and_process_links(file_path):
#     # Reading the links from the file
#     with open(file_path, 'r') as file:
#         links = file.readlines()
#
#     # Removing duplicates while preserving order
#     unique_links = list(dict.fromkeys(links))
#
#     # Returning the unique links
#     return [link.strip() for link in unique_links]
#
# # Specify the path to your file
# file_path = '/Users/jeffreycabrera/PythonProject/FETCHING_MISSING_LINKS/GACE_missing_links/missing_links-Associate-Associate.txt'
#
# # Reading and processing the links
# processed_links = read_and_process_links(file_path)
#
# # Printing the unique links
# for link in processed_links:
#     print(link)
