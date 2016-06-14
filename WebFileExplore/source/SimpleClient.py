
import socket

s = socket.socket()   # Create a socket object
host = socket.gethostname()    # Get localhost
port = 8888

s.connect((host, port))
print(s.recv(1024))
s.close()
