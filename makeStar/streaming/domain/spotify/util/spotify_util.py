import json
import os

def read_spotify_file(file_name: str):
    print("test")
    print(os.path.curdir)
    with open(file_name, 'r', encoding='utf-8') as f:
        try:
            my_data = json.load(f)
            return my_data
        except BaseException as e:
            print('The file contains invalid JSON')
            return None
