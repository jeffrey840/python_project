from fake_useragent import UserAgent
import requests
session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5://localhost:9150' #9150 for browser; 9050 for TOR service
session.proxies['https'] = 'socks5://localhost:9150'

# Your IP address appears to be: 185.220.100.253

# {'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

headers = {"User_Agent":UserAgent().random}
print(headers)


