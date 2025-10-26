import requests
from pprint import pprint


# token
base_url = 'http://127.0.0.1:8000/api/v1'
USER = 'admin@mail.ru'
PASSWORD = '1'

user_payload = {
    'email': USER,
    'password': PASSWORD,
}

token_url = f'{base_url}/token/'

response = requests.post(token_url, json=user_payload)
print(response.status_code)
access_token = response.json().get('access')
refresh_token = response.json().get('refresh')
print(access_token)
print(refresh_token)

# GET запрос /posts/
print('ИЗНАЧАЛЬНЫЙ СПИСОК ПОСТОВ')
response = requests.get(f'{base_url}/posts/')
print(response.status_code)
pprint(response.json())


# POST запрос /posts/
headers = {
    'Authorization': f'Bearer {access_token}',
}

post_payload = {
    'title': 'title111',
    'content': 'content111',
    'rating': 2,
    'tags': [],
    'author': 1,
}
response = requests.post(f'{base_url}/posts/', headers=headers, json=post_payload)
print('ДОБАВЛЕННЫЙ ПОСТ')
if response.status_code == 201:

    pprint(response.json())
else:
    pprint(response.json())


print('НОВЫЙ СПИСОК ПОСТОВ')
response = requests.get(f'{base_url}/posts/')
print(response.status_code)
pprint(response.json())

response = requests.delete(f'{base_url}/posts/14/', headers=headers)
print('УДАЛИЛИ ПОСТ')
print(response.status_code)
# print(response.json())

print('НОВЫЙ СПИСОК ПОСТОВ 2')
response = requests.get(f'{base_url}/posts/')
print(response.status_code)
pprint(response.json())