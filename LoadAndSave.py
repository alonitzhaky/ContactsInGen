import json
import os

def load_file(contacts_path: str): # Loading JSON file with all information
    with open(os.path.relpath(contacts_path)) as file:
        return json.load(file)

def save_file(contacts: list, contacts_path: str): 
    with open (os.path.relpath(contacts_path), "w") as file: 
        json.dump(contacts, file, indent = 4)
