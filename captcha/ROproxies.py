

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

def get_firefox_with_proxy(ip, port):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", ip)
    profile.set_preference("network.proxy.http_port", port)
    profile.set_preference("network.proxy.ssl", ip)
    profile.set_preference("network.proxy.ssl_port", port)
    profile.update_preferences()

    options = Options()
    options.profile = profile

    return webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

# List of proxies
proxies = [
    {"ip": "157.245.97.60", "port": 80},
    {"ip": "20.210.113.32", "port": 80},
    {"ip": "34.23.45.223", "port": 80},
    {"ip": "20.206.106.192", "port": 80},
    {"ip": "164.163.185.204", "port": 80},
    {"ip": "148.113.8.35", "port": 80},
    {"ip": "20.24.43.214", "port": 80},
    {"ip": "20.111.54.16", "port": 80},
    {"ip": "103.176.108.105", "port": 1414},
    {"ip": "47.254.47.61", "port": 84},
    {"ip": "119.13.103.211", "port": 20201},
    {"ip": "8.208.89.32", "port": 2019},
    {"ip": "91.202.230.219", "port": 8080},
    {"ip": "103.231.78.36", "port": 80},
    {"ip": "103.82.157.105", "port": 8080},
    {"ip": "94.45.74.60", "port": 8080},
    {"ip": "37.46.241.247", "port": 80},
    {"ip": "103.125.28.90", "port": 80},
    {"ip": "103.118.78.194", "port": 80},
    {"ip": "64.189.106.6", "port": 3129},
    {"ip": "149.62.183.209", "port": 3128},
    {"ip": "45.189.116.38", "port": 999},
    {"ip": "93.157.248.108", "port": 88},
    {"ip": "95.66.138.21", "port": 8880},
    {"ip": "123.3.141.167", "port": 80},
    {"ip": "5.189.172.158", "port": 3128},
    {"ip": "43.156.103.153", "port": 3128},
    {"ip": "14.207.84.214", "port": 8080},
    {"ip": "102.132.201.202", "port": 80},
    {"ip": "200.30.138.54", "port": 3128},
    {"ip": "103.179.58.122", "port": 80},
    {"ip": "79.110.197.229", "port": 8081},
    {"ip": "122.155.165.191", "port": 3128},
    {"ip": "45.174.76.22", "port": 999},
    {"ip": "190.239.221.234", "port": 999},
    {"ip": "91.235.220.122", "port": 80},
    {"ip": "143.47.244.130", "port": 3128},
    {"ip": "103.53.77.254", "port": 28080},
    {"ip": "8.208.85.34", "port": 8002},
    {"ip": "202.62.11.200", "port": 8080},
    {"ip": "8.213.128.6", "port": 3128},
]


browser = None  # Initialize the browser variable outside the loop

for proxy in proxies:
    try:
        print(f"Trying proxy {proxy['ip']}:{proxy['port']}...")
        browser = get_firefox_with_proxy(proxy["ip"], proxy["port"])
        browser.get("http://httpbin.org/ip")  # This will show your current IP to verify the proxy
        # ... [rest of your actions]
        browser.quit()
    except Exception as e:
        print(f"Error with proxy {proxy['ip']}:{proxy['port']} - {str(e)}")
        if browser:
            browser.quit()