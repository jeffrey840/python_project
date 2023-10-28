import webbrowser

def google_search(queries):
    base_url = "https://www.google.com/search?q={}"
    for query in queries:
        webbrowser.open_new_tab(base_url.format(query))

if __name__ == "__main__":
    topics = ["oracle 1z0-808 question {} exam topics".format(i) for i in range(1, 10)]
    google_search(topics)
