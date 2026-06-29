import base64
import random
import string
import os

MASTER_PASSWORD = "admin123"
FILE_NAME = "vault.txt"


def encode_password(password):
    return base64.b64encode(password.encode()).decode()


def decode_password(encoded):
    return base64.b64decode(encoded.encode()).decode()


def generate_password():
    length = int(input("Password Length: "))

    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(random.choice(chars) for _ in range(length))

    print("\nGenerated Password:")
    print(password)


def add_account():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    encoded = encode_password(password)

    with open(FILE_NAME, "a") as file:
        file.write(f"{website},{username},{encoded}\n")

    print("✅ Credentials Saved Successfully!")


def view_accounts():
    if not os.path.exists(FILE_NAME):
        print("No Records Found!")
        return

    print("\n===== SAVED ACCOUNTS =====")

    with open(FILE_NAME, "r") as file:
        for line in file:
            website, username, password = line.strip().split(",")

            print(f"\nWebsite : {website}")
            print(f"Username: {username}")
            print(f"Password: {decode_password(password)}")


def search_account():
    website_name = input("Enter Website: ").lower()

    if not os.path.exists(FILE_NAME):
        print("No Records Found!")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            website, username, password = line.strip().split(",")

            if website.lower() == website_name:
                print("\n===== ACCOUNT FOUND =====")
                print(f"Website : {website}")
                print(f"Username: {username}")
                print(f"Password: {decode_password(password)}")
                found = True

    if not found:
        print("Account Not Found!")


def delete_account():
    website_name = input("Enter Website to Delete: ").lower()

    if not os.path.exists(FILE_NAME):
        print("No Records Found!")
        return

    records = []
    deleted = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            website, username, password = line.strip().split(",")

            if website.lower() != website_name:
                records.append(line)
            else:
                deleted = True

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if deleted:
        print("✅ Account Deleted!")
    else:
        print("Account Not Found!")


master = input("Enter Master Password: ")

if master != MASTER_PASSWORD:
    print("❌ Incorrect Master Password!")
    exit()

while True:
    print("\n===== ADVANCED PASSWORD MANAGER =====")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Delete Account")
    print("5. Generate Strong Password")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        search_account()

    elif choice == "4":
        delete_account()

    elif choice == "5":
        generate_password()

    elif choice == "6":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
