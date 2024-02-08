
import time
import random
import subprocess
from bs4 import BeautifulSoup
import requests

# Function to restart Tor
def restart_tor():
    try:
        print("Restarting Tor...")
        time.sleep(random.randint(10, 15))
        x = subprocess.run("sudo /etc/init.d/tor restart", shell=True, timeout=30)
    except Exception as e:
        print(f"Error restarting Tor: {e}")
        return False
    print("Tor restarted successfully. Waiting...")
    time.sleep(random.randint(25, 30))
    return x.returncode == 0

# Function to scrape data using Tor as a proxy
def scrape_with_tor(url):
    # Set up Tor proxy
    session = requests.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}

    try:
        # Send request
        response = session.get(url)
        time.sleep(10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example scraping logic
        # Replace this with your own scraping logic
        tags = soup.find_all('p', class_="mt-4")
        if tags and 'Your IP made too many requests' in tags[0].text:
            print("CAPTCHA detected. Restarting Tor...")
            if restart_tor():
                print("Tor restarted successfully. Retrying last request...")
                # Retry last request after Tor restart
                return scrape_with_tor(url)
            else:
                print("Failed to restart Tor. Exiting.")
                return None
        else:
            # Process scraped data
            # Replace this with your own processing logic
            return soup
    except Exception as e:
        print(f"Error scraping data: {e}")
        return None


# Example usage
url = 'https://www.zillow.com/homes/for_sale/Houston-tx-77080/2_p'
scraped_data = scrape_with_tor(url)
if scraped_data:
    print(scraped_data)
else:
    print("Failed to scrape data.")
