import requests
import json
url = "https://data.mongodb-api.com/app/data-rgdnx/endpoint/data/beta/action/find"

payload = json.dumps({
    "collection": "users",
    "database": "myFirstDatabase",
    "dataSource": "Cluster0",
    "projection": {
        # "_id": 1
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'YUnOfKoeFKvOy8b4BCFwi3Yu1W6v6OETCS2hPo8LW2je71NqqJfw5V0meElVNlt4'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(len(response.content))
