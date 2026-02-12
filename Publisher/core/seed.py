import json
import os

from core.db import get_db

def load_init_data(file_path, coll):

    if not os.path.exists(file_path):
        print(f"file not found at path: {file_path}")
        return
    
    db = get_db()
    cool = db[coll]

    with open(file_path) as file:
        file_data = json.load(file)

    return cool.insert_many(file_data)


