FILE_NAME = "passwords.txt"


def add_account():
    website = input("Enter Website/App Name: ")
    username = input("Enter Username/Email: ")
    password = input("Enter Password: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{website},{username},{password}\n")

    print("✅ Account Saved Successfully!")


def view_accounts():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No Accounts Saved!")
            return

        print("\n===== SAVED ACCOUNTS =====")

        for record in records:
            website, username, password = record.strip().split(",")

            print(f"\n🌐 Website: {website}")
            print(f"👤 Username: {username}")
            print(f"🔑 Password: {password}")

    except FileNotFoundError:
        print("No Accounts Found!")


def search_account():
    website_name = input("Enter Website Name: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for record in file:
                website, username, password = record.strip().split(",")

                if website_name in website.lower():
                    print(f"\n🌐 Website: {website}")
                    print(f"👤 Username: {username}")
                    print(f"🔑 Password: {password}")
                    found = True

            if not found:
                print("Account Not Found!")

    except FileNotFoundError:
        print("No Accounts Found!")


while True:
    print("\n===== PASSWORD VAULT =====")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        search_account()

    elif choice == "4":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
