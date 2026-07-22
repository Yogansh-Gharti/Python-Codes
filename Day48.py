import os
import base64
import hashlib
from cryptography.fernet import Fernet

# Generate AES-compatible key from password
def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)


def encrypt_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    output_file = filename + ".enc"

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    print(f"\n✅ File Encrypted Successfully!")
    print(f"Saved As: {output_file}")


def decrypt_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        output_file = filename.replace(".enc", "")

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("\n✅ File Decrypted Successfully!")
        print(f"Saved As: {output_file}")

    except Exception:
        print("\n❌ Wrong Password or Invalid Encrypted File!")


while True:

    print("\n====== FILE ENCRYPTION SUITE ======")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        file = input("Enter File Path: ")

        if not os.path.exists(file):
            print("File Not Found!")
            continue

        password = input("Enter Password: ")

        encrypt_file(file, password)

    elif choice == "2":

        file = input("Enter Encrypted File Path: ")

        if not os.path.exists(file):
            print("File Not Found!")
            continue

        password = input("Enter Password: ")

        decrypt_file(file, password)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")
