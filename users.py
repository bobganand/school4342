import requests

url = "https://dummyjson.com/users"

response = requests.get(url=url)
response_json = response.json()
users = response_json['users']

for user in users:
    if user['age'] == 28:
        print(f"{user['firstName']} {user['lastName']}")
