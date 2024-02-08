#
# from selenium import webdriver
# from stem import Signal
# from stem.control import Controller
# import requests
#
# with Controller.from_port(port=9051) as controller:
#     controller.authenticate(password='your_control_password')
#     controller.signal(Signal.NEWNYM)
#
# profile = webdriver.FirefoxProfile()
# profile.set_preference("network.proxy.type", 1)
# # Set proxy to the entry point of your ChainProxy or directly to Tor if not using additional proxies
# profile.set_preference("network.proxy.socks", "localhost")
# profile.set_preference("network.proxy.socks_port", 9050)  # Default Tor port
# browser = webdriver.Firefox(firefox_profile=profile)
# session = requests.session()
# session.proxies = {'http': 'socks5h://localhost:9050',
#                    'https': 'socks5h://localhost:9050'}

# import requests
# import time
# proxies = {
#     'http': 'socks5h://localhost:9050',
#     'https': 'socks5h://localhost:9050'
# }
#
# response = requests.get('https://www.zillow.com/homes/for_sale/Houston-tx-77080/3_p', proxies=proxies)
# time.sleep(20)
#
#
# print(response.raw)

