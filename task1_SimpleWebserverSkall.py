# #import socket module
# from socket import *
# import sys # In order to terminate the program
# serverSocket = socket(AF_INET, SOCK_STREAM)
#
# #Prepare a sever socket
# #Write your code here
# serverPort = 12000
# serverSocket.bind(('', serverPort))
# serverSocket.listen(1)
# #End of your code
# while True:
# 	#Establish the connection print('Ready to serve...') connectionSocket, addr =
# 	print("Ready to serve...")
# 	try:
# 		#Write your code here
# 		connectionSocket, addr = serverSocket.accept()
# 		#End of your code
# 		# Write your code here
# 		message = connectionSocket.recv(1024).decode()
# 		# End of your code
# 		filename = message.split()[1]
# 		f = open(filename[1:])
# 		# Write your code here
# 		outputdata = f.read()
# 		f.close()
# 		#End of your code
#
# 		#Send one HTTP header line into socket
# 		#Write your code here
#
# 		#End of your code
#
# 		#Send the content of the requested file to the client
# 		for i in range(0, len(outputdata)):
# 			connectionSocket.send(outputdata[i].encode())
# 		connectionSocket.send("\r\n".encode())
# 		connectionSocket.close()
#
#
# 	except IOError:
# 		#Send response message for file not found
#     	#Write your code here			First \r\n: Terminate HTTP/1.1 200. Second: Terminate the last header line
# 		connectionSocket.send("HTTP/2.2 404 Not found\r\n\r\n".encode())
# 		connectionSocket.close()
# 		continue
#     	#End of your code
#
# 		#Close client socket
#
#         #Write your code here
#
# 		#End of your code
# serverSocket.close()
# sys.exit()#Terminate the program after sending the corresponding data