import socket

def serversideGetPlaySocket():
    socketServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    socketServer.bind(("127.0.0.1", 60003))
    socketServer.listen(1)
    (socketClient, addr) = socketServer.accept()
    print(socketClient)
    print("connection from {}".format(addr))
    return socketClient

def clientsideGetPlayerSocket(host):
    socketClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    socketClient.connect((host, 60003))
    return socketClient

def checkTheWinner():
    clientMove = input("Make Move:")
    ServerMove = input("Make Move")
    clientCheck  = clientMove
    serverCheck = ServerMove
    
    if(clientCheck == "R" and serverCheck == "R"):
        sock.sendall(bytearray(clientCheck, "ascii"))
        print("Sent:" , clientCheck)
        
        serverCheck = sock.recv(1024)
        print("received" , serverCheck.decode("ascii"))
        
        sock.sendall(bytearray(serverCheck, "ascii"))
        print("Sent:" , serverCheck)
        
        clientCheck = sock.recv(1024)
        print("received" , clientCheck.decode("ascii"))


ans = "?"
while ans not in {"C" , "S"}:
    ans = input("Do you want ti be server (S) or client (C):: ")
    if ans=="S":
        sock = serversideGetPlaySocket()
    elif ans == "C":
        host = input("Enter the server's name or IP: ")
        sock =clientsideGetPlayerSocket(host)
        

numberOfRounds = 0      
while numberOfRounds < 5:
    checkTheWinner()
    numberOfRounds += 1