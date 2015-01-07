import json

import requests


username = ""  # Your RAX Cloud username
apikey = ""  # Your API KEY
ddi = ""  # Your DDI
region = "DFW"  # Region of CloudDB

header = {"Content-Type": "application/json"}
body = json.dumps(
    {"auth": {"RAX-KSKEY:apiKeyCredentials": {"username": username, "apiKey": apikey}}})
response = requests.post('https://identity.api.rackspacecloud.com/v2.0/tokens',
                         headers=header, data=body, verify=False)
service_catalog = response.json()
auth = service_catalog['access']['token']['id']

header = {"Content-Type": "application/json", "X-Auth-Token": auth}
cloud_url = "https://{0}.databases.api.rackspacecloud.com/v1.0/{1}/".format(region, ddi)
resp = requests.get(url=cloud_url + "/flavors", headers=header)

print json.dumps(resp.json(), indent=4)