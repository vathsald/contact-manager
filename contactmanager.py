contacts = {}
def save_contact(contacts):
    with open("contacts.txt", "w") as file:
        for name in contacts:
            file.write(name + "," + contacts[name] + "\n")


def add_contact(contacts):
    name = input("Enter the contact name:").strip().title()
    if name in contacts:
        print("Contact already exists")
        check = input("Overwrite? (y/n):")
        if check.lower() == "y":
            updated_number = input("Enter updated contact number").strip()
            if updated_number.isdigit() and len(updated_number) == 10:
                contacts[name] = updated_number
            
            else:
                print("Invalid number")
            return 
        else:
            return
    
    number = input("Enter contact number:")
    if number.isdigit() and len(number) == 10:
        contacts[name] = number
    else:
        print("Invalid number")
    save_contact(contacts)


def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts")
    else:
        for name in contacts:
            print("Name:", name, "|", "Number:", contacts[name])


def search_contact(contacts):
    try:
        name = input("Enter the name to be searched:").strip().title()
    except:
        print("Invalid name")
        return
    if name in contacts:
        print("Name:", name, "|", "Number:", contacts[name])
    else:
        print("Contact does not exist")


def delete_contact(contacts):
    if len(contacts) == 0:
        print("No contacts to delete")
    else:
        for name in contacts:
             print("Name:", name, "|", "Number:", contacts[name])
        delete_name = input("Enter the contact name to be deleted:").strip().title()
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted successfully")
        else:
            print("Contact does not exist")
    save_contact(contacts)


def update_contact(contacts):
    if len(contacts) == 0:
        print("No contacts to update")
    else:
        for name in contacts:
            print("Name:", name, "|", "Number:", contacts[name])
        try:
            update_name = input("Enter the contact to be updated:").strip().title()
        except:
            print("Invalid name")
            return
        if update_name in contacts:
            updated_number = input("Enter updated contact number").strip()
            if updated_number.isdigit() and len(updated_number) == 10:
                contacts[update_name] = updated_number
            else:
                print("Invalid number")
        else:
            print("Invalid name")
    save_contact(contacts)


try:
    with open("contacts.txt", "r") as file:
        for line in file:
            name, number = line.strip().split(",")
            contacts[name] = number
except:
    pass

while True:
    print("1.Add contact")
    print("2.View contacts")
    print("3.Search contacts")
    print("4.Delete contact")
    print("5.Update contact")
    print("6.Exit")

    try:
        Choice = int(input("Enter your choice:"))
    except:
        print("Invalid choice")
        continue
    if Choice == 1:
        add_contact(contacts)

    elif Choice == 2:
        view_contacts(contacts)

    elif Choice == 3:
        search_contact(contacts)

    elif Choice == 4:
        delete_contact(contacts)

    elif Choice == 5:
        update_contact(contacts)

    elif Choice == 6:
        print("Exiting...")
        break
