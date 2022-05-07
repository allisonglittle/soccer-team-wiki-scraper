# ----------------------------------------------------------------------
# Author: Allison Little
# Program: Soccer Image Scraper
# Version: 1.0.0
# Description: Uses GET Request to obtain image source address of
#   a specified nation's soccer team crest from Wikipedia. Returns a
#   JSON object containing the image address.
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import json


# ----------------------------------------------------------------------
# Function takes in a country name, issues a GET request to Wikipedia
#   and returns the image address of the country's soccer team crest.
# ----------------------------------------------------------------------
def crest_img_scraper(country):
    url = 'https://en.wikipedia.org/wiki/' + country +'_national_football_team'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find first image from wikipedia page
    image = soup.find('img', attrs={'title': 'Shirt badge/Association crest'})
    # attrs={'class':
    #                 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}
    img_src = []
    images = soup.find_all('img')
    for image in images:
        if image['alt'] == 'Shirt badge/Association crest':
            img_src.append(image['src'])
            break
    return img_src


# ----------------------------------------------------------------------
# Function takes in a country name and returns a JSON object containing
#   the image address of the country's soccer team crest.
# ----------------------------------------------------------------------
def get_crest(country):
    img_src = crest_img_scraper(country)
    json_img_src = json.dumps({'crest-source': img_src[0]})
    return json_img_src

print(get_crest('Japan'))
