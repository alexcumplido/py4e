"""
The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2012386.html (Sum ends with 80)
"""

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = "http://py4e-data.dr-chuck.net/comments_2012386.html"
html = urllib.request.urlopen(URL, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('tr')
count = 0
for t in tags: 
    for number in t.contents[1].contents[0]: 
        if number.isdigit(): count += int(number)
    
print(count)