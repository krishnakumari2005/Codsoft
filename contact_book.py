def load_contacts():
    try:
        with open("contacts.txt", "r") as f:
            data = {}
            for line in f:
                name, phone = line.strip().split(",")
                data[name] = phone
            return data
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open("contacts.txt", "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")

contacts = load_contacts()

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact saved.")

    elif choice == "2":
        for name, phone in contacts.items():
            print(f"{name} → {phone}")

    elif choice == "3":
        name = input("Enter name to delete: ")
        contacts.pop(name, None)
        save_contacts(contacts)
        print("Deleted.")

    elif choice == "4":
        break
