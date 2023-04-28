# Yelp Scraper - A Python script to scrape Yelp restaurant data

## Author: Darien Nouri
## Script: scraper.py

## Description

This script allows you to scrape Yelp restaurant data and save it in a CSV file. The script can handle both single URLs and a list of URLs stored in a file. It requires a working internet connection and a properly configured selenium webdriver.

### Dependencies

To run the script, you will need to install the following Python libraries:

- pandas
- BeautifulSoup (bs4)
- selenium

You can install these libraries using pip:

```sh
pip install pandas beautifulsoup4 selenium
```

### Import required libraries and functions

The script imports the following Python libraries and functions:

- os
- time
- pandas as pd
- BeautifulSoup from bs4
- webdriver and Options from selenium
- get_restaurant_containers, parse_restaurant_container, and get_restaurant_page_data from YelpFunctions

### Function: scrape_yelp_data(driver, url_list, scrape_page_limit=None)

Parameters:

- driver (selenium.webdriver): Webdriver used to interact with the website
- url_list (list): List of URLs to scrape
- scrape_page_limit (int, optional): Maximum number of pages to scrape per URL (default: 30)

Returns: DataFrame containing scraped restaurant data

The function performs the following tasks:

- Iterate through the given list of URLs and build a new URL by appending pagination parameters
- Iterate through each page within the specified limit (default 30)
- Retrieve and parse the page source using BeautifulSoup and LXML parser
- Extract restaurant container elements from the parsed HTML
- Iterate through restaurant containers and parse individual container content
- Extend the restaurant data with additional information by fetching data from its Yelp detail page
- Append the parsed data to the dataContainer
- Create a DataFrame with the scraped data and save it as a CSV file
  - If the CSV file doesn't exist, create it with headers
  - If the CSV file exists, append the DataFrame data without headers

## Usage

Run the script using the following command-line arguments:

- --url : A single URL for scraping, mutually exclusive with --file
- --file : A file containing a list of URLs for scraping, mutually exclusive with --url
- --limit: (Optional) Page limit for scraping

### Examples

To scrape a single URL:

```sh
python yelp_scraper.py --url "https://www.yelp.com/biz/business-name"
```

To scrape a list of URLs from a file:

```sh
python yelp_scraper.py --file "urls.txt"
```

To scrape with a page limit:

```sh
python yelp_scraper.py --file "urls.txt" --limit 5
```


## Sample Output (CSV) 



| name          | businessUrl                             | priceRange | rating | reviewCount | neighborhoods     | healthRating   | takesReservations | address                              |
|---------------|-----------------------------------------|------------|--------|-------------|-------------------|----------------|-------------------|--------------------------------------|
| WAU           | /biz/wau-new-york?osq=Restaurants      | $$         | 4.0    | 153         | ['Upper West Side'] | N/A          | True              | 434 Amsterdam Ave New York, NY 10024 |
| The Warren    | /biz/the-warren-new-york?osq=Restaurants | $$         | 4.0    | 277         | ['West Village']    |                | True              | 131 Christopher St New York, NY 10014 |
| Izakaya MEW   | /biz/izakaya-mew-new-york-3?osq=Restaurants | $$      | 4.5    | 2730        | ['Midtown West']    |                | True              | 53 W 35th St New York, NY 10001      |
| Tessa         | /biz/tessa-new-york?osq=Restaurants     | $$$        | 4.0    | 447         | ['Upper West Side'] | N/A          | True              | 349 Amsterdam Ave New York, NY 10024 |
| LumLum        | /biz/lumlum-new-york?osq=Restaurants    | $$         | 4.5    | 214         | ["Hell's Kitchen"]  |                | True              | 404 W 49th New York, NY 10019        |
| Osteria Cotta | /biz/osteria-cotta-new-york?osq=Restaurants | $$      | 4.0    | 1031        | ['Upper West Side'] | A            | True              | 513 Columbus Ave New York, NY 10024  |
| NARO          | /biz/naro-new-york?osq=Restaurants      | $$$$       | 4.5    | 16          | ['Midtown West']    |                | True              | 610 5th Ave New York, NY 10020       |
| Teranga Harlem | /biz/teranga-harlem-new-york?osq=Restaurants | $$     | 4.5    | 131         | ['East Harlem']     | Grade Pending | True              | 1280 5th Ave New York, NY 10029      |
| BCD Tofu House | /biz/bcd-tofu-house-new-york-3?osq=Restaurants | $$    | 4.0    | 2380        | ['Koreatown']       |                | True              | 5W 32nd St New York, NY 10001        |

<br>

## Note
The use of this script is for educational purposes only. Please do not use this script for commercial purposes. The author is not responsible for any misuse of this script. Please use responsibly. 
