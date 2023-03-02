from socket import *
import sys
import _thread as thread

# Dette er omtrent akkurat de samme linjene kode som i den enkle serveren, kun linjen med thread som er ny.
# Men det var viktig å flytte dem inn i ulike funksjoner, slik at handle_requests kan bli kalt hver gang
# en ny klient kobler seg på.

# Tar inn serverSocket fra main (som er en lyttende socket som har bundet ip og port sammen)
def listen_for_clients(connection):
    while True:
        connectionSocket, addr = connection.accept()                    # Her mottar de et nytt port-nummer
        thread.start_new_thread(handle_requests, (connectionSocket,))   # komma -> tuple med ett element


# Tar i mot connectionSocket fra listen_for_clients, som har blitt akseptert og fått nytt port-nummer.
# Inni denne funksjonen mottas melding om filnavn fra klienten, headeren sendes, så sendes resten tilbake til klienten.
def handle_requests(connectionSocket):
    while True:
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            filename = filename[1:]
            f = open(filename)
            outputdata = f.read()
            f.close()

            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: text/html\r\n\r\n'
            connectionSocket.send(header.encode())

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
            break
        except IOError:
            connectionSocket.send("HTTP/2.2 404 Not found\r\n\r\n <html> Feil side!  </html>".encode())
            connectionSocket.close()
            break


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


# Gjør at vi automatisk går inn i main ved oppstart
if __name__ == '__main__':
    main()
