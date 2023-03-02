from socket import *
import sys
import _thread as thread


def listen_for_clients(connection):
    while True:
        connectionSocket, addr = connection.accept()
        thread.start_new_thread(handle_requests, (connectionSocket, addr))


def handle_requests(connection):
    while True:
        try:
            message = connection.recv(1024).decode()
            filename = message.split()[1]
            filename = filename[1:]
            f = open(filename)
            outputdata = f.read()
            f.close()

            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: text/html\r\n\r\n'
            connection.send(header.encode())

            for i in range(0, len(outputdata)):
                connection.send(outputdata[i].encode())
            connection.send("\r\n".encode())
            connection.close()
            break
        except IOError:
            connection.send("HTTP/2.2 404 Not found\r\n\r\n <html> Feil side!  </html>".encode())
            connection.close()
            continue


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = 12000
    try:
        serverSocket.bind(('127.0.0.1', serverPort))
    except:
        sys.exit()
    serverSocket.listen(1)
    listen_for_clients(serverSocket)
    serverSocket.close()
    sys.exit()

if __name__ == '__main__':
    main()