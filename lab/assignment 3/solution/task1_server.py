import socket

def server_program():
    
    host = socket.gethostname()
    port = 5001  

    server_socket = socket.socket()  
    
    server_socket.bind((host, port))  

    
    server_socket.listen(1) 
    print(f"Server listening on {host}:{port}")

    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))

    
    data = conn.recv(1024).decode()
    if not data:
        
        print("No data received. Connection might have closed.")
    else:
        print("Received from client: " + str(data))

    conn.close()  
    print("Connection closed.")

if __name__ == '__main__':
    server_program() 