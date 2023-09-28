import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_message = 'Hello, UDP server! I am client'
client_sock.sendto(client_message.encode('utf-8'),('127.0.0.1', 9999))
data, addr = client_sock.recvfrom(1024)
print("Server's message:")
print(str(data))
client_sock.close()
