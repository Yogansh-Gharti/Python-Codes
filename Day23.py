import os
import shutil
from datetime import datetime

BACKUP_DIR = "Backups"

os.makedirs(BACKUP_DIR, exist_ok=True)


def create_backup():
    source = input("Enter Folder Path to Backup: ")

    if not os.path.exists(source):
        print("❌ Folder Not Found!")
        return

    folder_name = os.path.basename(os.path.abspath(source))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    destination = os.path.join(
        BACKUP_DIR,
        f"{folder_name}_{timestamp}"
    )

    shutil.copytree(source, destination)

    print("\n✅ Backup Created Successfully!")
    print("Location:", destination)


def list_backups():
    backups = os.listdir(BACKUP_DIR)

    print("\n===== AVAILABLE BACKUPS =====")

    if not backups:
        print("No Backups Found!")
        return

    for i, backup in enumerate(backups, start=1):
        print(f"{i}. {backup}")


def restore_backup():
    backups = os.listdir(BACKUP_DIR)

    if not backups:
        print("No Backups Available!")
        return

    list_backups()

    try:
        choice = int(input("\nSelect Backup Number: "))

        backup_name = backups[choice - 1]

        destination = input("Enter Restore Folder Path: ")

        restore_path = os.path.join(destination, backup_name)

        shutil.copytree(
            os.path.join(BACKUP_DIR, backup_name),
            restore_path
        )

        print("✅ Backup Restored Successfully!")

    except (ValueError, IndexError):
        print("Invalid Selection!")

    except FileExistsError:
        print("Destination Folder Already Exists!")


while True:
    print("\n===== FILE BACKUP UTILITY =====")
    print("1. Create Backup")
    print("2. List Backups")
    print("3. Restore Backup")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_backup()

    elif choice == "2":
        list_backups()

    elif choice == "3":
        restore_backup()

    elif choice == "4":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
