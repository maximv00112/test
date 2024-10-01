import socket

HOST = 'ip'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.connect((HOST, PORT))
    
    befehl = socket.recv(1024).decode('utf-8')
    
    if befehl == "1":
        print("befehl 1 hier:")
    elif befehl == "2":
        print("befehel 2 hier:")
except:
    print("an error has accoured!")
finally:
    socket.close()