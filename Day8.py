FILE_NAME = "contacts.txt"


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone}\n")

    print("✅ Contact Saved Successfully!")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("No Contacts Found!")
            return

        print("\n===== CONTACT LIST =====")
        for contact in contacts:
            name, phone = contact.strip().split(",")
            print(f"👤 {name} - 📞 {phone}")

    except FileNotFoundError:
        print("No Contacts Found!")


def search_contact():
    search_name = input("Enter Name to Search: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for contact in file:
                name, phone = contact.strip().split(",")

                if search_name in name.lower():
                    print(f"\n👤 Name: {name}")
                    print(f"📞 Phone: {phone}")
                    found = True

            if not found:
                print("Contact Not Found!")

    except FileNotFoundError:
        print("No Contacts Found!")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
