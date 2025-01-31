import requests
import json
import threading
import time

API_URL = "http://localhost:8282/api/orders"
HEADERS = {"Content-Type": "application/json"}
NUM_REQUESTS = 200000
CUSTOMER_CODE_BASE = "COPLDSAKDFFDSNBBO"
REQUESTS_PER_SECOND = 3


def generate_payload(customer_index):
    return {
        "customerName": f"Fryda Cliente {customer_index}",
        "customerCode": f"{CUSTOMER_CODE_BASE}{customer_index:05d}",
        "orderStatus": "PENDING",
        "items": [
            {
                "productCode": f"PROD{customer_index:05d}{order:05d}",
                "productName": f"Product {order + 1}",
                "quantity": 1,
                "unitPrice": round(10 + (order % 100) * 0.5, 2)
            }
            for order in range(5000)
        ]
    }


def send_request(customer_index):
    payload = generate_payload(customer_index)
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    print(f"CustomerCode: {payload['customerCode']} -> Status: {response.status_code}")


threads = []
for i in range(NUM_REQUESTS):
    thread = threading.Thread(target=send_request, args=(i,))
    thread.start()
    threads.append(thread)

    if i % REQUESTS_PER_SECOND == 0:
        time.sleep(1)

for thread in threads:
    thread.join()

print("✅ Todas as requisições foram enviadas!")
