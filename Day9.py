import os
import shutil

folder_path = input("Enter Folder Path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".exe", ".msi"]
}

for category in file_types:
    os.makedirs(os.path.join(folder_path, category), exist_ok=True)

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        _, extension = os.path.splitext(file)

        moved = False

        for category, extensions in file_types.items():

            if extension.lower() in extensions:

                destination = os.path.join(folder_path, category, file)

                shutil.move(file_path, destination)

                print(f"Moved: {file} -> {category}")

                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)

            shutil.move(file_path,
                        os.path.join(other_folder, file))

            print(f"Moved: {file} -> Others")

print("\nFile Organization Completed!")
