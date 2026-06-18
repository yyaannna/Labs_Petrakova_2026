import socket
import ast

HOST = '127.0.0.1'
PORT = 5000


def check_expression(expr):
    try:
        # Перевірка синтаксису виразу
        ast.parse(expr, mode='eval')
        return "Вираз синтаксично правильний"
    except:
        return "Помилка синтаксису"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Сервер запущений...")

conn, addr = server.accept()
print(f"Підключено клієнта: {addr}")

while True:
    data = conn.recv(1024).decode()

    if not data or data.lower() == 'exit':
        break

    print("Отримано:", data)

    result = check_expression(data)

    conn.send(result.encode())

conn.close()
server.close()