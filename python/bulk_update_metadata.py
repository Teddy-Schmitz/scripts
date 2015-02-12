#Bulk change server metadata based on server name.

import pyrax
import re

name_filter = "" #can be a regex server name IE datanode*
rax_region = "" #IAD, HKG, SYD, LON, DFW, ORD
rax_username = "" #Your RAX Username
rax_apikey = "" #Your RAX Api Key
dry_run = True # Set to True to test your filter before applying metadata changes.
metadata_tag = "tag" #Can be any string
metadata_value = "" #Value for the tag


pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credentials(rax_username,
                      rax_apikey, region=rax_region)

cs = pyrax.cloudservers

servers = cs.servers.list()

found = []

for obj in servers:
    try:
        if re.match(name_filter, getattr(obj, "name")):
            found.append(obj)
    except AttributeError:
        continue

for server in found:
    print "Modifying server {0}".format(server.name)
    if not dry_run:
        cs.servers.set_meta(server, {metadata_tag:metadata_value})

