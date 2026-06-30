import os

def rename_files(folder_path, prefix="", suffix=""):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist!")
        return

    files = [
        file for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file))
    ]

    if not files:
        print("No files found.")
        return

    for index, file in enumerate(files, start=1):
        old_path = os.path.join(folder_path, file)

        name, extension = os.path.splitext(file)

        new_name = f"{prefix}{index}_{name}{suffix}{extension}"

        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

        print(f"✅ {file}  →  {new_name}")

    print("\n🎉 All files renamed successfully!")


folder = input("Enter Folder Path: ")
prefix = input("Enter Prefix (optional): ")
suffix = input("Enter Suffix (optional): ")

rename_files(folder, prefix, suffix)
