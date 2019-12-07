import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'http://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_error:
        print(f"error is {http_error}")
    except Exception as error:
       print(f"error is {error}") 
    else:
        print('Success!')

