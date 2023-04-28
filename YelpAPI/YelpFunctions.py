# Author: Darien Nouri
# Script: YelpFunctions.py

import os
import platform
import requests
import zipfile
from io import BytesIO
from bs4 import BeautifulSoup
import json

# Function to get restaurant containers from BeautifulSoup object
def get_restaurant_containers(soup):
    try:
        item = soup.select_one('script[data-hypernova-key="yelpfrontend__5385__yelpfrontend__GondolaSearch__dynamic"]').text
        json_string = item.split('<!--')[1].split('-->')[0]
        json_obj = json.loads(json_string)
        restaurant_containers = json_obj['legacyProps']['searchAppProps']['searchPageProps']['mainContentComponentsListProps'][2:-8]
        return restaurant_containers
    except Exception:
        return None

# Function to parse restaurant container and return business info
def parse_restaurant_container(json_obj):
    business_info_container = {}
    params = ['name', 'businessUrl', 'priceRange', 'rating', 'reviewCount', 'neighborhoods']

    try:
        for param in params:
            business_info_container[param] = json_obj['searchResultBusiness'].get(param)

        if not business_info_container['priceRange']:
            return None
        else:
            return business_info_container
    except Exception:
        return None

# Function to get restaurant page data including health rating, address, and reservation information
def get_restaurant_page_data(business_url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    restaurant_url = f'https://www.yelp.com{business_url}'
    response = requests.get(restaurant_url, headers=headers, verify=False).text
    soup = BeautifulSoup(response, 'lxml')

    health_rating = soup.find('span', class_='label-spacing-v2__09f24__RiEXv css-ux5mu6')
    address = soup.find('p', class_='css-qyp8bo')

    page_data_container = {'healthRating': health_rating, 'address': address}

    for i in page_data_container.keys():
        try:
            page_data_container[i] = page_data_container[i].text
        except Exception:
            page_data_container[i] = None

    try:
        soup.find('span', class_='css-1p9ibgf').text
        page_data_container['takesReservations'] = True
    except Exception:
        try:
            soup.find('span', class_='css-qyp8bo').text
            page_data_container['takesReservations'] = False
        except Exception:
            page_data_container['takesReservations'] = None

    return page_data_container
