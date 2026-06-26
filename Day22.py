import hashlib
import os


def calculate_hash(filename):
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


while True:
    print("\n===== FILE INTEGRITY CHECKER =====")
    print("1. Generate SHA-256 Hash")
    print("2. Compare Two Files")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        filename = input("Enter File Name: ")

        if os.path.exists(filename):
            file_hash = calculate_hash(filename)

            print("\n===== FILE HASH =====")
            print(file_hash)

        else:
            print("❌ File Not Found!")

    elif choice == "2":
        file1 = input("Enter First File: ")
        file2 = input("Enter Second File: ")

        if os.path.exists(file1) and os.path.exists(file2):

            hash1 = calculate_hash(file1)
            hash2 = calculate_hash(file2)

            print("\n===== COMPARISON RESULT =====")

            if hash1 == hash2:
                print("✅ Files are IDENTICAL")
            else:
                print("❌ Files are DIFFERENT")

            print("\nHash 1:")
            print(hash1)

            print("\nHash 2:")
            print(hash2)

        else:
            print("❌ One or both files do not exist!")

    elif choice == "3":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
