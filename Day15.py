FILE_NAME = "patients.txt"


def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")
    contact = input("Enter Contact Number: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{patient_id},{name},{age},{disease},{contact}\n")

    print("✅ Patient Record Added Successfully!")


def view_patients():
    try:
        with open(FILE_NAME, "r") as file:
            patients = file.readlines()

        if not patients:
            print("No Patient Records Found!")
            return

        print("\n===== PATIENT RECORDS =====")

        for patient in patients:
            pid, name, age, disease, contact = patient.strip().split(",")

            print(f"\n🆔 Patient ID: {pid}")
            print(f"👤 Name: {name}")
            print(f"🎂 Age: {age}")
            print(f"🩺 Disease: {disease}")
            print(f"📞 Contact: {contact}")

    except FileNotFoundError:
        print("No Patient Records Found!")


def search_patient():
    search_id = input("Enter Patient ID: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for patient in file:
                pid, name, age, disease, contact = patient.strip().split(",")

                if pid == search_id:
                    print("\n===== PATIENT FOUND =====")
                    print(f"🆔 Patient ID: {pid}")
                    print(f"👤 Name: {name}")
                    print(f"🎂 Age: {age}")
                    print(f"🩺 Disease: {disease}")
                    print(f"📞 Contact: {contact}")

                    found = True
                    break

            if not found:
                print("❌ Patient Not Found!")

    except FileNotFoundError:
        print("No Patient Records Found!")


while True:
    print("\n===== HOSPITAL PATIENT RECORD SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
