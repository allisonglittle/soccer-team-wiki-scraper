Run the following from windows command prompt:
cd soccer-api
py -3 -m venv venv
venv\Scripts\activate
pip install Flask
pip install requests
pip install bs4

set FLASK_APP=soccer_api
flask run

For instructions for other terminals:
https://flask.palletsprojects.com/en/2.1.x/quickstart/
