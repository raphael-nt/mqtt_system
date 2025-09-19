import json
import random
import string
import time
import os

NUM_RECORDS = 10
OUTPUT_FILE = "qrscan_data"
OUTPUT_FORMAT = "json" # txt, json
LOCATIONS = ["boot1", "boot2", "boot3"]
CHECK_VALUES = [0, 1] # in 1, out 0

def generate_token(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_data(num_records):
    return [
        {
            "token": generate_token(),
            "location": random.choice(LOCATIONS),
            "check": random.choice(CHECK_VALUES),
            "epoch": int(time.time())
        }
        for _ in range(num_records)
    ]

if __name__ == "__main__":
    data_list = generate_data(NUM_RECORDS)
    full_path = OUTPUT_FILE + (".json" if OUTPUT_FORMAT=="json" else ".txt")

    if OUTPUT_FORMAT == "txt":
        with open(full_path, "a", encoding="utf-8") as f: # w
            for record in data_list:
                line = f"{record['token']},{record['location']},{record['check']},{record['epoch']}"
                f.write(line + "\n")
    elif OUTPUT_FORMAT == "json":
        with open(full_path, "a", encoding="utf-8") as f: # w
            json.dump(data_list, f, ensure_ascii=False, indent=2)

    print(f"Generated {NUM_RECORDS} records in {os.path.abspath(full_path)}")