import requests
import re
from bs4 import BeautifulSoup
import concurrent.futures

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

def test_proxy(proxy):
    """Test if a proxy is working by making a request to httpbin"""
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
        if response.status_code == 200:
            return proxy
    except requests.RequestException:
        pass
    return None

proxies = fetch_proxies_from_spys() + fetch_proxies_from_free_proxy_list()

# Use ThreadPoolExecutor to test proxies concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    working_proxies = list(filter(None, executor.map(test_proxy, proxies)))

with open("proxies_list.txt", 'w') as file:
    for proxy in working_proxies:
        print(proxy, file=file)

print(f"Total proxies: {len(proxies)}")
print(f"Working proxies: {len(working_proxies)}")
