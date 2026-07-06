import os


def format_size(size):
    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def analyze_folder(folder_path):
    total_size = 0
    total_files = 0
    total_folders = 0
    largest_files = []

    if not os.path.exists(folder_path):
        print("❌ Folder does not exist!")
        return

    for root, dirs, files in os.walk(folder_path):

        total_folders += len(dirs)

        for file in files:

            file_path = os.path.join(root, file)

            try:
                size = os.path.getsize(file_path)

                total_size += size
                total_files += 1

                largest_files.append((file, size))

            except:
                pass

    largest_files.sort(key=lambda x: x[1], reverse=True)

    print("\n===== FOLDER REPORT =====")
    print(f"Folder: {folder_path}")
    print(f"Total Size : {format_size(total_size)}")
    print(f"Total Files: {total_files}")
    print(f"Subfolders : {total_folders}")

    print("\nTop 5 Largest Files")

    for file, size in largest_files[:5]:
        print(f"{file} --> {format_size(size)}")

    with open("folder_report.txt", "w") as report:

        report.write("===== Folder Analysis Report =====\n\n")
        report.write(f"Folder: {folder_path}\n")
        report.write(f"Total Size: {format_size(total_size)}\n")
        report.write(f"Files: {total_files}\n")
        report.write(f"Subfolders: {total_folders}\n\n")

        report.write("Top 5 Largest Files\n")

        for file, size in largest_files[:5]:
            report.write(f"{file} --> {format_size(size)}\n")

    print("\n✅ Report Saved as folder_report.txt")


folder = input("Enter Folder Path: ")

analyze_folder(folder)
