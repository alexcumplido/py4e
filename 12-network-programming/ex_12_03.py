"""
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
"""
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
count = 0
for line in fhand:
    for letter in line.decode().strip():
       count += 1
       if count <= 3000: print(letter)
       
print('Total characters:', count)