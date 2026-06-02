import json
import os

FILE = "data/students.json"

def load_data():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            content = f.read().strip()

            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        return []


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)