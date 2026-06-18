import threading
import queue
import random
import time

t1 = 5   
t2 = 4   

messages = queue.Queue()

running = True


def producer():
    counter = 1

    while running:
        delay = random.randint(1, t1)
        time.sleep(delay)

        message = f"Повідомлення #{counter}"

        messages.put(message)

        print(f"[ГЕНЕРАЦІЯ] Створено: {message}")

        counter += 1


def consumer():
    while running:
        message = messages.get()

        delay = random.randint(1, t2)
        time.sleep(delay)

        print(f"[ОБРОБКА] {message}")

        messages.task_done()


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

try:
    time.sleep(30)

except KeyboardInterrupt:
    pass

running = False

print("Завершення програми...")