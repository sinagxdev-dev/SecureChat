import socket
import threading # Step 1: Import the magic tool

HOST = '127.0.0.1'
PORT = 55555

# Step 2: Define what the "Employee" does
def handle_client(client, address):
    print(f"[+] New Thread started for {address}")
    
    # MISSION: Move your "While True" receive/send loop from the old code
    # INSIDE here. This function runs separately for every user.
    
    pass # <--- YOUR CODE GOES HERE

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[*] Server is listening on {HOST}:{PORT}...")

    # Step 3: The Receptionist Loop
    while True:
        client, address = server.accept()
        print(f"[+] Connected with {str(address)}")

        # Step 4: Don't block! Create a thread instead.
        # target = the function to run
        # args = the variables to pass to that function
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()
        
        # Optional: Print how many people are online
        print(f"[Active Connections] {threading.active_count() - 1}")
print()
if __name__ == "__main__":
    start_server()
