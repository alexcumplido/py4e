"""
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
"""

#Extracting Data from JSON
import ssl
import urllib.request, urllib.parse, urllib.error
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_default = f"http://py4e-data.dr-chuck.net/comments_2012389.json"
url = input('Enter location: ') or url_default
try:
    uh = urllib.request.urlopen(url, context=ctx).read()
except:
    print("Non valid location")
    quit()

data = json.loads(uh)
count = 0
sum_count = 0
for item in data["comments"]:
    count += 1
    sum_count += int(item["count"])

print(f"Number of comments: {count}")
print(f"Count computed: {sum_count}")