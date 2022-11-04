import socket

def server_program():
    #create a socket 
    sockS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    #we want to be server so bind to IP address and port number 
    sockS.bind(('127.0.0.1', 60003))
    #amount of client connection request we can handle simultaneously
    sockS.listen(1)
    
    while True:
        print("\nlistening...\n")
        (sockC, addr) = sockS.accept()
        print("connection from {}".format(addr))
        while True:
            data = sockC.recv(1024)
            if not data:
                break
            print ("received:", data.decode("ascii"))
            answer = "thanks for the data!"
            sockC.sendall (bytearray (answer, "ascii"))
            print ("answered:", answer)
        sockC.close()
        print('client {} disconnected'. format (addr) )
        
def client_program():
    #create a socket 
   sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
   
   #Attempt to connect to a certain server
   sock.bind(('127.0.0.1', 60003)) 
   
   message = input("Type your message:")
   
   #send some data to the server 
   sock.sendall(bytearray(message, "ascii"))
   print("sent: ", message)
   
   #expect data: wait until some data is received from server
   data = sock.recv(1024)
   print("received:" , data.decode("ascii"))
   
   #close my socket
   sock.close()
