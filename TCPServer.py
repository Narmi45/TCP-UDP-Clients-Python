import socket
import threading
# Threading allows us to run multiple tasks and function calls at the same time
# Accept multiple connections at the same time

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    # Pass in IP and PORT, we want the server to listen on this specific IP and PORT
    
    server.listen(5)
    # Tells the server we want to listen
    # Maximum backlog of connections set to 5
    # (The number of pending connections the queue will hold = 5)

    print(f'[*] Listening on {IP}:{PORT}')
    # This is a F-String in Python, which contains expressions inside braces

    while True:
    # Servers main loop, where it waits for an incoming connection
        client, address = server.accept()
        # When a connection occurs:
        # Store client socket info into client variable
        # Store remote connection details into address variable
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # Address[0] is the IP, Address[1] is the Port
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # Create a new thread object that points to our handle_client function
        # We pass the client socket object as an argument
        client_handler.start()
        # We then start the thread to handle the client connection
        # Main server loop is ready to handle another incoming connection

def handle_client(client_socket):
    with client_socket as sock:
    # Pass the client_socket as a parameter
        request = sock.recv(1024)
        # Store the received data from the client into the request variable
        print(f'[*] Received: {request.decode("utf-8")}')
        # Print the decoded request variable sent by the client
        sock.send(b'ACK')
        # Send ACK as bytes back to the client 

if __name__ == '__main__':
    main()
