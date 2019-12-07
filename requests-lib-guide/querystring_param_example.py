import requests

response = requests.get(
        'https://api.github.com/search/repositories',
        params={'q': 'requests+language:python'},
)

json_response = response.json()
repository = json_response['items'][0]
print(f'repo name: {repository["name"]}')
print(f'repo description: {repository["description"]}')

