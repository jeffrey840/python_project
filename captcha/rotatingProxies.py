import time
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

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

def get_proxies():
    proxies = fetch_proxies_from_spys() + fetch_proxies_from_free_proxy_list()
    with open("unfiltered_proxies_list.txt", 'w') as file:
        for proxy in proxies:
            print(proxy, file=file)
    return proxies

def set_up_browser_with_proxy(proxy):
    firefox_options = Options()
    firefox_options.set_preference("network.proxy.type", 1)
    firefox_options.set_preference("network.proxy.http", proxy.split(":")[0])
    firefox_options.set_preference("network.proxy.http_port", int(proxy.split(":")[1]))
    firefox_options.set_preference("network.proxy.ssl", proxy.split(":")[0])
    firefox_options.set_preference("network.proxy.ssl_port", int(proxy.split(":")[1]))

    # Ensure geckodriver is installed and set in the PATH
    GeckoDriverManager().install()

    browser = webdriver.Firefox(options=firefox_options)
    return browser

def main():
    proxies = get_proxies()
    for proxy in proxies:
        try:
            browser = set_up_browser_with_proxy(proxy)

            # Test if the proxy works by navigating to Google
            browser.get("https://www.google.com")

            # If the above line doesn't throw an exception, the proxy is likely good
            # You can add your main tasks here

            time.sleep(5)  # Wait for 5 seconds before switching to the next proxy
            browser.quit()

        except Exception as e:
            print(f"Error with proxy {proxy}: {e}")
            if browser:
                browser.quit()


if __name__ == "__main__":
    main()
