import json
import random
import string
import os

NUM_RECORDS = 10
OUTPUT_FILE = "register_data"
OUTPUT_FORMAT = "json"  # txt, json

# for example
FIRST_NAME = ["กชพร", "ขยานี", "ชนิตรา", "ธยาดา"]
LAST_NAME = ["บุญถึง", "สมศักดิ์", "จันทนา", "เกียรติ"]
GENDERS = ["ชาย", "หญิง"]
SCHOOLS = ["โรงเรียนวีระพิทยา", "โรงเรียนกลาโหมอุทิศ", "โรงเรียนโยธินบูรณะ"]

def generate_phone():
    return "0" + "".join(random.choice(string.digits) for _ in range(9))

def generate_email():
    return "user" + "".join(random.choice(string.digits) for _ in range(4)) + "@gmail.com"

def generate_data(num_records):
    data = []
    for _ in range(num_records):
        firstName = random.choice(FIRST_NAME)
        lastName = random.choice(LAST_NAME)
        record = {
            "firstName": firstName,
            "lastName": lastName,
            "age": random.randint(10,60),
            "gender": random.choice(GENDERS),
            "school": random.choice(SCHOOLS),
            "email": generate_email(),
            "phone": generate_phone()
        }
        data.append(record)
    return data

if __name__ == "__main__":
    data_list = generate_data(NUM_RECORDS)

    full_path = OUTPUT_FILE + (".json" if OUTPUT_FORMAT == "json" else ".txt")

    if OUTPUT_FORMAT == "txt":
        with open(full_path, "w", encoding="utf-8") as f: # a
            for r in data_list:
                line = f"{r['firstName']},{r['lastName']},{r['age']},{r['gender']},{r['school']},{r['email']},{r['phone']}"
                f.write(line + "\n")
    elif OUTPUT_FORMAT == "json":
        with open(full_path, "w", encoding="utf-8") as f: # a
            json.dump(data_list, f, ensure_ascii=False, indent=2)

    print(f"Generated {NUM_RECORDS} records in {os.path.abspath(full_path)}")