""""
Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. 
Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.
"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    URL = input('Enter URL: ') or "http://data.pr4e.org/romeo-full.txt"
    HOST = URL.split('/')[2]
    PORT= 80
    mysock.connect((HOST, PORT))
except:
    print('Invalid URL')
    quit()

CMD = f'GET {URL} HTTP/1.0\r\n\r\n'.encode()
mysock.send(CMD)

body_data = b""
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    body_data = body_data + data
 
mysock.close()
body_data = body_data[body_data.find(b"\r\n\r\n")+4:]

for word in body_data.decode():
   for letter in word:
       count += 1
       if count <= 3000: print(letter)
       
print('Total characters:', count)

