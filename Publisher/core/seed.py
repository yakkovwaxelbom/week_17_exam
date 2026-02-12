import json
import os


def load_init_data(file_path, coll):

    if not os.path.exists(file_path):
        print(f"file not found at path: {file_path}")
        return
    with open(file_path) as file:
        file_data = json.load(file)

    return coll.insert_many(file_data)


