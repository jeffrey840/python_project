import requests
import re
from bs4 import BeautifulSoup

def fetch_proxies_from_spys():
    """Fetch proxies from spys.me"""
    response = requests.get("https://spys.me/proxy.txt")
    content = response.text
    return re.findall(r"[0-9]+(?:\.[0-9]+){3}:[0-9]+", content, re.MULTILINE)

def fetch_proxies_from_free_proxy_list():
    """Fetch proxies from free-proxy-list.net"""
    response = requests.get("https://free-proxy-list.net/")
    soup = BeautifulSoup(response.content, 'html.parser')
    proxy_text = soup.find('textarea').get_text()
    return re.findall(r"[0-9]+(?:\.[0-9]+){3}:[0-9]+", proxy_text)

if __name__ == "__main__":
    proxies = fetch_proxies_from_spys() + fetch_proxies_from_free_proxy_list()

    with open("proxies_list.txt", 'w') as file:
        for proxy in proxies:
            print(proxy, file=file)

#             this code fetchecxs from multiple proxies and creates s afile with the proxies
