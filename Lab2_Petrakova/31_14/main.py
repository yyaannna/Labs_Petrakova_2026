import os
import time
import random
import shutil
import multiprocessing
from concurrent.futures import ThreadPoolExecutor


CATALOG1 = "Catalog1"
CATALOG2 = "Catalog2"
CATALOG3 = "Catalog3"

PATTERN = "Python"

NUM_THREADS = 4

CHECK_INTERVAL = 2



# Створення каталогів
for directory in [CATALOG1, CATALOG2, CATALOG3]:
    os.makedirs(directory, exist_ok=True)



def file_generator():

    counter = 1

    while True:

        filename = f"file_{counter}.txt"

        filepath = os.path.join(CATALOG1, filename)

        print(f"[ГЕНЕРАЦІЯ] Створення {filename}")

        with open(filepath, "w", encoding="utf-8") as file:

            for i in range(10000):

                if random.random() < 0.1:
                    line = f"Рядок {i} містить {PATTERN}\n"
                else:
                    line = f"Звичайний рядок {i}\n"

                file.write(line)

        counter += 1

        time.sleep(random.randint(2, 5))



def process_file(filepath):

    filename = os.path.basename(filepath)

    print(f"[ПЕРЕВІРКА] {filename}")

    found = False

    try:
        with open(filepath, "r", encoding="utf-8") as file:

            for line in file:

                if PATTERN in line:
                    found = True
                    break

        if found:
            destination = os.path.join(CATALOG2, filename)

            print(f"[ЗНАЙДЕНО] {filename} -> Catalog2")

        else:
            destination = os.path.join(CATALOG3, filename)

            print(f"[НЕ ЗНАЙДЕНО] {filename} -> Catalog3")

        shutil.move(filepath, destination)

    except Exception as e:
        print(f"[ПОМИЛКА] {filename}: {e}")



def main():

    generator_process = multiprocessing.Process(
        target=file_generator
    )

    generator_process.start()

    processed_files = set()

    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:

        try:
            while True:

                files = os.listdir(CATALOG1)

                for filename in files:

                    filepath = os.path.join(CATALOG1, filename)

                    if filepath not in processed_files:

                        processed_files.add(filepath)

                        executor.submit(
                            process_file,
                            filepath
                        )

                time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:

            print("\nЗавершення програми...")

            generator_process.terminate()
            generator_process.join()


if __name__ == "__main__":
    main()