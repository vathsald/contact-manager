contacts = {}
try:
    with open("contacts.txt", "r") as file:
        for line in file:
            name,number=line.strip().split(",") 
            contacts[name] = number
except:
    pass
while True:
    print("1.Add contact")
    print("2.View contacts")
    print("3.Search contacts")
    print("4.Delete contact")
    print("5.Exit")

    Choice = int(input("Enter your choice:"))

    if Choice == 1:
        print("Enter the contact name:")
        name = input()
        print("Enter the contact number:")
        number = input()
        if number.isdigit() and len(number)==10:
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
        name = input("Enter the name to be searched:")
        if name in contacts:
            print(name, contacts[name])
        else:
            print("Contact does not exist")
    elif Choice == 4:
        if len(contacts) == 0:
            print("No contacts to delete")
        for name in contacts:
            print(name, contacts[name])
        delete_name = input("Enter the contact name to be deleted:")
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deletedd successfully")
        else:
            print("Contact does not exist")
    elif Choice == 5:
        print("Exiting...")
        break
    with open("contacts.txt", "w") as file:
        for name in contacts:
            file.write(name +","+contacts[name]+"\n")