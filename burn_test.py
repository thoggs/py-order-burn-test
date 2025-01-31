import requests
import json
import threading
import time
import random
import string

API_URL = "http://localhost:8282/api/orders"
HEADERS = {"Content-Type": "application/json"}
NUM_REQUESTS = 200000
REQUESTS_PER_SECOND = 3
ITEMS_PER_ORDER = 2000


def generate_random_code(prefix, length):
    characters = string.ascii_uppercase + string.digits
    return prefix + ''.join(random.choices(characters, k=length - len(prefix)))


def generate_payload():
    customer_code = generate_random_code("COPL", 16)
    return {
        "customerName": f"Fryda Cliente {customer_code}",
        "customerCode": customer_code,
        "orderStatus": "PENDING",
        "items": [
            {
                "productCode": generate_random_code("PRD", 16),
                "productName": f"Product {i + 1}",
                "quantity": 1,
                "unitPrice": round(10 + (i % 100) * 0.5, 2)
            }
            for i in range(ITEMS_PER_ORDER)
        ]
    }


def send_request():
    payload = generate_payload()
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    print(f"CustomerCode: {payload['customerCode']} -> Status: {response.status_code}")


threads = []
for i in range(NUM_REQUESTS):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

    if i % REQUESTS_PER_SECOND == 0:
        time.sleep(1)

for thread in threads:
    thread.join()

print("✅ Todas as requisições foram enviadas!")
