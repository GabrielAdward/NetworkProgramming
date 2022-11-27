import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(1)
print('Listening on port %s ...' %8080)

while True:
    # Wait for client connections    
    (client_conn, client_adress) = server_socket.accept()
    # Get the client request
    request = client_conn.recv(1024).decode("ascii")
    # Send HTTP response
    response = "HTTP/1.1 200 ok Everything works\n\n<br> Your Browser Sent The Following Request: </br>\n"
    client_conn.sendall(response.encode())
    client_conn.sendall(bytearray("\n", "ASCII") )
    client_conn.sendall (bytearray("<html>\n", "ASCII"))
    client_conn.sendall (bytearray("<pre>", "ASCII"))
    client_conn.sendall (request.encode())
    client_conn.sendall (bytearray("</pre>", "ASCII"))
    client_conn.sendall (bytearray("</html>\n", "ASCII"))
    client_conn.close()
# Close socket
server_socket.close()
