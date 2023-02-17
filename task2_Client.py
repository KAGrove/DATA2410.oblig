import sys
import socket

if len(sys.argv) < 4:       # We need 4 arguments that the client writes in the terminal
    print("Usage: client.py server_host server_port filename")
    sys.exit()

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((server_host, server_port))

http_request = "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(filename, server_host)
# Will look like this:
# GET /index.html HTTP/1.1
# Host: 127.0.0.1

clientSocket.send(http_request.encode())
# Sends an HTTP request to the server

response = clientSocket.recv(1024)
# Receives the server's response

while response:
    print(response.decode(), end='')
    response = clientSocket.recv(1024)

clientSocket.close()