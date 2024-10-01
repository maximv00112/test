import socket

HOST = 'ip'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5) # max 5 verbindungen

while True:
    communication_socket, address = server.accept() #waiting for connection
    print(f"Connected to {address}")
    print("Welchen Befehl wollen sie ausführen?")
    befehl = input()
    
    if befehl == "1":
        print("befehl 1 wird ausgeführt")
    elif befehl == "2":
        print("befehl 2 wird ausgeführt")
        
    communication_socket.send(f"{befehl}".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")