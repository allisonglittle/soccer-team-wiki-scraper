# ----------------------------------------------------------------------
# Author: Allison Little
# Program: REST API for national soccer team wiki-scraper
# Version: 1.0.0
# Description: An API that allows users to send a GET Request for
#   national soccer team data and returns JSON objects with the
#   requested data.
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------
from flask import Flask, request
from image_scraper import get_crest


# ----------------------------------------------------------------------
# REST API
# ----------------------------------------------------------------------
app = Flask('Soccer-API')


@app.route('/crest', methods=['GET'])
def return_crest_json():
    args = request.args
    nation = args.get('nation')
    if nation is not None:
        return get_crest(nation)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
