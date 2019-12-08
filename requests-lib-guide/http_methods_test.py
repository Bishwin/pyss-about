import requests

def http_post():
    return requests.post('https://httpbin.org/post', data={'key': 'value'})


def test_http_post_returns_200():
    response = http_post()
    assert response.status_code == 200

def test_post_returns_content():
    response = http_post()
    print(response.content)
    assert response.content
