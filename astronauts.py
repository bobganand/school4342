import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url=url)

response_json = response.json()
people = response_json['people']

for person in people:
    print(person['name'])


