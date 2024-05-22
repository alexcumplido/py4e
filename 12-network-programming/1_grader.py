
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    URL = input('Enter URL: ') or "http://data.pr4e.org/intro-short.txt"
    HOST = URL.split('/')[2]
    PORT= 80
    mysock.connect((HOST, PORT))
except:
    print('Invalid URL')
    quit()

CMD = f'GET {URL} HTTP/1.0\r\n\r\n'.encode()
mysock.send(CMD)

response_data = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    response_data = response_data + data
mysock.close()

# Look for the end of the header 
pos = response_data.find(b"\r\n\r\n")
print('Header length', pos)
print(response_data[:pos].decode())