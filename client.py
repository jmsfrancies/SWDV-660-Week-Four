import socket

HOST = '127.0.0.1'  # The server's IP address
PORT = 9500        # The same port as the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        user_input = str(input("Enter Hi for Hello and Goodbye for Goodbye: ")).encode('UTF-8')
        user_input = bytes(user_input)
        s.sendall(b'%s' % (user_input))
        data = s.recv(1024)
        if user_input == bytes('Hi','UTF-8'):
            print('Received', repr(data))
            continue
        else:
            break

print('Received', repr(data))
