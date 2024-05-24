"""
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first plus_code from the JSON. 
An Open Location Code is a textual identifier that is another form of address based on the location of the address.
"""

# API End Point static subset of the Open Street Map Data
# http://py4e-data.dr-chuck.net/opengeo?


# Import libraries
# setup request code parsing parameters
# Retrieve and parse data
# Get target data

import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_flags = ssl.CERT_NONE
url_service = f"http://py4e-data.dr-chuck.net/opengeo?"

while True:
    address = input('Enter location: ') 
    if len(address) < 1: break

    address = address.strip()
    params = dict()
    params['q'] = address

    url_complete = url_service + urllib.parse.urlencode(params)
    print('Retrieving', url_complete)

    uh = urllib.request.urlopen(url_complete, context=ctx)
    data = uh.read().decode()
    info = json.loads(data)
    plus_code = info["features"][0]['properties']['plus_code']
    print(f"{address} plus code value: {plus_code}")