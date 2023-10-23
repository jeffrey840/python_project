from bs4 import BeautifulSoup
import requests

def fetch_webpage(url):
    
    response = requests.get(url)
    return response.content

def extract_titles(content):
   
    soup = BeautifulSoup(content, 'html.parser')
    titles = soup.find_all('a', class_='storylink')
    return [title.text for title in titles]

def main():
    
    url = 'https://news.ycombinator.com/'
    content = fetch_webpage(url)
    titles = extract_titles(content)
    
    for index, title in enumerate(titles, 1):
        print(f"{index}. {title}")

if __name__ == "__main__":
    main()




