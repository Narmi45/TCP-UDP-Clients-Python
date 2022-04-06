import socket
# Socket is an IP address coupled with a PORT number
# Example: 127.0.0.1 on Port 80 is a socket 

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Create a socket object
# AF_INET is a parameter that indicates we are using a standard IPv4 address/hostname
# SOCK_DGRAM indicates that this is a UDP client

client.sendto(b"This is being sent via UDP",(target_host, target_port))
# Sending some data as bytes to the target host and port
# Because UDP is a connectionless protocol, there is no call to connect()

data, addr = client.recvfrom(4096)
# Receive both the UDP data and the details of the remote host and port
# 4096 is the bufsize, which is the maximum amount of data to be received at once

print(data.decode())
client.close()
# Printing the received data and then closing the socket

# You can connect to yourself by specifying the target_host to 127.0.0.1
# Then, you can use netcat, nc -ulp 80, to take in the data from this code.
# Note there won't be any response because we haven't set anything to send data 
# to us.
