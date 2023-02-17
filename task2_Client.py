import sys
import socket

if len(sys.argv) < 4:
    print("Usage: client.py server_host server_port filename")
    sys.exit()

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((server_host, server_port))

http_request = "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(filename, server_host)
clientSocket.send(http_request.encode())

response = clientSocket.recv(1024)
while response:
    print(response.decode(), end='')
    response = clientSocket.recv(1024)

clientSocket.close()