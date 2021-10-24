import json
import urllib.request as request

response = request.urlopen("https://jsonplaceholder.typicode.com/users")
body = response.read()
json_response = json.loads(body.decode('utf-8'))

for item in json_response:
    print(item['name'])
