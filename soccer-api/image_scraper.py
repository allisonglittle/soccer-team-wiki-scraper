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
    # Trying out multiple urls because some wiki page names differ
    urls = create_url_list(country)
    attr = {'alt': 'Shirt badge/Association crest'}

    for url in urls:
        crest_image = get_image_tag(url, attr)
        if crest_image is not None:
            return crest_image['src']

    return ''


# ----------------------------------------------------------------------
# Function takes in a country and returns possible urls to check
# ----------------------------------------------------------------------
def create_url_list(country):
    url = ['https://en.wikipedia.org/wiki/' + country +'_national_football_team',
           'https://en.wikipedia.org/wiki/' + country + '_national_soccer_team',
           'https://en.wikipedia.org/wiki/' + country + '_men%27s_national_soccer_team',
           'https://en.wikipedia.org/wiki/' + country + '_men%27s_national_football_team']
    return url


# ----------------------------------------------------------------------
# Function takes in a url and image attribute
# ----------------------------------------------------------------------
def get_image_tag(url, attr):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find first image from wikipedia page
    crest_image = soup.find('img', attrs=attr)

    return crest_image


# ----------------------------------------------------------------------
# Function takes in a country name and returns a JSON object containing
#   the image address of the country's soccer team crest.
# ----------------------------------------------------------------------
def get_crest(country):
    img_src = crest_img_scraper(country)
    json_img_src = json.dumps({'crest-source': img_src})
    return json_img_src

