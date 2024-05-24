""" 
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
"""

#Extracting Data from XML
import ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_default = f"http://py4e-data.dr-chuck.net/comments_2012388.xml"
url = input('Enter location: ') or url_default
try:
    uh = urllib.request.urlopen(url, context=ctx).read()
except:
    print("Non valid location")
    quit()

tree = ET.fromstring(uh)
xlm_tags = tree.findall('comments/comment')
count = 0
sum_count = 0
for item in xlm_tags:
    count += 1
    sum_count += int(item.find('count').text)

print(f"Number of comments: {count}")
print(f"Count computed: {sum_count}")
