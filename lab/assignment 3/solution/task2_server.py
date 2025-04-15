import socket

def count_vowels(message):
    vowels = "aeiouAEIOU"
    count = 0
    for char in message:
        if char in vowels:
            count += 1
    return count

def server_program():
    host = socket.gethostname()
    port = 5002 

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port} for Task 2")

    conn, address = server_socket.accept()
    print("Task 2 Connection from: " + str(address))

    while True:
        
        data = conn.recv(1024).decode()
        if not data:
            
            print("Client disconnected.")
            break
        print("Received from client: " + str(data))

        vowel_count = count_vowels(str(data))
        response = ""
        if vowel_count == 0:
            response = "Not enough vowels"
        elif vowel_count <= 2:
            response = "Enough vowels I guess"
        else:
            response = "Too many vowels"

        print(f"Sending response: {response}")
        conn.send(response.encode())

    conn.close()
    print("Task 2 Connection closed.")

if __name__ == '__main__':
    server_program() 