import socket
# Socket is an IP address coupled with a PORT number
# Example: 127.0.0.1 on Port 80 is a socket 

target_host = "localhost"
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Create a socket object
# AF_INET is a parameter that indicates we are using a standard IPv4 address/hostname
# SOCK_STREAM indicates that this is a TCP client

client.connect((target_host, target_port))
# This is a tuple (())
# Command to connect to the client, the parameter is declared above

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# Sending some data as bytes - that is what the b is for
# The HTTP GET request method is used to request a resource from the server. 
# The GET request should only receive data (the server must not change its state). 
# If you want to change data on the server, use POST, PUT, PATCH or DELETE methods.

response = client.recv(4096)
# Receive some data in the form of bytes
# 4096 is the bufsize, which is the maximum amount of data to be received at once

print(response.decode())
client.close()
# Printing the response and then closing the socket

# You can connect to yourself by specifying the target_host to localhost.
# Then, you can use netcat, nc -lvnp 80, to take in the data from this code.
# Note there won't be any response because we haven't set anything to send data 
# to us.
