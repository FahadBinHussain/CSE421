import socket

def client_program():
    host = socket.gethostname()
    port = 5002 

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        print("Connected to Task 2 server.")
    except socket.error as e:
        print(f"Connection error: {e}")
        return

    message = input(" -> ") 

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) 
        data = client_socket.recv(1024).decode() 

        print('Received from server: ' + data) 

        message = input(" -> ") 

    client_socket.close() 
    print("Connection closed.")

if __name__ == '__main__':
    client_program() 