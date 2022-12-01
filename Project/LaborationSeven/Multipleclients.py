import socket
import select

PORT = 60003
sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockServer.bind(("", PORT))
sockServer.listen(1)

listOfSockets = [sockServer]

print("Listening on port {}".format(PORT))

while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockServer:
        (sockC, addr) = sockServer.accept()
        sock = sockC
        listOfSockets.append(sock)
        for s in listOfSockets:
            if s != sockServer:
                s.send("[{}{}] (connected)".format(addr[0], addr[1]).encode())
    else:
        data = sock.recv(1024)
        if not data:
            print("Client disconnected")
            listOfSockets.remove(sock)
            sock.close()
            for s in listOfSockets:
                if s != sockServer:
                    s.send("[{}{}] (disconnected)".format(addr[0], addr[1]).encode())
        else:
            for s in listOfSockets:
                if s != sockServer:
                    s.send("[{}{}] {}".format(addr[0], addr[1], data.decode()).encode())