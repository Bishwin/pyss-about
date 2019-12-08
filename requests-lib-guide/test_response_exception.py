import requests
from requests.exceptions import HTTPError

url = 'https://api.github.com'
invalid_url = 'https://api.github.com/invalid'

def get(url):
    return requests.get(url)


def test_get_with_valid_url_returns_200():
    result = get(url)
    assert result.status_code == 200 


def test_get_with_invalid_url_returns_404():
    result = get(invalid_url)
    assert result.status_code == 404


def test_get_with_invalid_url_raises_HTTPError():
    import pytest
    with pytest.raises(HTTPError):
        result = get(invalid_url)
        result.raise_for_status()


def test_get_json_returns_dictionary():
   result = get(url)
   assert type(result.json()) == dict


