import os

KEY = 123


def encrypt_file(filename):
    try:
        with open(filename, "rb") as file:
            data = file.read()

        encrypted_data = bytes([byte ^ KEY for byte in data])

        encrypted_file = filename + ".enc"

        with open(encrypted_file, "wb") as file:
            file.write(encrypted_data)

        print(f"\n✅ File Encrypted Successfully!")
        print(f"Saved As: {encrypted_file}")

    except FileNotFoundError:
        print("❌ File Not Found!")


def decrypt_file(filename):
    try:
        with open(filename, "rb") as file:
            data = file.read()

        decrypted_data = bytes([byte ^ KEY for byte in data])

        if filename.endswith(".enc"):
            output_file = filename[:-4]
        else:
            output_file = "decrypted_" + filename

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print(f"\n✅ File Decrypted Successfully!")
        print(f"Saved As: {output_file}")

    except FileNotFoundError:
        print("❌ File Not Found!")


while True:
    print("\n===== FILE ENCRYPTION TOOL =====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        filename = input("Enter File Name: ")

        if os.path.exists(filename):
            encrypt_file(filename)
        else:
            print("❌ File Does Not Exist!")

    elif choice == "2":
        filename = input("Enter Encrypted File Name: ")

        if os.path.exists(filename):
            decrypt_file(filename)
        else:
            print("❌ File Does Not Exist!")

    elif choice == "3":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
