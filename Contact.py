import json
from typing import Dict

NAME_FIELD = "name"
TELEPHONE_FIELD = "telephone"

class Contact:
    def __init__(self, name: str, phone_number: int):
        self.name = name
        self.phone_number = phone_number
    
    def to_dict(self) -> Dict:
      return {
        NAME_FIELD: self.name,
        TELEPHONE_FIELD: self.phone_number
      }

    def __str__(self):
        return f"[Name: {self.name}, Phone-Number: {self.phone_number}]"
