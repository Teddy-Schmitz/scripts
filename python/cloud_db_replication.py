import json

import requests


username = ""  # Your RAX Cloud username
apikey = ""  # Your API KEY
ddi = ""  # Your DDI
region = "DFW"  # Region of CloudDB
replicant_volume_size = 1  # Replicant data storage size in GB, Min 1.
replicant_flavor = 2  # ID or url of the flavor of the CloudDB (ram).
replicant_name = ""  # Name of the replicant instance.
master_id = ""  # UUID of the master.
datastore = "Percona"  # Datastore name. MySql, Percona, MariaDB
datastore_version = "5.6"  # Datastore version. 5.5, 5.6, 10

header = {"Content-Type": "application/json"}
body = json.dumps(
    {"auth": {"RAX-KSKEY:apiKeyCredentials": {"username": username, "apiKey": apikey}}})
response = requests.post('https://identity.api.rackspacecloud.com/v2.0/tokens',
                         headers=header, data=body, verify=False)
service_catalog = response.json()
auth = service_catalog['access']['token']['id']

header = {"Content-Type": "application/json", "X-Auth-Token": auth}
cloud_url = "https://{0}.databases.api.rackspacecloud.com/v1.0/{1}/".format(region, ddi)
replicant_data = {"instance":
                      {
                          "volume": {
                              "size": replicant_volume_size
                          },
                          "datastore": {
                              "version": datastore_version,
                              "type": datastore
                          },
                          "flavorRef": replicant_flavor,
                          "name": replicant_name,
                          "replica_of": master_id
                      }
}

resp = requests.post(url=cloud_url + "/instances", headers=header, data=json.dumps(replicant_data))

print resp.json()