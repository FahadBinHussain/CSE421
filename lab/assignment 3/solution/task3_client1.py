import socket

def client_program():
    host = socket.gethostname()
    port = 5003 

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        print(f"Connected to Task 3 server on {host}:{port}.")
    except socket.error as e:
        print(f"Connection error: {e}")
        return

    message = input(" -> ") 

    while message.lower().strip() != 'bye':
        try:
            client_socket.send(message.encode()) 
            data = client_socket.recv(1024).decode() 

            if not data:
                print("Server disconnected.")
                break

            print('Received from server: ' + data) 

            message = input(" -> ") 
        except socket.error as e:
            print(f"Socket error during communication: {e}")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    client_socket.close() 
    print("Connection closed.")

if __name__ == '__main__':
    client_program() 