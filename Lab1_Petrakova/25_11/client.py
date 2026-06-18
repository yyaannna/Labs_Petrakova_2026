import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Підключено до сервера")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("\nСпіврозмовник:", message)

        except:
            break


thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

while True:
    msg = input("Ви: ")

    if msg.lower() == 'exit':
        break

    client.send(msg.encode())

client.close()