import threading
import queue
import random
import time
import math


N = 200              
M = 4                
T1 = 5             
OPEN_TIME = 120      

SIMULATIONS = 100    
TARGET_PROB = 0.9    



class Spectator:
    def __init__(self, sid, arrival_time):
        self.sid = sid
        self.arrival_time = arrival_time
        self.enter_time = None



class Turnstile(threading.Thread):

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):

        while True:
            spectator = self.q.get()

            if spectator is None:
                break

            service_time = random.randint(1, T1)

            time.sleep(service_time * SCALE)

            spectator.enter_time = current_time[0]

            self.q.task_done()



SCALE = 0.01   

def simulate(arrive_before):

    global current_time
    current_time = [0]

    queues = [queue.Queue() for _ in range(M)]

    turnstiles = [Turnstile(q) for q in queues]

    for t in turnstiles:
        t.start()

    spectators = []

    for i in range(N):

        arrival = random.uniform(-arrive_before, 0)

        spectators.append(Spectator(i, arrival))

    spectators.sort(key=lambda s: s.arrival_time)

    start = time.time()

    for spectator in spectators:

        now = time.time() - start
        target = spectator.arrival_time + arrive_before

        if target > now:
            time.sleep((target - now) * SCALE)

        current_time[0] = spectator.arrival_time

        shortest = min(queues, key=lambda q: q.qsize())

        shortest.put(spectator)

    for q in queues:
        q.join()

    for q in queues:
        q.put(None)

    for t in turnstiles:
        t.join()

    success = 0

    for spectator in spectators:

        if spectator.enter_time is not None:
            if spectator.enter_time <= 0:
                success += 1

    probability = success / N

    return probability



arrive_before = 10

while True:

    probs = []

    for _ in range(SIMULATIONS):
        p = simulate(arrive_before)
        probs.append(p)

    avg_prob = sum(probs) / len(probs)

    print(
        f"Час приходу: {arrive_before:3} сек | "
        f"Ймовірність встигнути: {avg_prob:.3f}"
    )

    if avg_prob >= TARGET_PROB:
        break

    arrive_before += 10


print("\n----------------------------------")
print(
    f"Мінімальний час приходу: "
    f"{arrive_before} сек"
)
print(
    f"Ймовірність проходу: "
    f"{avg_prob:.3f}"
)