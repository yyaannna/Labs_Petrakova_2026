import socket
import os

HOST = '127.0.0.1'
PORT = 5000

SAVE_DIR = "received_files"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Сервер запущений...")
print("Очікування підключення клієнта...")

conn, addr = server.accept()
print(f"Підключено клієнта: {addr}")

filename = conn.recv(1024).decode()

filepath = os.path.join(SAVE_DIR, filename)

with open(filepath, 'wb') as file:
    print(f"Отримання файлу: {filename}")

    while True:
        data = conn.recv(1024)

        if not data:
            break

        file.write(data)

print("Файл успішно отримано та збережено")
print(f"Шлях: {filepath}")

conn.close()
server.close()