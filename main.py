from colorama import Fore, Style
from LoadAndSave import load_file, save_file
from ContactBook import ContactBook

contacts = []
DATA_FILE = "contactbook.json"

def menu():
    print(Fore.RED + "Welcome to Contacts Manager v2.0.0!" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + "Please enter your selection according to the menu." + Style.RESET_ALL)
    print("a - Add a contact")
    print("r - Remove a contact")
    print("s - Search for a contact")
    print("p - Print a list of all contacts")
    print("x - Exit")
    user_selection = input(Fore.GREEN + "Your selection: " + Style.RESET_ALL)
    return user_selection

def main():
    try:
        existing_contacts = load_file(DATA_FILE)
    except FileNotFoundError:
        existing_contacts = None
    contactbook = ContactBook(existing_contacts)
    load_file(DATA_FILE)
    user_selection = ""
    while user_selection != "x":
        user_selection = menu() # As long as user did not select "x", program will always run. 
        if user_selection == "a":
            contactbook.add_contact(input("Please enter contact's name: "), int(input("Please enter contact's number: ")))
        if user_selection == "r":
            contactbook.remove_contact(contactbook.search_contact(input("Contact's Name? ")))
        if user_selection == "s": 
            contactbook.search_contact(input("Contact's name? "))
            print(Fore.GREEN + "Success!" + Style.RESET_ALL)
        if user_selection == "p":
            print(contactbook)
            print(Fore.GREEN + "Success!" + Style.RESET_ALL)
    print(Fore.MAGENTA + "Thank you for using my software. Bye!")
    save_file(contactbook.make_contact_json(), DATA_FILE)
            

if __name__ == "__main__":
    main()
