FILE_NAME = "notes.txt"


def add_note():
    note = input("Enter Note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("✅ Note Saved Successfully!")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No Notes Found!")
            return

        print("\n===== ALL NOTES =====")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note.strip()}")

    except FileNotFoundError:
        print("No Notes Found!")


def search_note():
    keyword = input("Enter keyword to search: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            print("\n===== SEARCH RESULTS =====")

            for i, note in enumerate(file, start=1):
                if keyword in note.lower():
                    print(f"{i}. {note.strip()}")
                    found = True

            if not found:
                print("No matching notes found.")

    except FileNotFoundError:
        print("No Notes Found!")


def delete_note():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No Notes Available!")
            return

        view_notes()

        note_no = int(input("\nEnter note number to delete: "))

        if 1 <= note_no <= len(notes):
            notes.pop(note_no - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(notes)

            print("✅ Note Deleted Successfully!")

        else:
            print("Invalid Note Number!")

    except FileNotFoundError:
        print("No Notes Found!")


while True:
    print("\n===== PERSONAL NOTES MANAGER =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        search_note()

    elif choice == "4":
        delete_note()

    elif choice == "5":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
