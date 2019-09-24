import socket

HOST = '127.0.0.1'  # Localhost 
PORT = 9500        # Port 9500 is the Port that the Server will attempt to connect to the client with

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if data == bytes('Hi','UTF-8'):
                conn.send(bytes("Hello",'UTF-8'))
                continue
            else:
                conn.send(bytes("GoodBye",'UTF-8'))
                break
                s.close()