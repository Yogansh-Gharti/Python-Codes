import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    return password


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    return score


def show_result(score):
    print("\n===== PASSWORD REPORT =====")

    if score <= 2:
        print("❌ Weak Password")
    elif score <= 4:
        print("⚠️ Medium Password")
    else:
        print("✅ Strong Password")

    print(f"Security Score: {score}/5")


while True:
    print("\n===== SMART PASSWORD TOOL =====")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        length = int(input("Enter Password Length: "))
        password = generate_password(length)

        print(f"\nGenerated Password: {password}")

    elif choice == "2":
        password = input("Enter Password: ")

        score = check_strength(password)

        show_result(score)

        if score < 5:
            print("\nSuggestions:")
            print("- Use uppercase letters")
            print("- Use lowercase letters")
            print("- Add numbers")
            print("- Add special symbols")
            print("- Keep length at least 8 characters")

    elif choice == "3":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
