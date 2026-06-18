import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Підключення до сервера встановлено")

while True:
    expr = input("Введіть арифметичний вираз: ")

    client.send(expr.encode())

    if expr.lower() == 'exit':
        break

    response = client.recv(1024).decode()
    print("Відповідь сервера:", response)

client.close()