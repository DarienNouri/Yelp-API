"""
This script is a Yelp Scraper that scrapes Yelp data given a single URL or a list of URLs.


Imports:
    - argparse: Used to create and handle command-line arguments for the script.
    - os: Provides a way to use operating system dependent functionality.
    - warnings: A module to issue warning messages upon certain conditions.
    - selenium: A web testing library used to automate browser activities.
    - scraper: A module containing the main scraping functionality (scrape_yelp_data function).


Functions:
    - read_url_file(file_path): Reads a file containing a list of URLs and returns them as a list.
    - main(): The main function that parses command-line arguments, initializes the scraper, and performs the scraping.


Usage:
    Run the script using the following command-line arguments:
        --url : A single URL for scraping, mutually exclusive with --file
        --file : A file containing a list of URLs for scraping, mutually exclusive with --url
        --limit: (Optional) Page limit for scraping


Example:
    To scrape a single URL:
    python yelp_scraper.py --url "https://www.yelp.com/biz/business-name"
    
    To scrape a list of URLs from a file:
python yelp_scraper.py --file "urls.txt"

To scrape with a page limit:
python yelp_scraper.py --file "urls.txt" --limit 5
"""


import argparse
import os
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraper import scrape_yelp_data

warnings.filterwarnings('ignore')

def read_url_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def main():
    parser = argparse.ArgumentParser(description="Yelp Scraper")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url', help='A single URL for scraping')
    group.add_argument('--file', help='A file containing a list of URLs for scraping')
    parser.add_argument('--limit', type=int, default=None, help='Page limit for scraping')
    args = parser.parse_args()

    if args.url:
        urlList = [args.url]
    else:
        urlList = read_url_file(args.file)

    scrape_page_limit = args.limit

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": os.getcwd()})
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)
    driver.set_page_load_timeout(10000)

    scraped_data = scrape_yelp_data(driver, urlList, scrape_page_limit)
    driver.quit()

if __name__ == "__main__":
    main()

