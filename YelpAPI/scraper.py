import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from YelpFunctions import get_restaurant_containers, parse_restaurant_container, get_restaurant_page_data

def scrape_yelp_data(driver, url_list):
    dataContainer = []

    for i in url_list:
        e = 30
        d = -30
        d += e
        start = "&start="
        f = i + "{}{}".format(start, d)
        driver.get(f)

        for k in range(30):
            url = driver.current_url
            driver.get(url)
            time.sleep(4)

            try:
                html = driver.page_source
            except:
                print("ISSUE WITH PAGE SOURCE")
                break

            soup = BeautifulSoup(html, 'lxml')
            restaurantContainers = get_restaurant_containers(soup)

            if restaurantContainers is None:
                print("page: {} | total scraped {}".format(k, len(dataContainer)+1))
                break

            for container in restaurantContainers:
                parsed = parse_restaurant_container(container)

                if parsed is not None:
                    print(parsed['name'])
                    restaurantPagePayload = get_restaurant_page_data(parsed['businessUrl'])
                    parsed.update(restaurantPagePayload)
                    dataContainer.append(parsed)

            print("page: {} | total scraped {}".format(k, len(dataContainer)))

            try:
                df = pd.DataFrame(dataContainer, columns=['name', 'businessUrl', 'priceRange', 'rating', 'reviewCount',
                                                         'neighborhoods', 'healthRating',
                                                         'takesReservations', 'address'])

                savename = os.path.join(os.getcwd(), 'yelpData' + '.csv')
                if not os.path.isfile(savename):
                    df.to_csv(savename, header=df.columns, index=False)
                else:
                    df.to_csv(savename, mode='a', header=False, index=False)

            except:
                pass

    return pd.DataFrame(dataContainer)


