import socket

def calculate_salary(hours):
    try:
        hours = float(hours)
        if hours < 0:
            return "Error: Hours cannot be negative."
        elif hours <= 40:
            salary = hours * 200
            return f"Tk {salary:.2f}"
        else:
            salary = 8000 + (hours - 40) * 300
            return f"Tk {salary:.2f}"
    except ValueError:
        return "Error: Invalid input. Please send a number for hours worked."

def server_program():
    host = socket.gethostname()
    port = 5004 

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port} for Task 4")

    conn, address = server_socket.accept()
    print("Task 4 Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            print("Client disconnected.")
            break
        print("Received hours from client: " + str(data))

        salary_response = calculate_salary(str(data))

        print(f"Calculated Salary: {salary_response}")
        print(f"Sending salary to client...")
        conn.send(salary_response.encode())

    conn.close()
    print("Task 4 Connection closed.")

if __name__ == '__main__':
    server_program() 