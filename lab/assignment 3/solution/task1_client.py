# my github: https://github.com/FahadBinHussain
# my portfolio: https://oangrybird.onrender.com/

import socket
import platform

def get_ip_address():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1' 
    finally:
        s.close()
    return IP

def client_program():
    host = socket.gethostname()  
    port = 5001  

    client_socket = socket.socket()  
    try:
        client_socket.connect((host, port))  
    except socket.error as e:
        print(f"Connection error: {e}")
        return

    
    ip_address = get_ip_address()
    device_name = platform.node() 
    message = f"IP: {ip_address}, Device Name: {device_name}"

    client_socket.send(message.encode())  
    print(f"Sent to server: {message}")

    client_socket.close()  
    print("Connection closed.")

if __name__ == '__main__':
    client_program() 