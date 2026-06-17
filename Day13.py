FILE_NAME = "library.txt"


def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{title},{author},Available\n")

    print("✅ Book Added Successfully!")


def view_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        if not books:
            print("No Books Found!")
            return

        print("\n===== LIBRARY BOOKS =====")

        for book in books:
            title, author, status = book.strip().split(",")

            print(f"\n📖 Title : {title}")
            print(f"✍️ Author: {author}")
            print(f"📌 Status: {status}")

    except FileNotFoundError:
        print("Library is Empty!")


def search_book():
    keyword = input("Enter Book Title: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for book in file:
                title, author, status = book.strip().split(",")

                if keyword in title.lower():
                    print(f"\n📖 Title : {title}")
                    print(f"✍️ Author: {author}")
                    print(f"📌 Status: {status}")
                    found = True

            if not found:
                print("Book Not Found!")

    except FileNotFoundError:
        print("Library is Empty!")


def issue_book():
    book_name = input("Enter Book Title to Issue: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        updated_books = []
        found = False

        for book in books:
            title, author, status = book.strip().split(",")

            if title.lower() == book_name and status == "Available":
                updated_books.append(f"{title},{author},Issued\n")
                found = True
            else:
                updated_books.append(book)

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_books)

        if found:
            print("✅ Book Issued Successfully!")
        else:
            print("Book Not Available!")

    except FileNotFoundError:
        print("Library is Empty!")


def return_book():
    book_name = input("Enter Book Title to Return: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        updated_books = []
        found = False

        for book in books:
            title, author, status = book.strip().split(",")

            if title.lower() == book_name and status == "Issued":
                updated_books.append(f"{title},{author},Available\n")
                found = True
            else:
                updated_books.append(book)

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_books)

        if found:
            print("✅ Book Returned Successfully!")
        else:
            print("Issued Book Not Found!")

    except FileNotFoundError:
        print("Library is Empty!")


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
