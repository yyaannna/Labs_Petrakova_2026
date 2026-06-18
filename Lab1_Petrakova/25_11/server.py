import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print("Сервер запущений...")
print("Очікування підключення клієнтів...")


def handle_client(client_socket, client_address):
    print(f"Клієнт підключився: {client_address}")

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            print(f"Повідомлення від {client_address}: {message}")

            # Пересилання повідомлення іншому клієнту
            for client in clients:
                if client != client_socket:
                    client.send(message.encode())

        except:
            break

    print(f"Клієнт відключився: {client_address}")

    clients.remove(client_socket)
    client_socket.close()


while len(clients) < 2:
    client_socket, client_address = server.accept()
    clients.append(client_socket)

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )
    thread.start()

print("Два клієнти підключені. Чат активний.")