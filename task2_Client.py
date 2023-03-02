import sys
import socket

if len(sys.argv) < 4:       # De 4 argumentene som klienten skriver i terminalen
    print("Usage: client.py server_host server_port filename")
    sys.exit()

server_host = sys.argv[1]           # IP-adresse
server_port = int(sys.argv[2])      # Port-adresse
filename = sys.argv[3]              # filnavn

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((server_host, server_port))

http_request = "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(filename, server_host)
# http_request:
# GET /index.html HTTP/1.1
# Host: 127.0.0.1

# Sender http request-en til serveren
clientSocket.send(http_request.encode())

# Mottar headeren
response = clientSocket.recv(1024)

# Mottar (.recv) 1 gang for hver sending (.send)
while response:
    print(response.decode(), end='')
    response = clientSocket.recv(1024)

clientSocket.close()