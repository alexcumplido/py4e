"""
Following Links in Python

The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

http://py4e-data.dr-chuck.net/known_by_Eden.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: B

"""
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = "http://py4e-data.dr-chuck.net/known_by_Eden.html"
html = urllib.request.urlopen(URL, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

input_pos = input('Enter position: ')
input_count = input('Enter count: ')
try:
    position = int(input_pos)
    count = int(input_count)
except:
    print('Some of the inputs were invalid')
    quit()

for number in range(count):
    link_pars = tags[position-1].get('href', None)
    print(link_pars)
    html_pars = urllib.request.urlopen(link_pars, context=ctx).read() 
    soup_pars = BeautifulSoup(html_pars, 'html.parser')
    tags = soup_pars('a')
    

