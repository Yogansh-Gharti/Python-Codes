import os
import zipfile


def create_zip(folder_path, zip_name):
    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        return

    if not zip_name.endswith(".zip"):
        zip_name += ".zip"

    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zip_file:

        for root, folders, files in os.walk(folder_path):

            for file in files:
                file_path = os.path.join(root, file)

                arcname = os.path.relpath(
                    file_path,
                    folder_path
                )

                zip_file.write(file_path, arcname)

    print(f"\n✅ ZIP Created Successfully!")
    print(f"Saved As: {zip_name}")


def extract_zip(zip_name, destination):

    if not os.path.exists(zip_name):
        print("❌ ZIP File Not Found!")
        return

    os.makedirs(destination, exist_ok=True)

    with zipfile.ZipFile(zip_name, "r") as zip_file:
        zip_file.extractall(destination)

    print("✅ ZIP Extracted Successfully!")


def list_zip(zip_name):

    if not os.path.exists(zip_name):
        print("❌ ZIP File Not Found!")
        return

    with zipfile.ZipFile(zip_name, "r") as zip_file:

        print("\n===== ZIP CONTENTS =====")

        for file in zip_file.namelist():
            print(file)


while True:

    print("\n===== ZIP FILE MANAGER =====")
    print("1. Create ZIP")
    print("2. Extract ZIP")
    print("3. View ZIP Contents")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        folder = input("Folder Path: ")
        zip_name = input("ZIP File Name: ")

        create_zip(folder, zip_name)

    elif choice == "2":
        zip_name = input("ZIP File Path: ")
        destination = input("Extract To Folder: ")

        extract_zip(zip_name, destination)

    elif choice == "3":
        zip_name = input("ZIP File Path: ")

        list_zip(zip_name)

    elif choice == "4":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
