import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"заявка-{request_id}"
    request_queue.put(request)
    print(f"згенеровано заявку {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"виконання звявки {request}")
    else:
        print("черга пуста")

while True:
    generate_request()
    time.sleep(random.uniform(0.5, 1.5))  # випадковий інтервал
    process_request()
    time.sleep(random.uniform(0.5, 1.5))  # випадковий інтервал

    user_input = input("нажми ентер щоб продовжити або напиши ехіт: ")
    if user_input.lower() == 'ехіт':
        break