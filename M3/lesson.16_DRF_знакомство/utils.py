import requests

# curl -X POST http://127.0.0.1:8000/api/v1/token/ -H 'Content-Type: application/json' -d '{"email": "admin@mail.ru", "password": "1"}'
# url = 'http://127.0.0.1:8000/api/v1/token/'
# payload = {
#     "email": "admin@mail.ru",
#     "password": "1",
# }
#
# response = requests.post(url, json=payload)
# print(response.status_code)
# print(response.json())

# refresh
url = 'http://127.0.0.1:8000/api/v1/token/refresh/'
payload = {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MDU0NTAwNCwiaWF0IjoxNzYwNDU4NjA0LCJqdGkiOiJkYzU4ODc5MzA5ZjE0OTBmODJiODdjMDA0ZjlhMTJlNCIsInVzZXJfaWQiOiIxIn0.IleeMTaSHtcPjCBRzHFTrzAgrGKK9f9KIvjqIF1tpCQ",

}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())

