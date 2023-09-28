import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9999))

while True:
    data, addr = sock.recvfrom(1024)
    print(str(data))
    message = 'Hello, client! I am UDP server'.encode('utf-8')
    sock.sendto(message, addr)
