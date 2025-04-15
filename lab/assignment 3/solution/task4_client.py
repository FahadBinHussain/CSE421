import socket

def client_program():
    host = socket.gethostname()
    port = 5004 

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        print(f"Connected to Task 4 server on {host}:{port}.")
    except socket.error as e:
        print(f"Connection error: {e}")
        return

    while True:
        hours_worked = input("Enter hours worked (or type 'bye' to exit): ")
        if hours_worked.lower().strip() == 'bye':
            break

        try:
            client_socket.send(hours_worked.encode()) 
            data = client_socket.recv(1024).decode() 

            if not data:
                print("Server disconnected.")
                break

            print('Calculated Salary from server: ' + data) 
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