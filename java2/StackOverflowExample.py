from seleniumbase import Driver
import time
# todo: this test ran correctly
#switch my proxy on  system netroks
# tested it and failed , then i swritvched back to my original proxy
def test_undetected_chrome():
    # Initialize the undetected Chrome driver from SeleniumBase
    driver = Driver(uc=True)

    # Navigate to the website
    driver.get("https://nowsecure.nl/#relax")

    # Wait for a few seconds to observe the result
    time.sleep(6)

    # Check if the text "OH YEAH, you passed!" is present
    if "OH YEAH, you passed!" in driver.page_source:
        print("Successfully bypassed detection!")
    else:
        print("Failed to bypass detection.")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_undetected_chrome()



