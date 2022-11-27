import socket
import select

port = 60003
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", port))
serverSocket.listen(1)

listOfSockets = [serverSocket]

print("Listening on port {}".format(port))
while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]
    if sock==serverSocket:
        (sock,addr) = serverSocket.accept()
        listOfSockets.append(sock)
        clientIPAdress = sock.getpeername()
        for sock in listOfSockets:
            if sock != serverSocket:
                sock.sendall(bytearray("[{}] has connected to the server".format(clientIPAdress), "ascii"))
    else:
        data = sock.recv(2048)
        if not data:
            for sock in listOfSockets:
                if sock != serverSocket:
                    DisconnectClient = sock.getpeername()
                    sock.sendall(bytearray("[{}] has disconnected".format(DisconnectClient), "ascii"))
            sock.close()
            listOfSockets.remove(sock)
        else:
            DisconnectClient= data.decode("ascii")
            for sock in listOfSockets:
                if sock != serverSocket:
                    clientIPAdress =sock.getpeername()
                    sock.sendall(bytearray("[{}{}] : {}".format(clientIPAdress[0], clientIPAdress[1], DisconnectClient), "ascii"))

