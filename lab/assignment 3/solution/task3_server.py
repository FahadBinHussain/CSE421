import socket
import threading

def count_vowels(message):
    vowels = "aeiouAEIOU"
    count = 0
    for char in message:
        if char in vowels:
            count += 1
    return count

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            data = conn.recv(1024).decode()
            if not data:
                print(f"[DISCONNECTED] {addr} disconnected gracefully.")
                connected = False
            else:
                print(f"[{addr}] Received: {data}")

                vowel_count = count_vowels(data)
                response = ""
                if vowel_count == 0:
                    response = "Not enough vowels"
                elif vowel_count <= 2:
                    response = "Enough vowels I guess"
                else:
                    response = "Too many vowels"

                print(f"[{addr}] Sending: {response}")
                conn.send(response.encode())
        except socket.error as e:
            print(f"[ERROR] Socket error with {addr}: {e}")
            connected = False
        except Exception as e:
            print(f"[ERROR] Unexpected error with {addr}: {e}")
            connected = False

    print(f"[CLOSING CONNECTION] {addr}")
    conn.close()

def start_server():
    host = socket.gethostname()
    port = 5003 
    server_addr = (host, port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(server_addr)
    server.listen()
    print(f"[LISTENING] Server is listening on {host}:{port} for Task 3")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server() 