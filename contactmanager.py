class ContactManager:
    def __init__(self):
        self.contacts = {}

    def save_contact(self):
        with open("contacts.txt", "w") as file:
            for name in self.contacts:
                file.write(name + "," + self.contacts[name] + "\n")

    def add_contact(self):
        name = input("Enter the contact name:").strip().title()
        if name in self.contacts:
            print("Contact already exists")
            check = input("Overwrite? (y/n):")
            if check.lower() == "y":
                updated_number = input("Enter updated contact number").strip()
                if updated_number.isdigit() and len(updated_number) == 10:
                    self.contacts[name] = updated_number
                    self.save_contact()
                else:
                    print("Invalid number")
                return
            else:
                return

        number = input("Enter contact number:")
        if number.isdigit() and len(number) == 10:
            self.contacts[name] = number
            self.save_contact()
        else:
            print("Invalid number")
        

    def view_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts")
        else:
            for name in self.contacts:
                print("Name:", name, "|", "Number:", self.contacts[name])

    def search_contact(self):
        try:
            name = input("Enter the name to be searched:").strip().title()
        except:
            print("Invalid name")
            return
        if name in self.contacts:
            print("Name:", name, "|", "Number:", self.contacts[name])
        else:
            print("Contact does not exist")

    def delete_contact(self):
        if len(self.contacts) == 0:
            print("No contacts to delete")
        else:
            for name in self.contacts:
                print("Name:", name, "|", "Number:", self.contacts[name])
            delete_name = input("Enter the contact name to be deleted:").strip().title()
            if delete_name in self.contacts:
                del self.contacts[delete_name]
                print("Contact deleted successfully")
            else:
                print("Contact does not exist")
        self.save_contact()

    def update_contact(self):
        if len(self.contacts) == 0:
            print("No contacts to update")
        else:
            for name in self.contacts:
                print("Name:", name, "|", "Number:", self.contacts[name])
            try:
                update_name = input("Enter the contact to be updated:").strip().title()
            except:
                print("Invalid name")
                return
            if update_name in self.contacts:
                updated_number = input("Enter updated contact number").strip()
                if updated_number.isdigit() and len(updated_number) == 10:
                    self.contacts[update_name] = updated_number
                else:
                    print("Invalid number")
            else:
                print("Invalid name")
        self.save_contact()

    def load_contacts(self):

        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    name, number = line.strip().split(",")
                    self.contacts[name] = number
        except:
            pass

manager = ContactManager()
manager.load_contacts()

while True:
    print("--"*30)
    print("1.Add contact")
    print("2.View contacts")
    print("3.Search contacts")
    print("4.Delete contact")
    print("5.Update contact")
    print("6.Exit")
    print("--"*30)

    try:
        Choice = int(input("Enter your choice:"))
    except:
        print("Invalid choice")
        continue
    if Choice == 1:
        manager.add_contact()

    elif Choice == 2:
        manager.view_contacts()

    elif Choice == 3:
        manager.search_contact()

    elif Choice == 4:
        manager.delete_contact()

    elif Choice == 5:
        manager.update_contact()

    elif Choice == 6:
        print("Exiting...")
        break
