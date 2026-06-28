import hashlib
import os


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception:
        return None


def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder):

        for file in files:

            path = os.path.join(root, file)

            file_hash = calculate_hash(path)

            if file_hash is None:
                continue

            if file_hash in hashes:
                duplicates.append((path, hashes[file_hash]))
            else:
                hashes[file_hash] = path

    return duplicates


folder = input("Enter Folder Path: ")

if not os.path.exists(folder):
    print("❌ Folder Not Found!")
    exit()

duplicates = find_duplicates(folder)

if not duplicates:
    print("\n✅ No Duplicate Files Found!")

else:
    print("\n===== DUPLICATE FILES =====")

    for i, (duplicate, original) in enumerate(duplicates, start=1):
        print(f"\n{i}. Duplicate : {duplicate}")
        print(f"   Original  : {original}")

    choice = input(
        "\nDo you want to delete duplicate files? (yes/no): "
    ).lower()

    if choice == "yes":

        for duplicate, _ in duplicates:

            try:
                os.remove(duplicate)
                print(f"Deleted: {duplicate}")

            except Exception:
                print(f"Could not delete: {duplicate}")

        print("\n✅ Duplicate Files Removed Successfully!")

    else:
        print("No Files Deleted.")
