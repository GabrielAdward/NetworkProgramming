import socket

wins4win = 3


def serversideGetPlaySocket():
    socketServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    socketServer.bind(("127.0.0.1", 60003))
    socketServer.listen(1)
    (socketClient, addr) = socketServer.accept()
    print(socketClient)
    print("connection from {}".format(addr))
    gameLoop(socketClient)
    socketClient.close()
    socketServer.close()

def clientsideGetPlayerSocket(host):
    socketClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    socketClient.connect((host, 60003))
    gameLoop(socketClient)
    socketClient.close()



def checkRule(myMove, enemyMove):
    enemyScore = 0
    myScore = 0
    if (myMove == "R" and enemyMove == "S") or (myMove == "P" and enemyMove == "R") or (myMove == "S" and enemyMove == "P"):
        myScore += 1
    if (enemyMove == "R" and myMove == "S") or (enemyMove == "P" and enemyMove == "R") or (enemyMove == "S" and myMove == "P"):
        enemyScore += 1

    
def onStart():
    ans = "?"
    while ans not in {"C" , "S"}:
        ans = input("Do you want ti be server (S) or client (C):: ")
        if ans=="S":
            serversideGetPlaySocket()
        elif ans == "C":
            host = input("Enter the server's name or IP: ")
            clientsideGetPlayerSocket(host)
            

def gameLoop(socketClient, myScore, enemyScore):
    numberOfRounds = 0
    while (myScore < 10 or enemyScore<10) and (numberOfRounds<10):
        myMove = input("Make Move:")
        socketClient.sendall(bytearray(myMove, "ascii"))
        print("Sent:" , myMove)
        enemyMove = socketClient.recv(1024).decode("ascii")
        print("received" , enemyMove)
        checkRule(myMove, enemyMove)
        print(myMove, enemyMove)
        numberOfRounds +=1
        


onStart()