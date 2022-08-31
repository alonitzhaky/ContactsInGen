from colorama import Fore, Style, Back
from Contact import Contact, NAME_FIELD, TELEPHONE_FIELD

class ContactBook:
    def __init__(self, existing_contacts = None):
        self.contacts = [] if existing_contacts is None else existing_contacts

    def add_contact(self, contact_name: str, phone_number: int):
        self.contacts.append(Contact(contact_name, phone_number).to_dict())
        print(Fore.GREEN + f"Success! Added - {contact_name}" + Style.RESET_ALL)

    def remove_contact(self, contact_name: str):
        if self.search_contact(contact_name) is not None:
            self.contacts = list(filter(lambda contact: contact[NAME_FIELD] != contact_name, self.contacts))
            print(Fore.RED + f"Removed - {contact_name}" + Style.RESET_ALL)

    def search_contact(self, contact_name):
        contact = list(filter(lambda contact: contact[NAME_FIELD] == contact_name, self.contacts))

        if not len(contact):
            print(Back.RED + f"There is no contact with the name - [{contact_name}]" + Style.RESET_ALL + "\n")
        else:
            return Contact(contact[0][NAME_FIELD], contact[0][TELEPHONE_FIELD])
    
    def get_all_contacts(self):
      return self.contacts

    def __str__(self) -> str:
        return ", ".join([str(Contact(contact[NAME_FIELD], contact[TELEPHONE_FIELD])) for contact in self.contacts])
        
