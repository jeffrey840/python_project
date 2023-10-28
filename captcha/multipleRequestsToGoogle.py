import webbrowser

# List of queries you want to search for
queries = ["what is 9*5", "what is 9*6"]

# Open each query in a new tab
for query in queries:
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(url)

# this creates two tabs on google
# one tab shows what is 9*6 and the other what is 9*5
