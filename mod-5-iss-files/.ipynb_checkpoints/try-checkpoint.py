import json
import requests

url="http://api.open-notify.org/iss-now.json"

response = requests.get("http://api.open-notify.org/iss-now.json")
need_dict=response.json()
print(need_dict)