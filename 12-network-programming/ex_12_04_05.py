"""
Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. 
Do not display the paragraph text, only count them. 
Test your program on several small web pages as well as some larger web pages.

Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. 
Remember that recv receives characters (newlines and all), not lines.
"""

from bs4 import BeautifulSoup
import ssl
import urllib.request, urllib.parse, urllib.error
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
try: 
    url = input('Enter - ') or "https://docs.python.org"
    html = urllib.request.urlopen(url, context=ctx).read()
except:
    print('Invalid URL')
    quit()
soup =  BeautifulSoup(html, 'html.parser')
tags = soup('p')
print(f'Number of paragraphs:', len(tags))

