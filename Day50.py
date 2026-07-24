import os
import shutil
import hashlib
import pandas as pd
from pathlib import Path

FOLDER = input("Enter Folder Path: ")

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css"]
}

duplicates = []
report = []


def file_hash(path):
    sha = hashlib.sha256()

    with open(path, "rb") as file:

        while chunk := file.read(4096):
            sha.update(chunk)

    return sha.hexdigest()


known_hashes = {}

for root, dirs, files in os.walk(FOLDER):

    for file in files:

        full_path = os.path.join(root, file)

        ext = Path(file).suffix.lower()

        moved = False

        for category, extensions in CATEGORIES.items():

            if ext in extensions:

                destination = os.path.join(FOLDER, category)

                os.makedirs(destination, exist_ok=True)

                new_path = os.path.join(destination, file)

                if not os.path.exists(new_path):

                    shutil.move(full_path, new_path)

                    report.append({
                        "File": file,
                        "Category": category
                    })

                moved = True
                break

        current_path = os.path.join(
            destination if moved else root,
            file
        )

        if os.path.exists(current_path):

            h = file_hash(current_path)

            if h in known_hashes:

                duplicates.append(current_path)

            else:

                known_hashes[h] = current_path

report_df = pd.DataFrame(report)

report_df.to_csv(
    "organization_report.csv",
    index=False
)

with open("duplicates.txt", "w") as file:

    if duplicates:

        for item in duplicates:
            file.write(item + "\n")

print("\n========== ORGANIZATION COMPLETE ==========")

print(f"Files Organized : {len(report)}")

print(f"Duplicates Found: {len(duplicates)}")

print("\nReport Saved:")
print("organization_report.csv")
print("duplicates.txt")
