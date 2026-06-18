import threading
import random
import time
from collections import deque


class MessageQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def add_message(self, message, priority=False):
        with self.lock:
            if priority:
                self.queue.appendleft((message, priority))
            else:
                self.queue.append((message, priority))

    def get_message(self):
        with self.lock:
            if len(self.queue) > 0:
                return self.queue.popleft()
            return None

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0


t1 = 5
t2 = 4

running = True

messages = MessageQueue()


def producer():
    counter = 1

    while running:
        time.sleep(random.randint(1, t1))

        # Випадкове визначення пріоритету
        priority = random.choice([True, False])

        if priority:
            msg = f"ПРІОРИТЕТНЕ повідомлення #{counter}"
        else:
            msg = f"Звичайне повідомлення #{counter}"

        messages.add_message(msg, priority)

        print(f"[ГЕНЕРАЦІЯ] {msg}")

        counter += 1


def consumer():
    while running:
        if not messages.is_empty():

            msg, priority = messages.get_message()

            # Імітація обробки
            time.sleep(random.randint(1, t2))

            print(f"[ОБРОБКА] {msg}")

        else:
            time.sleep(0.5)


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

try:
    time.sleep(30)

except KeyboardInterrupt:
    pass

running = False

producer_thread.join()
consumer_thread.join()

print("Програму завершено")