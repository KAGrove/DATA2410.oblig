from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 12000
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

while True:
	print("Ready to serve...")
	try:
		print("try 1")
		connectionSocket, addr = serverSocket.accept()
		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1]		# Henter det andre elementet i message, som er HTTP/GET-request
		print("F:", filename)
		filename = filename[1:]				# Fjerner skråstrek foran linken som mottas
		f = open(filename)
		print("try 2")
		outputdata = f.read()
		f.close()

		# HTTP response headers
		print("Før header")
		header = 'HTTP/1.1 200 OK\r\n'
		header += 'Content-Type: text/html\r\n\r\n'
		connectionSocket.send(header.encode())
		print("etter header")

		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode()) 
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()

	except IOError:
		print("Erroren")
		connectionSocket.send("HTTP/2.2 404 Not found\r\n\r\n".encode())
		connectionSocket.close()
		continue

print("Til slutt")
serverSocket.close()
sys.exit()