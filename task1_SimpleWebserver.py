from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 12000
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

while True:
	print("Ready to serve...")
	try:
		connectionSocket, addr = serverSocket.accept()
		message = connectionSocket.recv(1024).decode()		# message = GET /index.html HTTP/1.1 Host: localhost
		filename = message.split()[1]		# Henter det andre elementet i message
		filename = filename[1:]				# Fjerner skråstrek foran linken som mottas
		f = open(filename)
		outputdata = f.read()				# Det som klienten skal motta (om noen linjer)
		f.close()

		# HTTP response headers - Dette bare sender "header" til klienten, ikke essensielt for overføringen
		header = 'HTTP/1.1 200 OK\r\n'
		header += 'Content-Type: text/html\r\n\r\n'
		connectionSocket.send(header.encode())

		for i in range(0, len(outputdata)):					# Sender alt fra index.html til klienten
			connectionSocket.send(outputdata[i].encode()) 
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()

	except IOError:
		print("Error")
		# Først format som sendes, så html til nettleseren:
		connectionSocket.send("HTTP/2.2 404 Not found\r\n\r\n <html> Feil side!  </html>".encode())
		connectionSocket.close()
		continue

serverSocket.close()
sys.exit()