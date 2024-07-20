import requests
import json

response = requests.get('https://dummyapi.online/api/movies')
if response.status_code == 200:
    data = json.loads(response.text)

print(data)
print(dir(data))
