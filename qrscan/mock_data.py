import json
import random
import string
import time
import os

OUTPUT_FILE = "qrscan_data.json"
LOCATIONS = ["network", "programming", "electricity"]

NUM_SUCCESS = 10
NUM_RECORDS = 100

def generate_token(length=20):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def load_data():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_data(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_success_tokens(num_success, locations, data):
    tokens = [generate_token() for _ in range(num_success)]
    for token in tokens:
        for loc in locations:
            record = {
                "token": token,
                "location": loc,
                "check": 1,
                "epoch": int(time.time())
            }
            data.append(record)
            print(f"[SUCCESS] Check-in: {record}")
            time.sleep(1)
    for token in tokens:
        for loc in locations:
            record = {
                "token": token,
                "location": loc,
                "check": 0,
                "epoch": int(time.time())
            }
            data.append(record)
            print(f"[SUCCESS] Check-out: {record}")
            time.sleep(1)

def generate_random_records(num_records, locations, data):
    for _ in range(num_records):
        token = generate_token()
        record = {
            "token": token,
            "location": random.choice(locations),
            "check": random.choice([0,1]),
            "epoch": int(time.time())
        }
        data.append(record)
        print(f"[RANDOM] Record: {record}")
        time.sleep(1)

if __name__ == "__main__":
    data = load_data()
    generate_success_tokens(NUM_SUCCESS, LOCATIONS, data)
    generate_random_records(NUM_RECORDS, LOCATIONS, data)
    save_data(data)
    print(f"Total records: {len(data)} in {os.path.abspath(OUTPUT_FILE)}")
import json
import random
import string
import time
import os

OUTPUT_FILE = "qrscan_data.json"
LOCATIONS = ["network", "programming", "boot3"]

NUM_SUCCESS = 2
NUM_RECORDS = 10

def generate_token(length=20):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def load_data():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_data(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_success_tokens(num_success, locations, data):
    tokens = [generate_token() for _ in range(num_success)]
    for token in tokens:
        for loc in locations:
            record = {
                "token": token,
                "location": loc,
                "check": 1,
                "epoch": int(time.time())
            }
            data.append(record)
            print(f"[SUCCESS] Check-in: {record}")
            time.sleep(1)
    for token in tokens:
        for loc in locations:
            record = {
                "token": token,
                "location": loc,
                "check": 0,
                "epoch": int(time.time())
            }
            data.append(record)
            print(f"[SUCCESS] Check-out: {record}")
            time.sleep(1)

def generate_random_records(num_records, locations, data):
    for _ in range(num_records):
        token = generate_token()
        record = {
            "token": token,
            "location": random.choice(locations),
            "check": random.choice([0,1]),
            "epoch": int(time.time())
        }
        data.append(record)
        print(f"[RANDOM] Record: {record}")
        time.sleep(1)

if __name__ == "__main__":
    data = load_data()
    generate_success_tokens(NUM_SUCCESS, LOCATIONS, data)
    generate_random_records(NUM_RECORDS, LOCATIONS, data)
    save_data(data)
    print(f"Total records: {len(data)} in {os.path.abspath(OUTPUT_FILE)}")