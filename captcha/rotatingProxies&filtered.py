import time
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

def get_proxies_from_file():
    """Read proxies from the previously generated file"""
    with open("proxies_list.txt", 'r') as file:
        return [line.strip() for line in file]

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
    proxies = get_proxies_from_file()
    for proxy in proxies:
        try:
            browser = set_up_browser_with_proxy(proxy)

            # Test if the proxy works by navigating to Google
            browser.get("https://www.google.com")

            # If the above line doesn't throw an exception, the proxy is likely good
            # You can add your main tasks here

            time.sleep(18)  # Wait for 5 seconds before switching to the next proxy
            browser.quit()

        except Exception as e:
            print(f"Error with proxy {proxy}: {e}")
            if browser:
                browser.quit()

if __name__ == "__main__":
    main()
