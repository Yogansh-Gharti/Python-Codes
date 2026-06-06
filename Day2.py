import random
import string

print("=== Secure Password Generator ===")

length = int(input("Enter password length: "))

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_characters = lowercase + uppercase + digits + symbols

password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(symbols)
]

password.extend(random.choice(all_characters) for _ in range(length - 4))

random.shuffle(password)

final_password = "".join(password)

print("\nGenerated Password:")
print(final_password)
