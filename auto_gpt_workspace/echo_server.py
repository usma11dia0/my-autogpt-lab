# Import necessary modules
import socket
import sys

# Define server address and port number
HOST = ''
PORT = 8888

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket object to IP address and port number
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

# Set socket to listen for incoming connections
s.listen(10)
print('Socket now listening')

# Handle incoming connections
while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    
    # Receive data from client
    data = conn.recv(1024)
    reply = 'Server output: ' + data.decode('utf-8')
    
    # Echo data back to client
    conn.sendall(reply.encode('utf-8'))
    
    # Close connection
    conn.close()

s.close()