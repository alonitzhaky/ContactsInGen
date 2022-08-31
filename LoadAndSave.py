import json

def load_file(DATA_FILE): # Loading JSON file with all information
    with open (DATA_FILE) as file:
        return json.load(file)

def save_file(json_list, DATA_FILE): 
    with open (DATA_FILE, "w") as file: 
        json.dump(json_list, file)