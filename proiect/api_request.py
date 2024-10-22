# import requests
# import json
#
# url = "http://127.0.0.1:8004/api/api/"
# payload = json.dumps({
#     "city": "Craciova2",
#     "country": "Romania"
# })
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.request("POST", url, headers=headers, data=payload)
# print(response.json())

import requests

url = "https://v6.exchangerate-api.com/v6/678c9af77fe3877b3a333016/latest/EUR"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()["conversion_rates"]["RON"])
