
import requests

BASE_URL = "http://127.0.0.1:8000"

print("Testing GET /")
response = requests.get(f"{BASE_URL}/", timeout=30)
print(response.status_code, response.json())

print("\nTesting GET /health")
response = requests.get(f"{BASE_URL}/health", timeout=30)
print(response.status_code, response.json())

test_inputs = [
    "This movie is absolutely amazing!",
    "This movie is boring and disappointing."
]

for text in test_inputs:
    print(f"\nTesting: {text}")

    response = requests.post(
        f"{BASE_URL}/predict",
        json={"text": text},
        timeout=120
    )

    print(response.status_code, response.json())

print("\nTesting invalid input")
response = requests.post(
    f"{BASE_URL}/predict",
    json={"text": ""},
    timeout=30
)
print(response.status_code, response.json())
