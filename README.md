Title:
DataHarvest: Multimedia Content Collector

Description:
This project involves the creation of an automated web scraping tool using Python and Selenium WebDriver, designed to extract questions, and images from a specific educational forum. The tool navigates to given discussion URLs provided in a text file, selectively parses HTML content to exclude disclaimers and metadata, and downloads any associated images into a designated directory. The text content is organized and written into an output file with references to the downloaded images, mimicking a structured discussion format.

Key Functions:
- Reads a list of URLs from an external text file to ensure flexibility and easy batch processing.
- Implements the use of Selenium with the Brave browser to programmatically interact with web pages, simulating human browsing behavior.
- Employs WebDriverWait and Expected Conditions to ensure robust and dynamic content loading.
- Utilizes Python's `requests` library to handle HTTP requests for downloading images.
- Integrates random delays between requests to mitigate the risk of being blocked by the server and to imitate human-like access patterns.
- Writes extracted content to a text file with a clear, readable format, providing an organized collection of study materials.

Technologies and Libraries Used:
- Language: Python
- Browser Automation: Selenium WebDriver
- HTTP Requests: Requests library
- Delay Implementation: time and random libraries
- Browser: Brave Browser (Chrome can also be used with minor modifications)

This project showcases skills in web scraping, automation, and data organization, highlighting the ability to create a tool that simplifies the process of gathering information.
