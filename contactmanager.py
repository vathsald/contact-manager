contacts = {}
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

    Choice = int(input("Enter your choice:"))

    if Choice == 1:
        print("Enter the contact name:")
        name = input().strip().capitalize()
        print("Enter the contact number:")
        number = input()
        if number.isdigit() and len(number) == 10:
            contacts[name] = number
        else:
            print("Invalid number")
    elif Choice == 2:
        if len(contacts) == 0:
            print("No contacts")
        else:
            for name in contacts:
                print(name, contacts[name])
    elif Choice == 3:
        name = input("Enter he name to be searched:").strip().capitalize()
        if name in contacts:
            print(name, contacts[name])
        else:
            print("Contact does not exist")
    elif Choice == 4:
        if len(contacts) == 0:
            print("No contacts to delete")
        else:
            for name in contacts:
                print(name, contacts[name])
            delete_name = input("Enter the contact name to be deleted:").strip().capitalize()
            if delete_name in contacts:
                del contacts[delete_name]
                print("Contact deleted successfully")
            else:
                print("Contact does not exist")
    elif Choice == 5:
        if len(contacts) == 0:
            print("No contacts to update")
        else:
            for name in contacts:
                print(name, contacts[name])
            update_name = input("Enter the contact to be updated:").strip().capitalize()
            if update_name in contacts:
                updated_number = input("Enter updated contact number").strip()
                if updated_number.isdigit() and len(updated_number) == 10:
                    contacts[update_name] = updated_number
                else:
                    print("Invalid number")
    elif Choice == 6:
        print("Exiting...")
        break
    with open("contacts.txt", "w") as file:
        for name in contacts:
            file.write(name + "," + contacts[name] + "\n")
