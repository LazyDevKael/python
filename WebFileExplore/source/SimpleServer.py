
import socket

s = socket.socket()    # Create a new socket object
host = socket.gethostname()    # Get localhost
port = 8888				# Reverse a port for your service
s.bind((host, port))      # Bind to the port

s.listen(5)
while True:
	c, addr = s.accept()    # Establish connection with client
	print("Got connection from " + str(addr))
	c.send(b"Thank you for connecting...")
	c.close()               # Close the connection


