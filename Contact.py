import json

class Contact:
    name = ""
    tel = 0

    def __init__(self, name = "", tel = 0):
        self.name = name
        self.tel = tel

    def __str__(self):
        return json.dumps ({"name": self.name, "tel": self.tel})
