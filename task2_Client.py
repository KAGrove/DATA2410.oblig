import socket

server_ip = "127.0.0.1"
server_port = 12000

# Open a connection to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Send an HTTP GET request
request = "GET /index.html HTTP/1.1\r\nHost: {}\r\n\r\n".format(server_ip)
client_socket.sendall(request.encode())

# Receive the response
response = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

# Parse the response and extract the data
response_str = response.decode()
header, body = response_str.split("\r\n\r\n", 1)
print(header)
print(body)

# Close the connection
client_socket.close()
