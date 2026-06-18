import socket
import os

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = input("Введіть ім'я файлу: ")

if not os.path.exists(filename):
    print("Файл не знайдено")
    client.close()
    exit()

client.send(os.path.basename(filename).encode())

import time
time.sleep(0.1)

with open(filename, 'rb') as file:
    while True:
        data = file.read(1024)

        if not data:
            break

        client.send(data)

print("Файл успішно відправлено")

client.close()