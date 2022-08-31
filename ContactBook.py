from colorama import Fore, Style, Back
from Contact import Contact
import json

class ContactBook:
    contacts = []

    def __init__(self, existing_contacts = None):
        self.contacts = [] if existing_contacts is None else existing_contacts
        

    def add_contact(self, name = "", tel = 0):
        self.contacts.append(Contact(name, tel))
        print(Fore.GREEN + "Success!" + Style.RESET_ALL)

    def remove_contact(self, contact_name):
        self.contacts.remove(contact_name)
        print(Fore.RED + "Removed.\n" + Style.RESET_ALL)

    def search_contact(self, contact_name):
        for contact in self.contacts:
            if type(contact) is Contact:
                if contact.name == contact_name:
                    return contact
        return (Back.RED + "\nThere is no contact with that name." + Style.RESET_ALL + "\n")
    
    def make_contact_json(self):
        result = []
        for contact in self.contacts:
            result.append(json.loads(contact.__str__()))
        return result

    def __str__(self) -> str:
        result = ""
        for contact in self.contacts:
            result += contact.__str__()
        return result
        