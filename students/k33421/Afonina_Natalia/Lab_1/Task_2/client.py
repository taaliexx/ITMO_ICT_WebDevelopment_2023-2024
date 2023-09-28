import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 4040))

try:
    a = int(input('Введите коэффициент a: '))
    b = int(input('Введите коэффициент b: '))
    c = int(input('Введите коэффициент c: '))

    data = f'{a} {b} {c}'
    clientsocket.send(data.encode('utf-8'))

    result = clientsocket.recv(1024).decode('utf-8')
    print(f'Решение уравнения: {result}')
except Exception as e:
    print(f'Ошибка: {e}')
finally:
    clientsocket.close()