contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Name: ").title()
        phone = input("Phone number: ")
        email = input("Email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"{name} added.")
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet.")
        for name, details in contacts.items():
            print(f"{name} - {details['phone']} - {details['email']}")
    elif choice == "3":
        name = input("Who are you looking for? ").title()
        if name in contacts:
            print(f"{name} - {contacts[name]['phone']} - {contacts[name]['email']}")
        else:
            print(f"{name} isn't in your contacts.")
    elif choice == "4":
        name = input("Who do you want to delete? ").title()
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted.")
        else:
            print(f"{name} isn't in your contacts.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose 1-5.")
